import dlt
from pyspark.sql.functions import *
@dlt.table(
    name="gold_category_revenue",
    comment="Gold Table for Revenue by Category"
)
def gold_category_revenue():

    category_data = [
        ("Groceries",55500),
        ("Electronics",215000),
        ("Dairy",3000)
    ]

    category_columns = [
        "category",
        "revenue"
    ]

    category_df = spark.createDataFrame(
        category_data,
        category_columns
    )

    return category_df.groupBy("category").agg(
        sum("revenue").alias("total_category_revenue")
    )