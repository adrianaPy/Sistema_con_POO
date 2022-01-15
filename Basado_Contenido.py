import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import warnings
from Clase_Clientes import Client, Clients
from Clases_Recommender import ColabRecommender, ContentRecommender
from Diccionario import credict

warnings.filterwarnings("ignore")

data          = pd.read_csv('base_de_datos.csv')
numeric_data  = data.loc[:,["Age","Credit amount","Duration"]]
clients       = Clients(numeric_data)
indices = np.arange(1000)

#Análisis de datos...
X = clients.getX() # Guarda datos normalizados
y = clients.getY() # Asigna etiquetas

# Dividimos los datos en prueba y entrenamiento:
X_train, X_test, Y_train, y_test,indices_train,indices_test  = train_test_split(X,y,indices,test_size=0.2, random_state=1, stratify=y)
# Declaramos el constructor de la clase de recomendación por contenido:
contentRecommender = ContentRecommender(X_train,Y_train)

# Con el objeto declarado contentRecommender, llamamos a la función set_neighbors
contentRecommender.set_neighbors(15)
contentRecommender.knc_fit()

clients_test =  data.loc[indices_test,["Age","Credit amount","Duration"]]
clients_test['Key'] = contentRecommender.knc_recommend(X_test)[0:200]


clients_test['Recommendation'] = clients_test['Key'].map(credict)
print(clients_test)


