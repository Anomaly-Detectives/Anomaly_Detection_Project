import numpy as np
import pandas as pd


def prep_df(df):
    # convert date to datetime and set as index
    df.date = pd.to_datetime(df.date)
    df = df.set_index(df.date)

    #fill nulls with 0 
    df = df.fillna(0) 

    # convert all date objects to datetime
    dt=['end_date', 'start_date', 'created_at', 'updated_at']
    df[dt] = df[dt].apply(pd.to_datetime)

    #drop column with nothing but null entries
    df = df.drop(columns=('deleted_at'))
    #drop id column given same info in cohort_id
    df = df.drop(columns=('id'))
    #drop duplicate date column
    df = df.drop(columns=('date'))
    #drop slack column, same as name column
    df = df.drop(columns=('slack'))
    #drop time, not needed
    df = df.drop(columns=('time'))

    #change datatype
    df.program_id = df.program_id.astype(int)
    df.cohort_id = df.cohort_id.astype(int)

    return df
