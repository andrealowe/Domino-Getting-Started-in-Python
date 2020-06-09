import pickle
import datetime
import pandas as pd

#bring in serialized model
with open('model.pkl', 'rb') as f:
    m = pickle.load(f)
    
    
#function that uses model to predict the power generation 
def predict(year, month, day):
    '''
    Input:
    year - integer
    month - integer
    day - integer

    Output:
    predicted generation in MW
    '''
    ds = pd.DataFrame({'ds': [datetime.datetime(year,month,day)]})
    return m.predict(ds)['yhat'].values[0]