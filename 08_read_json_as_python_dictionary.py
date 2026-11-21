import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("JSONInlineView").getOrCreate()

data = [(1, "Apple"), (2, "Banana"), (3, "Grapes")]
df = spark.createDataFrame(data, ["id", "fruit"])

# Print each row as a JSON string.
for json_row in df.toJSON().collect():
    print(json_row)

# Convert collected Rows into Python dictionaries.
dict_result = [row.asDict() for row in df.collect()]
print(dict_result)

spark.stop()
