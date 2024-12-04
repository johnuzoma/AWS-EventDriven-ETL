import boto3
import datetime as dt

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucket = 'mybucket-dec-2024'

    source_key = 'New/deminis.csv'
    destination_key = f"Processed/deminis-{dt.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')}.csv"

    try:
        # Copy the file to the new location
        s3.copy_object(
            Bucket=bucket,
            CopySource={'Bucket': bucket, 'Key': source_key},
            Key=destination_key
        )

        # Delete the original file
        s3.delete_object(
            Bucket=bucket,
            Key=source_key
        )
        
        return {
            'statusCode': 200,
            'body': f'Successfully moved {source_key} to {destination_key}'
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': f'Error moving file: {str(e)}'
        }
