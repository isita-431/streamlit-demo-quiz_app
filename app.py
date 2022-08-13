import streamlit as st 
import pandas as pd 
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys
import os
import streamlit.components.v1 as stc
st.set_page_config(page_title='Data Profiler',layout='wide')

st.title('QUIZ APP')

name = st.text_input(label='Enter your name : ')

st.markdown("1.What is the right syntax to load the dataframe  in pandas?")
right = st.checkbox("pandas.read_csv(‘student_records.csv’)")
n1 =st.checkbox("pandas.read.csv(‘student_records.csv’)")
n2 = st.checkbox("pandas.readcsv(‘student_records.csv’)")
n3= st.checkbox("pandas.csv(‘student_records.csv’)")
if right:
	stc.html("<p style='color:green'>Right Answer!</p>")
elif  n1 or n2 or n3:
	stc.html("<p style='color:red'>Wrong Answer!</p>")

st.markdown("2.How do we check the rows and their information and type in the data frame?")
n1 = st.checkbox("student_records.inspect_data()")
n2 =st.checkbox("student_records.inspect()")
right = st.checkbox("student_records.info()")
n3= st.checkbox("student_records.describe()")
if right:
	stc.html("<p style='color:green'>Right Answer!</p>")
elif  n1 or n2 or n3:
	stc.html("<p style='color:red'>Wrong Answer!</p>")

st.markdown("3. How to find the number of rows in a dataframe:")
n1 = st.checkbox("print(student_records.shape)")
right =st.checkbox("print(student_records.shape[0])")
n2 = st.checkbox("print(student_records.rows)")
n3= st.checkbox("print(student_records.n_rows)")
if right:
	stc.html("<p style='color:green'>Right Answer!</p>")
elif  n1 or n2 or n3:
	stc.html("<p style='color:red'>Wrong Answer!</p>")

st.markdown("4.Right syntax to Select the column  “marks” from “student_records” .(multi choice)")
n0 = st.checkbox("student_records[‘marks’]")
n1 =st.checkbox("student_records.[‘Studentname’]")
n2 = st.checkbox("student_records[‘marks’’]]")
n3= st.checkbox("student_records.marks")
if n1 and n3:
	stc.html("<p style='color:green'>Right Answer!</p>")
elif  n0 or n2:
	stc.html("<p style='color:red'>Wrong Answer!</p>")

st.markdown("5.Select the right way to select “Student name” from student_records dataframe.")
n2 = st.checkbox("student_records.Student name")
n1 =st.checkbox("student_records.[‘Student name’]")
right = st.checkbox("student_records[“Student name”]")
n3= st.checkbox("student_records[Student name]")
if right:
	stc.html("<p style='color:green'>Right Answer!</p>")
elif  n1 or n2 or n3:
	stc.html("<p style='color:red'>Wrong Answer!</p>")
