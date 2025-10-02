# 📊 Business Sales Dashboard

An **interactive sales analytics dashboard** built with **Streamlit**, **Pandas**, and **Plotly**, enabling businesses to explore sales performance, profits, and customer insights with ease.

🔗 **Live Demo:** [Business Sales Dashboard](https://business-sales-dashboard.streamlit.app/)

---

## 🚀 Overview
This dashboard helps businesses monitor and analyze their sales data interactively.  
It provides **real-time KPIs, trend analysis, customer insights, and visual reports** to support better decision-making.

Key highlights:
- Track **Total Sales, Profit, Average Order Value, and Unique Customers**.
- Explore **monthly sales vs. profit trends**.
- Analyze **sales distribution by category, region, and customer segment**.
- Identify **top-performing products**.
- Visualize **profit contribution with heatmaps**.
- Apply **Pareto (80/20) analysis** to spot the most valuable customers.

---

## 🛠 Tech Stack
- **Streamlit** – Interactive web app framework  
- **Pandas** – Data processing & transformation  
- **Plotly Express** – Advanced data visualization  
- **CSV Dataset (train.csv)** – Sample business sales dataset

---

## 📂 Features
- **Sidebar Filters**: Users can filter results by *Region* and *Category*  
- **Business KPIs**: Display of total sales, total profit, average order value, and unique customers  
- **Sales & Profit Trends**: Interactive line chart showing performance over time  
- **Category & Region Analysis**: Bar charts to compare performance across product categories and regions  
- **Customer Segment Analysis**: Sales and profit share across segments (if available)  
- **Heatmap Analysis**: Profit breakdown across categories and regions  
- **Top Products**: Identify the top 10 products by sales  
- **Pareto Analysis**: Apply the 80/20 rule to spot top customers contributing to revenue  

---

## 📊 Dataset
The app uses a sample **retail sales dataset** (`train.csv`) containing:
- **Order Details**: Order Date, Customer ID, Region, Category, Product Name  
- **Financial Metrics**: Sales, Profit, Discount  
- **Customer Segments** (if available)

> If the dataset does not include `Profit`, the app automatically calculates it from `Sales` and `Discount` (or assumes a default margin).

---

## ⚙️ Installation & Usage
To run locally:

```bash
# Clone the repository
git clone https://github.com/your-username/business-sales-dashboard.git
cd business-sales-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📈 Future Enhancements

- Add a forecasting module for sales prediction  
- Include drill-down filters (e.g., sub-category level)  
- Enhance data export functionality (download reports and filtered datasets)  
- Integrate real-time data sources (SQL/Cloud databases)  
- Add user authentication and role-based dashboards  
- Build a Dockerized version for easier deployment  

---

## 🎯 Use Cases

- **Business Performance Monitoring**: Quickly track sales and profit KPIs across regions and categories  
- **Sales Reporting**: Generate insights for executives and stakeholders in a visual, interactive format  
- **Customer & Product Analysis**: Identify high-value customers and top-performing products for targeted strategies  
- **Data Storytelling**: Present insights interactively to improve decision-making and strategy discussions  

---

🔥 This project demonstrates data visualization, business analytics, and interactive dashboarding skills, highly relevant for roles in Data Science, Analytics, and Business Intelligence (BI).
