import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count

spark = SparkSession.builder.appName("VowelCheck").getOrCreate()

data = [
    ("apple",),
    ("banana",),
    ("grape",),
    ("orange",),
    ("kiwi",),
    ("umbrella",),
]
df = spark.createDataFrame(data, ["Word"])

vowel_condition = col("Word").substr(1, 1).isin(
    ["a", "e", "i", "o", "u"]
)

df = df.withColumn(
    "StartsWithVowel",
    when(vowel_condition, 1).otherwise(0),
)

result = (
    df.groupBy("StartsWithVowel")
      .agg(count("*").alias("Count"))
      .withColumn(
          "Category",
          when(col("StartsWithVowel") == 1, "Vowel").otherwise("Consonant"),
      )
)

result.show()
spark.stop()
