#!/usr/bin/env python3
# Copyright (c) 2023 oatsu
"""
WAVファイルを生成して、そのWAVファイルをDiff-SVCで歌声変換するUTAUプラグイン。
"""

import pathlib
import sys
from glob import glob
from os import chdir, getcwd
from os.path import abspath, dirname, join
from pprint import pprint
from tempfile import TemporaryDirectory
from time import sleep
from tkinter.filedialog import asksaveasfilename

import colored_traceback.always
import utaupy
from natsort import natsorted
from PyUtauCli.projects.Render import Render
from PyUtauCli.projects.Ust import Ust
from torch.device import cuda
from tqdm.auto import tqdm

DIFF_SVC_DIR = join(dirname(__file__), 'diff-svc')
ORIGINAL_WD = getcwd()

# autopep8: off ----------------------------------
# diff-svc modules
sys.path.append(DIFF_SVC_DIR)
chdir(DIFF_SVC_DIR)
import utils
from infer import *
from infer_tools.infer_tool import *
from preprocessing.data_gen_utils import get_pitch_crepe, get_pitch_parselmouth
from utils.hparams import hparams

chdir(dirname(__file__))
# autopep8: on -------------------------------------


def run_diffsvc(wav_in, wav_out, model_dir, diff_svc_dir=DIFF_SVC_DIR):
    """Diff-SVCを使って音声ファイルを変換する
    """
    pprint([wav_in, wav_out, model_dir, diff_svc_dir])

    # Diff-SVC 用のモデルを探す
    ckpt_files = natsorted(glob(join(model_dir, '*.ckpt')))
    if len(ckpt_files) == 0:
        raise FileNotFoundError(f'No .ckpt files found in {model_dir}')
    model_path = abspath(ckpt_files[0])
    config_path = abspath(join(model_dir, 'config.yaml'))
    print(f'Diff-SVC model: {model_path}')
    print(f'Diff-SVC config: {config_path}')

    # diff-svc settings--------------------------
    chdir(DIFF_SVC_DIR)
    hubert_gpu = cuda.is_available()
    project_name = None
    svc_model = Svc(project_name, config_path, hubert_gpu, model_path)

    f0_tst, f0_pred, audio = run_clip(
        svc_model,
        file_path=wav_in,
        key=0,
        acc=20,
        use_crepe=True,
        use_pe=True,
        thre=0.05,
        use_gt_mel=False,
        add_noise_step=30,
        project_name=None,
        out_path=wav_out
    )

    chdir(ORIGINAL_WD)


def main(plugin_path):
    """utaupyでプロジェクト情報を取得、PyUtauPluginでwav生成、Diff-SVCで音声変換
    """
    # utaupyで読み取り
    plugin = utaupy.utauplugin.load(plugin_path)
    voice_dir = plugin.voicedir
    ust_path = plugin.setting.get('Project')
    cache_dir = plugin.setting.get('CacheDir', 'cache')

    # wavファイルの保存先を指定
    wav_out = asksaveasfilename(
        initialdir=dirname(ust_path),
        filetypes=[('Wave sound file', '.wav'), ('All files', '*')],
        defaultextension='.wav')
    assert wav_out != ''

    # 一時フォルダにustを出力してPyUtauCliで読み直す
    with TemporaryDirectory() as temp_dir:
        # utaupyでプラグインをustファイルとして保存する
        temp_ust = join(temp_dir, 'temp.ust')
        plugin.as_ust().write(temp_ust)
        # pyutaucliでustを読み込みなおす
        ust = Ust(temp_ust)
        ust.load()

    # PyUtauCli でレンダリング
    render = Render(
        ust,
        voice_dir=str(voice_dir),
        cache_dir=str(cache_dir),
        output_file=str(wav_out),
        logger=None)
    render.clean()
    render.resamp()
    render.append()

    # Diff-SVC で音声変換
    model_dir = join(voice_dir, 'diff-svc-model')
    diff_svc_dir = join(dirname(__file__), 'diff-svc')
    run_diffsvc(
        wav_in=wav_out,
        wav_out=wav_out,
        model_dir=model_dir,
        diff_svc_dir=diff_svc_dir)


if __name__ == "__main__":
    main(sys.argv[1])
