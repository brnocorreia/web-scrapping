import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np

# Vamos procurar as 50 primeiras empresas. Como cada página tem 10 empresas, buscaremos as 5 primeiras páginas. #

complete_list = []

for i in range(1,6):

    # Setando os parâmetros de url e headers para acesso a página #
    url_match = f'https://www.glassdoor.com.br/Avalia%C3%A7%C3%B5es/index.htm?overall_rating_low=0&page={i}&filterType=RATING_OVERALL'
    headers = {'user-agent':'Mozilla/5.0'}

    # Realizando o get do código macarrônico em HTML da página #
    response = requests.get(url_match, headers = headers)

    # Transformando o código macarrônico em algo mais estruturado, processo de 'parser' #
    soup = response.text
    beautiful_soup = BeautifulSoup(soup, 'html.parser')

    # Buscando todos os nomes, avaliações e segmentos e pondo-os em uma lista a ser limpa posteriormente #
    employer_name_list = beautiful_soup.find_all('h2', {'data-test': re.compile('employer-short-name')})
    employer_rating_list = beautiful_soup.find_all('span', {'data-test': re.compile('rating')})
    employer_industry_list = beautiful_soup.find_all('span', {'data-test': re.compile('employer-industry')})
    
    #  #
    for name, rating, industry in zip(employer_name_list, employer_rating_list, employer_industry_list):
        employer_name = name.text
        employer_rating = rating.text.replace(',','.')
        employer_industry = industry.text

        complete_list.append((employer_industry, employer_name, employer_rating))

        
df_complete = pd.DataFrame(complete_list, columns = ['Segmento','Nome', 'Avaliação (0.0 - 5.0)'])
df_complete