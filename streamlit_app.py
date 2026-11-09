
import yfinance as yf
import pandas as pd
import streamlit as st

st.title("Microsoft (MSFT) Sharpe Ratio")

ticker = "MSFT"
rf_monthly = 0.0025

# Download 5 years of monthly stock data
data = yf.download(ticker, period="5y", interval="1mo")

if not data.empty:
    close_prices = data["Close"][ticker]

    monthly_returns = close_prices.pct_change().dropna()

    excess_returns = monthly_returns - rf_monthly
    mean_excess_return = excess_returns.mean()
    std_dev_return = monthly_returns.std()

    monthly_sharpe_ratio = mean_excess_return / std_dev_return

    st.metric(
        label="Monthly Sharpe Ratio",
        value=f"{monthly_sharpe_ratio:.3f}"
    )
else:
    st.error("No data found for MSFT.")
