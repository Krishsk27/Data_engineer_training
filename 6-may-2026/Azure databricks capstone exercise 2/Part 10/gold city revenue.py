import dlt
from pyspark.sql.functions import *
@dlt.table(
    name="gold_city_revenue",
    comment="Gold Table for Revenue by City"
)
def gold_city_revenue():

    city_data = [
        (301,"Hyderabad",20000),
        (302,"Bengaluru",35000),
        (303,"Delhi",90000),
        (304,"Hyderabad",125000)
    ]

    city_columns = [
        "order_id",
        "city",
        "revenue"
    ]

    city_df = spark.createDataFrame(city_data, city_columns)

    return city_df.groupBy("city").agg(
        sum("revenue").alias("total_city_revenue")
    )