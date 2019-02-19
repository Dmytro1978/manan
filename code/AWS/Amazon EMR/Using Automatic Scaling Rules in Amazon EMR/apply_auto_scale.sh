#!/bin/bash
#set -vx

# Create/update automatic scaling policy for Core Instance Group:
aws emr put-auto-scaling-policy --cluster-id j-XLH3LUMMGOLE --instance-group-id ig-1GOYKOOJJ0LU9 --auto-scaling-policy file://autoscaleconfig-core.json --region us-west-2
 
# Create/updatee automatic scaling policy for Task Instance Group:
aws emr put-auto-scaling-policy --cluster-id j-XLH3LUMMGOLE --instance-group-id ig-HYAJ48P6HQLH --auto-scaling-policy file://autoscaleconfig-task.json  --region us-west-2