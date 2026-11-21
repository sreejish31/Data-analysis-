import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, substring, count

spark = SparkSession.builder.appName("FirstLetterCount").getOrCreate()

data = [
    ("Alice",), ("Bob",), ("Charlie",), ("David",),
    ("Eve",), ("Amy",), ("Aaron",), ("Brian",),
]
df = spark.createDataFrame(data, ["Name"])

result = (
    df.withColumn("First Letter", substring(col("Name"), 1, 1))
      .groupBy("First Letter")
      .agg(count("*").alias("Count"))
      .orderBy(col("Count").desc(), col("First Letter"))
      .limit(5)
)

result.show()
spark.stop()
