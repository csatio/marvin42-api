import pandas as pd
import streamlit as st 
from datetime import datetime
import time
import requests
import os

urlbase = 'https://mighty-bastion-45199.herokuapp.com/'


def get_result(x):
    try:
        result = pd.DataFrame.from_dict(x.json())
    except:
        result = x.text
    return result

def api_post(route, payload):
    url = urlbase + route
    x = requests.post(url, data = payload)
    df = get_result(x)
    return df

def api_get(route):
    url = urlbase + route
    x = requests.get(url)
    df = get_result(x)
    return df

st.markdown("# BITCOIN BOT MARVIN 42")


def robot():
  token = os.environ.get('MARVIN_TOKEN')
  ticker = 'BTCUSDT'
  df = api_post('cripto_quotation', {'token': token, 'ticker': ticker})

  iter=0
  while iter<3:
    
    st.markdown(datetime.now())
    st.write(df.tail)

    time.sleep(60)
    iter=iter+1

if __name__ == '__main__':
    robot()
    