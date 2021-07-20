import pandas as pd

def get_data(file_name, col_names): 
    df = pd.read_csv(file_name, 
                 sep="\s", 
                 header=None, 
                 names = col_names, 
                 usecols=[0, 1, 2, 3, 4, 5])
    
    return df