# Analise-Dados-com-Python

```
df = spark.read \
    .option("header", "true") \
    .option("sep", ";") \
    .option("encoding", "ISO-8859-1") \
    .option("inferSchema", "true") \
    .csv('dados')
```