import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, count, col

spark = SparkSession.builder.appName("WordCount").getOrCreate()

data = [
    ("The cat is in the bag",),
    ("The dog is in the yard",),
]
df = spark.createDataFrame(data, ["Sentence"])

word_counts = (
    df.select(explode(split(col("Sentence"), " ")).alias("Word"))
      .groupBy("Word")
      .agg(count("*").alias("Count"))
      .orderBy(col("Word"))
)

word_counts.show()
spark.stop()
