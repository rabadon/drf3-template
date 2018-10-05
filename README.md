# Django Rest Framework Template

## 概要
Django Rest Frameworkのテンプレート。
サンプル内容は、LoLのチャンピオンを評価するアプリケーションを作るためのAPI。
勉強用の為それ以外にも何か実装しているかもしれない。

## このテンプレートでDRFを始める

#### ローカルにクローン
`git clone https://github.com/rabadon/drf3-template.git`

#### 必要なパッケージをインストール
```
pip install pymysql
pip install django
pip install djagorestframwork
pip install djagorestframwork-jwt
pip install django-rest-swagger
```

#### サーバーを起動
`python manage.py runserver`

#### アクセス
http://localhost:8000

##### URLS
管理画面(Django)
- http://localhost:8000/admin

API(DjangoRestFramework) + jwt認証
- http://localhost:8000/api
- http://localhost:8000/api/token/obtain

API SWAGGER(DjangoRestFramework-swagger)
- http://localhost:8000/swagger

## 実装されている機能やテンプレートの内容
- JWT認証
- APIテスト(Swagger)
- 大規模アプリケーションに対応できるディレクトリ構成

## 環境
- dev: ローカルで実行
- test: 本番のテストで実行
- prod: 本番で実行

## 標準から変更したディレクトリ構成

## 主要ファイルの詳細
