import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import min, max, avg

spark = SparkSession.builder.appName("AggregateExample").getOrCreate()

data = [
    (1, "John", 34.5),
    (2, "Alice", 29.3),
    (3, "Bob", 41.0),
]
df = spark.createDataFrame(data, ["ID", "Name", "Age"])

df.select(
    min("Age").alias("MinAge"),
    max("Age").alias("MaxAge"),
    avg("Age").alias("AvgAge"),
).show()

spark.stop()
