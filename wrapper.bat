@echo UTAU wav renderer with PyUtauCli and Diff-SVC.
@echo This software uses Diff-SVC (https://github.com/prophesier/diff-svc) by prophesier.
@echo This software uses DiffSinger Community Vocoder (NSF-HiFiGAN, 2022-12-11)."

"./python-3.9.13-embed-amd64_PreparedForDiffSvc/python.exe" -m pip install --upgrade pip light-the-torch

"./python-3.9.13-embed-amd64_PreparedForDiffSvc/Scripts/ltt.exe" install torch torchaudio torchvision --isolated --python ./python-3.9.13-embed-amd64_PreparedForDiffSvc/python.exe

"./python-3.9.13-embed-amd64_PreparedForDiffSvc/python.exe" ./utau_renderer_with_diff_svc.py  %*

@echo ------------------------------
@echo UTAU wav renderer with PyUtauCli and Diff-SVC.
@echo This software uses Diff-SVC (https://github.com/prophesier/diff-svc) by prophesier.
@echo This software uses DiffSinger Community Vocoder (NSF-HiFiGAN, 2022-12-11).
@echo ------------------------------
@echo 本ソフトを使用した動画や音声をはじめとした何らかの制作物を公開する場合には、Diff-SVC の規約にある通り、Diff-SVC の原作者名 (prophesier) とリポジトリへのリンク(https://github.com/prophesier/diff-svc)を絶対に明記してください。"
@echo ------------------------------

@PAUSE
