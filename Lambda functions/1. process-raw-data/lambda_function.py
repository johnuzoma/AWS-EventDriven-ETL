import boto3
import pandas as pd
import io

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    bucket = 'mybucket-dec-2024'    
    folder = 'landing-zone'

    # List objects in the landing-zone folder
    response = s3.list_objects_v2(Bucket=bucket, Prefix=folder)

    # Find the Excel file in the folder
    excel_file = next((obj['Key'] for obj in response.get('Contents', []) 
                       if obj['Key'].lower().endswith('.xlsx')), None)

    if excel_file:
        # Read Excel file from S3
        excel_object = s3.get_object(Bucket=bucket, Key=excel_file)
        excel_data = excel_object["Body"].read()

        # Convert to DataFrame using 2nd row as headers
        df = pd.read_excel(io.BytesIO(excel_data), header=1)

        # Remove blank rows
        df = df.dropna(how="all")

        # Convert DataFrame to CSV
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)

        # Upload CSV to S3 (New folder)
        s3.put_object(Bucket=bucket, Key="New/deminis.csv", Body=csv_buffer.getvalue())

        # Delete the original excel file
        s3.delete_object(
            Bucket=bucket,
            Key=excel_file
        )

        return {
            "statusCode": 200,
            "body": f"File {excel_file} was processed and saved as deminis.csv in the 'New' folder"
        }
    else:
        return {
            "statuscode": 200,
            "body": "No Excel file found in the 'landing-zone' folder. No action taken"
        }

