import pandas as pd
from sqlalchemy import create_engine

# Leer el archivo CSV
csv_file_path = 'C:/Users/USER/Downloads/Supervisores.csv'
df = pd.read_csv(csv_file_path)

# Crear una conexión a la base de datos
engine = create_engine('postgresql://postgres:1234@localhost:5432/Supervisors')

# Insertar los datos en la tabla articles
df.to_sql('Supervisors', engine, schema='public', if_exists='replace', index=False)