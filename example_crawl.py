from pathlib import Path
import platform
import time

# MacOS では executable_path で指定しないと上手く読み込めなかった
import chromedriver_binary

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
  """
  メイン関数
  """
  
  prepareHtmlDirectory()
  driver = createDriver()
  
  pageSource = getPageSource(driver, 'http://google.com/')
  writePageSource(pageSource, 'google.html')
  
  time.sleep(1)
  driver.quit()

def createDriver():
  """
  Chrome WebDriver を生成する
  
  Returns
  -------
  driver : webdriver.Chrome
    WebDriver
  """
  
  # ChromeDriver のパスを指定する
  #executablePath = '/usr/local/bin/chromedriver'
  # Chrome オプション
  chromeOptions = webdriver.ChromeOptions()
  # MacOS では Headless モードにすると上手く起動しなかったので避ける
  if platform.system() != 'Darwin':
    print('Headless Mode')
    chromeOptions.add_argument('--headless')
  chromeOptions.add_argument('--disable-gpu')
  chromeOptions.add_argument('--no-sandbox')
  # ChromeDriver を生成する : もしグローバル変数を変更する場合は 'global driver' とグローバル宣言を行う
  driver = webdriver.Chrome(
    #executable_path = executablePath,
    options = chromeOptions
  )
  return driver

def prepareHtmlDirectory():
  """
  ./html/ ディレクトリを作成する
  """
  
  htmlDir = Path(Path.cwd()).joinpath('html')
  if not htmlDir.exists():
    htmlDir.mkdir()
    print('Create HTML Directory')
  else:
    print('HTML Directory is already exists')

def getPageSource(driver, url):
  """
  URL を指定してソースを取得する
  
  Parameters
  ----------
  driver : webdriver.Chrome
    WebDriver
  url : str
    URL
  
  Returns
  -------
  page_source : str
    HTML ソース
  """
  
  driver.get(url)
  print(f'{url} : {driver.title}')
  return driver.page_source

def writePageSource(pageSource, fileName):
  """
  ソースをファイルに書き出す
  
  Parameters
  ----------
  pageSource : str
    HTML ソース
  fileName : str
    保存ファイル名
  """
  
  file = Path(Path.cwd()).joinpath('html').joinpath(fileName)
  file.write_text(pageSource, encoding = 'utf-8')
  print('Write Success')

# 本ファイルをインポートした時に main() 関数が実行されないようにする
if __name__ == '__main__':
  main()
