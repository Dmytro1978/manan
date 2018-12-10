## Append to a Dataframe

To append to a DataFrame, use the union method.

### Scala

```scala
val firstDF = spark.range(3).toDF("myCol")
val newRow = Seq(20)
val appended = firstDF.union(newRow.toDF())
display(appended)
```
### Python

```python
firstDF = spark.range(3).toDF("myCol")
newRow = spark.createDataFrame([[20]])
appended = firstDF.union(newRow)
display(appended)
```