FROM python:3.8.16-slim

COPY . /app/

WORKDIR /app

RUN apt-get update
RUN pip install -r requirements.txt

EXPOSE 1234

ENTRYPOINT ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "1234"]
# ENTRYPOINT /usr/local/bin/uvicorn src.main:app --port 1234
# CMD ["gunicorn -k uvicorn.workers.UvicornWorker src.main:app --bind '0.0.0.0:8000'"]