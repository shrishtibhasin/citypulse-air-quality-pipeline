from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, current_timestamp
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("CityPulseStreamProcessor") \
    .getOrCreate()

schema = StructType([
    StructField("city", StringType(), True),
    StructField("parameter", StringType(), True),
    StructField("value", FloatType(), True),
])

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "air-quality-stream") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)") \
            .select(from_json(col("value"), schema).alias("data")) \
            .select("data.*") \
            .withColumn("ingested_at", current_timestamp())

query = json_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
