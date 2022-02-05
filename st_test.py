import streamlit as st
import pandas as pd
import yfinance as yf

#st.dataframe(df, 200, 100)

"""
# My first app
Here's our first attempt at using data to create a table:
"""

#import streamlit as st
import numpy as np


ticker = 'AAPL'
tsla = yf.Ticker(ticker)
hist = tsla.history(period='1y')

#dataframe = np.random.randn(10, 20)
#st.dataframe(hist)
st.dataframe(hist.style.highlight_max(axis=0))

st.line_chart(hist.Open)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data



df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option




# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)





import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

#st.table(hist)
