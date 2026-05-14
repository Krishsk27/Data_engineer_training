import os
print("Starting Customer Order Pipeline")
os.system("python preprocessing.py")
os.system("python spark_processing.py")
print("Pipeline Executed Successfully")