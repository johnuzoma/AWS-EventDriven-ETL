# AWS-EventDriven-ETL

#### Solution Architecture
![AWS-Event-Driven-ETL drawio](https://github.com/user-attachments/assets/e47fbb9a-6372-44e0-92b9-52ef748128c6)

#### Purpose
I created this project to demonstrate my skills in event-driven applications.

#### Event
When an Excel file is uploaded to a specific folder (landing-zone) in S3 bucket. I configured this by creating an event rule using Amazon EventBridge. [Link](https://github.com/johnuzoma/AWS-EventDriven-ETL/blob/main/event-pattern.json) to JSON file.
#### Action
A Step Function that includes a series of activities including:
- A Python-based Lambda function to process raw Excel data from landing-zone, which includes using 2nd row as headers, removing blank rows, and saving in CSV format in another S3 folder (New) while automatically deleting the source file. [Link](https://github.com/johnuzoma/AWS-EventDriven-ETL/blob/main/Lambda%20functions/1.%20process-raw-data/lambda_function.py) to code.
- A Python-based Glue Job that reads the CSV file from New folder. [Link](https://github.com/johnuzoma/AWS-EventDriven-ETL/blob/main/Glue%20job/sample-job.py) to code.
- A Python-based Lambda function to move the CSV file from New to Processed, renaming the file to include a timestamp in Processed. [Link](https://github.com/johnuzoma/AWS-EventDriven-ETL/blob/main/Lambda%20functions/2.%20move-csv-to-processed/lambda_function.py) to code.

To get this to work, I had to configure some IAM roles and permissions.

Below is the workflow in AWS Step Functions.

<img width="395" alt="workflow" src="https://github.com/user-attachments/assets/4d57738f-7e7b-43d4-9493-1e39c1920732">

#### Video Demo
Coming soon.
