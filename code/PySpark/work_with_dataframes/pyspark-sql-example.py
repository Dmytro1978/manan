# Table city (city.csv)
'''
city_id,city_name,city_code,country_id
1,Odessa,ODS,1
2,Kiev,KBP,1
3,San Francisco,SFO,2
'''
# Table country (country.csv)
'''
country_id,country_name,country_code
1,Ukraine,UA
2,United States of America,USA
'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col

spark = SparkSession.builder.appName("Python Spark SQL basic example").config("spark.some.config.option", "some-value").getOrCreate()
df = spark.read.csv("s3://tmp-landing-zone/thedates/thedates.csv")
df.show()

# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("dates")

sqlDF = spark.sql("SELECT * FROM dates")
sqlDF.show()

''' +----------+                                                                    
    |       _c0|
    +----------+
    |1970-01-01|
    |1970-01-02|
    |1970-01-03|
    |1970-01-04|
    |1970-01-05|
    |1970-01-06|
    |1970-01-07|
    |1970-01-08|
    |1970-01-09|
    |1970-01-10|
    |1970-01-11|
    |1970-01-12|
    |1970-01-13|
    |1970-01-14|
    |1970-01-15|
    |1970-01-16|
    |1970-01-17|
    |1970-01-18|
    |1970-01-19|
    |1970-01-20|
    +----------+
    only showing top 20 rows  
'''

sqlDF = spark.sql("SELECT * FROM dates where _c0 = '1978-02-20'")
sqlDF.show()

''' +----------+
    |       _c0|
    +----------+
    |1978-02-20|
    +----------+  
'''

sqlDF = spark.sql("SELECT * FROM dates where _c0 between '1978-02-20' and '1978-02-28'")
sqlDF.show()

''' +----------+
    |       _c0|
    +----------+
    |1978-02-20|
    |1978-02-21|
    |1978-02-22|
    |1978-02-23|
    |1978-02-24|
    |1978-02-25|
    |1978-02-26|
    |1978-02-27|
    |1978-02-28|
    +----------+  
'''


regexDF = sqlDF.withColumn("_c0", regexp_replace("_c0","-02-","-03-"))
regexDF.show()

''' +----------+
    |       _c0|
    +----------+
    |1978-03-20|
    |1978-03-21|
    |1978-03-22|
    |1978-03-23|
    |1978-03-24|
    |1978-03-25|
    |1978-03-26|
    |1978-03-27|
    |1978-03-28|
    +----------+  
'''

dfCity = spark.read.csv("s3://tmp-landing-zone/city/city.csv")
dfCity.show()

''' +-------------+---------+
    |          _c0|      _c1|
    +-------------+---------+
    |    city_name|city_code|
    |       Odessa|      ODS|
    |         Kiev|      KBP|
    |San Francisco|      SFO|
    +-------------+---------+
'''

dfCity = spark.read.option("header", "true").csv("s3://tmp-landing-zone/city/city.csv")
dfCity.show()

''' +-------------+---------+
    |    city_name|city_code|
    +-------------+---------+
    |       Odessa|      ODS|
    |         Kiev|      KBP|
    |San Francisco|      SFO|
    +-------------+---------+
'''

dfCity.createOrReplaceTempView("city")

sqlDF = spark.sql("SELECT * FROM city where city_name like 'San%'")
sqlDF.show()

''' +-------------+---------+                                                       
    |    city_name|city_code|
    +-------------+---------+
    |San Francisco|      SFO|
    +-------------+---------+
'''

dfCountry = spark.read.option("header", "true").csv("s3://tmp-landing-zone/country/country.csv")
dfCountry.show()

''' +----------+--------------------+-------------+
    |country_id|        country_name| country_code|
    +----------+--------------------+-------------+
    |         1|             Ukraine|           UA|
    |         2|United States of ...|          USA|
    +----------+--------------------+-------------+
'''

 dfCountry.createOrReplaceTempView("country")
 spark.sql("SELECT t1.city_name, t2.country_name FROM city t1, country t2 where t1.country_id = t2.country_id").show()

''' +-------------+--------------------+
    |    city_name|        country_name|
    +-------------+--------------------+
    |         Kiev|             Ukraine|
    |       Odessa|             Ukraine|
    |San Francisco|United States of ...|
    +-------------+--------------------+
'''



# Let's repeat it again:

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Python Spark SQL basic example").config("spark.some.config.option", "some-value").getOrCreate()

#Create a DataFrame for cities
dfCity = spark.read.option("header", "true").csv("s3://tmp-landing-zone/city/city.csv")
dfCity.show()

#Create a DataFrame for countries
dfCountry = spark.read.option("header", "true").csv("s3://tmp-landing-zone/country/country.csv")
dfCountry.show()

# Register the DataFrame as a SQL temporary view for cities
dfCity.createOrReplaceTempView("city")
# Register the DataFrame as a SQL temporary view for countries
dfCountry.createOrReplaceTempView("country")

#Join city with countries
spark.sql("SELECT t1.city_name, t2.country_code FROM city t1, country t2 where t1.country_id = t2.country_id").show()

''' +-------------+------------+
    |    city_name|country_code|
    +-------------+------------+
    |         Kiev|          UA|
    |       Odessa|          UA|
    |San Francisco|         USA|
    +-------------+------------+
'''