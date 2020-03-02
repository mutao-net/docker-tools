# docker-tools
- dockerを使って色々と遊んでみたものを保管しておくリポジトリ

## mysql
```
cd mysql
cd docker-compose up -d
mysql user$ docker exec -it mysql_db_1  bash
```
- dockerを使ってlocalにmysqlコンテナを立てる
- スキーマの作成とテストデータの投入までやってくれる

## jenkins
- jenkinsのお試し
- 今後slaveも作る
```
$ docker-compose up -d
$ docker container exec -it jenkins ssh-keygen -t rsa -C ""
$ docker exec -it jenkins  bash
# cat /var/jenkins_home/.ssh/id_rsa.pub
```

## django
- djangoのサンプルプロジェクト作成
- DBはmysql
- c.f. https://djangoproject.jp/doc/ja/1.0/ref/django-admin.html
```
docker-compose run web django-admin.py startproject examplepj .
```