FROM tiangolo/uvicorn-gunicorn:python3.10

# Set the working directory in the container to /app
ENV APP_HOME /app

WORKDIR $APP_HOME

# Conditionally copy the cached virtual environment and set the PATH
COPY . .
RUN pip install -r requirements.txt;

# Set the environment variable for running the application
ENV PYTHONUNBUFFERED=1

# Expose ports
EXPOSE 5000 8000 8080

# Cloud Run
#CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker --threads 8 --timeout 120 app.main:app

CMD exec uvicorn app.main:app --host 0.0.0.0 --port $PORT