import boto3
import uuid

def lambda_handler(event, context):
    
    client = boto3.client('s3')
        
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key'] 
        
        if key == 'staging/employee/_SUCCESS':
            ''' For testing
            client = boto3.client('s3')
            
            uuid_ = uuid.uuid4()
            response = client.put_object(
                Bucket='mdmytro-dw3',
                Body='',
                Key='tmp555/' + str(uuid_)
            )
            '''
        
            client = boto3.client('glue')
        
            mapping =  [("trans_id", "long", "trans_id", "long"), ("trans_amt", "long", "trans_amt", "long"), ("trans_date", "string", "trans_date", "string"), ("dt", "string", "dt", "string")]
            
            
            response = client.start_job_run(
                JobName='glj_employee',
                Arguments={
                    '--source_database': 'mdmytro-dw3-staging',
                    '--source_table_name': 'employee',
                    '--targer_database': 'mdmytro-dw3-core',
                    '--target_table_name': 'employee',
                    '--column_mapping': str(mapping),
                    '--load_type': 'full',
                    '--partitioning': 'yes',
                    '--partition_column': 'CREATE_DATE'
                },
                AllocatedCapacity=10,
                Timeout=10,
                NotificationProperty={
                    'NotifyDelayAfter': 20
                }
            )