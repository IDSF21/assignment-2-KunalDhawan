# Performing necessary imports

import streamlit as st
st.set_page_config(layout="wide")

import numpy as np
import pandas as pd
from io import BytesIO

import matplotlib.pyplot as plt 
import plotly.figure_factory as ff
import plotly.express as px
import matplotlib
import seaborn as sns


st.markdown("# Interactive Data Science Assignment 2 | IBM Employee Data Analysis")


data = pd.read_csv('IDS_assignment2_data.csv')
#@st.cache(persist=True)


if st.sidebar.checkbox("I want to explore the data first - EDA", True, key=1):

	st.markdown("Lets look at the distribution of the chosen column for the selected department")

	select_dept = st.sidebar.selectbox('Select a Department', data['Department'].unique())

	#getting the department selected
	department_selected_data = data[data['Department'] == select_dept]

	variable = st.sidebar.radio("Select variable for EDA", ('Education', 'Age', 'Gender', 'JobRole', 'MonthlyIncome', 'PerformanceRating', 'WorkLifeBalance', 'JobInvolvement', 'JobSatisfaction'))

	if(variable == 'Age'):
		fig = plt.figure(figsize=(7, 7))
		fig = px.histogram(department_selected_data, x="Age")
		fig.update_layout(
		    title={
		        'text': 'Age distibution for ' + select_dept + ' department',
		        'x':0.5,
		        'xanchor': 'center'})

		col1, col2, col3 = st.columns([2,6,1])

		with col1:
			st.write("")

		with col2:
			st.plotly_chart(fig)

		with col3:
			st.write("")

		

	if(variable == 'Education'):
		fig, ax = plt.subplots(figsize=(7, 7))
		fig = px.pie(names=department_selected_data['Education'].value_counts().index, values=department_selected_data['Education'].value_counts().values)
		fig.update_layout(
		    title={
		        'text': 'Eduction distribution for ' + select_dept + ' department',
		        'x':0.5,
		        'xanchor': 'center'})

		col1, col2, col3 = st.columns([2,6,1])

		with col1:
			st.write("")

		with col2:
			st.plotly_chart(fig)

		with col3:
			st.write("")


	if(variable == 'Gender'):
		fig, ax = plt.subplots(figsize=(5, 5))
		fig = px.pie(names=department_selected_data['Gender'].value_counts().index, values=department_selected_data['Gender'].value_counts().values)
		fig.update_layout(
		    title={
		        'text': 'Gender distribution for ' + select_dept + ' department',
		        'x':0.5,
		        'xanchor': 'center'})

		col1, col2, col3 = st.columns([2,6,1])

		with col1:
			st.write("")

		with col2:
			st.plotly_chart(fig)

		with col3:
			st.write("")


	if(variable == 'JobRole'):
		fig, ax = plt.subplots(figsize=(5, 5))
		fig = px.pie(names=department_selected_data['JobRole'].value_counts().index, values=department_selected_data['JobRole'].value_counts().values)
		fig.update_layout(
		    title={
		        'text': 'Job role distribution for ' + select_dept + ' department',
		        'x':0.5,
		        'xanchor': 'center'})

		col1, col2, col3 = st.columns([2,6,1])

		with col1:
			st.write("")

		with col2:
			st.plotly_chart(fig)

		with col3:
			st.write("")

	if(variable == 'PerformanceRating'):
		fig, ax = plt.subplots(figsize=(5, 5))
		fig = px.pie(names=department_selected_data['PerformanceRating'].value_counts().index, values=department_selected_data['PerformanceRating'].value_counts().values)
		fig.update_layout(
		    title={
		        'text': 'Performance rating distribution for ' + select_dept + ' department',
		        'x':0.5,
		        'xanchor': 'center'})

		col1, col2, col3 = st.columns([2,6,1])

		with col1:
			st.write("")

		with col2:
			st.plotly_chart(fig)

		with col3:
			st.write("")

	if(variable == 'WorkLifeBalance'):
		fig, ax = plt.subplots(figsize=(5, 5))
		fig = px.pie(names=department_selected_data['WorkLifeBalance'].value_counts().index, values=department_selected_data['WorkLifeBalance'].value_counts().values)
		fig.update_layout(
		    title={
		        'text': 'Work life balance distribution for ' + select_dept + ' department',
		        'x':0.5,
		        'xanchor': 'center'})

		col1, col2, col3 = st.columns([2,6,1])

		with col1:
			st.write("")

		with col2:
			st.plotly_chart(fig)

		with col3:
			st.write("")

	if(variable == 'JobInvolvement'):
		fig, ax = plt.subplots(figsize=(5, 5))
		fig = px.pie(names=department_selected_data['JobInvolvement'].value_counts().index, values=department_selected_data['JobInvolvement'].value_counts().values)
		fig.update_layout(
		    title={
		        'text': 'Job involvement distribution for ' + select_dept + ' department',
		        'x':0.5,
		        'xanchor': 'center'})

		col1, col2, col3 = st.columns([2,6,1])

		with col1:
			st.write("")

		with col2:
			st.plotly_chart(fig)

		with col3:
			st.write("")

	if(variable == 'JobSatisfaction'):
		fig, ax = plt.subplots(figsize=(5, 5))
		fig = px.pie(names=department_selected_data['JobSatisfaction'].value_counts().index, values=department_selected_data['JobSatisfaction'].value_counts().values)
		fig.update_layout(
		    title={
		        'text': 'Job satisfaction distribution for ' + select_dept + ' department',
		        'x':0.5,
		        'xanchor': 'center'})

		col1, col2, col3 = st.columns([2,6,1])

		with col1:
			st.write("")

		with col2:
			st.plotly_chart(fig)

		with col3:
			st.write("")


	if(variable == 'MonthlyIncome'):
		fig = plt.figure(figsize=(7, 7))
		fig = px.histogram(department_selected_data, x="MonthlyIncome", nbins=20)
		fig.update_layout(
		    title={
		        'text': 'Monthly income ($) distibution for ' + select_dept + ' department',
		        'x':0.5,
		        'xanchor': 'center'})

		col1, col2, col3 = st.columns([2,6,1])

		with col1:
			st.write("")

		with col2:
			st.plotly_chart(fig)

		with col3:
			st.write("")


