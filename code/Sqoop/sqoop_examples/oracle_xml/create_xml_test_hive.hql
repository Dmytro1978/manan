CREATE TABLE xml_test
STORED AS AVRO
LOCATION '/user/hive/warehouse/xml_test'
TBLPROPERTIES ('avro.schema.url'='hdfs:///user/hive/warehouse/avsc/xml_test.avsc');