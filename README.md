# 岩田組の `TODO TASKS API` チュートリアル

これは岩田組メンバーが作ったFastAPIになれるために使うリポジトリです。

## アプリ構成
- [FastAPI](https://fastapi.tiangolo.com/ja/) : APIをPythonで開発するためのフレームワーク
- [SQLAlchemy](https://www.sqlalchemy.org/) : Pythonでデータベースを簡単に操作するためのORMラッパー
- [alembic](https://alembic.sqlalchemy.org/en/latest/) : Pythonで使えるマイグレーションツール
- [SQLite](https://www.sqlite.org/index.html) : サーバーが不必要なデータベース

## チュートリアルの行い方
[これらのステップ](/steps/)に従って、上から行ってください。
もしわからなければ、それぞれのステップごとにブランチが分かれているのでぜひ、活用してください。

### ステップ一覧
1. データベースのテーブルを作成するs
2. タスクの作成機能
3. タスクの一覧取得機能
4. タスク完了機能
5. タスクの削除機能
6. タスクの編集機能

## 環境構築

1. 依存パッケージのインストールをする
```bash
$ pip install -r requirements.txt
```

2. データベース、テーブルの作成
```bash
$ alembic upgrade head
```

3. サーバーを起動
```bash
$ python run.py
```
