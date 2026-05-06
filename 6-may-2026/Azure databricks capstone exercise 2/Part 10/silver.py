import dlt
from pyspark.sql.functions import *
@dlt.table(
    name="silver_orders",
    comment="Cleaned Silver Orders Table"
)
def silver_orders():

    return (
        dlt.read("bronze_orders")
        .withColumn(
            "order_date",
            to_date(col("order_date"), "yyyy-MM-dd")
        )
        .filter(col("quantity") > 0)
    )