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


ticker_1 = 'AAPL'
ticker_2 = 'TSLA'

t1 = yf.Ticker(ticker_1)
hist_1 = t1.history(period='3mo')
t2 = yf.Ticker(ticker_2)
hist_2 = t2.history(period='3mo')


st.subheader(ticker_1)
st.dataframe(hist_1.style.highlight_max(axis=0))
st.subheader(ticker_2)
st.dataframe(hist_2.style.highlight_max(axis=0))



st.line_chart(hist_1.Open)
st.line_chart(hist_2.Open)

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
