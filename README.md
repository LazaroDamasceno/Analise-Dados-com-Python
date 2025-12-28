# Analise-Dados-com-Python

```
path = '/Volumes/workspace/dados_csv/bpc/'

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("sep", ";") \
    .option("encoding", "latin1") \
    .load(path)

df = spark \
    .read \
    .csv(
        path, 
        header=True, 
        encoding='latin1', 
        sep=';'
    )
```
