from prophet import Prophet
from database import load_data
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------
# LOAD DATA
# -------------------------
df = load_data()

# -------------------------
# DAILY SALES
# -------------------------
daily_sales = (
    df.groupby('order_date')['amount']
    .sum()
    .reset_index()
)

# -------------------------
# RENAME COLUMNS
# Prophet requires:
# ds = date
# y = target
# -------------------------
daily_sales.rename(
    columns={
        'order_date': 'ds',
        'amount': 'y'
    },
    inplace=True
)

# -------------------------
# CREATE MODEL
# -------------------------
model = Prophet()

# Train model
model.fit(daily_sales)

# -------------------------
# FUTURE DATES
# Predict next 30 days
# -------------------------
future = model.make_future_dataframe(
    periods=30
)

# Forecast
forecast = model.predict(future)

# -------------------------
# SHOW PREDICTIONS
# -------------------------
print(
    forecast[
        ['ds', 'yhat']
    ].tail(30)
)

# -------------------------
# PLOT FORECAST
# -------------------------
fig = model.plot(forecast)

plt.title(
    "Sales Forecast"
)

plt.show()