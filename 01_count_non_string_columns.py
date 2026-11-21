import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("NonStringColumns").getOrCreate()

data = [
    (1, "John", 34.5),
    (2, "Alice", 29.3),
    (3, "Bob", 41.0),
]
columns = ["ID", "Name", "Age"]

df = spark.createDataFrame(data, columns)

non_string_columns = [
    field for field in df.schema.fields
    if not isinstance(field.dataType, StringType)
]

print(f"Number of non-string columns: {len(non_string_columns)}")
spark.stop()
