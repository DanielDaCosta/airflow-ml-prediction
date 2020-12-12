FROM puckel/docker-airflow

WORKDIR /airflow
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt