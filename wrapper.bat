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
@echo �{�\�t�g���g�p��������≹�����͂��߂Ƃ������炩�̐��앨�����J����ꍇ�ɂ́ADiff-SVC �̋K��ɂ���ʂ�ADiff-SVC �̌���Җ� (prophesier) �ƃ��|�W�g���ւ̃����N(https://github.com/prophesier/diff-svc)���΂ɖ��L���Ă��������B"
@echo ------------------------------

@PAUSE
