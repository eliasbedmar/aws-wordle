# import pandas as pd
#
# df = pd.read_csv('./AwsServices.csv')
#
# for index, row in df.iterrows():
#     svc.append(row[0])

svc = [
    'execute-api', 'apigateway', 'apigateway', 'appflow', 'app-integrations', 'appstream', 'athena', 'braket', 'chime',
    'clouddirectory', 'cloudfront', 'cloudsearch', 'cloudwatch', 'evidently', 'logs', 'synthetics', 'codeguru',
    'codeguru-profiler', 'codeguru-reviewer', 'cognito-identity', 'cognito-sync', 'cognito-idp', 'comprehend',
    'comprehendmedical', 'connect', 'profile', 'voiceid', 'wisdom', 'dlm', 'detective', 'devops-guru', 'dynamodb',
    'dax', 'ec2', 'autoscaling', 'imagebuilder', 'ec2-instance-connect', 'ebs', 'ecr', 'ecr-public', 'ecs',
    'elasticfilesystem', 'elastic-inference', 'eks', 'elasticmapreduce', 'elastictranscoder', 'elasticache',
    'emr-containers', 'events', 'schemas', 'finspace', 'forecast', 'frauddetector', 'freertos', 'fsx', 'gamelift',
    'glacier', 'groundtruthlabeling', 'guardduty', 'healthlake', 'honeycode', 'inspector', 'inspector2', 'ivs',
    'kendra', 'cassandra', 'kinesis', 'kinesisanalytics', 'kinesisanalytics', 'firehose', 'kinesisvideo', 'lex',
    'lex', 'lightsail', 'geo', 'lookoutequipment', 'lookoutmetrics', 'lookoutvision', 'machinelearning', 'macie2',
    'macie', 'managedblockchain', 'grafana', 'aps', 'kafka', 'kafkaconnect', 'airflow', 'mechanicalturk', 'memorydb',
    'ec2messages', 'mobileanalytics', 'monitron', 'mq', 'neptune-db', 'nimble', 'es', 'personalize', 'mobiletargeting',
    'ses', 'sms-voice', 'polly', 'qldb', 'quicksight', 'rds', 'rds-data', 'rds-db', 'redshift', 'redshift-data',
    'rekognition', 'tag', 'route53', 'route53domains', 'route53-recovery-cluster', 'route53-recovery-control-config',
    'route53-recovery-readiness', 'route53resolver', 's3', 's3-object-lambda', 's3-outposts', 'sagemaker', 'ses',
    'ssmmessages', 'ses', 'swf', 'sdb', 'sns', 'sqs', 'storagegateway', 'sumerian', 'textract', 'timestream', 'transcribe',
    'translate', 'workdocs', 'worklink', 'workmail', 'workmailmessageflow', 'workspaces', 'wam', 'workspaces-web',
    'mediaimport', 'kafka-cluster', 'discovery', 'arsenal', 'account', 'activate', 'amplify', 'amplifybackend',
    'amplifyuibuilder', 'appmesh', 'appmesh-preview', 'apprunner', 'appconfig', 'application-autoscaling',
    'application-cost-profiler', 'mgn', 'appsync', 'artifact', 'auditmanager', 'autoscaling-plans', 'backup',
    'backup-gateway', 'backup-storage', 'batch', 'aws-portal', 'budgets', 'bugbust', 'acm', 'acm-pca', 'chatbot',
    'cloudformation', 'servicediscovery', 'cloud9', 'cloudformation', 'cloudhsm', 'cloudshell', 'cloudtrail',
    'rum', 'codeartifact', 'codebuild', 'codecommit', 'codedeploy', 'codepipeline', 'codestar', 'codestar-connections',
    'codestar-notifications', 'compute-optimizer', 'config', 'awsconnector', 'controltower', 'cur', 'ce', 'dataexchange',
    'dms', 'deepcomposer', 'deeplens', 'deepracer', 'devicefarm', 'directconnect', 'ds', 'elasticbeanstalk', 'drs',
    'elemental-appliances-software', 'elemental-activations', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage',
    'mediapackage-vod', 'mediastore', 'mediatailor', 'fis', 'fms', 'globalaccelerator', 'glue', 'databrew', 'groundstation',
    'health', 'access-analyzer', 'identitystore', 'importexport', 'iot', 'iot1click', 'iotanalytics', 'iotdeviceadvisor',
    'iotwireless', 'iot-device-tester', 'iotevents', 'iotfleethub', 'iotfleetwise', 'greengrass', 'greengrass', 'iotroborunner',
    'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iq', 'iq-permission', 'kms', 'lakeformation', 'lambda', 'license-manager',
    'aws-marketplace', 'aws-marketplace', 'marketplacecommerceanalytics', 'aws-marketplace', 'aws-marketplace',
    'aws-marketplace-management', 'aws-marketplace', 'aws-marketplace', 'aws-marketplace', 'serviceextract', 'mgh',
    'refactor-spaces', 'migrationhub-strategy', 'mobilehub', 'network-firewall', 'opsworks', 'opsworks-cm', 'organizations',
    'outposts', 'panorama', 'pi', 'pricing', 'proton', 'purchase-orders', 'resiliencehub', 'ram', 'resource-groups',
    'robomaker', 'savingsplans', 'secretsmanager', 'securityhub', 'sts', 'sms', 'serverlessrepo', 'servicecatalog',
    'shield', 'signer', 'snow-device-management', 'snowball', 'sqlworkbench', 'sso', 'sso-directory', 'states', 'support',
    'ssm', 'ssm-guiconnect', 'ssm-incidents', 'ssm-contacts', 'resource-explorer', 'tiros', 'transfer', 'trustedadvisor',
    'waf', 'waf-regional', 'wafv2', 'wellarchitected', 'xray', 'datasync', 'applicationinsights', 'datapipeline', 'dbqms',
    'elasticloadbalancing', 'elasticloadbalancing', 'elemental-support-cases', 'elemental-support-content', 'connect-campaigns',
    'iam', 'launchwizard', 'networkmanager', 'rbin', 'servicequotas'
]

svc_lenghts = set()

for i in svc:
    ln = len(i)
    svc_lenghts.add(ln)

print(svc_lenghts)

svc_lenghts_freq = {}
for l in svc_lenghts:
    svc_lenghts_freq[l] = 0

for s in svc:
    svc_lenghts_freq[len(s)] += 1

print(svc_lenghts_freq)

svc_3 = []
svc_6 = []
svc_5 = []
svc_7 = []

for s in svc:
    if len(s) == 3:
        svc_3.append(s)
    if len(s) == 6:
        svc_6.append(s)
    if len(s) == 7:
        svc_7.append(s)
    if len(s) == 5:
        svc_5.append(s)

print(svc_3)
print(svc_6)
print(svc_7)
print(svc_5)