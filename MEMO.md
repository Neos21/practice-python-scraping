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

```sh
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
```

- 単一行コメントアウトはシャープ `#`
  - Pipfile もシャープでコメントアウトできる
- 複数行コメントアウトはダブルクォート3つ `"""` で囲む
- シングルクォートとダブルクォートの違いはなし (JavaScript と同じ)
- `print(f'str')` は `print('str'.format())` の糖衣構文
