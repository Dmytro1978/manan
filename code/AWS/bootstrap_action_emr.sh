# Copyright 2018 Amazon.com, Inc or its affiliates. All Rights reserved
# Bootstrap steps to run Sqoop on EMR
#!/bin/bash
#set -vx

s3_bucket=mdmytro-dw
s3_binary_folder=binary
s3_unix_shell_folder=unix_shell
s3_src_dir=${s3_bucket}/${s3_folder}
work_dir=/home/hadoop


aws s3 cp s3://${s3_bucket}/${s3_unix_shell_folder}/ ${work_dir} --recursive --exclude "*" --include "run_sqoop*.sh"
chmod 777 ${work_dir}/run_sqoop*.sh



#Copy SQL Server driver for Sqoop
sudo aws s3 cp s3://${s3_bucket}/${s3_binary_folder}/sqljdbc42.jar /usr/lib/sqoop/lib/
#Copy SQL Server 2000 driver for Sqoop
sudo aws s3 cp s3://${s3_bucket}/${s3_binary_folder}/jtds-1.3.1.jar /usr/lib/sqoop/lib/
#Copy Oracle driver for Sqoop 
sudo aws s3 cp s3://${s3_bucket}/${s3_binary_folder}/ojdbc6.jar /usr/lib/sqoop/lib/


#Copy Oracle client, jdbc and sqlplus
aws s3 cp s3://${s3_bucket}/${s3_binary_folder}/oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm ${work_dir}
aws s3 cp s3://${s3_bucket}/${s3_binary_folder}/oracle-instantclient12.1-jdbc-12.1.0.2.0-1.x86_64.rpm ${work_dir}
aws s3 cp s3://${s3_bucket}/${s3_binary_folder}/oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm ${work_dir}

#Install Oracle client, jdbc and sqlplus
sudo rpm -ivh ${work_dir}/oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm
sudo rpm -ivh ${work_dir}/oracle-instantclient12.1-jdbc-12.1.0.2.0-1.x86_64.rpm
sudo rpm -ivh ${work_dir}/oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm


