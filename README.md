# Practice Python Scraping

Python でスクレイピングする


## Installation

```sh
# Python 3.7・pip3 は各自インストールしておく・pipenv をインストールする
$ pip install pipenv

# pipenv で環境復元する
$ pipenv install --dev

# pipenv 経由でサンプルスクリプトを実行する
$ pipenv run start
# pipenv run python example_crawl.py
# → ./html/google.html が生成される

# HTML ファイルからスクレイピングして JSON データをまとめる
$ pipenv run python example_scrape.py
# → ./json/google.json が生成される
```
