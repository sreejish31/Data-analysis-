from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("CSVPerPartition")
    .getOrCreate()
)

data = [(1, "A"), (2, "B"), (3, "C"), (4, "D"), (5, "E")]
df = spark.createDataFrame(data, ["id", "value"])

df.repartition(3).write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("output_csv")

spark.stop()
