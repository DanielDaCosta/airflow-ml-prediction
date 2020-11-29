from os import getenv

# Input Data
READ_BUCKET = getenv('READ_BUCKET')
READ_DATA_PATH = getenv('READ_DATA_PATH')
READ_MODELS_PATH = getenv('READ_MODELS_PATH')

# Output Data
WRITE_BUCKET = getenv('WRITE_BUCKET')
WRITE_DATA_PATH = getenv('WRITE_DATA_PATH')