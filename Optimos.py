from sklearn.model_selection import train_test_split
import pandas as pd
from Clase_Clientes import Client, Clients
from Clases_Recommender import ColabRecommender, ContentRecommender

data          = pd.read_csv('base_de_datos.csv')
selected_cols = ["Age","Credit amount", "Duration"]
c_data        = data.loc[:,selected_cols]
clients       = Clients(c_data)

X = clients.getX()
y = clients.getY()

# Scikit-learn tiene una función que podemos usar llamada "train_test_split" 
# que nos facilita dividir nuestro conjunto de datos en datos de entrenamiento y de prueba:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)
contentRecommender = ContentRecommender(X_train,y_train)
from sklearn.model_selection import GridSearchCV

# #Creamos un nuevo modelo KNN:
knn2 = contentRecommender.knc()
 
#Creamos un diccionario de todos los valores que queremos probar para n_neighbors
prime = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97) 
param_grid = {"n_neighbors": prime} #Debemos utilizar números primos para evitar duplicados

#Usamos gridsearch para probar todos los valores de n_neighbors
knn_gscv = GridSearchCV(knn2, param_grid, cv=5)

#ajustar modelo a los datos
knn_gscv.fit(X, y)

print(knn_gscv.best_params_)
print(knn_gscv.best_score_)
