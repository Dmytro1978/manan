# AWS Glue job "glj_employee"
import boto3
import time
import sys
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

def date_to_partition_format(p_date, p_format):
    date_str = datetime.strptime(p_date, p_format)
    return "%s-%02d-%02d" % (date_str.year, date_str.month, date_str.day)

#this function gets executed for each row
def modify_line(next_line):
    dt_prt = date_to_partition_format(next_line["CREATE_DATE"], '%Y-%m-%d %H:%M:%S')
    
    #do any transformation here:
    
    new_line={}
    new_line["ID"]           = next_line["ID"]
    new_line["NAME"]         = next_line["NAME"]
    new_line["AGE"]          = next_line["AGE"]
    new_line["SEX"]          = next_line["SEX"]
    new_line["CREATE_DATE"]  = next_line["CREATE_DATE"]
    new_line["PROCESS_NAME"] = next_line["PROCESS_NAME"]
    new_line["UPDATE_DATE"]  = next_line["UPDATE_DATE"]
    
    #for key,value in next_line.iteritems(): # this code does not work if the source is Avro 
    #    new_line[key.upper()]= value
        
    new_line["dt"] = dt_prt # <-- creating a partition column
    
    return new_line

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'bucket_name', 'source_database', 'source_table_name', 'targer_database', 'target_table_name', 'column_mapping', 'load_type', 'partitioning', 'partition_column'])

bucket_name = args["bucket_name"]
source_database = args["source_database"]
source_table_name = args["source_table_name"]
targer_database = args["targer_database"]
target_table_name = args["target_table_name"]
column_mapping = args["column_mapping"]
load_type = args["load_type"]
partitioning = args["partitioning"]
partition_column = args["partition_column"]
 

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "mdmytro_dw3_staging", table_name = "employee", transformation_ctx = "datasource0")
#datasource0.printSchema()

# -------delete existing table folder START---------
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

objects_to_delete = []

#for obj in bucket.objects.filter(Prefix='core/employee/'): # loops through all objects in "core/employee/". It's inefficient if we want to delete all objects in "core/employee/", it's better to delete the "core/employee/" itself and then create it again 
#    objects_to_delete.append({'Key': obj.key})
    
objects_to_delete.append({'Key': 'core/employee/'})

#objects_to_delete.append({'Key': target_bucket})
if len(objects_to_delete) > 0:
    bucket.delete_objects(
        Delete={
            'Objects': objects_to_delete
        }
    )
    time.sleep(10) # let the objects get deleted

client = boto3.client('s3')

#create empty folder
response = client.put_object(
    Bucket=bucket_name,
    Body='',
    Key='core/employee/'
)
# -------delete existing table folder END---------

time.sleep(5)

transformed_frame = Map.apply(frame = datasource0, f=modify_line, transformation_ctx = "transformed_frame")

applymapping1 = ApplyMapping.apply(frame = transformed_frame, mappings = [("id", "string", "id", "string"), ("name", "string", "name", "string"), ("age", "string", "age", "string"), ("sex", "string", "sex", "string"), ("create_date", "string", "create_date", "string"), ("process_name", "string", "process_name", "string"), ("update_date", "string", "update_date", "string"), ("dt", "string", "dt", "string")], transformation_ctx = "applymapping1")

resolvechoice2 = ResolveChoice.apply(frame = applymapping1, choice = "make_struct", transformation_ctx = "resolvechoice2")

dropnullfields3 = DropNullFields.apply(frame = resolvechoice2, transformation_ctx = "dropnullfields3")

datasink4 = glueContext.write_dynamic_frame.from_options(frame = dropnullfields3, connection_type = "s3", connection_options = {"path": "s3://mdmytro-dw3/core/employee", "partitionKeys": ["dt"]}, format = "parquet", transformation_ctx = "datasink4")

job.commit()