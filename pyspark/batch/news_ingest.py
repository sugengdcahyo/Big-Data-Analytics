import finnhub
import os
from dotenv import load_dotenv

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

load_dotenv()


spark = SparkSession.builder \
    .appName("News batch processing") \
    .config("spark.hadoop.fs.defaultFS", os.getenv("HDFS_URL")) \
    .getOrCreate()

sc = SparkContext.getOrCreate()

# Setup client
finnhub_client = finnhub.Client(api_key=os.getenv("FINNHUB_API_KEY"))
news = finnhub_client.general_news('general')

json_rdd = sc.parallelize(news)
df = spark.read.json(json_rdd)

# df.write.save(f"{os.getenv('HDFS_URL')}/output/finnews.json", format="json")

df.write.mode('append').save(os.path.join(os.getenv('HDFS_URL'), "output/finnews.json"), format="json")


# Stock candles
# res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)