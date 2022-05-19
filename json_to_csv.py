from pyspark.sql import SparkSession

spark=SparkSession.builder.getOrCreate()

df=spark.read.json('/home/raja/Downloads/sample1.json',multiLine=True)
df.repartition(1).write.mode('overwrite').format('csv').save('/home/raja/Documents/spark/json_to_csv_inpyspark.csv')
