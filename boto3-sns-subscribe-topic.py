import pprint
from boto3_helper import init_aws_session

session = init_aws_session()
sns = session.client('sns')
sns_resource = session.resource('sns')

topics = sns.list_topics()
topic_arn = topics['Topics'][0]['TopicArn']
topic = sns_resource.Topic(arn=topic_arn)
subscription = topic.subscribe(Protocol='email', Endpoint='info@unbiased-coder.com', ReturnSubscriptionArn=True)
pprint.pprint(subscription)