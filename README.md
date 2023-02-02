# UTAU Renderer with Diff-SVC

Render wav and convert it with [Diff-SVC](https://github.com/prophesier/diff-svc) model

## 注意事項 / NOTES

- This software uses [Diff-SVC](https://github.com/prophesier/diff-svc) by [prophesier](https://github.com/prophesier).
- The bundled Diff-SVC scripts are copy of [UtaUtaUtau's fork of Diff-SVC](https://github.com/UtaUtaUtau/diff-svc).
- \[EN\] You need to obey [Diff-SVC's Notes](https://github.com/prophesier/diff-svc/blob/main/README.md).
  - **Especially, please obey the sentense** `If you redistribute the code in this repository or publicly publish any results produced by this project (including but not limited to video website submissions), please indicate the original author and source code (this repository). ` .
  - The copy shown below can be not the latest. Please check the latest notes and licenses.
- \[JP\] 本ソフトを使用する場合には、[Diff-SVCの規約](https://github.com/prophesier/diff-svc/blob/main/README.md)を順守してください。
  - **とくに、本ソフトを使用した動画や音声をはじめとした何らかの制作物を公開する場合には、Diff-SVC の規約にある通り、Diff-SVC の原作者名 (prophesier) とリポジトリへのリンク(https://github.com/prophesier/diff-svc)を絶対に明記してください**。 

## コンセプト
- UTAUの出力音にNSFを適用することで高音質化を図る。
- プラグインとしてエンジンを起動できるので、様々なフィルターをかけることができる

## 処理内容

1. UTAUプラグインとして起動し、[PyUtauCli](https://github.com/delta-kimigatame/PyUtauCli) でWAVファイルを一時ファイルとして生成する。
2. [Diff-SVC](https://github.com/prophesier/diff-svc) でWAVファイルを加工する。

## 使い方 / USAGE

1. UTAUプラグインとして、本ソフトをUTAUにインストールする。
2. UTAU音源のフォルダに `diff-svc-model` というフォルダを作成して、そこに Diff-SVC 用の CKPT ファイルとそのモデル用の config.yaml を配置する。
3. UTAUエディタ上でノートを範囲選択し、本ソフトをプラグインとして起動する。
