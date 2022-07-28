import time
import requests
import pandas as pd
import streamlit as st

url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.11428/dados?formato=json'


st.set_page_config(layout="wide", page_title='Inflação no Brasil')

def load_data(url):
    try:
        resp = requests.get(url)
    except Exception as e:
        st.error('Não foi possível acessar a API do Banco do Brasil')
        return False
        #return error
    if resp.status_code != 200:
        st.error(f'Não foi possível acessar a API do Banco do Brasil, retorno {resp.status_code}')
        return False
    else:
        df = pd.read_json(resp.text)
        df.data = pd.to_datetime(df.data)
        df = df.set_index('data')
        df.rename({'valor': 'indice'}, axis=1, inplace=True)
        return df

st.title('Evolução inflação no Brasil, dados desde 1991')

with st.spinner(text="Carregando dados"):
    data = load_data(url)
if not isinstance(data, bool):
    st.line_chart(data)