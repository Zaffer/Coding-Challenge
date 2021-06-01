"""This module does the query execution to the database"""


import io
import pandas as pd
import psycopg2 as pg

from test_dbconfig import get_db_kwargs

DB_KWARGS = get_db_kwargs()

def exc_qrs_get_dfs (query_string_list):
    """Excute the list of queries as sql and returns dataframes.

    Args:
        query_string_list ([str]): list of query strings to execute on database

    Returns:
        response ([dataframe]): the data from database a dataframe for each query

    Errors:
        response ([str]): returns a list (equal in length to args list length)
                          of string message with database error"""
    con = None
    response = []

    # declare dataframe list
    df_list = []
            
    try:
        # connect to server
        con = pg.connect(**DB_KWARGS) 
        
        # loop through the list 
        for query in query_string_list:    
            # create a cursor
            cur = con.cursor()
        
            # create new stringIO
            store = io.StringIO()
            # put query into sql
            sql_string = "COPY ({query}) TO STDOUT WITH CSV HEADER".format(query=query)
            # put sql response into stringio
            cur.copy_expert(str(sql_string), store)
            # prepare to read csv
            store.seek(0)
            # put csv into dataframe
            df = pd.read_csv(store, na_filter=False)
            # add dataframe to list
            df_list.append(df)

            # commit executions
            con.commit()
            # close the cursor
            cur.close()

            response = df_list

    except pg.Error as error:
        for query in query_string_list:
            response.append(error)
    finally:
        if con is not None:
            con.close()

    return response
    