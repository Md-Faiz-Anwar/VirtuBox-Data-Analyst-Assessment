# VirtuBox Data Analyst Assessment - Analysis Script
import pandas as pd
import numpy as np

# Load Olist files
orders = pd.read_csv("olist_orders_dataset.csv")
items = pd.read_csv("olist_order_items_dataset.csv")
customers = pd.read_csv("olist_customers_dataset.csv")
products = pd.read_csv("olist_products_dataset.csv")
reviews = pd.read_csv("olist_order_reviews_dataset.csv")
payments = pd.read_csv("olist_order_payments_dataset.csv")
sellers = pd.read_csv("olist_sellers_dataset.csv")
translation = pd.read_csv("product_category_name_translation.csv")

# Date conversion
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"], errors="coerce"
)
orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"], errors="coerce"
)
orders["order_estimated_delivery_date"] = pd.to_datetime(
    orders["order_estimated_delivery_date"], errors="coerce"
)

# Remove duplicate item rows if any
items = items.drop_duplicates()

# Join core datasets
df = items.merge(orders, on="order_id", how="left")
df = df.merge(customers, on="customer_id", how="left")
df = df.merge(products, on="product_id", how="left")
df = df.merge(sellers, on="seller_id", how="left")
df = df.merge(reviews[["order_id", "review_score"]], on="order_id", how="left")
df = df.merge(translation, on="product_category_name", how="left")

# Calculated fields
df["total_order_value"] = df["price"] + df["freight_value"]
df["delivery_days"] = (
    df["order_delivered_customer_date"] - df["order_purchase_timestamp"]
).dt.days
df["estimated_days"] = (
    df["order_estimated_delivery_date"] - df["order_purchase_timestamp"]
).dt.days
df["delivery_delay_days"] = df["delivery_days"] - df["estimated_days"]
df["late_delivery"] = df["delivery_delay_days"] > 0
df["order_month"] = df["order_purchase_timestamp"].dt.to_period("M").astype(str)

# Export processed data
df.to_csv("processed_data.csv", index=False)

print("Processed rows:", len(df))
print("Revenue:", df["price"].sum())
print("Average review:", df["review_score"].mean())
print("Late delivery rate:", df["late_delivery"].mean())
