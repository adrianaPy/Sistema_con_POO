import pandas as pd
import numpy as np
from numpy import random

#Esta funci'on construye una matriz cliente producto con el criterio de la sección 4.2
def build_client_product_matrix(clients):

    #print(clients.getNClients())
    cols = ['Tarjeta de Credito Oro','Tarjeta de Credito Plata','Tarjeta de Credito Bronce',
            'Prestamo hipotecario','Prestamo automotriz','Prestamo personal','Tarjeta de Debito',
            'Transferencias','Cuenta corriente','Cuenta de ahorro','Cambio de moneda','Cheques']
    
    
    data = pd.DataFrame(index=np.arange(clients.getNClients()),columns = cols)
      
    for i in range(clients.getNClients()):
        if clients.clients[i].get_key() == 'key_A':                
            data.at[i,'Tarjeta de Credito Oro']    = random.randint(3,5)
            data.at[i,'Tarjeta de Credito Plata']  = random.randint(2,4)
            data.at[i,'Tarjeta de Credito Bronce'] = random.randint(1,3)
            data.at[i,'Prestamo hipotecario']      = random.randint(3,5)

            data.at[i,'Prestamo automotriz']       = random.randint(3,5)
            data.at[i,'Prestamo personal']         = random.randint(3,5)
            data.at[i,'Tarjeta de Debito']         = random.randint(1,3)
            data.at[i,'Transferencias']            = random.randint(3,5)

            data.at[i,'Cuenta corriente']          = random.randint(3,5)
            data.at[i,'Cuenta de ahorro']          = random.randint(2,4)
            data.at[i,'Cambio de moneda']          = random.randint(1,3)
            data.at[i,'Cheques']                   = random.randint(3,5)

            
            
        elif clients.clients[i].get_key() == 'key_B':                
            data.at[i,'Tarjeta de Credito Oro']    = random.randint(2,4)
            data.at[i,'Tarjeta de Credito Plata']  = random.randint(3,5)
            data.at[i,'Tarjeta de Credito Bronce'] = random.randint(1,3)
            data.at[i,'Prestamo hipotecario']      = random.randint(2,4)

            data.at[i,'Prestamo automotriz']       = random.randint(3,5)
            data.at[i,'Prestamo personal']         = random.randint(3,5)
            data.at[i,'Tarjeta de Debito']         = random.randint(1,3)
            data.at[i,'Transferencias']            = random.randint(3,5)

            data.at[i,'Cuenta corriente']          = random.randint(3,5)
            data.at[i,'Cuenta de ahorro']          = random.randint(2,4)
            data.at[i,'Cambio de moneda']          = random.randint(1,3)
            data.at[i,'Cheques']                   = random.randint(3,5)

            

        else:
            data.at[i,'Tarjeta de Credito Oro']    = random.randint(1,3)
            data.at[i,'Tarjeta de Credito Plata']  = random.randint(2,4)
            data.at[i,'Tarjeta de Credito Bronce'] =  random.randint(3,5)
            data.at[i,'Prestamo hipotecario']      = random.randint(1,3)

            data.at[i,'Prestamo automotriz']       = random.randint(3,5)
            data.at[i,'Prestamo personal']         = random.randint(3,5)
            data.at[i,'Tarjeta de Debito']         = random.randint(1,3)
            data.at[i,'Transferencias']            = random.randint(3,5)

            data.at[i,'Cuenta corriente']          = random.randint(3,5)
            data.at[i,'Cuenta de ahorro']          = random.randint(2,4)
            data.at[i,'Cambio de moneda']          = random.randint(1,3)
            data.at[i,'Cheques']                   = random.randint(3,5)


            
    return data    
