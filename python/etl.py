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
)
import pyspark

sc = spark.sparkContext
sqlContext = SQLContext(sc)

aerei = spark.read.option("header", True).csv(
    "/home/david/Documents/data_science/python/dataset/sorgenti/aerei.csv"
)
aeroporti_dest = spark.read.option("header", True).csv(
    "/home/david/Documents/data_science/python/dataset/sorgenti/aeroporti_dest.csv"
)
aeroporti_orig = spark.read.option("header", True).csv(
    "/home/david/Documents/data_science/python/dataset/sorgenti/aeroporti_orig.csv"
)
compagnie = spark.read.option("header", True).csv(
    "/home/david/Documents/data_science/python/dataset/sorgenti/compagnie.csv"
)
log_ritardi = spark.read.option("header", True).csv(
    "/home/david/Documents/data_science/python/dataset/sorgenti/log_ritardi.csv"
)
stati_dest = spark.read.option("header", True).csv(
    "/home/david/Documents/data_science/python/dataset/sorgenti/stati_dest.csv"
)
stati_orig = spark.read.option("header", True).csv(
    "/home/david/Documents/data_science/python/dataset/sorgenti/stati_orig.csv"
)

prova1 = log_ritardi.join(
    aeroporti_orig, aeroporti_orig.IATAOrig == log_ritardi.Origin)
prova1 = prova1.join(aeroporti_dest, aeroporti_dest.IATADest == prova1.Dest)
prova1 = prova1.join(aerei, aerei.TailNumA == prova1.TailNum)
prova1 = prova1.join(compagnie, compagnie.UniqueCarrierA ==
                     prova1.UniqueCarrier)
prova1 = prova1.join(
    stati_dest, stati_dest.StateCodeDestA == prova1.StateCodeDest)
prova1 = prova1.join(
    stati_orig, stati_orig.StateCodeOrigA == prova1.StateCodeOrig)

ripulito1 = prova1.select(
    "dayofweek",
    "weekofmonth",
    "day",
    "month",
    "partofdaydep",
    "partofdayarr",
    "deptime",
    "airtime",
    "crsarrtime",
    "flightnum",
    "tailnumid",
    "actualelapsedtime",
    "crselapsedtime",
    "depdelay",
    "iataorigid",
    "iatadestid",
    "distance",
    "taxiIn",
    "taxiOut",
    "carrierdelay",
    "weatherdelay",
    "nasdelay",
    "securitydelay",
    "lateaircraftdelay",
    "airportorig",
    "countryorig",
    "statecodeorigid",
    "airportdest",
    "countrydest",
    "statecodedestid",
    "uniquecarrierid",
    "airline",
    "statenamedest",
    "regiondest",
    "statenameorig",
    "regionorig",
    "arrdelay",
)
