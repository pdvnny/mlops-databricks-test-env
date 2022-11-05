# Databricks notebook source
inp1 = [1, 2, 3, 4, 5] # testing if the methods can receive and return values


inp2 = [5, 4, 3, 2, 1] # testing if the method can sort 


expect = [1, 2, 3, 4, 5] # This should be the answer for both tests

# COMMAND ----------

from sorting import bubble_sort, selection_sort

def test1(inp, exp):
    return (bubble_sort(inp) == exp)


def test2(inp, exp):
    return (selection_sort(inp) == exp)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Here is a reference that says ABOVE should work
# MAGIC 
# MAGIC [files-in-repos](https://docs.databricks.com/_static/notebooks/files-in-repos.html)

# COMMAND ----------

# MAGIC %md
# MAGIC # Experimenting with understanding the environment

# COMMAND ----------

import os

print(os.getcwd())

# COMMAND ----------

pwd

# COMMAND ----------

# MAGIC %md
# MAGIC Path to `sorting` file  
# MAGIC 
# MAGIC Complete path: `/Workspace/Repos/pgdunn@bu.edu/mlops-databricks-test-env/sorting.py`  
# MAGIC Relative path to current file: `sorting.py`

# COMMAND ----------

# MAGIC %md
# MAGIC I was trying to find the `sorting` script so that I can import the functions

# COMMAND ----------

# MAGIC %md
# MAGIC ls

# COMMAND ----------

# MAGIC %md
# MAGIC ls /

# COMMAND ----------

# MAGIC %md
# MAGIC ls /usr

# COMMAND ----------

# MAGIC %md
# MAGIC ls /home

# COMMAND ----------

# MAGIC %md
# MAGIC ls /Workspace

# COMMAND ----------

# MAGIC %md
# MAGIC ls /databricks
