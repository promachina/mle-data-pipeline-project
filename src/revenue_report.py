import argparse

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F


parser = argparse.ArgumentParser()

parser.add_argument('--input_green', required=True)
parser.add_argument('--output', required=True)

args = parser.parse_args()

input_green = args.input_green
output = args.output


spark = SparkSession.builder \
    .appName('test') \
    .getOrCreate()

bucket = "[bucket]"
spark.conf.set('temporaryGcsBucket', bucket)

df_green = spark.read.parquet(input_green)
df_green.printSchema()


df_green = df_green \
    .withColumnRenamed('lpep_pickup_datetime', 'pickup_datetime') \
    .withColumnRenamed('lpep_dropoff_datetime', 'dropoff_datetime')


common_colums = [
    'VendorID',
    'pickup_datetime',
    'dropoff_datetime',
    'store_and_fwd_flag',
    'RatecodeID',
    'PULocationID',
    'DOLocationID',
    'passenger_count',
    'trip_distance',
    'fare_amount',
    'extra',
    'mta_tax',
    'tip_amount',
    'tolls_amount',
    'improvement_surcharge',
    'total_amount',
    'payment_type',
    'congestion_surcharge'
]



df_green.registerTempTable('trips_data')


df_result = spark.sql("""
SELECT 
    -- Reveneue grouping 
    PULocationID AS revenue_zone,
    date_trunc('month', pickup_datetime) AS revenue_month,

    -- Revenue calculation 
    SUM(fare_amount) AS revenue_monthly_fare,
    SUM(extra) AS revenue_monthly_extra,
    SUM(mta_tax) AS revenue_monthly_mta_tax,
    SUM(tip_amount) AS revenue_monthly_tip_amount,
    SUM(tolls_amount) AS revenue_monthly_tolls_amount,
    SUM(improvement_surcharge) AS revenue_monthly_improvement_surcharge,
    SUM(total_amount) AS revenue_monthly_total_amount,
    SUM(congestion_surcharge) AS revenue_monthly_congestion_surcharge,

    -- Additional calculations
    AVG(passenger_count) AS avg_montly_passenger_count,
    AVG(trip_distance) AS avg_montly_trip_distance
FROM
    trips_data
GROUP BY
    1, 2
""")

# Write the output to BigQuery
# config = SparkBigQueryConfigBuilder() \
#     .withOutputTable("probable-sunup-390815.taxifisch.green-taxi") \
#     .withTemporaryGcsBucket("probable-sunup-390815.taxifisch.green-taxi-temp") \
#     .build()

df_result.write \
    .format("bigquery") \
    .option("table", "probable-sunup-390815.taxifisch.green-taxi") \
    .mode("overwrite") \
    .save()

# df_result.coalesce(1) \
#     .write.parquet(output, mode='overwrite')