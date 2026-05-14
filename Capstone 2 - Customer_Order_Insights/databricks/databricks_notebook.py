from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("CustomerETL") \
    .getOrCreate()

df = spark.read.csv(
    "/FileStore/tables/processed_orders.csv",
    header=True,
    inferSchema=True
)

display(df)

cleaned_df = df.filter(
    col("delayed") == 1
)

display(cleaned_df)

cleaned_df.write.format("delta") \
    .mode("overwrite") \
    .save("/tmp/delayed_customers")

cleaned_df.write.mode("overwrite") \
    .saveAsTable("delayed_customers")

spark.sql("""
SELECT customer_id,
       COUNT(*) AS total_delays
FROM delayed_customers
GROUP BY customer_id
ORDER BY total_delays DESC
LIMIT 5
""").show()

spark.stop()