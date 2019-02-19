# Using Automatic Scaling Rules in Amazon EMR



This note describes two methods of using the automatic scaling rules in Amazon EMR.
 
## Applying automatic scaling rules via AWS CLI.
 
The following AWS CLI commands will create or update automatic scaling rules for an EMR cluster. You will only need to provide a cluster id and instance group ids. The automatic scaling rules are listed in JSON files (see Appendix A).
 
### Create/update automatic scaling policy for Core Instance Group:

```sh
aws emr put-auto-scaling-policy --cluster-id j-XXXXXXXXXXXX --instance-group-id ig-HYAJ48P6HQLH --auto-scaling-policy file://autoscaleconfig-core.json --region us-west-2
```
### Create/updatee automatic scaling policy for Task Instance Group:

```sh
aws emr put-auto-scaling-policy --cluster-id j-XXXXXXXXXXXX --instance-group-id ig-XXXXXXXXXXXX --auto-scaling-policy file://autoscaleconfig-task.json  --region us-west-2
```

## Applying automatic scaling rules via AWS Management Console.

### Step 1
In AWS Management Console navigate to Amazon EMR user interface, click on EMR cluster you want to activate automatic scaling on and switch to Hardware tab:

![Picture](pic/picture1.png)

### Step 2
In the open tab scroll to the right and find Auto Scaling column. Click on   icon for CORE instance group:

![Picture](pic/picture2.png)

### Step 3
In the opened window fill out all the fields according to the following autoscaling rules:

![Picture](pic/picture3.png)

Scale out automatic scaling policy:
1. ScaleOutYARNLowMemory: Add 2 instances if YARNMemoryAvailablePercentage is less than or equal to 35 for 1 five-minute periods with a cooldown of 120 seconds
2. ScaleOutContainerPending: Add 2 instances if ContainerPendingRatio is greater than 0.75 for 1 five-minute period with a cooldown of 120 seconds
Scale in automatic scaling policy:
3. ScaleInYARNAvailableMemory: Terminate 1 instance if YARNMemoryAvailablePercentage is greater than or equal to 75 for 3 five-minute periods with a cooldown of 300seconds
4. ScaleInContainerAvailable:         Terminate 1 instance if ContainerPendingRatio is less than or equal to 0.15 for 3 five-minute periods with a cooldown of 300 seconds

To find ScaleInYARNAvailableMemory and ContainerPendingRatio metrics you need to scroll to the end of the dropdown list:

![Picture](pic/picture4.png)

### Step 4
The metrics entered for **CORE** instance group should look as follows:

![Picture](pic/picture5.png)

Click *Modify* button to save the changes.

### Step 5
Repeat the steps listed above for **TASK** instance group applying the following rules:

Scale out automatic scaling policy:
1. ScaleOutYARNLowMemory: Add 5 instances if YARNMemoryAvailablePercentage is less than or equal to 35 for 1 five-minute period with a cooldown of 120 seconds
2. ScaleOutContainerPending: Add 5 instances if ContainerPendingRatio is greater than or equal to 0.75 for 1 five-minute period with a cooldown of 120 seconds
Scale in automatic scaling policy:
3. ScaleInYARNAvailableMemory: Terminate 2 instances if YARNMemoryAvailablePercentage is greater than or equal to 75 for 3 five-minute periods with a cooldown of 300seconds
4. ScaleInContainerAvailable: Terminate 2 instances if ContainerPendingRatio is less than or equal to 0.15 for 3 five-minute periods with a cooldown of 300 seconds
 
### Step 6
Once you finish entering the metrics for TASK instance group they should look as follows:

![Picture](pic/picture6.png)

Click *Modify* button to save the changes.

### Step 7
Now you should see the autoscaling rules attached to both instance groups:

![Picture](pic/picture7.png)


## Appendix A

### Automatic Scaling Rules for Core Instance Group

