import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from datetime import datetime

# Streamlit Page Configuration
st.set_page_config(page_title="Real-Time Stock Market Dashboard", 
                   layout="wide")

# Sidebar Configuration
st.sidebar.title("Stock Market Dashboard")
STOCK_SYMBOL = st.sidebar.text_input("Enter Stock Symbol", value="AAPL")
REFRESH_INTERVAL = st.sidebar.slider("Refresh Interval (seconds)", 30, 300, 60)

# Fetch Real-Time Data
@st.cache_data(ttl=REFRESH_INTERVAL)
def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1d", interval="1m")
    return hist

# Plotting Function
def plot_stock_data(data, symbol):
    fig = make_subplots(rows=2, cols=1, 
                        shared_xaxes=True,
                        row_heights=[0.7, 0.3],
                        vertical_spacing=0.2,
                        subplot_titles=(f"{symbol} Real-Time Stock Price", "Trading Volume"))
    
    # Closing Price Line Chart
    fig.add_trace(go.Scatter(x=data.index, 
                             y=data['Close'], 
                             mode='lines', 
                             name='Close Price',
                             line=dict(color='blue', width=2)), 
                  row=1, col=1)
    
    # Volume Bar Chart
    fig.add_trace(go.Bar(x=data.index, 
                         y=data['Volume'], 
                         name='Volume',
                         marker_color='orange'), 
                  row=2, col=1)
    
    # Update Layout
    fig.update_layout(title=f"{symbol} Real-Time Stock Dashboard",
                      xaxis_title="Time",
                      yaxis_title="Price (USD)",
                      xaxis2_title="Time",
                      yaxis2_title="Volume",
                      template="plotly_dark",
                      showlegend=True,
                      height=800)
    
    fig.update_xaxes(rangeslider_visible=False)
    return fig

# Real-Time Dashboard Display
st.title("📊 Real-Time Stock Market Dashboard")
st.subheader(f"Live Monitoring of {STOCK_SYMBOL}")

data = fetch_stock_data(STOCK_SYMBOL)

if not data.empty:
    st.plotly_chart(plot_stock_data(data, STOCK_SYMBOL), use_container_width=True)
else:
    st.warning("No data available. Please check the stock symbol or try again later.")

st.info(f"Dashboard refreshes every {REFRESH_INTERVAL} seconds.")
