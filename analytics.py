from database import load_data


# Load data
df = load_data()

print("\n===== DATASET INFO =====")
print(df.shape)


# -------------------------
# KPI 1: Total Revenue
# -------------------------
total_revenue = df['amount'].sum()

print("\nTotal Revenue:")
print(round(total_revenue, 2))


# -------------------------
# KPI 2: Total Orders
# -------------------------
total_orders = len(df)

print("\nTotal Orders:")
print(total_orders)


# -------------------------
# KPI 3: Average Order Value
# -------------------------
avg_order_value = df['amount'].mean()

print("\nAverage Order Value:")
print(round(avg_order_value, 2))


# -------------------------
# KPI 4: Categories Revenue
# -------------------------
category_sales = (
    df.groupby('category')['amount']
    .sum()
    .sort_values(ascending=False)
)

print("\n===== TOP CATEGORIES =====")
print(category_sales.head())


# -------------------------
# KPI 5: Top States
# -------------------------
top_states = (
    df.groupby('ship_state')['amount']
    .sum()
    .sort_values(ascending=False)
)

print("\n===== TOP STATES =====")
print(top_states.head())


# -------------------------
# KPI 6: Order Status
# -------------------------
status_summary = (
    df['status']
    .value_counts()
)

print("\n===== ORDER STATUS =====")
print(status_summary.head())