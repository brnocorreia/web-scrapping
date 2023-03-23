#!/usr/bin/env python
# coding: utf-8

# In[72]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np


# In[73]:


headers = {'user-agent': 'Mozilla/5.0'}


response = requests.get('https://www.glassdoor.com.br/Sal%C3%A1rios/cientista-de-dados-sal%C3%A1rio-SRCH_KO0,18.htm', 
                        headers = headers)


# In[74]:


soup = response.text


# In[75]:


beautiful_soup = BeautifulSoup(soup, 'html.parser')


# In[76]:


employer_list = beautiful_soup.find_all('h3', 
                                        {'data-test': re.compile('salaries-list-item-.*-employer-name')})

salary_list = beautiful_soup.find_all('div', 
                                      {'data-test': re.compile("salaries-list-item-.*-salary-info")})


# In[79]:


complete_list = []

for employer, salary in zip(employer_list, salary_list):
    employer_name = employer.find('a').text
    
    employer_salary = salary.find('h3').text
    employer_salary = employer_salary.replace('R$', '').replace('\xa0', '').replace('.', '')
    
    complete_list.append((employer_name, employer_salary))
    

    


# In[80]:


df_complete = pd.DataFrame(complete_list, columns = ['Employer', 'Salary'])

df_complete['Salary'] = df_complete['Salary'].astype(np.float32)
df_complete


# In[83]:


def salary_search_glassdoor(url_glassdoor):
    headers = {'user-agent': 'Mozilla/5.0'}


    response = requests.get(url_glassdoor, 
                        headers = headers)
    
    soup = response.text
    beautiful_soup = BeautifulSoup(soup, 'html.parser')
    
    employer_list = beautiful_soup.find_all('h3', {'data-test': re.compile('salaries-list-item-.*-employer-name')})

    salary_list = beautiful_soup.find_all('div', {'data-test': re.compile("salaries-list-item-.*-salary-info")})
    
    complete_list = []

    for employer, salary in zip(employer_list, salary_list):
        employer_name = employer.find('a').text

        employer_salary = salary.find('h3').text
        employer_salary = employer_salary.replace('R$', '').replace('\xa0', '').replace('.', '')

        complete_list.append((employer_name, employer_salary))
        
    df_complete = pd.DataFrame(complete_list, columns = ['Employer', 'Salary'])

    df_complete['Salary'] = df_complete['Salary'].astype(np.float32)
    df_complete
    
    return df_complete


# In[87]:


df_civil = salary_search_glassdoor('https://www.glassdoor.com.br/Sal%C3%A1rios/engenheiro-civil-sal%C3%A1rio-SRCH_KO0,16.htm')
df_civil


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




