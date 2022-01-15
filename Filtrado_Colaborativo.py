import pandas as pd
from sklearn.model_selection import train_test_split
import warnings
from Clase_Clientes import Client, Clients
from Clases_Recommender import ColabRecommender
from numpy import random
from Funcion_Construccion_Matriz import build_client_product_matrix

warnings.filterwarnings("ignore")

data          = pd.read_csv('base_de_datos.csv')
numeric_data  = data.loc[:,["Age","Credit amount","Duration"]]
clients       = Clients(numeric_data)

#X = clients.getX()
y = clients.getY()


data = build_client_product_matrix(clients)

client_product_matrix = data.iloc[:,10:]
print(client_product_matrix)
#client_product_matrix = build_client_product_matrix(clients)

# y = clients.getY() #client_product_matrix['key'].values
X = client_product_matrix  #client_product_matrix.drop(columns=['key'])

#Clasifier
X_train, X_test, Y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=1, stratify=y)
colabRecommender = ColabRecommender(X_train,Y_train)
colabRecommender.set_neighbors(10)
colabRecommender.knc_fit()
#print(colabRecommender.recommend(X_test)[0:200])



#Nearest neighbors
colabRecommender_NN = ColabRecommender(X_train=X)
colabRecommender_NN.set_neighbors(10)
colabRecommender.nn_fit()
d,i = colabRecommender.knn_kneighbors()
print(d,i)

#imprimir recomendaciones y vecinos más cercanos
