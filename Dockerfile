from python:3.7-alpine

RUN apk add --no-cache gcc musl-dev
ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
ADD . /app
CMD ["/app/startup.sh"]
