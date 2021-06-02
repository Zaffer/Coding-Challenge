"""This module has the functions that get data from the database"""


import logging as log
#import io
from pandas import DataFrame
from flask import request


from test_database import (
    execute_queries_get_dataframes,
    exc_qrs_get_dfs)

log.basicConfig(level=log.DEBUG)
log.info('----- QRS_GETS.PY -----')


def get_table(table=None):
    """Gets all data needed to display map from the desk being scanned.

    Args:
        table=None (str): determines which table to return

    Return:
        response_object (obj): python object of returned dataframes of the following:
            "users_table" (df): if arg was user
            "data_table" (df): if arg was data"""
    log.info(">> get_table(table=None). table: %s", table)

    # ˅
    person_query = request.args.get('person')
    print(person_query)
    query_select_records = (
        "SELECT * FROM records WHERE person = '{person}'".format(person=person_query))

    # query_select_data = ("SELECT * FROM data")

    query_list = [
        query_select_records,
        # query_select_data
    ]
    log.info("query list: %s", query_list)

    try:
        # get the data
        response_list = exc_qrs_get_dfs(query_list)
        log.info("database responses: %s", response_list)

        response_object = {
            "records_table": response_list[0],
            "data_table": response_list[1]}

    except Exception as error:
        log.info(error)
        return error

    # ˅
    if table == "records":
        response_object.pop("data_table")
        return response_object

    if table == "data":
        response_object.pop("records_table")
        return response_object

    return response_object
