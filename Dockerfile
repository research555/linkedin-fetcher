FROM tiangolo/uvicorn-gunicorn:python3.10

ENV APP_HOME /app
ENV PYTHONUNBUFFERED=1

WORKDIR $APP_HOME
COPY . .
RUN pip install -r requirements.txt;

EXPOSE 5000 8000 8080

CMD exec uvicorn app.main:app --host 0.0.0.0 --port $PORT