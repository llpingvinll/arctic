import pandas as pd

tables = pd.read_html("https://job.firstvds.ru/spares.json")

print(tables[0])
