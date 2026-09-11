# VirtuBox Data Analyst Assessment – README

## Dataset
Brazilian E-Commerce Public Dataset by Olist (Kaggle).
Source: Kaggle – Olist Brazilian E-Commerce Public Dataset.

## Objective
Analyze revenue performance, product-category performance, delivery performance and customer satisfaction, and convert the findings into actionable business recommendations.

## Data Preparation
The analysis uses the Olist orders, order items, customers, products, sellers, reviews, payments and category-translation files.

Main preparation steps:
1. Converted order and delivery date columns to date/time format.
2. Checked and removed duplicate records where appropriate.
3. Reviewed missing values in important fields.
4. Joined related datasets using order_id, customer_id, product_id and seller_id.
5. Created calculated fields including total_order_value, delivery_days, estimated_days, delivery_delay_days, late_delivery and order_month.
6. Used the processed data for business analysis and the Looker Studio dashboard.

## Dashboard
The Looker Studio dashboard contains:
- Revenue KPI
- Processed Orders KPI
- Average Order Value
- Average Review Score
- Late Delivery %
- Monthly Revenue Trend
- Revenue by Product Category
- Product-category filter

## Key Findings
- Health & Beauty is the highest-revenue category.
- Watches & Gifts is the second-highest-revenue category.
- São Paulo (SP) contributes the highest customer-state revenue.
- Office Furniture has the highest late-delivery rate among the analyzed categories.
- Late-delivered orders have substantially lower average review scores than on-time orders.
- Bed & Bath has high revenue but comparatively lower customer review performance.

## Recommendations
1. Improve delivery performance through logistics and seller coordination.
2. Maintain inventory and targeted marketing for high-revenue categories.
3. Investigate customer-experience issues in Bed & Bath.

## Analytical Limitation
The analysis shows an association between late delivery and lower review scores, but it does not prove that late delivery alone causes lower ratings.

## AI Assistance
ChatGPT was used occasionally for concept clarification, troubleshooting formulas/code, analysis suggestions and improving presentation wording. Core data preparation, analysis and dashboard work were reviewed against the dataset.
