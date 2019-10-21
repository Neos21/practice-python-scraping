from pathlib import Path

from bs4 import BeautifulSoup

# メイン
def main():
  html = getHtml('google.html')
  
  # BeautifulSoup でパースする
  soup = BeautifulSoup(html, 'html.parser')
  
  # id 指定で要素を1つ取得してみる : select() を使うと CSS セレクタで取得できる
  print('#footer > p')
  print('  ' + soup.select('#footer > p')[0].string)
  
  # p 要素を全て取得してみる
  paragraphElements = soup.find_all('p')
  print('p')
  # 配列の長さを取得してループすることで index を取得する
  # index が不要なら for paragraphElement in paragraphElements: としても良い
  for index in range(len(paragraphElements)):
    paragraphElement = paragraphElements[index]
    print(f'  [{index}] : {paragraphElement.string}')
  
  print('End')

# HTML ファイルを読み込んで中身を返す
def getHtml(fileName):
  file = Path(Path.cwd()).joinpath('html').joinpath(fileName)
  htmlStr = file.read_text()
  return htmlStr

# 本ファイルをインポートした時に main() 関数が実行されないようにする
if __name__ == '__main__':
  main()
