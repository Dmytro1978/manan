############################################################################################################################################################
# File: batch_trans_v2.sh
# Author: Dmytro Manannykov (mdmytro@amazon.com), PeopleInsight team
# Description:
#   The script transfers data from multiple tables in a loop (batch processing). For each iteration, the script kicks off "trans_ora_s3.sh" or "trans_s3_rs.sh" 
#   in accordance with first received parameter – "ora_s3" or "s3_rs". The second parameter indicates the number of a file with the list of tables to process. 
#   You can create several text files with dirfferent table lists and process them in parallel on several clusters. 
#   If first parameter is equal to "ora_s3" and the second paramter is equal to 1 then the script kicks off "trans_ora_s3.sh" and transfers the 
#   data from Oracle to S3 for tables listed in "batch_trans_ora_s3_1.txt". If the parameter is equal to "s3_rs" the second paramter is equal to 2 then the 
#   script kicks off "trans_s3_rs.sh" and transfers data from S3 to Redshift for tables listed in "batch_trans_s3_rs_2.txt" 
#   When an iteration is succeeded the program creates SUCCESS flag file for that table on disc. If the iteration fails the program creates FAILURE flag file. 
#   In this case the loop does not break, it allows the process to finish all iteration (regardless of success or failure). In the end of the process if any 
#   step failed the failure code is returned and the cluster reruns the program (there are 3 attempts to rerun). When program reruns it reads SUCCESS and 
#   FAILURE flag files and only runs the transfer script for failed tables.
# Examples: 
#   ./batch_trans_v2.sh ora_s3, 1 # the script will process "batch_trans_ora_s3_1.txt" file
#   ./batch_trans_v2.sh s3_rs, 2 # the script will process "batch_trans_s3_rs_2.txt" file
############################################################################################################################################################

#!/bin/bash
#set -vx

program=`basename "$0"`

if [ $# -lt 2 ]
then
    echo "Too few argumetns! Example: ${program} <flow_type:ora_s3|s3_rs> <cluster_number:1,2,3,4,..>"
    exit 1
fi

flow=$1
cluster_number=$2

function write_log
{
    dt=$(TZ="US/Pacific" date +'%Y-%m-%d%t%H:%M:%S')
    echo "${dt}: ${log_entry}" >> /home/hadoop/$program.log
}

log_entry="Start"; write_log

if [ ! -f /home/hadoop/batch_trans_${flow}_${cluster_number}.txt ]
then
    log_entry="There is no /home/hadoop/batch_trans_${flow}_${cluster_number}.txt file!"; write_log
    exit 1
fi

while read line
do
    if [ -f /home/hadoop/${line}_${flow}_trans_SUCCESS ]
    then
        continue
    else
        /home/hadoop/trans_${flow}.sh $line
        status=$?
        if [ $status -eq 0 ]
        then
            log_entry=" ${line}: transferred"; write_log
            touch /home/hadoop/${line}_${flow}_trans_SUCCESS
            if [ -f /home/hadoop/${line}_${flow}_trans_FAILURE ]
            then
                rm /home/hadoop/${line}_${flow}_trans_FAILURE
            fi
        else
            log_entry="${line}: transfer error!"; write_log
            touch /home/hadoop/${line}_${flow}_trans_FAILURE
        fi
    fi
done < /home/hadoop/batch_trans_${flow}_${cluster_number}.txt

log_entry="Done"; write_log

if ls /home/hadoop/*${flow}_trans_FAILURE >/dev/null 2>&1
then
    exit 1
else
    exit 0
fi