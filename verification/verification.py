from elasticsearch import Elasticsearch
import os


ELASTICSEARCH_PROTOCOL=os.getenv('ELASTICSEARCH_PROTOCOL')
URL_ELASTICSEARCH=os.getenv('ELASTICSEARCH_DB')


es = Elasticsearch(
        hosts=[ELASTICSEARCH_PROTOCOL+URL_ELASTICSEARCH],
        #basic_auth=("usuario", "contraseña")
    )

index = "attendance_facts"
query = {
    "query": {
        "match_all": {}  # cualquier otra consulta
    }
}

response = es.search(index=index, body=query, size=10000)  # ajustar el 'size'
hits = response['hits']['hits']

attendance_data = [hit['_source'] for hit in hits]



#==========INTEGRITY OF DATA=================
import pandas as pd


df = pd.DataFrame(attendance_data)

# Verificar si hay valores nulos en los campos importantes
missing_values = df.isnull().sum()

# Verificar si los valores de ciertos campos están dentro de rangos válidos
df['worked_minutes'] = df['worked_minutes'].apply(lambda x: 0 if x < 0 else x)
df['absent_minutes'] = df['absent_minutes'].apply(lambda x: 0 if x < 0 else x)

# Verificar si hay valores negativos en campos como 'worked_minutes', 'absent_minutes', etc.
negative_values = df[df['worked_minutes'] < 0]

print("Missing Values:\n", missing_values)
print("Negative Values:\n", negative_values)




#==========ERROR OF RESULTS=================
import seaborn as sns
import matplotlib.pyplot as plt


# Histogram of worked minutes
sns.histplot(df['worked_minutes'], kde=True)
plt.title("Distribution of minutes worked")
plt.show()

# Histogram of absent minutes
sns.histplot(df['absent_minutes'], kde=True)
plt.title("Distribution of absent minutes")
plt.show()





#==========ERROR OF RESULTS=================
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Supón que tienes la columna 'scheduled_minutes' como el valor esperado
# Evaluación del error absoluto
mae = mean_absolute_error(df['scheduled_minutes'], df['worked_minutes'])

# Evaluación del error cuadrático medio
rmse = np.sqrt(mean_squared_error(df['scheduled_minutes'], df['worked_minutes']))

# Imprimir resultados
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Root Mean Squared Error (RMSE): {rmse}")





# Agrupar por posición y obtener estadísticas descriptivas
grouped_by_position = df.groupby('position').agg({
    'worked_minutes': ['mean', 'std', 'min', 'max'],
    'absent_minutes': ['mean', 'std', 'min', 'max']
})

print(grouped_by_position)
