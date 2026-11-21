import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    size,
    element_at,
    array_contains,
    sort_array,
    explode,
)

spark = SparkSession.builder.appName("ArrayColumnExample").getOrCreate()

data = [
    (1, ["Apple", "Banana", "Grapes"]),
    (2, ["Orange", "Kiwi"]),
    (3, ["Mango", "Pineapple", "Watermelon"]),
]
df = spark.createDataFrame(data, ["ID", "Fruits"])

df_operations = (
    df.withColumn("ArraySize", size(col("Fruits")))
      .withColumn("FirstElement", element_at(col("Fruits"), 1))
      .withColumn("SecondElement", element_at(col("Fruits"), 2))
      .withColumn("HasApple", array_contains(col("Fruits"), "Apple"))
      .withColumn("SortedArray", sort_array(col("Fruits")))
)

df_operations.show(truncate=False)

exploded_df = df.select(
    col("ID"),
    explode(col("Fruits")).alias("Fruit"),
)

exploded_df.show()
spark.stop()
