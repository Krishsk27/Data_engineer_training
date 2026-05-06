import dlt
from pyspark.sql.functions import *
@dlt.table(
    name="silver_orders_revenue",
    comment="Silver Orders with Revenue"
)
def silver_orders_revenue():

    return (
        dlt.read("silver_orders")
        .withColumn(
            "total_revenue",
            col("quantity") * 1000
        )
    )