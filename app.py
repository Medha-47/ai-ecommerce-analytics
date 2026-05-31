import streamlit as st
import plotly.express as px
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="AI E-Commerce Analytics",
    layout="wide"
)

# -------------------------
# LOAD DATA
# -------------------------
@st.cache_data
def get_data():

    df = pd.read_csv(
        "data/cleaned_ecommerce.csv"
    )

    df['order_date'] = pd.to_datetime(
        df['order_date']
    )

    return df

df = get_data()

# -------------------------
# TITLE
# -------------------------
st.title("📊 AI-Powered E-Commerce Analytics Platform")

st.markdown("""
Analyze sales, customer behavior,
revenue trends, and business insights.
""")

st.divider()

# -------------------------
# FILTERS
# -------------------------
st.subheader("🔍 Filters")

col1, col2, col3 = st.columns(3)

# CATEGORY FILTER
with col1:

    category_options = sorted(
        df['category']
        .dropna()
        .unique()
        .tolist()
    )

    selected_category = st.multiselect(
        "Category",
        options=category_options,
        placeholder="Select category..."
    )

# STATE FILTER
with col2:

    state_options = sorted(
        df['ship_state']
        .dropna()
        .unique()
        .tolist()
    )

    selected_state = st.multiselect(
        "State",
        options=state_options,
        placeholder="Select states..."
    )

# STATUS FILTER
with col3:

    status_options = sorted(
        df['status']
        .dropna()
        .unique()
        .tolist()
    )

    selected_status = st.multiselect(
        "Order Status",
        options=status_options,
        placeholder="Select order status..."
    )

# -------------------------
# APPLY FILTERS
# -------------------------
filtered_df = df.copy()

# Category Filter
if selected_category:
    filtered_df = filtered_df[
        filtered_df['category']
        .isin(selected_category)
    ]

# State Filter
if selected_state:
    filtered_df = filtered_df[
        filtered_df['ship_state']
        .isin(selected_state)
    ]

# Status Filter
if selected_status:
    filtered_df = filtered_df[
        filtered_df['status']
        .isin(selected_status)
    ]

st.divider()

# -------------------------
# KPI CALCULATIONS
# -------------------------
total_revenue = filtered_df['amount'].sum()

total_orders = len(filtered_df)

avg_order_value = (
    filtered_df['amount']
    .mean()
)

total_categories = (
    filtered_df['category']
    .nunique()
)

# -------------------------
# KPI CARDS
# -------------------------
st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Total Revenue",
        f"₹{total_revenue:,.2f}"
    )

with col2:
    st.metric(
        "📦 Total Orders",
        total_orders
    )

with col3:
    st.metric(
        "🛒 Avg Order Value",
        f"₹{avg_order_value:,.2f}"
    )

with col4:
    st.metric(
        "🧵 Categories",
        total_categories
    )

st.divider()

# -------------------------
# CHARTS
# -------------------------
col1, col2 = st.columns(2)

