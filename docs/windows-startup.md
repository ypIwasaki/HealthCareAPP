# Windows 最小起動（Issue 01）

## できることとコードの役割

日本語の「ヘルスケア」ウィンドウを開き、「終了」ボタンまたは右上の × で閉じます。
体重記録の入力・保存は後続 Issue の範囲です。この段階では DB を作成しません。

読む順番:

1. `main.py`: ソース実行と実行ファイルで共通の入口。イベントループの終了コードを返します。
2. `healthcare/app.py`: QApplication と画面を作成して表示します。戻り値を保持し、イベントループ中の画面の寿命を保ちます。
3. `healthcare/main_window.py`: 日本語表示と終了ボタンを持つ View。データ操作がないため、空の Controller・Model・保存処理はまだ追加しません。
4. `tests/test_startup.py` / `tests/startup_scenario.py`: 起動境界から実際の Qt 画面を作り、日本語表示と終了を別プロセスで検証します。モックは使いません。
5. `scripts/build-windows.ps1`: バージョン確認、固定依存の導入、整合性確認、PyInstaller によるビルド。

## 固定した環境

Windows x64 / CPython **3.12.14** / PySide6 **6.11.2** / PyInstaller **6.22.3**。
Python は `.python-version`、ビルドと間接依存は `requirements-windows.txt`、型チェックは `requirements-dev.txt` で固定します。
グラフ用 Matplotlib は、この段階では未使用のため後続 Issue で互換性を確認して追加します。

- [PySide6 6.11.2](https://pypi.org/project/PySide6/6.11.2/): Python 3.10 以上・3.15 未満、Windows x64 wheel あり。
- [PyInstaller 6.22.3](https://pypi.org/project/pyinstaller/6.22.3/): Python 3.8 以上・3.16 未満、Windows x64 対応。
- [Python 3.12.14](https://www.python.org/downloads/release/python-31214/): Windows ビルドは [uv の管理する Python](https://docs.astral.sh/uv/concepts/python-versions/) を利用できます。

## ビルドと開発実行

Windows x64 上で実行します。WSL の Python から Windows 用 exe は作りません。
Windows 側にソースを取得し、そのルートを PowerShell で開きます。
Python 3.12.14 x64 が既にあれば、その `python.exe -m venv .venv` でも準備できます。
未導入の場合は、[uv の公式導入手順](https://docs.astral.sh/uv/getting-started/installation/)に従って uv を用意し、以下を実行します。

```powershell
uv python install 3.12.14
uv venv --python 3.12.14 --seed .venv
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\build-windows.ps1
```

`Bypass` はこのビルド用プロセスだけに適用します。実行ポリシーの恒久変更は不要です。
Windows PowerShell 5.1 と PowerShell 7 で読めるよう、スクリプトは ASCII にしています。
初回は依存パッケージ取得のためネットワークが必要です。
Python の指定を変える場合はスクリプトの `-Python 'C:\path\to\python.exe'` を使用します。

開発中のソース実行と検証:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe main.py
.\.venv\Scripts\python.exe -m mypy
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_startup.py -v
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

テストはデスクトップが利用できる Windows で実行します。終了ボタンとウィンドウ終了を確認し、終了しない場合はタイムアウトで失敗します。

## 配布物の使い方と起動確認

1. `dist\HealthCareAPP` **全体**を Windows 内の任意のフォルダ（例: `C:\Users\利用者名\Apps\HealthCareAPP`）へコピーします。exe だけを取り出さず、`_internal` も一緒に置きます。
2. エクスプローラーで `HealthCareAPP.exe` のアイコンをダブルクリックします。必要ならこの exe のショートカットをデスクトップに作成します。
3. 「ヘルスケア」「体重記録と振り返り」が日本語で表示され、コンソールが開かないことを確認します。
4. 「終了」をクリックし、ウィンドウとプロセスが終了することを確認します。
5. アイコンから再起動し、右上の × でも終了できることを確認します。

配布フォルダには Python と Qt を同梱します。日常利用に Python・uv・WSL・開発用端末は不要です。
WSL 内の `dist` を直接使わず Windows 内へコピーすることで、WSL のファイル共有にも依存しません。
ビルド成果物・仮想環境は Git 管理対象外です。

## 検証記録

2026-09-16、Windows 11 x64（10.0.26200）、CPython 3.12.14 で実施。
使用した Python は Codex 同梱の Windows ランタイムから作成した `.venv`。

- TDD: 実装前は `ModuleNotFoundError` で失敗し、実装後は起動・終了の2経路が成功。
- 型チェック: `python -m mypy` 成功（6ファイル）。
- 依存整合性: `python -m pip check` 成功。
- Windows ビルド: Windows PowerShell 5.1 からスクリプトを実行し成功。
- 全テスト: `python -m unittest discover -s tests -v` 成功（1テスト、ボタン／ウィンドウ終了の2シナリオ）。
- 配布物: Windows ローカルフォルダにコピーし、エクスプローラーの exe アイコンをダブルクリックして日本語表示を確認。「終了」と右上の × の両方で終了し、プロセスが残らないことを確認。
- 独立性: PATH を Windows システム領域だけにしたプロセスでも起動。ロードした `python312.dll`・`Qt6Core.dll`・`Qt6Widgets.dll` がすべて配布フォルダ内であることを確認。WSL や別途 Python の起動は不要。WSL 自体の停止および Python 未導入の別 PC での確認は未実施。
- コンソール非表示: 実画面と PE subsystem=2（Windows GUI）を確認。
- exe SHA-256: `F6B539D16128D984099E3C9FFEB4ABDEC2DC82471BE6F336135C055C3EE0AC3B`（同一バイナリの照合用。再ビルド時のバイト一致は保証しません）。

ビルド時に開発ツール Poppler の `icuuc.dll` が PATH から混入し、QtWidgets が WinError 127 で起動できない問題を検出しました。
Qt6Core が要求する ICU 関数と混入 DLL の export が一致しないことを確認し、ビルドスクリプトで PATH を限定しました。
修正後は配布物の Qt6Core・Qt6Gui・Qt6Widgets のロードと実画面の起動に成功しています。PATH はビルド終了時に復元します。

## レビュー記録

比較元は利用者が指定した作業開始時点 `6b5232a46650ad372094e3002b88ad6427327dc9`、実装コミットは `548c11e`。
code-review スキルに従い、独立した2担当でレビューしました。

### Standards

指摘0件。用語・ADR・責任分担・必要な機能だけを増やす方針と整合しています。
各ファイルの役割、読む順番、手順と検証結果が文書化され、修正すべきコードスメルも見つかりませんでした。

### Spec

指摘0件。日本語画面、終了操作、Windows ビルド、依存固定、再現手順と結果が揃っています。
後続 Issue の機能を追加していません。実機確認は実装担当の結果と本記録に基づく評価です。
WSL 停止・Python 未導入の別 PC での確認は未実施ですが、同梱 DLL と限定 PATH での起動が独立性を裏付けています。
