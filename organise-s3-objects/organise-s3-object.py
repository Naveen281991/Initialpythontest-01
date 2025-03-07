
import boto3
from datetime import datetime


todays_date = today.strftime("%Y%m%d")

def lambda_handler(event, context):
        
    s3_client = boto3.client('s3')


    bucket_name = "pythonlambda-12"

    list_objects_response = s3_client.list_objects_v2(Bucket="pythonlambda-12")
    get_contents = list_objects_response.get("contents")
    get_all_s3_objects_and_folder_names = []

    
    if get_contents:
      for item in get_contents:
        s3_object_name = item.get("content-type")
        



    get_all_s3_objects_and_folder_names.append("pythonlambda-12")  



    get_all_s3_objects_and_folder_names

    ['Appple.jpg', 'dog.xml', 'House.jpeg', 'index.html']


    directory_names = todays_date + "/"


    if directory_names not in get_all_s3_objects_and_folder_names:
        s3_client.put_object(Bucket="pythonlambda-12", Key=directory_names) 


    response = s3_client.list_objects_v2(Bucket="pythonlambda-12")


    get_contents = response.get("Contents", [])


    for item in get_contents:
            object_creation_date = item["LastModified"].strftime("%Y%m%d") + "/"  # Corrected variable usage
            object_name = item["Key"]

            # Ensure we are moving only files (not folders)
            if object_creation_date == directory_names and "/" not in object_name:
                copy_source = {"Bucket": bucket_name, "Key": object_name}


    if object_creation_date == "pythonlambda-12" and "/" not in object_name:
            s3_client.copy_object(Bucket=bucket_name, CopySource=bucket_name+"/"+object_name, Key="pythonlambda-12"+object_name)
            s3_client.delete_object(Bucket=bucket_name, Key=object_name)


