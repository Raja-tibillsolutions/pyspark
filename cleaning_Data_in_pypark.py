from pyspark.sql import SparkSession
#from pyspark.sql.functions import col
from  pyspark.sql.functions import lit

spark=SparkSession.builder.getOrCreate()

#Droping empty rows
#df=spark.read.csv('/home/raja/Documents/first.csv')
#n=df.dropna()
#n.show()
# n.repartition(1).write.mode('overwrite').format('csv').save('/home/raja/Documents/spark/drop_empty_in_pyspark.csv')


#droup duolicates
# df=spark.read.csv('/home/raja/Documents/first.csv')
# df.dropDuplicates().repartition(1).write.mode('overwrite').format('csv').save('/home/raja/Documents/spark/drop_duplicates_in_spark')

#Filling Empty rows With NA
# df=spark.read.csv('/home/raja/Documents/first.csv')
# df.na.fill('NA').show()


#Deleteing paticular column

#df=spark.read.csv('/home/raja/Documents/first.csv',header=True)
#d=df.drop('Name')
#d.show()

#Selecting paticular column

#df=spark.read.csv('/home/raja/Documents/first.csv',header=True)
#df.select('Name').show()

#Filtering the data on perticular values
#df=spark.read.csv('/home/raja/Documents/first.csv',header=True)
#df.filter(df.age == 22).show(truncate=False)


#Filling NA values with Thier Values
#df=spark.read.csv('/home/raja/Documents/first.csv',header=True)
#df.na.fill({'Name':'Raja','age':22,'phone':8096436911}).show()

#Add new column with static data
#df=spark.read.csv('/home/raja/Documents/first.csv',header=True)
#df.withColumn('place',lit('Bangalore')).show()
#Drop coloumn
df=spark.read.csv('/home/raja/Documents/first.csv')
df.drop(col('Name')).show()
