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