#!/bin/bash
#set -vx
 
spark-submit \
    --deploy-mode client \
    --master yarn \
    --name sample_spark_job \
    --conf spark.executor.instances=6 \
    --conf spark.hadoop.fs.s3.consistent=false \
    --conf spark.dynamicAllocation.enabled=false \
    --conf spark.app.params.dedupe.parallelism=5 \
    --conf spark.driver.memory=8G \
    --conf spark.speculation=false \
    --conf spark.executor.memory=4G \
    --conf spark.executor.memoryOverhead=4G \
    --conf spark.driver.maxResultSize=0 \
    --conf spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version=2 \
    --conf spark.executor.extraJavaOptions="-XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:ParallelGCThreads=24 -XX:ConcGCThreads=8" \
    --jars s3://my-bucket/my_jars/my_job.jar \
    --class main_class s3://my-bucket/my_jars/my_job.jar \
    s3://my-bucket/my_job_parameters/my_job_params.json >> sample_spark_job.log 2>&1