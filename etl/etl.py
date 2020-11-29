try:
    import unzip_requirements
except ImportError:
    pass
import json
import datetime
import pandas as pd
from config import READ_BUCKET, \
    READ_DATA_PATH, \
    READ_MODELS_PATH, \
    WRITE_BUCKET, \
    WRITE_DATA_PATH
from s3_utils import read_csv_from_s3, \
    read_sav_from_s3, \
    save_results


def main():

    # Getting the current time
    start_time = datetime.datetime.now()
    print('Loading CSV from s3')
    df_plan = read_csv_from_s3(READ_BUCKET, f'{READ_DATA_PATH}/test_data.csv',
                               sep=',')

    print('Loading model from s3')
    model = read_sav_from_s3(READ_BUCKET, f'{READ_MODELS_PATH}/xgb_model.sav')

    print('Making prediction')
    predictions = model.predict(df_plan)
    results = pd.Series(data=predictions, index=df_plan.index)

    # Save the results on s3
    s3_results = save_results(WRITE_BUCKET, WRITE_DATA_PATH,
                              results, start_time)
    print(f's3 responses results:\n{s3_results}')

    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "Successfully Executed!"})
    }

    return response