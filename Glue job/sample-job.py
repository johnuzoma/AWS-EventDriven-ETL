import boto3
import pandas as pd
import io

# Initialize S3 client
s3 = boto3.client('s3')

# Define your S3 bucket and file path
bucket = 'mybucket-dec-2024'
file_key = 'New/deminis.csv'

# Read the CSV file from S3
obj = s3.get_object(Bucket=bucket, Key=file_key)
df = pd.read_csv(io.BytesIO(obj['Body'].read()))

#print(df.head())