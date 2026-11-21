import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import map_from_arrays

spark = SparkSession.builder.appName("MapFromArraysExample").getOrCreate()

df = spark.createDataFrame(
    [
        (1, ["Apple", "Banana", "Grapes"], ["Red", "Yellow", "Green"]),
    ],
    ["ID", "Fruits", "Colors"],
)

# Create a map that pairs each fruit with its corresponding color.
df = df.withColumn(
    "FruitColorMap",
    map_from_arrays("Fruits", "Colors"),
)

df.show(truncate=False)
spark.stop()
