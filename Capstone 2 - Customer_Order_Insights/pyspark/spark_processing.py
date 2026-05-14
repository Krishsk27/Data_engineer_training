from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("CustomerOrderInsights") \
    .getOrCreate()

orders_df = spark.read.csv(
    "processed_orders.csv",
    header=True,
    inferSchema=True
)

customers_df = spark.createDataFrame([
    (1, "Chennai"),
    (2, "Bangalore"),
    (3, "Hyderabad")
], ["customer_id", "region"])

joined_df = orders_df.join(
    customers_df,
    on='customer_id',
    how='inner'
)

delayed_df = joined_df.filter(
    col("delayed") == 1
)

grouped_df = delayed_df.groupBy(
    "region"
).count()

grouped_df.show()

grouped_df.write.csv(
    "delayed_region_output",
    header=True,
    mode="overwrite"
)

spark.stop()