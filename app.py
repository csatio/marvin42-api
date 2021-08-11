import streamlit as st 
from datetime import datetime
import time

st.markdown("# BITCOIN BOT MARVIN 42")


def robot():
  iter=0
  while iter<3:
    
    st.markdown(datetime.now())
    time.sleep(60)
    iter=iter+1

if __name__ == '__main__':
    robot()
    