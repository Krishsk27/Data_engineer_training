import dlt
from pyspark.sql.functions import *
@dlt.table(
    name = "gold_department_revenue_final"
)
def gold_department_revenue_final():

    return dlt.read("silver_patient_visits_final") \
        .groupBy("department") \
        .agg(
            sum("total_bill").alias("total_revenue")
        )