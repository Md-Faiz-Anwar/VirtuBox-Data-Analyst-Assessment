# VirtuBox Data Analyst Assessment

## Project Overview

This project was completed as part of the Data Analyst Assessment for VirtuBox Infotech.

The analysis focuses on Brazilian e-commerce data to identify business performance trends, customer experience patterns, delivery issues, and opportunities for improvement.

The project includes data preparation, exploratory analysis, business insights, recommendations, dashboard development, and management presentation.

---

## Dataset

**Dataset:** Brazilian E-Commerce Public Dataset by Olist

**Source:** Kaggle

**Dataset Link:**  
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The dataset contains approximately 100,000 orders from the Brazilian e-commerce marketplace Olist covering the period 2016–2018.

It includes multiple related datasets covering:

- Customers
- Orders
- Order Items
- Payments
- Reviews
- Products
- Sellers
- Geolocation
- Product Category Translation

---

## Business Objective

The objective of this analysis is to understand:

- Overall e-commerce revenue and order performance
- Product category performance
- Geographic revenue distribution
- Customer satisfaction
- Delivery performance
- The relationship between delivery delays and customer reviews
- Business opportunities for improving customer experience and operational performance

---

## Key Business Questions

1. Which product categories generate the highest revenue?
2. Which customer states contribute the most revenue?
3. How does delivery performance affect customer satisfaction?
4. Which categories or segments have higher delivery delays?
5. What actions can management take to improve business performance and customer experience?

---

## Data Preparation & Methodology

The raw datasets were processed using Python and Pandas.

Major data preparation steps included:

- Removing duplicate records where applicable
- Handling missing values
- Converting date and numeric fields to appropriate data types
- Standardizing category and state information
- Joining related datasets using common identifiers
- Creating calculated fields such as:
  - Total Order Value
  - Delivery Days
  - Estimated Delivery Days
  - Delivery Delay
  - Late Delivery Flag
  - Order Month
- Categorizing and aggregating data for business analysis
- Reviewing potential outliers and data quality issues

The processed dataset was then used for analysis and dashboard development.

---

## Key Findings

### 1. Product Category Performance

Health & Beauty generated the highest revenue among the major product categories, followed by Watches & Gifts and Bed & Bath Table.

### 2. Geographic Revenue Concentration

São Paulo (SP) contributed the largest share of revenue, followed by Rio de Janeiro (RJ) and Minas Gerais (MG).

### 3. Delivery & Customer Satisfaction

Late deliveries were associated with substantially lower average review scores compared with orders delivered on time.

- Average review score for late deliveries: approximately **2.26**
- Average review score for on-time deliveries: approximately **4.15**

This indicates that delivery performance is an important driver of customer experience.

### 4. Overall Customer Satisfaction

The overall average review score in the processed analysis was approximately **4.03 out of 5**.

### 5. Delivery Risk

The analysis identified delivery delays as an operational risk. Certain categories showed higher late-delivery rates and longer delivery times, requiring closer monitoring.

---

## Business Recommendations

### 1. Improve Delivery Performance

Identify high-delay categories, sellers, and regions and prioritize them for logistics improvement.

**Success Metric:** Reduction in late-delivery rate and average delivery time.

### 2. Focus on High-Performing Categories

Maintain inventory and marketing focus on high-revenue categories such as Health & Beauty and Watches & Gifts.

**Success Metric:** Revenue growth and improved category contribution.

### 3. Improve Customer Experience

Monitor low review scores and investigate orders affected by delivery delays.

**Success Metric:** Improvement in average review score and reduction in low-rated orders.

---

## Dashboard

An interactive Looker Studio dashboard was developed to provide a management-level view of:

- Total Revenue
- Processed Orders
- Average Order Value
- Average Review Score
- Late Delivery %
- Monthly Revenue Trend
- Revenue by Product Category
- Category Filtering
- Delivery and customer experience analysis

### Looker Studio Dashboard

https://lookerstudio.google.com/

The shareable dashboard link is also included in the assessment workbook.

---

## Project Files

| File | Description |
|------|-------------|
| `VirtuBox_Analysis_Script.py` | Python data preparation and analysis script |
| `VirtuBox_Management_Presentation_Final2.pptx` | Management presentation containing key findings and recommendations |
| `README_Methodology.txt` | Detailed methodology and assessment notes |
| `Brazilian_E-Commerce_Business_Analysis...` | Dashboard screenshot / analysis output |
| `README.md` | Project documentation |

---

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Sheets
- Looker Studio
- Microsoft PowerPoint
- Kaggle Dataset

---

## AI Usage

ChatGPT was used occasionally during the project for:

- Understanding analytical concepts
- Troubleshooting formulas and code
- Getting suggestions for analysis approaches
- Improving the wording and presentation of findings

The analysis and data preparation were performed using the processed dataset and the project workflow.

AI-generated suggestions were verified against the processed data. For example, the late-delivery calculation was checked and corrected after identifying how the field was being interpreted in Looker Studio.

---

## Conclusion

The analysis shows that revenue is concentrated in a few major product categories and states, while delivery performance has a strong relationship with customer satisfaction.

Improving logistics performance, focusing on high-performing categories, and proactively addressing delayed orders can help improve both operational efficiency and customer experience.

---

## Author

**Md Faiz Anwar**

**Project:** VirtuBox Data Analyst Assessment
