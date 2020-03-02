FROM python:3
ENV PYTONHUNBUFFRED 1 #pythonの標準（エラー）出力をbufferに溜め込まないための設定
RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/