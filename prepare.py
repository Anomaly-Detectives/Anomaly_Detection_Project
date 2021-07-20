import numpy as np
import pandas as pd


def prep_df(df):
    # convert date to datetime and set as index
    df.date = pd.to_datetime(df.date)
    df = df.set_index(df.date)

    # convert time column from object to datetime
    df.time = pd.to_datetime(df.time)

    # convert all date objects to datetime
    dt=['time', 'end_date', 'start_date', 'created_at', 'updated_at']
    df[dt] = df[dt].apply(pd.to_datetime)

    # drop column with nothing but null entries
    df = df.drop(columns=('deleted_at'))

    # drop id column given same info in cohort_id
    df = df.drop(columns=('id'))
    
    # drop duplicate date column
    df = df.drop(columns=('date'))
    
    return df