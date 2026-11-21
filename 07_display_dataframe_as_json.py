import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SimpleJSONDisplay").getOrCreate()

data = [(1, "Apple"), (2, "Banana"), (3, "Grapes")]
df = spark.createDataFrame(data, ["id", "fruit"])

# Display the DataFrame in tabular form.
df.show()

# Print each row as a JSON string.
for json_row in df.toJSON().collect():
    print(json_row)

spark.stop()
