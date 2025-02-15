### Real-Time Stock Market Dashboard  

This Streamlit application provides a real-time stock market dashboard that monitors live stock prices and trading volumes. It uses Yahoo Finance as the data source and visualizes the information using Plotly for interactive graphs.

---

## Features  
- **Real-Time Data Fetching:** Retrieves real-time stock data every few seconds.  
- **Interactive Graphs:** Displays live stock prices and trading volumes using Plotly's interactive charts.  
- **Customizable Settings:** Users can input a stock symbol (e.g., AAPL) and set the data refresh interval through the sidebar.  
- **User-Friendly Interface:** Built with Streamlit, ensuring a responsive and intuitive dashboard layout.  

---

## Requirements  
Before running the application, ensure you have the following dependencies installed:  

```sh
pip install streamlit yfinance pandas plotly
```

---

## Installation & Setup  
1. **Clone the Repository:**  
```sh
git clone <repository_url>
cd <repository_folder>
```

2. **Install Dependencies:**  
```sh
pip install -r requirements.txt
```

3. **Run the Dashboard:**  
```sh
streamlit run app.py
```

---

## Usage  
- Launch the dashboard using the command above.  
- Enter a valid stock symbol (e.g., AAPL, MSFT) in the sidebar.  
- Set your preferred data refresh interval (30 to 300 seconds).  
- View the real-time stock price chart and trading volume below.  

---

## Code Overview  
1. **Streamlit Page Configuration:**  
   - Sets the page title and layout using `st.set_page_config()`.  
2. **Sidebar Configuration:**  
   - Accepts user inputs for the stock symbol and refresh interval.  
3. **Data Fetching:**  
   - `fetch_stock_data(symbol)`: Uses the `yfinance` library to get real-time stock data with caching for efficient updates.  
4. **Plotting Function:**  
   - `plot_stock_data(data, symbol)`: Visualizes the stock's closing prices and trading volume using Plotly's `make_subplots()` function.  
5. **Real-Time Dashboard Display:**  
   - Combines the data fetching and plotting functions to display the dashboard in real-time.  

---

## Dependencies  
- **Streamlit:** For building the interactive web application.  
- **Yahoo Finance (`yfinance`):** To fetch real-time stock market data.  
- **Pandas:** For data manipulation and analysis.  
- **Plotly:** To create dynamic and interactive charts.  

---
