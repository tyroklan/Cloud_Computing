import boto3
import os
import webbrowser

# Choose your bucket name (if error occurs change bucket name)
BUCKET_NAME = 'image-upload-6001'
URL_AWS = '.s3.amazonaws.com/'
HTTP = 'https://'
filenames = []

# Enter your AWS S3 IAM Access Key and Secret Access Key
ACCESS_KEY = '********************'
SECRET_ACCESS_KEY = '****************************************'


# Creates the bucket
client = boto3.client('s3', aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_ACCESS_KEY)
response = client.create_bucket(
    ACL='public-read',
    Bucket= BUCKET_NAME,
)

# Store the names of the files in the array
for file in os.listdir():
    if '.jpg' in file:
        filenames.append(file)


# Loads each file in the folder from the Python file with extension .jpg into the bucket
for file in os.listdir():
    if '.jpg' in file:
        upload_file_bucket = BUCKET_NAME
        upload_file_key = str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key, ExtraArgs={'ACL':'public-read'})

# opens the browser with the URL of each image
for x in filenames:
    webbrowser.open_new(HTTP + BUCKET_NAME + URL_AWS + x)

