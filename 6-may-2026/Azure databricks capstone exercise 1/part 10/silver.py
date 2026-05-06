import dlt
from pyspark.sql.functions import *
@dlt.table(
    name = "silver_patient_visits_final"
)
def silver_patient_visits_final():

    return dlt.read("bronze_patient_visits_final") \
        .filter(col("bill_amount") > 0) \
        .withColumn(
            "city",
            upper(col("city"))
        ) \
        .withColumn(
            "department",
            initcap(col("department"))
        ) \
        .withColumn(
            "total_bill",
            col("bill_amount") + 500
        )