```json
    {
     "Constraints":
      {
       "MinCapacity": 3,
       "MaxCapacity": 10
      },
     "Rules":
     [
      {
       "Name": "ScaleOutYARNLowMemory",
       "Description": "Replicates the default scale-out rule in the console for YARN memory.",
       "Action":{
        "SimpleScalingPolicyConfiguration":{
          "AdjustmentType": "CHANGE_IN_CAPACITY",
          "ScalingAdjustment": 2,
          "CoolDown": 120
        }
       },
       "Trigger":{
        "CloudWatchAlarmDefinition":{
          "ComparisonOperator": "LESS_THAN_OR_EQUAL",
          "EvaluationPeriods": 1,
          "MetricName": "YARNMemoryAvailablePercentage",
          "Namespace": "AWS/ElasticMapReduce",
          "Period": 300,
          "Threshold": 35,
          "Statistic": "AVERAGE",
          "Unit": "PERCENT",
          "Dimensions":[
             {
               "Key" : "JobFlowId",
               "Value" : "${emr.clusterId}"
             }
          ]
        }
       }
      },
      {
        "Name": "ScaleOutContainerPending",
        "Description": "Replicates the default scale-out rule in the console for Containers Pending Ratio.",
        "Action":{
         "SimpleScalingPolicyConfiguration":{
           "AdjustmentType": "CHANGE_IN_CAPACITY",
           "ScalingAdjustment": 2,
           "CoolDown": 120
         }
        },
        "Trigger":{
         "CloudWatchAlarmDefinition":{
           "ComparisonOperator": "GREATER_THAN_OR_EQUAL",
           "EvaluationPeriods": 1,
           "MetricName": "ContainerPendingRatio",
           "Namespace": "AWS/ElasticMapReduce",
           "Period": 300,
           "Threshold": 0.75,
           "Statistic": "AVERAGE",
           "Unit": "COUNT",
           "Dimensions":[
              {
                "Key" : "JobFlowId",
                "Value" : "${emr.clusterId}"
              }
           ]
         }
        }
       },
       {
        "Name": "ScaleInYARNAvailableMemory",
        "Description": "Replicates the default scale-in rule in the console for YARN memory.",
        "Action":{
         "SimpleScalingPolicyConfiguration":{
           "AdjustmentType": "CHANGE_IN_CAPACITY",
           "ScalingAdjustment": -1,
           "CoolDown": 300
         }
        },
        "Trigger":{
         "CloudWatchAlarmDefinition":{
           "ComparisonOperator": "GREATER_THAN_OR_EQUAL",
           "EvaluationPeriods": 3,
           "MetricName": "YARNMemoryAvailablePercentage",
           "Namespace": "AWS/ElasticMapReduce",
           "Period": 300,
           "Threshold": 75,
           "Statistic": "AVERAGE",
           "Unit": "PERCENT",
           "Dimensions":[
              {
                "Key" : "JobFlowId",
                "Value" : "${emr.clusterId}"
              }
           ]
         }
        }
       },
       {
        "Name": "ScaleInContainerAvailable",
        "Description": "Replicates the default scale-in rule in the console for Containers Pending Ratio.",
        "Action":{
         "SimpleScalingPolicyConfiguration":{
           "AdjustmentType": "CHANGE_IN_CAPACITY",
           "ScalingAdjustment": -1,
           "CoolDown": 300
         }
        },
        "Trigger":{
         "CloudWatchAlarmDefinition":{
           "ComparisonOperator": "LESS_THAN_OR_EQUAL",
           "EvaluationPeriods": 3,
           "MetricName": "ContainerPendingRatio",
           "Namespace": "AWS/ElasticMapReduce",
           "Period": 300,
           "Threshold": 0.15,
           "Statistic": "AVERAGE",
           "Unit": "COUNT",
           "Dimensions":[
              {
                "Key" : "JobFlowId",
                "Value" : "${emr.clusterId}"
              }
           ]
         }
        }
       }
     ]
   }
```
### Automatic Scaling Rules for Task Instance Group

