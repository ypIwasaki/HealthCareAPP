---
status: accepted
---

# Python・Qt Widgets・SQLite を MVC で組み合わせる

Python の学習、アプリ内の表形式の DB 管理、本人の Windows PC 内での利用を満たす構成として、PySide6 の Qt Widgets と SQLite を採用する。アプリ全体は MVC とし、画面、操作の調整、データとルールを分け、SQL は専用の保存処理にまとめる。最初の体重記録では、MVVM による画面状態と部品の連動を中心に据える構成より、イベントから保存まで明示的に追える構成を優先する。

## 判断の理由と実装上の境界

- SQLite は PC 内の保存に適し、別の DB サーバーを起動する構成を省ける。SQL を読む学習にもつながるよう、まず Python の `sqlite3` を使う。
- Qt Widgets には表の表示・編集を構成する部品がある。表向けの Qt Model/View は画面用の仕組みとして扱い、アプリ全体の MVC の Model と同一視しない。
- 初版は体重記録から始め、換算設定・グラフ・DB 管理・バックアップへ段階的に増やす。食事記録は次の版で扱う。保存処理や記録の検証は複数の画面で共有できるようにする。
- グラフには Matplotlib を Qt の画面へ埋め込む構成を採用する。単独・比較表示と欠測日の表現をグラフ機能にまとめる。
- WSL は開発環境として使う。Windows 向けの実行確認と配布用ビルドは Windows 側で行う。実行ファイルは Windows 上で PyInstaller を使って作成し、最初の最小画面で起動とビルドを検証する。

2026-09-16 に利用者が仕様全体とともに本構成を承認した。ライブラリのバージョンは実装開始時に互換性を確認して固定する。

## 根拠資料

- [Qt for Python: Getting Started](https://doc.qt.io/qtforpython-6/gettingstarted.html)
- [Qt Model/View Programming](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html)
- [SQLite の適した用途](https://www.sqlite.org/whentouse.html)
- [Python sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [PyInstaller Manual](https://pyinstaller.org/en/stable/)
- [Matplotlib の Qt 埋め込み例](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_qt_sgskip.html)
