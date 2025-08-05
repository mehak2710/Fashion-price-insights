import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("data/fashion_products.csv")

# Title
st.title("👗 Fashion Price Range Analysis")

# Sidebar Filters
st.sidebar.header("Filter Options")
selected_brand = st.sidebar.multiselect("Select Brand", options=df['brand'].unique(), default=df['brand'].unique())
selected_category = st.sidebar.multiselect("Select Category", options=df['category'].unique(), default=df['category'].unique())

# Filter Data
filtered_df = df[(df['brand'].isin(selected_brand)) & (df['category'].isin(selected_category))]

# Show Data
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Price Distribution
st.subheader("Price Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df['price'], bins=10, kde=True, ax=ax)
st.pyplot(fig)

# Price by Category
st.subheader("Price Range by Category")
fig, ax = plt.subplots()
sns.boxplot(x="category", y="price", data=filtered_df, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Average Price per Brand
st.subheader("Average Price per Brand")
avg_price = filtered_df.groupby("brand")["price"].mean().sort_values(ascending=False)
fig, ax = plt.subplots()
avg_price.plot(kind="bar", ax=ax)
st.pyplot(fig)

# Price vs Sales
st.subheader("Price vs Sales Volume")
fig, ax = plt.subplots()
sns.scatterplot(x="price", y="sales", data=filtered_df, ax=ax)
st.pyplot(fig)
