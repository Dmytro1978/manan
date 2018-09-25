import sys
import boto3
import time
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

def date_to_partition_format(p_date, p_format):
    date_str = datetime.strptime(p_date, p_format)
    return "%s%02d" % (date_str.year, date_str.month)

#this function executes for each row
def modify_line(next_line):

    dt_prt = date_to_partition_format(next_line["trans_date"], '%Y-%m-%d')
 
    #do any transformation here:
    new_line = {
        "trans_id": next_line["trans_id"],
        "trans_amt": next_line["trans_amt"],
        "trans_date": next_line["trans_date"],
        "dt": dt_prt
    }

    return new_line

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "tmp-landing-zone", table_name = "transactions", transformation_ctx = "datasource0")

#convert to DataFrame to retrieve date values (YYYY-MM-DD) to generate partition names (dt=YYYYMM)
data_frame = datasource0.toDF()

#retrieve values for TRANS_DATE column
date_lst = data_frame.select("trans_date").collect()

s3 = boto3.resource('s3')
bucket = s3.Bucket('tmp-data-lake')

#generate a list of partitions
prt_dic = {}
for trans_date in date_lst:
    dt_prt = date_to_partition_format(trans_date[0], '%Y-%m-%d')
    prt_dic[dt_prt] = dt_prt #adding to the dictionary eliminates duplicates

#delete partitions
for prt_key in prt_dic:
 
    objects_to_delete = []
    for obj in bucket.objects.filter(Prefix='transactions/dt='+ prt_key + '/'):
        objects_to_delete.append({'Key': obj.key})

    #objects_to_delete.append({'Key': target_bucket})
    if len(objects_to_delete) > 0:
        bucket.delete_objects(
            Delete={
                'Objects': objects_to_delete
            }
        )
        
time.sleep(10) #wait for folders in S3 to be deleted

#do transformations on rows (function modify_line)
transformed_frame = Map.apply(frame=datasource0, f=modify_line, transformation_ctx = "transformed_frame")

applymapping1 = ApplyMapping.apply(frame = transformed_frame, mappings = [("trans_id", "long", "trans_id", "long"), ("trans_amt", "long", "trans_amt", "long"), ("trans_date", "string", "trans_date", "string"), ("dt", "string", "dt", "string")], transformation_ctx = "applymapping1")

resolvechoice2 = ResolveChoice.apply(frame = applymapping1, choice = "make_struct", transformation_ctx = "resolvechoice2")

dropnullfields3 = DropNullFields.apply(frame = resolvechoice2, transformation_ctx = "dropnullfields3")

#to store the data partitioned add "partitionKeys": ["<list of partition keys>"] to connection parameters
datasink4 = glueContext.write_dynamic_frame.from_options(frame = dropnullfields3, connection_type = "s3", connection_options = {"path": "s3://tmp-data-lake/transactions", "partitionKeys": ["dt"]}, format = "parquet", transformation_ctx = "datasink4")

job.commit()