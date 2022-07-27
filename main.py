import requests
import pandas as pd
import streamlit as st

url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.11428/dados?formato=json'


try:
    resp = requests.get(url)
except Exception as e:
    ...
    #return error

st.title('Evolução inflação no Brasil, dados desde 1991')

df = pd.read_json(resp.text)
df.data = pd.to_datetime(df.data)
df = df.set_index('data')
df['Acumulado 12 meses'] = df.rolling(window=12).sum()

st.line_chart(df)