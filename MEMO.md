# 2019-10-19

- https://qiita.com/sl2/items/1e503952b9506a0539ea
  - pipenv
- https://qiita.com/derodero24/items/9e9567790bde9e4b9d0c
- https://hacknote.jp/archives/48685/
  - selenium・chromedriver-binary
- https://qiita.com/akiko-pusu/items/86faca0cb9c877896c04
  - chromedriver-binary のバージョン調整
- https://qiita.com/toto1310/items/a8ab8391bc8169721b4f
  - `Pipfile` の `[scripts]` セクション
- https://github.com/pypa/pipenv/issues/598
  - `Pipfile.lock` を Git 管理して良いか
- https://dividable.net/python/python-scraping/
- https://qiita.com/Azunyan1111/items/b161b998790b1db2ff7a
  - スクレイピング

環境構築メモ。

```sh
# pip3 で pipenv をインストールする
$ pip install pipenv

# Pipfile を生成する
$ pipenv --python 3.7

# Selenium
$ pipenv install selenium

# Chrome のバージョンに合わせてインストールする
$ pipenv install chromedriver-binary~=77.0

# 実行してみる
$ python example.py

# Pipfile の '[scripts] start = ' に書いたスクリプトを実行する
$ pipenv run start

# pipenv を効かせて実行するには以下のように書く
$ pipenv run python example.py
```

- VSCode の Python Extension Pack をインストールしておくと良い
- 単一行コメントアウトはシャープ `#`
  - Pipfile もシャープでコメントアウトできる
- 複数行コメントアウトはダブルクォート3つ `"""` で囲む
- シングルクォートとダブルクォートの違いはなし (JavaScript と同じ)
- `print(f'str')` は `print('str'.format())` の糖衣構文


# 2019-10-21

- MacOS で試したらヘッドレス Chrome が上手く動かなかった
  - `--headless` を外し、`chromedriver_binary` を使わずに `executable_path` を指定すれば動いた
- 関数定義は `def`
  - インタプリタなのでグローバルなスコープから未定義の関数を呼び出せない
  - メイン処理を先頭に書きたい場合は `main()` 関数を定義し、末尾で `main()` を実行すれば良い
- 当該 `.py` ファイルを `import` されたときに `main()` 関数を実行しないようにするには、`if __name__ == '__main__':` という条件で判断すれば良い
- `if:`・`elif:`・`else:`。真偽値を反転するには `!` ではなく `not` を使う
- `pathlib.Path` でファイルやディレクトリの操作ができる
- 辞書 (Dict) は `{}` で宣言し、`myDict['key'] = value` と設定していく
- リスト (List) は `[]` で宣言し、`myList.append(item)` と追加していく
- 辞書は `import json` モジュールの `json.dump()` を使えば、JSON 形式に変換してファイルに保存できる

```sh
# HTML のパースに使える BeautifulSoup4 をインストールする
$ pipenv install beautifulsoup4
```

- ドキュメンテーションコメントのことは docstring と呼ぶ。書き方には種類があるが、複数行コメントで関数内などに書けば良い


# 2019-11-05

- `write_text()` では `newline = '\n'` が指定できなかった
- Docker Compose でまとめてみる

```sh
$ docker-compose up -d
Building my-python
# …中略…
Creating my-python ... done

$ docker ps
CONTAINER ID        IMAGE                                COMMAND               CREATED             STATUS              PORTS               NAMES
81526a50b822        practice-python-scraping_my-python   "tail -f /dev/null"   10 seconds ago      Up 9 seconds                            my-python

$ docker exec -it my-python bash
# docker-dompose.yaml の working_dir で指定したディレクトリで bash 接続できる

# 環境構築・実行
$$ pipenv install -dev
$$ pipenv run crawl
$$ pipenv run scrape
```
