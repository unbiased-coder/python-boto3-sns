import pprint
from boto3_helper import init_aws_session

session = init_aws_session()
sns = session.client('sns')

topic = sns.create_topic(Name='unbiased-coder-sns-topic')
pprint.pprint(topic)
