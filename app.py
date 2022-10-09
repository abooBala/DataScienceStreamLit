import imp
import yfinance as yf
import streamlit as sl
import pandas as pd

sl.write('''
# Simple Stock Price App

Shown are the stock, closing and volume of Apple

''')

tickerSymbol = 'AAPL'  # Defines the ticker symbol

tickerData = yf.Ticker(tickerSymbol) # Access data on the ticker

tickerDF = tickerData.history(period='1d', start='2001-10-05', end='2022-11-05')

sl.line_chart(tickerDF.Close)
sl.line_chart(tickerDF.Volume)
