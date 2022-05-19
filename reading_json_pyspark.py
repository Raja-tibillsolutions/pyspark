from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark=SparkSession.builder.appName('json file').getOrCreate()


df_spark=spark.read.json('/home/raja/Downloads/sample4.json',multiLine=True)
df_spark.show(truncate=0)