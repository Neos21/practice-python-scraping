# Practice Python Scraping

Python でスクレイピングするサンプルスクリプト。Docker・Docker Compose の練習も兼ねて。


## How To Use

- ローカルの Python 環境で実行する場合

```sh
# Python 3.7・pip3 は各自インストールしておく・pipenv をインストールする
$ pip install pipenv

# pipenv で環境復元する
$ pipenv install -dev

# Chrome を使ったクローリングスクリプトを実行する
$ pipenv run crawl
# → ./html/google.html が生成される

# HTML ファイルからスクレイピングして JSON データをまとめる
$ pipenv run scrape
# → ./json/google.json が生成される
```

- Docker で実行する場合

```sh
# Docker イメージを作成し my-python コンテナを起動する
$ docker-compose up -d

# my-python コンテナにアタッチする
$ docker exec -it my-python bash

# 環境構築・実行
$$ pipenv install -dev
$$ pipenv run crawl
$$ pipenv run scrape
```


## Author

[Neo](http://neo.s21.xrea.com/) ([@Neos21](https://twitter.com/Neos21))


## Links

- [Neo's World](http://neo.s21.xrea.com/)
- [Corredor](http://neos21.hatenablog.com/)
- [Murga](http://neos21.hatenablog.jp/)
- [El Mylar](http://neos21.hateblo.jp/)
- [Neo's GitHub Pages](https://neos21.github.io/)
- [GitHub - Neos21](https://github.com/Neos21/)
