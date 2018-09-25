import sys
import boto3
import time
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

#this function executes for each row
def modify_line(next_line):

    date_str = datetime.strptime(next_line["contract_date"], '%Y-%m-%d')
    yyyymm = "%s%02d" % (date_str.year, date_str.month)
 
    #do any transformation here:
    new_line = {
        "contract_id": next_line["contract_id"],
        "contract_amt": next_line["contract_amt"],
        "contract_date": next_line["contract_date"],
        "dt": yyyymm
    }

    return new_line

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

s3 = boto3.resource('s3')
bucket = s3.Bucket('tmp-data-lake')

#delete entire tanle in S3
objects_to_delete = []
for obj in bucket.objects.filter(Prefix='contracts/'):
    objects_to_delete.append({'Key': obj.key})

#objects_to_delete.append({'Key': target_bucket})
if len(objects_to_delete) > 0:
    bucket.delete_objects(
        Delete={
            'Objects': objects_to_delete
        }
    )
    time.sleep(10)

client = boto3.client('s3')

#create empty folder
response = client.put_object(
    Bucket='tmp-data-lake',
    Body='',
    Key='contracts/'
)

time.sleep(5)

datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "tmp-landing-zone", table_name = "contracts", transformation_ctx = "datasource0")

#do transformations on rows (function modify_line)
transformed_frame = Map.apply(frame=datasource0, f=modify_line, transformation_ctx = "transformed_frame")

applymapping1 = ApplyMapping.apply(frame = transformed_frame, mappings = [("contract_id", "long", "contract_id", "long"), ("contract_amt", "long", "contract_amt", "long"), ("contract_date", "string", "contract_date", "string"), ("dt", "string", "dt", "string")], transformation_ctx = "applymapping1")

resolvechoice2 = ResolveChoice.apply(frame = applymapping1, choice = "make_struct", transformation_ctx = "resolvechoice2")

dropnullfields3 = DropNullFields.apply(frame = resolvechoice2, transformation_ctx = "dropnullfields3")

#to store the data partitioned add "partitionKeys": ["<list of partition keys>"] to connection parameters
datasink4 = glueContext.write_dynamic_frame.from_options(frame = dropnullfields3, connection_type = "s3", connection_options = {"path": "s3://tmp-data-lake/contracts", "partitionKeys": ["dt"]}, format = "parquet", transformation_ctx = "datasink4")
job.commit()