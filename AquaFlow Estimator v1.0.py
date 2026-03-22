#----AquaFlow Estimator v4.0----
#Developed by Sandip Banik $ Gemini

import streamlit as st
#---1. Master Switch (Acess Control) ---
# this code is for you to give to paying customers.
ACCESS_CODE = "SANDIP2030"

st.set_page_config(page_title="aquaFlow Pro")
#---2. security layer ---
st.sidebar.title("Admin Access")
user_code = st.sidebar.text_input("Enter Access Key to Unlock", type="password")

if user_code != ACCESS_CODE:
    st.warning("Please enter a valid Access Key to use the software.")
    st.info("Contact Sandip Banik(owner) for a license.")
else:
    #---3. main application interface---
    st.title("AquaFlow Submersible Estimator")
    st.subheader("Professional Billing & Installation System")

    st.divider()

    # Input Section - Organized into two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Project Specs")
        water_depth = st.number_input("Water Level Depth (ft)", min_value=0.0, value=100.0)
        safety_margin = st.number_input("safety Margin (ft)", min_value=0.0, value=20.0)
        pipe_length = st.number_input("Single Pipe Length (ft)", min_value=1.0, value=10.0)

    with col2:
        st.write("### Pricing (INR)")
        pipe_cost = st.number_input("Cost per pipe(Rs.)", min_value=0.0, value=450.0)
        boring_cost = st.number_input("Boring Charge per foot (Rs.)", min_value=0.0, value=60.0)
        pump_cost = st.number_input("Pump Unit Price (Rs.)", min_value=0.0, value=12000.0)

    #4. mathematic calculation
    total_boring_depth = water_depth + safety_margin
    required_pipes = total_boring_depth / pipe_length

    #. automatic HP calculation
    if total_boring_depth <= 100:
        pump_hp = "1.0 HP"
    elif total_boring_depth <= 200:
        pump_hp = "1.5 HP"
    elif total_boring_depth <= 300:
        pump_hp = "2.0 HP"
    else:
        pump_hp = "3.0 HP or more (Heavy Duty)"

    #5. Financial calculations
    total_pipe_cost = required_pipes * pipe_cost
    total_boring_cost = total_boring_depth * boring_cost
    grand_total = total_pipe_cost + total_boring_cost + pump_cost

    #6. result display & Quotation
    st.divider()
    st.header("--- Official Quotation ---")

    #Key metrics display
    res_col1, res_col2 = st.columns(2)
    res_col1.metric("Total Boring", f"{total_boring_depth} ft")
    res_col2.metric("Pipes Required", f"{required_pipes:.1f} pcs")

    st.write(f"### Net Total Payable: Rs.{grand_total:,.2f}")

    # professional invoice generation for Screenshots
    st.code(f"""
    PROJECT INVOICE SUMMARY
    ---------------------------
    Total Boring Depth: {total_boring_depth} ft
    Pipes Required    : {required_pipes:.1f} pieces
    ---------------------------
    Boring Labor Cost : Rs.{total_boring_cost:,.2f}
    pipes Material    : Rs.{total_pipe_cost:,.2f}
    Pump Unit Price   : Rs.{pump_cost:,.2f}
    ---------------------------
    GRAND TOTAL       : Rs.{grand_total:,.2f}
    ---------------------------
    Issued by: Sandip Banik
    """, language="text")

    st.success("""Software active. Take a SCREENSHOT to SHARE with the client.
               Thank you for using AquaFlow Estimator!""")




