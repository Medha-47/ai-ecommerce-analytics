# ai-ecommerce-analytics
# AI-Powered E-Commerce Analytics Platform

## Overview

An end-to-end **AI-powered analytics platform** for e-commerce businesses that provides interactive dashboards, business insights, sales forecasting, and customer segmentation.

The platform enables businesses to analyze **128K+ e-commerce order records**, monitor sales trends, identify customer behavior patterns, and make data-driven decisions.

### Live Demo

https://ai-ecommerce-analytics-kby2zytu7hovszryelwvsj.streamlit.app/

### GitHub Repository

https://github.com/Medha-47/ai-ecommerce-analytics

---

## Features

### Interactive Analytics Dashboard

* Dynamic filtering by **category, state, and order status**
* KPI metrics including:

  * Total Revenue
  * Total Orders
  * Average Order Value
  * Category Insights

### Sales Trend Analytics

* Revenue trend visualization over time
* State-wise and category-wise performance analysis
* Order status distribution monitoring

### AI Sales Forecasting

* Implemented **time-series forecasting using Meta Prophet**
* Predicts **future sales trends for the next 30 days**
* Interactive visual forecast charts

### AI Customer Segmentation

* Implemented **KMeans clustering**
* Groups customers based on:

  * Spending behavior
  * Order frequency
* Helps identify premium and regular customers

### Data Export

* Download filtered analytics data as CSV
* Business-friendly reporting functionality

---

## Tech Stack

**Frontend / Dashboard**

* Streamlit
* Plotly

**Backend / Data Processing**

* Python
* Pandas
* NumPy

**Machine Learning**

* Prophet (Sales Forecasting)
* Scikit-Learn (KMeans Clustering)

**Database**

* MySQL Workbench

**Deployment**

* Streamlit Community Cloud
* GitHub

---

## Project Architecture

Raw E-Commerce Data
→ Data Cleaning & Preprocessing
→ MySQL Database
→ Analytics Engine (Pandas)
→ Interactive Dashboard (Streamlit)
→ AI Forecasting (Prophet)
→ Customer Segmentation (KMeans)
→ Deployment

---

## Results & Impact

* Processed and analyzed **128K+ e-commerce records**
* Built **interactive business intelligence dashboards**
* Enabled **30-day sales prediction**
* Automated customer segmentation for behavioral analysis
* Deployed as a **live cloud-based analytics platform**

---

## Installation

Clone repository:

```bash
git clone <your-github-link>
cd ai-ecommerce-analytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```

---

## Screenshots

<img width="1915" height="947" alt="image" src="https://github.com/user-attachments/assets/3047fb49-f685-422b-9de5-ba0406ae8d01" />
<img width="1904" height="803" alt="image" src="https://github.com/user-attachments/assets/2c1eed86-a0db-47a4-84af-f3e677599bae" />
<img width="1919" height="835" alt="image" src="https://github.com/user-attachments/assets/18ccdde0-05d0-48f3-bca3-4c478e337597" />
<img width="1919" height="837" alt="image" src="https://github.com/user-attachments/assets/a8ecda82-4c8c-439b-879a-a8ecff753cae" />
<img width="1919" height="906" alt="image" src="https://github.com/user-attachments/assets/cdf6b00c-6476-4107-9229-ea5e24bbb7f4" />
<img width="1893" height="929" alt="image" src="https://github.com/user-attachments/assets/5164f26d-d76b-4766-a1ea-570797927668" />







---

## Future Improvements

* Real-time database updates
* Advanced recommendation system
* Role-based dashboards
* Cloud database integration