# REVENUE BY CATEGORY
with col1:

    category_sales = (
        filtered_df
        .groupby('category')['amount']
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category_sales,
        x='category',
        y='amount',
        title='Revenue by Category'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# REVENUE BY STATE
with col2:

    unique_states = (
        filtered_df['ship_state']
        .nunique()
    )

    if unique_states > 1:

        state_sales = (
            filtered_df
            .groupby('ship_state')['amount']
            .sum()
            .sort_values(
                ascending=False
            )
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            state_sales,
            x='ship_state',
            y='amount',
            title='Top States by Revenue'
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    elif len(filtered_df) > 0:

        selected_state_name = (
            filtered_df['ship_state']
            .iloc[0]
        )

        state_revenue = (
            filtered_df['amount']
            .sum()
        )

        state_orders = len(filtered_df)

        st.subheader(
            f"📍 {selected_state_name}"
        )

        st.metric(
            "Revenue",
            f"₹{state_revenue:,.2f}"
        )

        st.metric(
            "Orders",
            state_orders
        )

st.divider()

# -------------------------
# ORDER STATUS DISTRIBUTION
# -------------------------
st.subheader(
    "📦 Order Status Distribution"
)

status_counts = (
    filtered_df['status']
    .value_counts()
    .reset_index()
)

status_counts.columns = [
    'status',
    'count'
]

fig = px.pie(
    status_counts,
    names='status',
    values='count',
    hole=0.4
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -------------------------
# SALES TREND OVER TIME
# -------------------------
st.divider()

st.subheader(
    "📈 Sales Trend Over Time"
)

# Daily Revenue
daily_sales = (
    filtered_df
    .groupby('order_date')['amount']
    .sum()
    .reset_index()
)

# Create Line Chart
fig = px.line(
    daily_sales,
    x='order_date',
    y='amount',
    title='Daily Revenue Trend',
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------
# AI SALES FORECASTING
# -------------------------
from prophet import Prophet

st.divider()

st.subheader(
    "🤖 AI Sales Forecast"
)

# Daily Sales
daily_sales = (
    filtered_df
    .groupby('order_date')['amount']
    .sum()
    .reset_index()
)

# Prophet format
forecast_data = (
    daily_sales.rename(
        columns={
            'order_date': 'ds',
            'amount': 'y'
        }
    )
)

# Train Model
model = Prophet()

model.fit(forecast_data)

# Future Dates
future = (
    model.make_future_dataframe(
        periods=30
    )
)

# Predict
forecast = (
    model.predict(future)
)

# Forecast Chart
fig = model.plot(forecast)

st.pyplot(fig)

# -------------------------
# CUSTOMER SEGMENTATION
# -------------------------
st.divider()

st.subheader(
    "🧠 AI Customer Segmentation"
)

# Customer Summary
customer_data = (
    filtered_df
    .groupby('ship_postal_code')
    .agg({
        'amount': 'sum',
        'order_id': 'count'
    })
    .reset_index()
)

customer_data.columns = [
    'customer_id',
    'total_spent',
    'total_orders'
]

# Scale data
scaler = StandardScaler()

scaled_features = scaler.fit_transform(
    customer_data[
        ['total_spent',
         'total_orders']
    ]
)

# KMeans
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

customer_data['segment'] = (
    kmeans.fit_predict(
        scaled_features
    )
)

# Rename segments
segment_names = {
    0: 'Regular Customers',
    1: 'Premium Customers',
    2: 'Low Value Customers'
}

customer_data['segment_name'] = (
    customer_data['segment']
    .map(segment_names)
)

# Plot
fig = px.scatter(
    customer_data,
    x='total_orders',
    y='total_spent',
    color='segment_name',
    title='Customer Segmentation'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------
# AI BUSINESS INSIGHTS
# -------------------------
st.divider()

st.subheader(
    "🧠 AI Business Insights"
)

# Metrics Calculation
top_category = (
    filtered_df
    .groupby('category')['amount']
    .sum()
    .idxmax()
)

top_state = (
    filtered_df
    .groupby('ship_state')['amount']
    .sum()
    .idxmax()
)

cancelled_orders = (
    filtered_df[
        filtered_df['status']
        .str.contains(
            "Cancelled",
            case=False,
            na=False
        )
    ]
)

cancellation_rate = (
    len(cancelled_orders)
    / len(filtered_df)
) * 100

highest_sales_day = (
    filtered_df
    .groupby('order_date')['amount']
    .sum()
    .idxmax()
)

best_day_revenue = (
    filtered_df
    .groupby('order_date')['amount']
    .sum()
    .max()
)

# Layout
col1, col2 = st.columns(2)

with col1:

    st.success(
        f"""
📌 Top Revenue Category: **{top_category}**

📍 Highest Revenue State: **{top_state}**

📦 Total Orders: **{len(filtered_df):,}**
"""
    )

with col2:

    st.info(
        f"""
❌ Cancellation Rate: **{cancellation_rate:.2f}%**

📈 Highest Sales Day: **{highest_sales_day}**

💰 Revenue on Best Day: **₹{best_day_revenue:,.2f}**
"""
    )

# -------------------------
# EXPORT FILTERED DATA
# -------------------------
st.divider()

st.subheader(
    "📥 Export Data"
)

csv = filtered_df.to_csv(
    index=False
)

st.download_button(
    label="⬇️ Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_ecommerce_data.csv",
    mime="text/csv"
)

# -------------------------
# FILTERED DATA TABLE
# -------------------------
st.subheader("📄 Filtered Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)