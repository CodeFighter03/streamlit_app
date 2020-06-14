import streamlit as st
import pandas as pd
import numpy as np
import autosentiment as at
import time

dfx=pd.DataFrame({
        'first column':[1,2,3,4,5],
        'second column':[10,20,30,40,50]
    })

st.title('BISMILLAHIR RAHMANIR RAHIM')
if st.checkbox('Show data'):
     dfx




option = st.sidebar.selectbox(
    'Which number do you like best?',
     dfx['first column'])

'You selected:', option


chart_line=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.sidebar.line_chart(chart_line)

'Starting a long compution'

latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'.....and now we\'re done!'


st.text('Design and Developed by \nSazin Reshed Samin'
        '\nEmail : sazinsamin50@gmail.com')




















