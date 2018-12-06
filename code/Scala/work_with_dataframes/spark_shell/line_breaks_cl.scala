// This code can be run is spark-shell line by line
// or from file: 
// 1. Run spark-shell
// 2. Type the following:  
//   :load line_breaks_cl.scala

import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder().appName("Spark SQL basic example").config("spark.some.config.option", "some-value").getOrCreate()

//read data from csv file into a dataframe
val df = spark.read.option("header", "true").csv("/Users/mdmytro/customer2.csv")

df.show()

//create a dataframe with line breaks 
val df_line_breaks = df.withColumn("DESC", regexp_replace(col("DESC"), "is", "\n"))

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

//delete file from disc to test the caching

//replacing line breaks with some data in all columns at once
//val df_resolved = df_line_breaks
//    .columns
//    .foldLeft(df_line_breaks) { (memoDF, colName) => 
//        memoDF.withColumn(
//            colName,
//            regexp_replace(col(colName), "\n", "is")
//        )
//    }

//replace line breaks with some data in all columns at once
val df_resolved = df_line_breaks.columns.foldLeft(df_line_breaks) { (memoDF, colName) => memoDF.withColumn(colName,regexp_replace(col(colName), "\n", "is"))}

df_resolved.show()

//store data on disc
df_resolved.write.option("header", "true").mode("overwrite").csv("/Users/mdmytro/customer2_resolved")

//uncache the dataframe
df_line_breaks.unpersist()



