# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 10:09:07 2022

@author: Ahmed.k
"""

import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

#salary parsing 

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

minus_hr= minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = minus_hr.apply(lambda x: int(x.split('-')[0]))

df['max_salary'] = minus_hr.apply(lambda x: int(x.split('-')[1]))     
                                  
df['avg_salary']=(df.min_salary+df.max_salary)/2


#Company name text only 

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#state field

df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of company

df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)

#parsing of job description

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
 
#r studio 
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

#spark 
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws 
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

df.columns

df_out = df.drop(['Unnamed: 0'], axis =1)

df_out.to_csv('salary_data_cleaned.csv',index = False)
