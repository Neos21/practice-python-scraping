FROM joyzoursky/python-chromedriver:3.7-selenium

# - Vi・Vim が入っていないのでインストールする
# - pip をアップデートして pipienv をインストールする
RUN set -x && \
  apt-get update && \
  apt-get install -y vim && \
  pip install --upgrade pip && \
  pip install pipenv
