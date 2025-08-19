# Python ランタイム（軽量）
FROM python:3.12-slim

# 便利な環境変数
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 依存に必要なツール（mysqlclient使わないので最低限でOK）
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 依存インストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# アプリ本体
COPY . /app

EXPOSE 5000

# backend をパッケージとして起動
CMD ["python", "-m", "backend.app"]
