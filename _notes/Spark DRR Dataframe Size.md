## How find spark RDD/Dataframe size

```scala
import org.apache.spark.sql.Row
import org.apache.spark.rdd.RDD
import org.apache.spark.rdd
import org.apache.spark.util.SizeEstimator

def calcRDDSize(rdd: RDD[String]): Long = {
  rdd.map(_.getBytes("UTF-8").length.toLong)
     .reduce(_+_) //add the sizes together
}

val rddOfDataframe = dataFrame.rdd.map(_.toString())

val size = calcRDDSize(rddOfDataframe)
```
