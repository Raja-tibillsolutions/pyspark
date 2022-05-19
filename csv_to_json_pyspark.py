from pyspark.sql import SparkSession

spark=SparkSession.builder.getOrCreate()

df_spark=spark.read.csv('/home/raja/Documents/first.csv')

df_spark.repartition(1).write.mode('overwrite').format('json').save('/home/raja/Documents/spark/csv_to_json.json')

