from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark=SparkSession.builder.getOrCreate()

#schema=StructType().add('context',StructType().add('sid',StringType()).add('did',StringType()).add('cdata',ArrayType(StructType().add('type',StringType()).add('id',StringType()).StructType().add('type',StringType()).add('id',StringType()))))\

df_spark=spark.read.json('/home/raja/Downloads/sample1.json',multiLine=True)
df_spark.show(truncate=0)