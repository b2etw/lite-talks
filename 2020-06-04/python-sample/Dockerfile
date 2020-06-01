FROM python:3-slim

ADD . /python-sample
WORKDIR /python-sample

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","app.py"]