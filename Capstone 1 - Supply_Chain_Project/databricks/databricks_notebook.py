from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("SupplyChainETL") \
    .getOrCreate()

df = spark.read.csv(
    "/FileStore/tables/processed_orders.csv",
    header=True,
    inferSchema=True
)

display(df)

cleaned_df = df.filter(col("is_delayed") == 1)

display(cleaned_df)

supplier_summary = cleaned_df.groupBy("supplier_id").count()

display(supplier_summary)

cleaned_df.write.format("delta") \
    .mode("overwrite") \
    .save("/tmp/delayed_orders")

cleaned_df.write.mode("overwrite") \
    .saveAsTable("delayed_orders")

supplier_summary.write.csv(
    "/tmp/delayed_orders_csv",
    header=True,
    mode="overwrite"
)

display(dbutils.fs.ls("/tmp"))

spark.sql("""
SELECT supplier_id,
       COUNT(*) AS delayed_orders
FROM delayed_orders
GROUP BY supplier_id
""").show()

spark.stop()