if st.sidebar.checkbox("Let's dive into the stories this dataset can tell", False, key=1):
	st.markdown("##### Lets look at the insights we can gain from this data")

	"""
	For this, let's divide out data into 2 sets of variables:

	* Category 1-

		1. Total working years (integer) - Years of experience of the candidate
		2. Job role (categorical) - The current role of the candidate at the company
		3. Education (categorical) - The education level of the candidate
		4. Gender (categorical) - The gender of the candidate
		5. Age (integer) - The age of the candidate

	* Category 2-

		1. Work life balance (categorical) - Work life balance of the candidate
		2. Monthly salary (integer) - Monthly salary of the candidate
		3. Job Satisfaction (categorical) - Job Satisfaction of the candidate
	"""

	st.markdown('Please Select Category1, Category2, and the department from the buttons on the left pannel')


	category_years = pd.cut(data.TotalWorkingYears,bins=[0,4,8,12,16,20,24,28,32,36,40],labels=['0-4','4-8','8-12','12-16','16-20','20-24','24-28','28-32','32-36','36-40'])
	data['TotalWorkingYears_cat'] = category_years

	category_age = pd.cut(data.Age,bins=[18, 22, 26, 30, 34, 38, 42, 46 , 50, 54, 60],labels=['18-22','22-26','26-30','30-34','34-38','38-42','42-46','46-50','50-54','54-60'])
	data['Age_cat'] = category_age

	category_MonthlyIncome = pd.cut(data.MonthlyIncome,bins=[1000, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000],labels=['1000-2500','2500-5000','5000-7500','7500-10000','10000-12500','12500-15000','15000-17500','17500-20000'])
	data['MonthlyIncome_cat'] = category_MonthlyIncome

	select_dept_2 = st.sidebar.selectbox('Select a Department', data['Department'].unique(), key=2)
	#getting the department selected
	department_selected_data = data[data['Department'] == select_dept_2]

	category1 = st.sidebar.radio("Select category 1", ('TotalWorkingYears', 'Education', 'Gender', 'JobRole', 'Age'))
	category2 = st.sidebar.radio("Select category 2", ('MonthlyIncome', 'WorkLifeBalance',  'JobSatisfaction'))


	if(category1 == 'TotalWorkingYears'):
		category1 = 'TotalWorkingYears_cat'

	if(category1 == 'Age'):
		category1 = 'Age_cat'

	if(category2 == 'MonthlyIncome'):
		category2 = 'MonthlyIncome_cat'

	df_temp = pd.crosstab(department_selected_data[category2], department_selected_data[category1])
	df_temp = (df_temp - df_temp.mean())/df_temp.std()

	fig = plt.figure(figsize=(10,7))
	ax = plt.axes()
	ax = sns.heatmap(df_temp)
	if(category1=='JobRole'):
		plt.xticks(rotation=15)
	buf = BytesIO()
	fig.savefig(buf, format="png")
	#st.pyplot(fig)

	st.markdown('  ')
	st.markdown("Based on your selection, following is the standardized count (zero mean, unit variance) of 'Category 2' variable per unique element in 'Category 1' ")

	col1, col2, col3 = st.columns([1,6,1])

	with col1:
		st.write("")

	with col2:
		st.image(buf)

	with col3:
		st.write("")


	st.markdown('  ')
	st.markdown('  ')
	st.markdown('  ')
	"""
	Playing with the above plot, we can make the following deductions - 

	* Across all departments, we can see that as the Years of Experience of the person increases, their salary increases, as expected.
	* For Department 'Research and Development', we see that people tend to get into the higher salary bucket at lesser years of experience as compared to 'Sales' and 'Human Resources Department'.
	* We see that education has a lesser correlation with Salary bucket as compared to Years of Experience, demonstrating that the company considered gives higher importance to the Years of Experience parameter as compared to Education level. Though, on average, candidates with Masters and Doctorate degrees have comparatively higher salaries than their counterparts, as seen by the sharp maroon blocks.
	* Age has a similar trend vs monthly salary like Years of experience, though not as sharp, showing that Years of experience matter more than age while deciding compensation.
	* For work-life balance vs education level in Research and Development department, we observe that candidates with Doctorate degree have comparatively bad work life balance as compared to other education levels.
	* Interestingly, for the different Job Levels in Research and Development Department, we observe that 'Manager' tends to have lower job satisfaction as compared to other job titles. Similarly, for the Sales department, the "Sales Executive" position tends to have the lowest job satisfaction.
	"""

	