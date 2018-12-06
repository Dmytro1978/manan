// This code can be run is spark-shell line by line
// or from file: 
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

//cache the dataframe:
df_line_breaks.persist() //persist() caches the dataframe in memory and on disc
//df_line_breaks.cache() //cache() - in memory only.
//persist() is better option than cache() because it will spill the RDD partitions to the Worker's local disk if they're evicted from memory
//cache() is an alias for persist(StorageLevel.MEMORY_ONLY)
//persist() definition: persist(StorageLevel.MEMORY_AND_DISK_ONLY)

//call a count method to be sure that the dataframe is completely persisted
df_line_breaks.count()

// show whether the dataframe is cached or not 
// the "dataframe.storageLevel.useMemory" feature is available in Spark (Scala) 2.1.0 and higher:
print(df_line_breaks.storageLevel.useMemory) 

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

// the command about in one string:
//val df_resolved8 = df_line_breaks.columns.foldLeft(df_line_breaks) { (memoDF, colName) => memoDF.withColumn(colName,regexp_replace(col(colName), "\n", "is"))}

df_line_breaks.unpersist()

// get number of partitions of the dataframe
print(df.rdd.partitions.size)

//repartition the dataframe
val df_partitioned = df.repartition(2)

// get number of partitions of the dataframe
print(df_partitioned.rdd.partitions.size)

//store repartitioned dataset on disc (there will be number of files equal to number of partitions)
df_partitioned.write.option("header", "true").mode("overwrite").csv("/Users/mdmytro/customer2_partitioned")

//the difference between copying a dataframe and creating a reference to it

//this will create a reference to the existing dataframe
val df_reference = df

//check if the dataframe is cached or not
//the "dataframe.storageLevel.useMemory" feature is available in Spark (Scala) 2.1.0 and higher:
print(df.storageLevel.useMemory)
print(df_reference.storageLevel.useMemory)

//cache the new dataframe in memory only
df_reference.cache()
df_reference.count()
//check that the old  dataframe is also cached (because it is just a reference to the new dataftame is just a reference to the old one)
print(df.storageLevel.useMemory) 

//uncache the dataframe
df.unpersist()
print(df_reference.storageLevel.useMemory)

//copy the dataframe to the new one
val df_copy = df.select("*")

//cache the dataframe in memory and on disc
df_copy.persist()
df_copy.count()

//check both dataframes
print(df_copy.storageLevel.useMemory)
print(df_resolved.storageLevel.useMemory)

df_copy.unpersist()

//select data from dataframe using SparkSQL
df.createOrReplaceTempView("customer")

val df_one = spark.sql("select * from customer where id = 2")
df_one.show()

//get dataframe size
import org.apache.spark.sql.Row
import org.apache.spark.rdd.RDD
import org.apache.spark.rdd
import org.apache.spark.util.SizeEstimator

//function that calculates a dataframe size
def calcRDDSize(rdd: RDD[String]): Long = {
  rdd.map(_.getBytes("UTF-8").length.toLong)
     .reduce(_+_) //add the sizes together
}

//get RDD from a dataframe
val rddOfDataframe = df.rdd.map(_.toString())

//pass RDD to the function
val size = calcRDDSize(rddOfDataframe)

