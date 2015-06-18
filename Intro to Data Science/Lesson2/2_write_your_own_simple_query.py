# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:47:31 2015

@author: altmeyer
"""

import pandas
import pandasql

def select_first_50(filename):
    # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.
    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    # Select out the first 50 values for "registrar" and "enrolment_agency"
    # in the aadhaar_data table using SQL syntax. 
    #
    # Note that "enrolment_agency" is spelled with one l. Also, the order
    # of the select does matter. Make sure you select registrar then enrolment agency
    # in your query.
    q = """
    -- YOUR QUERY HERE
    """
    print aadhaar_data

    #Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    pandasql.sqldf(aadhaar_data)
    print("SELECT * FROM aadhaar_data;", locals())
    return aadhaar_solution


select_first_50("C:\Users\\altmeyer\Documents\GitHub\Udacity\Intro to Data Science\intro_to_ds_programming_files\lesson_2\\basic_sql_quiz\\aadhaar_data.csv")