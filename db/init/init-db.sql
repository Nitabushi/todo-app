-- =========================================
-- init-db.sql (seed only)
-- このファイルは Docker の MySQL コンテナ初回起動時に
-- /docker-entrypoint-initdb.d/ 以下の *.sql として自動実行されます。
-- 役割は「初期データの投入」のみです。
-- ※ テーブル定義はアプリの ORM / マイグレーションで管理する方針を推奨します。
-- =========================================

-- DB がない場合に備えて作成（compose側の MYSQL_DATABASE でも作られます）
CREATE DATABASE IF NOT EXISTS todo_app
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE todo_app;

-- ここでは users / todos テーブルが既に存在している前提です。
-- もし初回にテーブルを SQL で作りたい場合は、CREATE TABLE 文を追加してください。

-- ====== 初期ユーザ投入 ======
-- password_hash には「ハッシュ値」を入れてください（平文はNG）。
-- 例）Python で生成: from werkzeug.security import generate_password_hash
--     print(generate_password_hash("Admin@1234"))
-- 下の REPLACE_WITH_HASH_* を実際のハッシュ文字列に置き換えてください。

INSERT INTO users (username, password_hash, role)
VALUES
  ('admin', 'REPLACE_WITH_HASH_ADMIN', 'admin'),
  ('user1', 'REPLACE_WITH_HASH_USER1', 'user');

-- ====== 初期ToDo投入（user1に紐づけ例）======
-- user_id は上で投入したユーザIDに合わせて調整してください。
INSERT INTO todos (user_id, title, detail, status)
VALUES
  (2, '最初のToDo', 'Docker化の動作確認', 0);
