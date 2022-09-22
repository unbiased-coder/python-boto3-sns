import pprint
from boto3_helper import init_aws_session

session = init_aws_session()
sns = session.client('sns')

topic = sns.delete_topic(TopicArn='arn:aws:sns:us-east-1:033533902081:unbiased-coder-sns-topic')
pprint.pprint(topic)
