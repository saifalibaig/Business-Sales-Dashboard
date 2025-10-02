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
✅ Sidebar filters for **Region & Category**  
✅ Key business KPIs displayed at the top  
✅ Line charts for **Sales & Profit trend over time**  
✅ Bar charts for **Sales by Category & Region**  
✅ Pie charts for **Segment-level insights**  
✅ Heatmap of **Profit by Region & Category**  
✅ Top 10 products by sales visualization  
✅ Pareto Analysis to identify **top customers driving revenue**  

---

## 📊 Dataset  
The app uses a sample **retail sales dataset** (`train.csv`) containing:  
- **Order Details**: Order Date, Customer ID, Region, Category, Product Name  
- **Financial Metrics**: Sales, Profit, Discount  
- **Customer Segments** (if available)  

> If the dataset does not include Profit, it is automatically calculated.  

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
