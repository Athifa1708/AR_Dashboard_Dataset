from sales_model import get_person_data, get_kpis
from generate_charts import generate_3d_data
import pandas as pd

print('CSV exists:', pd.io.common.exists('sales_data.csv'))
print('person_data keys sample:', list(get_person_data().keys())[:3])
print('kpis:', get_kpis())
print('3d bars count:', len(generate_3d_data()['bars']))
