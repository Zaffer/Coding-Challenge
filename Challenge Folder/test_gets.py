"""
This module has the functions that gets data from the database
"""

import logging as log
from pandas import DataFrame

from test_database import exc_qrs_get_dfs

log.basicConfig(level=log.DEBUG)
log.info('----- QRS_GETS.PY -----')

def get_table (table=None, person="", type=""):
    """
    Gets all data needed to display map from the desk being scanned.

    Args:
        table=None (str): determines which table to return

    Return:
        response_object (obj): python object of returned dataframes of the following:
            "users_table" (df): if arg was user
            "data_table" (df): if arg was data
    """


    log.info(">> get_table(table=None). table: %s", table)

    # Create a list of queries to send to the database depending on the type that is selected
    if type == "text":
        query_select_data = ("SELECT data.id, data.text FROM data " +
                                "JOIN records ON records.data_id = data.id " + 
                                "WHERE records.person='" + person + "'")

        query_list = [
            query_select_data    
        ]

        log.info("query list: %s", query_list)

        try:
            # Get data from database 
            response_list = exc_qrs_get_dfs(query_list)
            log.info("database responses: %s", response_list)


            response_object = {
                "data_table": response_list[0]
            }

        except Exception as error:
            log.info(error)
            return error

        return response_object

    query_select_data = ("SELECT data.id, data.json FROM data " + 
                            "JOIN records ON records.data_id = data.id " + 
                            "WHERE records.person='" + person + "'")

    query_list = [
        query_select_data    
    ]

    log.info("query list: %s", query_list)

    try:
        # Get data from database 
        response_list = exc_qrs_get_dfs(query_list)
        log.info("database responses: %s", response_list)

        response_object = {
            "data_table": response_list[0]
        }

    except Exception as error:
        log.info(error)
        return error

    return response_object