```json
    {
     "Constraints":
      {
       "MinCapacity": 0,
       "MaxCapacity": 30
      },
     "Rules":
     [
      {
       "Name": "ScaleOutYARNLowMemory",
       "Description": "Replicates the default scale-out rule in the console for YARN memory.",
       "Action":{
        "SimpleScalingPolicyConfiguration":{
          "AdjustmentType": "CHANGE_IN_CAPACITY",
          "ScalingAdjustment": 5,
          "CoolDown": 120
        }
       },
       "Trigger":{
        "CloudWatchAlarmDefinition":{
          "ComparisonOperator": "LESS_THAN_OR_EQUAL",
          "EvaluationPeriods": 1,
          "MetricName": "YARNMemoryAvailablePercentage",
          "Namespace": "AWS/ElasticMapReduce",
          "Period": 300,
          "Threshold": 35,
          "Statistic": "AVERAGE",
          "Unit": "PERCENT",
          "Dimensions":[
             {
               "Key" : "JobFlowId",
               "Value" : "${emr.clusterId}"
             }
          ]
        }
       }
      },
      {
        "Name": "ScaleOutContainerPending",
        "Description": "Replicates the default scale-out rule in the console for Containers Pending Ratio.",
        "Action":{
         "SimpleScalingPolicyConfiguration":{
           "AdjustmentType": "CHANGE_IN_CAPACITY",
           "ScalingAdjustment": 5,
           "CoolDown": 120
         }
        },
        "Trigger":{
         "CloudWatchAlarmDefinition":{
           "ComparisonOperator": "GREATER_THAN_OR_EQUAL",
           "EvaluationPeriods": 1,
           "MetricName": "ContainerPendingRatio",
           "Namespace": "AWS/ElasticMapReduce",
           "Period": 300,
           "Threshold": 0.75,
           "Statistic": "AVERAGE",
           "Unit": "COUNT",
           "Dimensions":[
              {
                "Key" : "JobFlowId",
                "Value" : "${emr.clusterId}"
              }
           ]
         }
        }
       },
       {
        "Name": "ScaleInYARNAvailableMemory",
        "Description": "Replicates the default scale-in rule in the console for YARN memory.",
        "Action":{
         "SimpleScalingPolicyConfiguration":{
           "AdjustmentType": "CHANGE_IN_CAPACITY",
           "ScalingAdjustment": -2,
           "CoolDown": 300
         }
        },
        "Trigger":{
         "CloudWatchAlarmDefinition":{
           "ComparisonOperator": "GREATER_THAN_OR_EQUAL",
           "EvaluationPeriods": 3,
           "MetricName": "YARNMemoryAvailablePercentage",
           "Namespace": "AWS/ElasticMapReduce",
           "Period": 300,
           "Threshold": 75,
           "Statistic": "AVERAGE",
           "Unit": "PERCENT",
           "Dimensions":[
              {
                "Key" : "JobFlowId",
                "Value" : "${emr.clusterId}"
              }
           ]
         }
        }
       },
       {
        "Name": "ScaleInContainerAvailable",
        "Description": "Replicates the default scale-in rule in the console for Containers Pending Ratio.",
        "Action":{
         "SimpleScalingPolicyConfiguration":{
           "AdjustmentType": "CHANGE_IN_CAPACITY",
           "ScalingAdjustment": -2,
           "CoolDown": 300
         }
        },
        "Trigger":{
         "CloudWatchAlarmDefinition":{
           "ComparisonOperator": "LESS_THAN_OR_EQUAL",
           "EvaluationPeriods": 3,
           "MetricName": "ContainerPendingRatio",
           "Namespace": "AWS/ElasticMapReduce",
           "Period": 300,
           "Threshold": 0.15,
           "Statistic": "AVERAGE",
           "Unit": "COUNT",
           "Dimensions":[
              {
                "Key" : "JobFlowId",
                "Value" : "${emr.clusterId}"
              }
           ]
         }
        }
       }
     ]
   }
```