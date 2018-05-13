import urllib.parse
import boto3
import json
import urllib

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
        param = urllib.parse.parse_qs(event['requestParameters'])
        label = param['Label'][0]
        user_id = param['UserID'][0]
        slack_id = param['SlackID'][0]
        user_type = param['UserType'][0]
        backlog_assinee = param['BacklogAssinee'][0]
        backlog_assinee_id = param['BacklogAssineeID'][0]
        phonenumber = param['PhoneNumber'][0]
        international_number = param['InternationalNumber'][0]

        if "Delete" in param:
            delete = param['Delete'][0]
        else:
            delete = "false"

        users = get_users_list()
        users.append({
            "Label": label,
            "UserID": user_id,
            "SlackID": slack_id,
            "UserType": user_type,
            "BacklogAssinee": backlog_assinee,
            "BacklogAssineeID": backlog_assinee_id,
            "PhoneNumber": phonenumber,
            "InternationalNumber": international_number,
            "Delete": delete
            })

        line_json = json.dumps(
            users, sort_keys=False, ensure_ascii=False, indent=4)
        print(line_json)
        s3 = boto3.resource('s3')
        obj = s3.Object(AWS_S3_BUCKET_NAME, JSON_NAME)
        obj.put(Body=line_json)

        return {
            'statusCode': 200,
            'headers': {
                    'access-control-allow-origin': '*',
                    'content-type': 'application/json'
            },
            'data': {
                "Label": label,
                "UserID": user_id,
                "SlackID": slack_id,
                "UserType": user_type,
                "BacklogAssinee": backlog_assinee,
                "BacklogAssineeID": backlog_assinee_id,
                "PhoneNumber": phonenumber,
                "InternationalNumber": international_number,
                "Delete": delete
            },
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
            'completed' : 0
        }
