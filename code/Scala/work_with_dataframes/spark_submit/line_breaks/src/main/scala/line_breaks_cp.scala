//this code should be compiled into jar:
//install sbt (using Homebrew)
//create folder structure (check the example of current struture)
//from project root folder run the following commands:
//sbt compile
//sbt package
//then run the following command:
//spark-submit --verbose --class "line_breaks" --master local[4] target/scala-2.11/line-breaks_2.11-1.0.jar

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.regexp_replace
import org.apache.spark.sql.functions.{col, udf}

object line_breaks {

    def main(args: Array[String]) {

        val spark = SparkSession.builder().appName("Spark SQL basic example").config("spark.some.config.option", "some-value").getOrCreate()

        //read data from csv file into a dataframe
        val df = spark.read.option("header", "true").csv("/Users/mdmytro/customer2.csv")

        df.show()

        //create a dataframe with like breaks 
        val df_line_breaks = df.withColumn("DESC", regexp_replace(col("DESC"), "is", "\n"))

        df_line_breaks.show()

        //cache the dataframe:
        df_line_breaks.persist() //persist - cache in memory and on disc
        //df_line_breaks.cache() //cache() - in memory only.
        //persist() is better option than cache() because it will spill the RDD partitions to the Worker's local disk if they're evicted from memory
        //cache() is an alias for persist(StorageLevel.MEMORY_ONLY)
        //persist() definition: persist(StorageLevel.MEMORY_AND_DISK_ONLY)
        df_line_breaks.count()

        // show whether the dataframe is cached or not 
        // the "dataframe.storageLevel.useMemory" feature is available in Spark (Scala) 2.1.0 and higher:
        print(df_line_breaks.storageLevel.useMemory) 

        //delete file from disc to test the caching

        //replace line breaks with some data in all columns at once
        val df_resolved = df_line_breaks
            .columns
            .foldLeft(df_line_breaks) { (memoDF, colName) => 
                memoDF.withColumn(
                    colName,
                    regexp_replace(col(colName), "\n", "is")
                )
            }

        //replace line breaks with some data in all columns at once
        //val df_resolved = df_line_breaks.columns.foldLeft(df_line_breaks) { (memoDF, colName) => memoDF.withColumn(colName,regexp_replace(col(colName), "\n", "is"))}

        df_resolved.show()

        //store data on disc
        df_resolved.write.option("header", "true").mode("overwrite").csv("/Users/mdmytro/customer2_resolved")

        //repartition the dataframe
        val df_partitioned = df_resolved.repartition(2)

        //print number lf partitions
        print(df_partitioned.rdd.partitions.size)

        //store repartitioned dataset on disc (there will be number of files equal to number of partitions)
        df_partitioned.write.option("header", "true").mode("overwrite").csv("/Users/mdmytro/customer2_partitioned")

        //uncache the dataframe
        df_line_breaks.unpersist()

    }
}