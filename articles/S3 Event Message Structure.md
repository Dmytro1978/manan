# S3 Event Message Structure
The notification message Amazon S3 sends to publish an event is a JSON message with the following structure. Note the following:

* The responseElements key value is useful if you want to trace the request by following up with Amazon S3 support. Both x-amz-request-id and x-amz-id-2 help Amazon S3 to trace the individual request. These values are the same as those that Amazon S3 returned in the response to your original PUT request, which initiated the event.

* The s3 key provides information about the bucket and object involved in the event. The object keyname value is URL encoded. For example "red flower.jpg" becomes "red+flower.jpg" (S3 returns the "application/x-www-form-urlencoded" as the content type in the response).

* The sequencer key provides a way to determine the sequence of events. Event notifications are not guaranteed to arrive in the order that the events occurred. However, notifications from events that create objects (PUTs) and delete objects contain a sequencer, which can be used to determine the order of events for a given object key.

* If you compare the sequencer strings from two event notifications on the same object key, the event notification with the greater sequencer hexadecimal value is the event that occurred later. If you are using event notifications to maintain a separate database or index of your Amazon S3 objects, you will probably want to compare and store the sequencer values as you process each event notification.

Note that:

* sequencer cannot be used to determine order for events on different object keys.

* The sequencers can be of different lengths. So to compare these values, you first left pad the shorter value with zeros and then do lexicographical comparison.

```json
{  
   "Records":[  
      {  
         "eventVersion":"2.0",
         "eventSource":"aws:s3",
         "awsRegion":"us-east-1",
         "eventTime": "The time, in ISO-8601 format, for example, 1970-01-01T00:00:00.000Z, when S3 finished processing the request",
         "eventName":"event-type",
         "userIdentity":{  
            "principalId":"Amazon-customer-ID-of-the-user-who-caused-the-event"
         },
         "requestParameters":{  
            "sourceIPAddress":"ip-address-where-request-came-from"
         },
         "responseElements":{  
            "x-amz-request-id":"Amazon S3 generated request ID",
            "x-amz-id-2":"Amazon S3 host that processed the request"
         },
         "s3":{  
            "s3SchemaVersion":"1.0",
            "configurationId":"ID found in the bucket notification configuration",
            "bucket":{  
               "name":"bucket-name",
               "ownerIdentity":{  
                  "principalId":"Amazon-customer-ID-of-the-bucket-owner"
               },
               "arn":"bucket-ARN"
            },
            "object":{  
               "key":"object-key",
               "size": "object-size",
               "eTag":"object eTag",
               "versionId":"object version if bucket is versioning-enabled, otherwise null",
               "sequencer": "a string representation of a hexadecimal value used to determine event sequence, 
                   only used with PUTs and DELETEs"            
            }
         }
      },
      {
          /* Additional events */
      }
   ]
}  
```
The following are example messages:

* Test message—When you configure an event notification on a bucket, Amazon S3 sends the following test message:

```json
{  
   "Service":"Amazon S3",
   "Event":"s3:TestEvent",
   "Time":"2014-10-13T15:57:02.089Z",
   "Bucket":"bucketname",
   "RequestId":"5582815E1AEA5ADF",
   "HostId":"8cLeGAmw098X5cv4Zkwcmo8vvZa3eH3eKxsPzbB9wrR+YstdA6Knx4Ip8EXAMPLE"
}
```
* Example message when an object is created using the PUT request—The following message is an example of a message Amazon S3 sends to publish an s3:ObjectCreated:Put event:

```json
{  
   "Records":[  
      {  
         "eventVersion":"2.0",
         "eventSource":"aws:s3",
         "awsRegion":"us-east-1",
         "eventTime":"1970-01-01T00:00:00.000Z",
         "eventName":"ObjectCreated:Put",
         "userIdentity":{  
            "principalId":"AIDAJDPLRKLG7UEXAMPLE"
         },
         "requestParameters":{  
            "sourceIPAddress":"127.0.0.1"
         },
         "responseElements":{  
            "x-amz-request-id":"C3D13FE58DE4C810",
            "x-amz-id-2":"FMyUVURIY8/IgAtTv8xRjskZQpcIZ9KG4V5Wp6S7S/JRWeUWerMUE5JgHvANOjpD"
         },
         "s3":{  
            "s3SchemaVersion":"1.0",
            "configurationId":"testConfigRule",
            "bucket":{  
               "name":"mybucket",
               "ownerIdentity":{  
                  "principalId":"A3NL1KOZZKExample"
               },
               "arn":"arn:aws:s3:::mybucket"
            },
            "object":{  
               "key":"HappyFace.jpg",
               "size":1024,
               "eTag":"d41d8cd98f00b204e9800998ecf8427e",
               "versionId":"096fKKXTRTtl3on89fVO.nfljtsv6qko",
               "sequencer":"0055AED6DCD90281E5"
            }
         }
      }
   ]
}
```

### Usage example

Amazon S3 can publish events (for example, when an object is created in a bucket) to AWS Lambda and invoke your Lambda function by passing the event data as a parameter. This integration enables you to write Lambda functions that process Amazon S3 events. In Amazon S3, you add bucket notification configuration that identifies the type of event that you want Amazon S3 to publish and the Lambda function that you want to invoke.

An example of a Lambda function that gets invoked when a file is posted to an S3 bucket:

``` Python
import boto3

def lambda_handler(event, context):
    
    client = boto3.client('s3')
        
    for record in event['Records']:
        bucket = record['s3']['bucket']['name'] # get a bucket name
        key = record['s3']['object']['key']  # get a key (full path to a file)
        
        if key == 'staging/employee/_SUCCESS': # check the file name
        
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
```
The code shown above triggers an AWS Glue job.  