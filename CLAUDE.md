# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

GitHub ActionsでPythonのlintチェック（ruff, mypy）を実行するためのテンプレートリポジトリ。Python 3.10〜3.13をサポート。

## 仮想環境

特に指定がなければvenvを使用する：

```bash
python -m venv venv
source venv/bin/activate
```

## コマンド

```bash
make init    # 依存関係のインストール
make lint    # ruff check + ruff format --check + mypy
make fmt     # ruff format + ruff check --fix（自動修正）
make run     # main.py実行
```

## Lint設定

- **ruff**: `pyproject.toml`で設定。行長79文字、E/F/Iルールを適用
- **mypy**: 厳格な型チェック（`disallow_untyped_defs`, `disallow_untyped_calls`等）

## 開発ルール

### 型安全性

- pydanticを使用してデータの型安全性を確保すること
- 全ての関数・メソッドに型アノテーションを付与すること（mypyの`disallow_untyped_defs`で強制）

### インポート

- PEP 8に従う

### ファイル構成

- 1クラス1ファイルで管理すること
- クラス名とファイル名を一致させること（例: `MyClass` → `my_class.py`）

### オブジェクト指向設計

- 単一責任の原則に従い、クラスを適切に分割すること
- 継承よりコンポジションを優先すること

### 定数管理

- マジックナンバー/マジックストリングは使用禁止
- 定数は`constants/`に定義して参照する

### Enum定義

- `auto()`は使用しない
- タプルで`(code, display_name)`の形式で定義し、プロパティでアクセスできるようにする

```python
from enum import Enum

class Status(Enum):
    ACTIVE = (1, "有効")
    INACTIVE = (0, "無効")

    def __init__(self, code: int, display_name: str) -> None:
        self._code = code
        self._display_name = display_name

    @property
    def code(self) -> int:
        return self._code

    @property
    def display_name(self) -> str:
        return self._display_name
```

### ディレクトリ構成

`app/`ディレクトリをプロジェクトに応じて適切な名前に変更し、以下の構成で管理する：

```text
<project_name>/
├── constants/    # Enum等の定数
├── models/       # pydanticモデル
├── services/     # ビジネスロジック
└── exceptions/   # カスタム例外
tests/            # テストコード
```

### Docstring

- 公開API（publicな関数/クラス）には必ずDocstringを書く
- Google styleで統一する

### テスト

- pytestを使用する
- テストファイルは`tests/`に配置し、`test_*.py`の命名規則に従う

### ログ出力

- `print()`は使用禁止
- `logging`モジュールを使用すること

### コード変更時の必須作業

- コード変更後は必ず `make lint` を実行してlintエラーがないことを確認すること
- lintエラーがある場合は修正してからコミットすること
