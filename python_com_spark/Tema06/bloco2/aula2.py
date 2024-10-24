from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

schema = StructType([
    StructField("id", StringType(), True),
    StructField("nome", StringType(), True),
    StructField("idade", StringType(), True)
])



df = spark.read.option("multiline", "true").json("arquivo.json")
df.show()

df.printSchema()
df.select("nome").show()
df.select(df["nome"], df["idade"] + 1).show()
df.groupBy("idade").count().show()
df.createOrReplaceTempView("people")
sqlDF = spark.sql("SELECT * FROM people")
sqlDF.show()

df.createGlobalTempView("people")

spark.sql('SELECT * FROM global_temp.people').show()
spark.newSession().sql("SELECT * FROM global_temp.people").show()