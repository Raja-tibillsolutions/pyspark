from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('merge').getOrCreate()
#read data

df1= spark.read.csv("/home/raja/Desktop/Ekstep/Exhust_reports2/exhaust_reports/0134766018946826241_userinfo_20220823.csv",header=True)
df1.printSchema()
df2 = spark.read.csv("/home/raja/Desktop/Ekstep/Exhust_reports2/exhaust_reports/0134766018946826241_progress_20220823.csv",header=True)
df2.printSchema()

df3 = df1.join(df2,['Collection Id','Collection Name','Batch Id','Batch Name','User UUID','State','District','Org Name','School Id','School Name','User Type','User Sub Type'],how='outer')\
       .select("Collection Id",'Collection Name','Batch Id','Batch Name','User UUID','User Name','Email ID','Mobile Number','Consent Provided','Consent Provided Date','Org Name','Declared Board','User Type','User Sub Type','State','District','Block Name','Cluster Name','School Id','School Name','Enrolment Date','Completion Date','Certificate Status','Progress','do_21347654821997772818 - Score')

df3.repartition(1).write.mode('overwrite').format('csv').option('header',True).save("/home/raja/Desktop/Ekstep/Exhust_reports2/output")
