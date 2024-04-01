from pyspark.sql import SparkSession
from pyspark import SparkContext

# Inisialisasi SparkSession
spark = SparkSession.builder \
    .appName("List Directory Example") \
    .getOrCreate()

# Mendapatkan SparkContext dari SparkSession
sc = spark.sparkContext

# Gunakan SparkContext untuk mengakses FileSystem
fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())

# Tentukan path HDFS yang ingin Anda lihat
hdfs_path = sc._jvm.org.apache.hadoop.fs.Path("hdfs://namenode:port/path/to/list")

# List direktori
status = fs.listStatus(hdfs_path)

# Tampilkan isi direktori
for file_status in status:
    print(file_status.getPath())

# Menutup SparkSession
spark.stop()
