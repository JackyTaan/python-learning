from pyspark.sql import SparkSession

# May take a little while on a local computer
spark = SparkSession.builder.appName("Basics").getOrCreate()

# We'll discuss how to read other options later.
# This dataset is from Spark's examples

# Might be a little slow locally
df = spark.read.json('people.json')

# Note how data is missing!
df.show()

df.printSchema()

df.columns

df.describe()

# from pyspark.sql.types import StructField,StringType,IntegerType,StructType

# data_schema = [StructField("age", IntegerType(), True),StructField("name", StringType(), True)]

# final_struc = StructType(fields=data_schema)

# df = spark.read.json('people.json', schema=final_struc)


# df.printSchema()

# df['age']

# type(df['age'])

# df.select('age')

# type(df.select('age'))

# df.select('age', 'name').show()

