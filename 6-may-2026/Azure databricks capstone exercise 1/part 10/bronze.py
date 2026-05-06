import dlt
from pyspark.sql.functions import *
@dlt.table(
    name = "bronze_patient_visits_final"
)
def bronze_patient_visits_final():
    data = [
        (1,"Aarav Khan","Hyderabad","Cardiology",5200),
        (2,"Priya Reddy","Bengaluru","Dermatology",2800),
        (3,"Rahul Mehta","Mumbai","Orthopedics",7500),
        (4,"Sneha Kapoor","Delhi","Pediatrics",2900),
        (5,"Kiran Patel","Chennai","Cardiology",5300),
        (6,"Ananya Das","Kolkata","Neurology",10000),
        (7,"Rohan Nair","Kochi","Neurology",7900),
        (8,"Farhan Ali","Hyderabad","Cardiology",8000),
        (9,"Nikhil Verma","Pune","General Medicine",2700)
    ]
    columns = [
        "visit_id",
        "patient_name",
        "city",
        "department",
        "bill_amount"
    ]
    return spark.createDataFrame(data, columns)