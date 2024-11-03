2024 Yahoo Hackson

アプリの説明
アプリ名：「あなたのなまえをおぼえん坊～自動プロフィール画像作成アプリ」

課題
始めたアルバイトや入社した人の名前を覚えられない！

使い方
1. コミュニケーションを取る中で相手のことをアプリに入力していきます
2. 最後に二人のツーショット写真を撮影
3. 相手のことが書かれたプロフィール画像を作成
4. 相手のことを覚えておくことができます

$ docker compose up --build -d   (-d  をつけると他のコマンドを)
-> コンテナの立ち上げ(docker-composes.yml)

$ docker-compose restart

$ docker exec -it app /bin/sh
-> コンテナ内に入る(shellを実行)

$ docker-compose down
-> containerの削除

~ Docker containerの削除
(base) keshi@kei-MacBook-Pro ss2312 % docker ps -a 
CONTAINER ID   IMAGE        COMMAND                   CREATED         STATUS                       PORTS     NAMES
a7740e990fa3   httpd        "httpd-foreground"        3 minutes ago   Exited (0) 2 minutes ago               festive_franklin
8d5c8ca6c3fa   ss2312-app   "docker-entrypoint.s…"   8 minutes ago   Exited (137) 2 minutes ago             app
(base) keshi@kei-MacBook-Pro ss2312 % docker rm a7740e990fa3
a7740e990fa3

$ docker container logs (app)
-> logの確認                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
