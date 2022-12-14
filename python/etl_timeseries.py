from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.functions import (
    explode,
    col,
    length,
    count,
    max,
    round,
    broadcast,
    lower,
    split,
    asc,
    desc
)
import pyspark

sc = spark.sparkContext
sqlContext = SQLContext(sc)

df = spark.read.option("header", True).csv(
    "dataset/Bakery_sales.csv"
)

df = df.drop('ticket_number')
df = df.drop('unit_price')

df.createOrReplaceTempView('prova')
prova = spark.sql(
    'select date,article,sum(int(quantity)) as quantita_totale from prova group by article,date')

prova.createOrReplaceTempView('prova')
conteggio = spark.sql(
    'select article,count(*) as conteggio from prova group by article')


baguette = spark.sql(
    'select date,quantita_totale as quantity from prova where article="TRADITIONAL BAGUETTE"')
baguette = baguette.orderBy(col(date))
baguette.repartition(1).write.csv("bakery", header=True)
