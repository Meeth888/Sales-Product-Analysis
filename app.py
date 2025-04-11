import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Sales Visualizer with Performance Levels")

# Input section
num_products = st.number_input("Enter number of products", min_value=1, max_value=20, step=1)

products = []
sales = []
performance = []

# Form for inputs
if num_products:
    with st.form("sales_form"):
        for i in range(num_products):
            col1, col2 = st.columns(2)
            with col1:
                product = st.text_input(f"Product {i+1} name", key=f"product_{i}")
            with col2:
                sale = st.number_input(f"Sales for Product {i+1}", min_value=0.0, key=f"sales_{i}")
            products.append(product)
            sales.append(sale)
        submitted = st.form_submit_button("Visualize")

    if submitted:
        # Apply conditional logic
        for sale in sales:
            if sale >= 1000:
                performance.append("High")
            elif sale >= 500:
                performance.append("Medium")
            else:
                performance.append("Low")

        # Show summary
        st.subheader("📋 Sales Summary")
        for i in range(num_products):
            st.write(f"**{products[i]}** ➝ Sales: ₹{sales[i]} → Performance: **{performance[i]}**")

        # Visualization
        color_map = {"High": "green", "Medium": "orange", "Low": "red"}
        colors = [color_map[perf] for perf in performance]

        fig, ax = plt.subplots()
        ax.bar(products, sales, color=colors)
        ax.set_xlabel("Products")
        ax.set_ylabel("Sales")
        ax.set_title("Sales Data Visualization")
        st.pyplot(fig)
