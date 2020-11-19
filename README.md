# Practice Python Scraping

Python でスクレイピングするサンプルスクリプト。Docker・Docker Compose の練習も兼ねて。


## How To Use

- ローカルの Python 環境、もしくは Python が実行可能な Docker コンテナ内で実行する場合
    - Python 3.7・pip3・Chrome ブラウザは各自インストールしておく

```sh
# pipenv をインストールする
$ pip install pipenv

# pipenv で環境を復元する
$ pipenv install --dev

# Chrome を使ったクローリングスクリプトを実行する
$ pipenv run crawl
# → ./html/google.html が生成される

# HTML ファイルからスクレイピングして JSON データをまとめる
$ pipenv run scrape
# → ./json/google.json が生成される
```

- Docker Compose で実行する場合

```sh
# Docker イメージを作成し my-python コンテナを起動する
$ docker-compose up -d

# my-python コンテナにアタッチする
$ docker exec -it my-python bash

# 環境構築・実行
$$ pipenv install --dev
$$ pipenv run crawl
$$ pipenv run scrape
```


## Links

- [Neo's World](https://neos21.net/)
