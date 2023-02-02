# UTAU Renderer with Diff-SVC

Render wav and convert it with [Diff-SVC](https://github.com/prophesier/diff-svc) model

## コンセプト
- UTAUの出力音にNSFを適用することで高音質化を図る。
- プラグインとしてエンジンを起動できるので、様々なフィルターをかけることができる

## 処理内容

1. UTAUプラグインとして起動し、[PyUtauCli](https://github.com/delta-kimigatame/PyUtauCli) でWAVファイルを一時ファイルとして生成する。
2. [Diff-SVC](https://github.com/prophesier/diff-svc) でWAVファイルを加工する。



