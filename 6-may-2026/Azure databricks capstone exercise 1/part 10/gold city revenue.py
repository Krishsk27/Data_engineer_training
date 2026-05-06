import dlt
from pyspark.sql.functions import *
@dlt.table(
    name = "gold_city_revenue_final"
)
def gold_city_revenue_final():

    return dlt.read("silver_patient_visits_final") \
        .groupBy("city") \
        .agg(
            sum("total_bill").alias("total_revenue")
        )