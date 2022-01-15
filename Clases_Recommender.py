from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors

class Recommender(object):
    def __init__(self,X_train,Y_train):
            self.X_train = X_train
            self.Y_train = Y_train

    def set_neighbors(self,n_neighbors=10):
        self.n_neighbors = n_neighbors

    #return KKNeighborsClassifier without parameter (nneighbors)
    def knc(self):
        self.knc = KNeighborsClassifier()
        return self.knc
        
    #Fit K-Neighbors classifer
    def knc_fit(self):
        self.knc = KNeighborsClassifier(self.n_neighbors)
        self.knc.fit(self.X_train,self.Y_train)
        
    def knc_recommend(self,users):        
        return self.knc.predict(users)

    #Fit Nearest Neighbors
    def nn_fit(self):
        self.nn  = NearestNeighbors(metric='cosine', algorithm='brute')
        self.nn.fit(self.X_train.values)
    
    def knn_kneighbors(self):
        distances, indices = self.nn.kneighbors(self.X_train.values, self.n_neighbors)
        return distances,indices

    
class ContentRecommender(Recommender):
    def __init__(self,X_train,Y_train):                
        Recommender.__init__(self,X_train,Y_train)        

    def recommend(self,users):
        return Recommender.knc_recommend(self,users)
            
class ColabRecommender(Recommender):
    def __init__(self,X_train,Y_train=None):                
        Recommender.__init__(self,X_train,Y_train)        
    
    def recommend(self,users):
        return Recommender.knc_recommend(self,users)

