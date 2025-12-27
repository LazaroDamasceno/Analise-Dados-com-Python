# Analise-Dados-com-Python

```
path = '/Volumes/workspace/default/dados_csv/'

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