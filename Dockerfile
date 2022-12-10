FROM python:3.10-alpine
RUN apk add gcc --no-cache
WORKDIR /bot
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app .

RUN cd /bot/app
CMD ["python", "__main__.py"]