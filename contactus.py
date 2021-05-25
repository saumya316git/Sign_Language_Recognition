import streamlit as st
import requests
import pandas as pd
from io import BytesIO
def contact():
	st.write('')
	st.write('')
	st.write('')
	st.warning('We would love to hear your thoughts,suggestions,concerns or problems with anything so that we can improve.')
	googleform = '[Click here to fill survey form](https://docs.google.com/forms/d/e/1FAIpQLScson_jNZPU7-pDtNq0nG0YVvjaIHRSm2et5KG9GxaCi_ZxjQ/viewform)'
	st.markdown(googleform, unsafe_allow_html=True)
	r = requests.get('https://docs.google.com/spreadsheets/u/1/d/1YMvnSUQcKrqu2SY-f9j0BpUeDYSzpQX-KmyQNVExUwE/export?format=csv&id=1YMvnSUQcKrqu2SY-f9j0BpUeDYSzpQX-KmyQNVExUwE&gid=267368344')
	data = r.content
	df = pd.read_csv(BytesIO(data),error_bad_lines=False) 
	st.write('')
	st.write('')
	st.write('')
	st.write('')
	st.write('')
	st.write('')
	st.write('')
	st.write('')


	st.success("**PRESENTERS: **")
	for i in range(1): # number of rows in your table! = 2 
		cols=st.beta_columns(3) # number of columns in each row! = 2 # first column of the ith row 
		cols[0].image('images\\SA1.jpg',use_column_width=True)
		cols[1].image('images\\SG3.png',use_column_width=True)
		cols[2].image('images\\RT1.jpg',use_column_width=True)

	for i in range(1): # number of rows in your table! = 2 
		cols=st.beta_columns(3) # number of columns in each row! = 2 # first column of the ith row 
		cols[0].write('__SAUMYA ACHANTANI__',use_column_width=True)
		cols[1].write('__SAUMYA GUPTA__',use_column_width=True)
		cols[2].write('__RUPALI TANEJA__',use_column_width=True)


	linkrt = '[LinkedIn](https://www.linkedin.com/in/saumyaachantani-2000/)'
	linksg = '[LinkedIn](https://www.linkedin.com/in/saumya-gupta-60a9481a9)'
	linksa = '[LinkedIn](https://www.linkedin.com/in/rupali-taneja-ba2619169)'

	for i in range(1): # number of rows in your table! = 2 
		cols=st.beta_columns(3) # number of columns in each row! = 2 # first column of the ith row 
		cols[0].markdown(linkrt, unsafe_allow_html=True)
		cols[1].markdown(linksg, unsafe_allow_html=True)
		cols[2].markdown(linksa, unsafe_allow_html=True)
	mailrt = '[Mail](saumya18csu194@ncuindia.edu)'
	mailsg = '[Mail](saumya18csu195@ncuindia.edu)'
	mailsa = '[Mail](rupali18csu182@ncuindia.edu)'

	for i in range(1): # number of rows in your table! = 2 
		cols=st.beta_columns(3) # number of columns in each row! = 2 # first column of the ith row 

		cols[0].markdown('<a href="mailto:saumya18csu194@ncuindia.edu">Mail</a>', unsafe_allow_html=True)
		cols[1].markdown('<a href="mailto:saumya18csu195@ncuindia.edu">Mail</a>', unsafe_allow_html=True)
		cols[2].markdown('<a href="mailto:rupali18csu182@ncuindia.edu">Mail</a>', unsafe_allow_html=True)