// This code can be run is spark-shell:
// 1. Run spark-shell
// 2. Type the following:  
//   :load line_breaks_cl.scala

import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder().appName("Spark SQL basic example").config("spark.some.config.option", "some-value").getOrCreate()

//read data from csv file into a dataframe
val df = spark.read.option("header", "true").csv("/Users/mdmytro/customer2.csv")

var dfTypes = df.dtypes //get column data types 

var elem1 = dfTypes(0) //first column data type

print(elem1._1) //print column name
print(elem1._2) //print column data type 

//print all column data types in a loop
for (i <- 0 to dfTypes.length -1) 
    print(dfTypes(i))

//store data in parquet format
df.write.mode("overwrite").parquet("/Users/mdmytro/customer2_pq")

//read stored data
val df_pq = spark.read.parquet("/Users/mdmytro/customer2_pq/")

//print the data
df_pq.show()

//create a dataframe with like breaks 
val df_line_breaks = df_pq.withColumn("DESC", regexp_replace(col("DESC"), "is", "\n"))

df_line_breaks.show()

//replace all line breaks with some data 
var df_resolved  = df_line_breaks.withColumn("DESC", regexp_replace(col("DESC"), "\n", "is"))

df_resolved.show()

//store resolved data in csv file
df_resolved.write.option("header", "true").mode("overwrite").csv("/Users/mdmytro/customer_final.csv")

//copy the dataframe (with line breaks) to the new one
df_resolved = df_line_breaks.select(col("*"))
df_resolved.show()

dfTypes = df_resolved.dtypes //get column data types

//replace line breaks in all string columns in a loop
for (i <- 0 to dfTypes.length -1)
    var tupCol = dfTypes(i)
    if (tupCol._2 == "StringType" )
        df_resolved = df_resolved.withColumn(tupCol._1, regexp_replace(col(tupCol._1), "\n", "is"))

df_resolved.show()

//store fixed data in a csv file 
df_resolved.write.option("header", "true").mode("overwrite").csv("/Users/mdmytro/customer_final2.csv")

//the difference between copying a dataframe and creating a reference to it

//this will create a reference to the existing dataframe
val df_reference = df_resolved

//check if the dataframe is cached or not
//the "dataframe.storageLevel.useMemory" feature is available in Spark (Scala) 2.1.0 and higher:
print(df_resolved.storageLevel.useMemory)
print(df_reference.storageLevel.useMemory)

//cache the new dataframe in memory only
df_reference.cache()
//check that the old  dataframe is also cached (because it is just a reference to the new dataftame is just a reference to the old one)
print(df_resolved.storageLevel.useMemory) 

//uncache the dataframe
df_resolved.unpersist()
print(df_reference.storageLevel.useMemory)

//copy the dataframe to the new one
val df_copy = df_resolved.select("*")

//cache the dataframe in memory and on disc
df_copy.persist()

//check both dataframes
print(df_copy.storageLevel.useMemory)
print(df_resolved.storageLevel.useMemory)

df_copy.unpersist()

df.createOrReplaceTempView("customer")

val df_one = spark.sql("select * from customer where id = 2")
df_one.show()

//replacing line breaks with some data in all columns at once
val df_resolved2 = df_line_breaks
    .columns
    .foldLeft(df_line_breaks) { (memoDF, colName) => 
        memoDF.withColumn(
            colName,
            regexp_replace(col(colName), "\n", "is")
        )
    }

df_resolved2.show()

//persistance & caching

val df_resolved8 = df_line_breaks.columns.foldLeft(df_line_breaks) { (memoDF, colName) => memoDF.withColumn(colName,regexp_replace(col(colName), "\n", "is"))}

val df_resolved7 = df.columns.foldLeft(df_line_breaks) { (memoDF, colName) => memoDF.withColumn(colName,regexp_replace(col(colName), "\n", "is"))}