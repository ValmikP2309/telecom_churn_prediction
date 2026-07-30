

import pandas as pd
import numpy as np 

def data_ingestion():
    
    df=pd.read_csv('https://raw.githubusercontent.com/ValmikP2309/telecom_churn_prediction/refs/heads/main/data/churn.csv')

    return(df)