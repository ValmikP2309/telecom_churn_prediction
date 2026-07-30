

import pandas as pd
import numpy as np 

def data_ingestion():
    
    df=pd.read_csv(r'C:\telecom_churn_prediction\data\churn.csv')

    return(df)