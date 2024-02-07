from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
import os
import pymysql

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load google gemini model and provide sql query as response
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([question,prompt])
    return response.text

def get_sql_response(sql):
    # Connect to the database
    MY_SQL_DB_PASSWORD = os.getenv('MY_SQL_DB_PASSWORD')
    my_db = pymysql.connect(
        host='localhost',
        user='root', 
        port=3306,
        password=MY_SQL_DB_PASSWORD,
        database='Students')
    
    my_cursor = my_db.cursor()
    my_cursor.execute(sql)
    rows = my_cursor.fetchall()
    my_db.commit()
    my_db.close()
    for row in rows:
        print(row)
    return rows
    
## Define Your Prompt
prompt="""
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, AGE, 
    DEPARTMENT \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where DEPARTMENT="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
"""

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=get_sql_response(response)
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)