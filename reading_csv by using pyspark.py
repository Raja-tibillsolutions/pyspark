from pyspark.sql import SparkSession

spark=SparkSession.builder.getOrCreate()
#Reading csv file
df_spark=spark.read.csv('/home/raja/Documents/first.csv')
df_spark.show()