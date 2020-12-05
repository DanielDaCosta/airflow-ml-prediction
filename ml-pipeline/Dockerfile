FROM python:3.7-slim

ENV APP_DIR /ml-pipeline

RUN mkdir -p ${APP_DIR}

WORKDIR ${APP_DIR}

COPY . .
RUN apt-get update
RUN apt-get install libgomp1
RUN pip install -r requirements.txt

ENV READ_BUCKET=ml-sls-deploy-prd
ENV READ_DATA_PATH=data
ENV READ_MODELS_PATH=models
ENV WRITE_BUCKET=ml-sls-deploy-prd-results
ENV WRITE_DATA_PATH=results

CMD ["python", "main.py"]