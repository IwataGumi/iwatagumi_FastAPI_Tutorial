# STEP 1 - データベース、ルーティングの設計

このステップでは、データベースのテーブルを作成する

## 作りたいアプリを考える
今回のアプリに必要な機能は以下のような感じです。

- ユーザー登録は不要
- タスクの一覧が取得できる
- 作成したタスクを誰でも削除、編集できる
- タスクが完了しているかどうかを判別できる


## データベースの構造

作成機能を考えるうえで重要なのは、データベースにどのような構造、どのような情報が保存するかを考えることが重要です。

例えば、あるSNSの投稿をデータベースに保存するために必要な構造は以下のようになると思います:
```
user_id: その投稿を行ったユーザーを特定するための情報
body: 投稿の内容
replys: 投稿に対する返信
views: 投稿の閲覧数
likes: 投稿のいいね数
created_at: 投稿の作成日時
```
さらに、どのようなデータタイプで保存するかどうかも検討する必要があります

### このアプリの必要なデータベースの構造を設計する

最初に先ほど述べた、このアプリの機能をよりサーバーとデータベースの関係を明確にして、必要となる情報を確認してみましょう。

#### タスクの作成
1. データベースにタスクを保存する
2. 作成したタスクをレスポンスする

#### タスクの一覧を取得
1. データベースにあるタスクをすべて取得
2. 取得したタスクたちをユーザーにレスポンスする

#### タスクの編集を行う
1. ユーザーから指定されたタスクを取得する
2. 取得したタスクのデータをユーザーから来たデータに変更する
3. 変更したタスクをデータベースに保存する
4. ユーザーに編集した結果のタスクをレスポンスする

#### タスクの削除を行う
1. ユーザーから指定されたタスクを取得する
2. 取得したタスクをデータベースから削除する
3. 削除したことをユーザーに伝える



となり、上記のように4種類の処理で作成したいアプリを表現でき、以下のように必要な構造とデータがわかると思います。

```
id (int) : タスクの指定するときに使う固有番号
name (str) : タスクの名前
content (str) : タスクの内容
is_completed (boolean) : タスクが完了しているかどうか
```

# データベースのテーブルを作成する

1. まず先ほど考えたデータベースの構造をclassとsqlalchemyの機能を使用して作成します。
```py

```