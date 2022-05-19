from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import functions as F

spark=SparkSession.builder.getOrCreate()
'''
flatten_schema=StructType(fields=[
    StructField('sensorName',StringType(),False),
    StructField('sensorDate',StringType(),True),
    StructField('sensorReading',ArrayType(
    StructType([
    StructField('sensorChannel',IntegerType(),False),
    StructField('sensorReading',DoubleType(),True),
    StructField('datetime',StringType(),True)

    ])

    ))
])

df=spark.read.json('/home/raja/Documents/schema.json',schema=flatten_schema)
df.show(truncate=0)
'''

f_schema=StructType(fields=[
    StructField('people',ArrayType(
    StructType([
    StructField('firstName',StringType(),False),
    StructField('lastName',StringType(),True),
    StructField('gender',StringType(),True),
    StructField('age',IntegerType(),True),
    StructField('number',StringType(),True)

    ])
    ))
])

schema = StructType().add('people',ArrayType(StructType().add('firstName',StringType()).add('lastName',StringType()).add('gender',StringType()).add('age',IntegerType()).add('number',StringType())))


df=spark.read.option('multiline','true').json('/home/raja/Downloads/sample4.json',schema=f_schema)
df=df.withColumn('exploded',F.explode(df['people']))
df = df.select(df['exploded'])
df.show(truncate=0)