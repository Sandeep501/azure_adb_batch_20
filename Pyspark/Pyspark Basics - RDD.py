# Databricks notebook source
# -- RDD
# -- Dataframes
# -- Datasets

# COMMAND ----------

data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)
rdd

# COMMAND ----------

rdd.collect()

# COMMAND ----------

# map
def square(n):
    return n**2

rdd2 = rdd.map(square)
rdd2.collect()

# COMMAND ----------

# map
rdd2 = rdd.map(lambda x: x**2)
rdd2.collect()

# COMMAND ----------

# map in python
ls = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, ls))
squares

# COMMAND ----------

# filter 
rdd3 = rdd.filter(lambda x: x % 2 == 0)
rdd3.collect()

# COMMAND ----------

# flatMap
words_rdd = sc.parallelize(["Hello World", "Good Evening"])
# words_rdd.collect()
rdd4 = words_rdd.flatMap(lambda line: line.split(" "))
rdd4.collect()

# COMMAND ----------

rdd5 = words_rdd.map(lambda line: line.split(" "))
rdd5.collect()

# COMMAND ----------

# s = "Hello World"
# s.split()

# COMMAND ----------

# reduce
# rdd.collect() [1, 2, 3, 4, 5]
total = rdd.reduce(lambda x, y: x + y)
total

# COMMAND ----------

type(total)

# COMMAND ----------

# reduceByKey
data = [("a", 1), ("b", 2), ("c", 3), ("a", 4), ("c", 3)]
rdd = sc.parallelize(data)  # --> output [("a", 5), ("b", 2), ("c", 3)]
reduced = rdd.reduceByKey(lambda x, y: x + y)
reduced.collect()

# COMMAND ----------

# groupByKey
rdd7 = rdd.groupByKey()
# rdd.collect()
print([(k, list(v)) for k, v in rdd7.collect()])


# COMMAND ----------

print([(k, set(v)) for k, v in rdd7.collect()])
