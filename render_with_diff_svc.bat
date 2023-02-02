@echo off
echo "UTAU wav renderer with PyUtauCli and Diff-SVC."
echo "This software uses Diff-SVC (https://github.com/prophesier/diff-svc) by prophesier."
echo "This software uses DiffSinger Community Vocoder (NSF-HiFiGAN, 2022-12-11)."
./python-3.9.13-embed-amd64_PreparedForDiffSvc/python.exe -m pip install --upgrade pip light-the-torch --quiet
./python-3.9.13-embed-amd64_PreparedForDiffSvc/Scripts/ltt.exe install torch torchaudio torchvision --quiet --python ./python-3.9.13-embed-amd64_PreparedForDiffSvc/python.exe
./python-3.9.13-embed-amd64_PreparedForDiffSvc/python.exe ./render_with_diff_svc.py
