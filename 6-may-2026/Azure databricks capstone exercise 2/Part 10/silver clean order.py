import dlt
from pyspark.sql.functions import *
@dlt.table(
    name="silver_clean_orders",
    comment="Orders after removing invalid records"
)
def silver_clean_orders():

    return (
        dlt.read("silver_orders_revenue")
        .filter(col("order_status").isNotNull())
    )