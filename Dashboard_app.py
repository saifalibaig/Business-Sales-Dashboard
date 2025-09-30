
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Load Dataset
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv('train.csv')
    df['Order Date'] = pd.to_datetime(
        df['Order Date'],
        errors='coerce',
        dayfirst=True,
        infer_datetime_format=True
    )
    df = df.dropna(subset=['Order Date'])  # drop bad rows
    df['YearMonth'] = df['Order Date'].dt.to_period('M').astype(str)

    # ✅ Calculate Profit if missing
    if "Profit" not in df.columns:
        if "Discount" in df.columns:
            df["Profit"] = df["Sales"] * (1 - df["Discount"])
        else:
            df["Profit"] = df["Sales"] * 0.2  # assume 20% margin if cost not available

    return df

df = load_data()

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

regions = st.sidebar.multiselect(
    "Select Region:",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

categories = st.sidebar.multiselect(
    "Select Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

df_filtered = df[
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories))
]

# -----------------------------
# KPI Section
# -----------------------------
st.markdown("## 📊 Business KPIs")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Sales", f"${df_filtered['Sales'].sum():,.0f}")

with col2:
    st.metric("🏆 Total Profit", f"${df_filtered['Profit'].sum():,.0f}")

with col3:
    st.metric("🛒 Avg Order Value", f"${df_filtered['Sales'].mean():,.2f}")

with col4:
    st.metric("👥 Unique Customers", df_filtered['Customer ID'].nunique())

st.markdown("---")

# -----------------------------
# Sales & Profit Trend
# -----------------------------
trend = (
    df_filtered.groupby("YearMonth")[["Sales", "Profit"]]
    .sum()
    .reset_index()
)

fig_trend = px.line(
    trend,
    x="YearMonth",
    y=["Sales", "Profit"],
    title="📈 Monthly Sales vs Profit Trend"
)
st.plotly_chart(fig_trend, use_container_width=True)

# -----------------------------
# Sales by Category
# -----------------------------
sales_category = df_filtered.groupby("Category")["Sales"].sum().reset_index()
fig_sales_cat = px.bar(sales_category, x="Category", y="Sales", title="🗂 Sales by Category")
st.plotly_chart(fig_sales_cat, use_container_width=True)

# -----------------------------
# Sales by Region
# -----------------------------
sales_region = df_filtered.groupby("Region")["Sales"].sum().reset_index()
fig_sales_reg = px.bar(sales_region, x="Region", y="Sales", title="🌍 Sales by Region")
st.plotly_chart(fig_sales_reg, use_container_width=True)

# -----------------------------
# Sales & Profit Share by Customer Segment 
# -----------------------------
if "Segment" in df_filtered.columns:
    seg_group = df_filtered.groupby("Segment").agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    ).reset_index()

    col1, col2 = st.columns(2)

    with col1:
        fig_sales_pie = px.pie(
            seg_group,
            names="Segment",
            values="Sales",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3,
            title="🥧 Sales Share by Segment"
        )
        st.plotly_chart(fig_sales_pie, use_container_width=True)

    with col2:
        fig_profit_pie = px.pie(
            seg_group,
            names="Segment",
            values="Profit",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set2,
            title="💹 Profit Share by Segment"
        )
        st.plotly_chart(fig_profit_pie, use_container_width=True)
else:
    st.warning("⚠️ No 'Segment' column found in dataset.")

# -----------------------------
# Top Products
# -----------------------------
top_products = df_filtered.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index()
fig_top_products = px.bar(top_products, x="Sales", y="Product Name", orientation="h",
                          title="🏅 Top 10 Products by Sales")
st.plotly_chart(fig_top_products, use_container_width=True)

# -----------------------------
# Profit Heatmap
# -----------------------------
profit_pivot = df_filtered.pivot_table(
    index="Region", columns="Category", values="Profit", aggfunc="sum", fill_value=0
)

fig_heatmap = px.imshow(
    profit_pivot,
    text_auto=True,
    color_continuous_scale="RdYlGn",
    title="🔥 Profit by Region & Category"
)
st.plotly_chart(fig_heatmap, use_container_width=True)

# -----------------------------
# Pareto Analysis (80/20 rule)
# -----------------------------
customer_sales = (
    df_filtered.groupby("Customer ID")["Sales"].sum().sort_values(ascending=False).reset_index()
)
customer_sales["Cumulative %"] = 100 * customer_sales["Sales"].cumsum() / customer_sales["Sales"].sum()

fig_pareto = px.line(customer_sales, x=customer_sales.index, y="Cumulative %",
                     title="📊 Cumulative Revenue Contribution")
fig_pareto.add_bar(x=customer_sales.index, y=customer_sales["Sales"], name="Customer Sales")

st.plotly_chart(fig_pareto, use_container_width=True)


