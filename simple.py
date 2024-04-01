from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("DAG Example") \
    .getOrCreate()

hdfs_input_path = "hdfs://46.250.229.129:9000/train.csv"

df = spark.read.csv(hdfs_input_path, header=True, inferSchema=True)

print(df)