import pprint
from boto3_helper import init_aws_session

session = init_aws_session()
sns = session.client('sns')

topics = sns.list_topics()
pprint.pprint(topics)
