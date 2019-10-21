from pathlib import Path
import platform
import time

# MacOS では executable_path で指定しないと上手く読み込めなかった
#import chromedriver_binary

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# メイン
def main():
  prepareHtmlDirectory()
  driver = createDriver()
  
  pageSource = getPageSource(driver, 'http://google.com/')
  writePageSource(pageSource, 'google.html')
  
  time.sleep(1)
  driver.quit()

# ChromeDriver を生成する
def createDriver():
  # ChromeDriver のパスを指定する
  executablePath = '/usr/local/bin/chromedriver'
  # Chrome オプション
  chromeOptions = webdriver.ChromeOptions()
  # MacOS では Headless モードにすると上手く起動しなかったので避ける
  if platform.system() != 'Darwin':
    chromeOptions.add_argument('--headless')
  chromeOptions.add_argument('--disable-gpu')
  chromeOptions.add_argument('--no-sandbox')
  # ChromeDriver を生成する
  # - もしグローバル変数を変更する場合は 'global driver' とグローバル宣言を行う
  driver = webdriver.Chrome(executable_path = executablePath, options = chromeOptions)
  return driver

# ./html/ ディレクトリを作成する
def prepareHtmlDirectory():
  htmlDir = Path(Path.cwd()).joinpath('html')
  if not htmlDir.exists():
    htmlDir.mkdir()
    print('Create HTML Directory')
  else:
    print('HTML Directory is already exists')

# URL を指定してソースを取得する
def getPageSource(driver, url):
  driver.get(url)
  print(f'{url} : {driver.title}')
  return driver.page_source

# ソースをファイルに書き出す
def writePageSource(pageSource, fileName):
  file = Path(Path.cwd()).joinpath('html').joinpath(fileName)
  file.write_text(pageSource)
  print('Write')

# 実行
main()
