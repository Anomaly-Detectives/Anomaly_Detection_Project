import pandas as pd
from env import host, user, password
import os

#################################### TXT file ####################################

def get_data(file_name, col_names): 
    df = pd.read_csv(file_name, 
                 sep="\s", 
                 header=None, 
                 names = col_names, 
                 usecols=[0, 1, 2, 3, 4, 5])
    
    return df

#################################### SQL ####################################
#################################### Connection ####################################

def get_db_url(database, host=host, user=user, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'


#################################### merged Data ####################################

def get_sql_data():
    '''
    This function takes in sql query with two joined tables
    and returns a pandas dataframe
    '''
    #identify url
    url = get_db_url("curriculum_logs")

    #create sql query
    sql = '''
    select *
    from logs
    left join cohorts on logs.cohort_id= cohorts.id
    '''

    #read in df from sql
    df = pd.read_sql(sql, url)

    return df

#################################### Cache Merged DF ####################################

def cache_merged_data(cached=False):
    '''
    This function reads in curriculum_logs and cohorts tables (joined)
    from Codeup database and caches it as a csv.
    If a csv already exists, it is pulled directly.
    '''
    if os.path.isfile('merged_data.csv'):
        df = pd.read_csv('merged_data.csv', index_col=0)

    else:

        #creates new csv if one does not already exist
        df = get_sql_data()
        df.to_csv('merged_data.csv')

    return df

#################################### Cohort Data ####################################


def cohorts_data():
    '''
    This function reads the cohorts table from the Codeup curriculum_logs db into a df
    '''
    # Create SQL query
    sql_query = '''
                SELECT *                    
                FROM cohorts
                '''

    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('curriculum_logs'))

    return df




#################################### Cache'ing Log Data ####################################

def cache_cohorts_data(cached=False):
    '''
    This function reads in cohorts table data from Codeup curriculum_logs database and writes data to
    a csv file if cached == False or if cached == True reads in cohorts df from
    a csv file, returns df.
    '''
    if cached == False or os.path.isfile('cohorts_df.csv') == False:

        # Read fresh data from db into a DataFrame
        df = cohorts_data()

        # Cache data
        df.to_csv('cohorts_data.csv')

    else:

        # If csv file exists or cached == True, read in data from csv file.
        df = pd.read_csv('cohorts_data.csv', index_col=0)