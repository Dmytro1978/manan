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
        var df_pq_line_breaks = df_pq.withColumn("DESC", regexp_replace(col("DESC"), "is", "\n"))

        df_pq_line_breaks.show()

        //store the data with line breaks in parquet format 
        df_pq_line_breaks.write.mode("overwrite").parquet("/Users/mdmytro/customer2_pq_line_breaks")

        //read the data from parquet file
        val df_pq_line_breaks2 = spark.read.parquet("/Users/mdmytro/customer2_pq_line_breaks/")

        df_pq_line_breaks2.persist() //cache the dataframe in memory and on disc 

        //replace all line breaks with some data 
        val df_pq_resolved  = df_pq_line_breaks2.withColumn("DESC", regexp_replace(col("DESC"), "\n", "is"))

        df_pq_resolved.show()

        //store resolved data in csv file
        df_pq_resolved.write.option("header", "true").mode("overwrite").csv("/Users/mdmytro/customer_final.csv")

        //copy the dataframe (with line breaks) to the new one
        var df_pq_resolved2 = df_pq_line_breaks2.select(col("*"))

        df_pq_resolved2.show()

        df_pq_resolved2.cache() //cache the dataframe in memory (only)

        var tupCol = ("","")
        dfTypes = df_pq_resolved2.dtypes //get column data types

        //replace line breaks in all string columns in a loop
        for (i <- 0 to dfTypes.length -1)
            tupCol = dfTypes(i)
            if (tupCol._2 == "StringType" )
                df_pq_resolved2 = df_pq_resolved2.withColumn(tupCol._1, regexp_replace(col(tupCol._1), "\n", "is"))

        df_pq_resolved2.show()

        //store fixed data in a csv file 
        df_pq_resolved2.write.option("header", "true").mode("overwrite").csv("/Users/mdmytro/customer_final2.csv")

        //unpersist both dataframes
        df_pq_line_breaks2.unpersist()
        df_pq_resolved2.unpersist()
    }
}