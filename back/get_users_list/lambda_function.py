import boto3
import json

# Labdaの環境変数にする
AWS_S3_BUCKET_NAME = '<User情報のJsonを格納するS3バケットの名前>'
JSON_NAME = '<User情報のJsonファイル名>'


def get_users_list():
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=AWS_S3_BUCKET_NAME, Key=JSON_NAME)
    r = response['Body'].read().decode('utf-8')
    data = json.loads(r)
    return data


def lambda_handler(event, context):
    try:

        users_list = get_users_list()
        print(users_list)

        '''
        電話番号をマスク
        '''
        for user in users_list:
            user["PhoneNumber"] = "***********"
            user["InternationalNumber"] = "***********"
        print(users_list)

        return {
            'statusCode': 200,
            'headers': {
                    'access-control-allow-origin': '*',
                    'content-type': 'application/json'
            },
            'data': users_list,
            'completed': 1

        }

    except Exception:
        import traceback
        traceback.print_exc()
        return {
            'statusCode': 200,
            'headers': {
                    'access-control-allow-origin': '*',
                    'content-type': 'application/json'
            },
            'completed': 0
        }
