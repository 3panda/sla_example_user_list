# sla_example_user_list
サーバーレス・アプリケーションのサンプルコード 
架空のUser情報をWeb上で作成、一覧の表示を行う 

## 前提条件
このリポジトリのコードをそのままでは動作しません
以下の対応が必要になります

- 必要なAPIはAWS API GateWayで作成する
- back/以下のコードはAWS Lambdaの関数として作成する

## front
Web画面の表示処理
最低限の処理をjqueryで作成している

## back
AWS Lambdaで作成する関数のコード  
Lambda上では必要に応じてAPI(API GateWay)を用意し紐づけておく必要がある

## json
S3に保存される架空のUser情報を管理するJsonファイルのフォーマット 

## 参考
AWS API GateWayなどについては[こちらを参考](https://gist.github.com/3panda/8f22cc1895e94f17cb20420527a23467)

