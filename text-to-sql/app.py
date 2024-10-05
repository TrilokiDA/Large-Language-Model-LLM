# Created by trilo at 04-10-2024
from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# fun to convert text to sql with the help of gemini-pro
def genai_response(query, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], query])
    return response.text

# fun to generate data based on sql
def sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# prompt used to convert text to sql
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

# streamlit app to get input and show output to user
st.set_page_config(page_title="SQL Q&A")
st.header("Gemini App To Retrieve SQL Data")
query = st.text_input("Input", key="input")
submit = st.button("Ask the question")

if submit:
    response = genai_response(query, prompt)
    print(response)
    data = sql_query(response, "student.db")
    st.subheader("The Response is:")
    for row in data:
        print(row)
        st.header(row)
