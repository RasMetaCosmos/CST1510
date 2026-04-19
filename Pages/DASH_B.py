import streamlit as st
import pandas as pd
import plotly.express as px
from appmod.cyber_incident import get_all_cyber_incdt
from appmod.dataB import check_connection
import datetime


st.set_page_config(
    page_title="Dashboard",
    page_icon="downloaddash.png",
    layout="wide"
)
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.warning("Please log in to access the dashboard.")
    if st.button("Go to Login Page"):
        st.session_state["logged_in"] = False
        st.switch_page("HOME.py")
    st.stop()
else:
    st.success("You are logged in!")

conn = check_connection()
data = get_all_cyber_incdt(conn)


st.title("Welcome to Main Page")
with st.sidebar:
    st.header("Navigation")
    severity_level = st.selectbox("severity Level", data["severity"].unique())
    category = st.selectbox("Category", 
    ["All"] + list(data["category"].unique()))
    
    
    st.subheader("Filter by Date")
    start_date = st.date_input("Start Date", value=datetime.date(2023, 1, 1))
    end_date = st.date_input("End Date", value=datetime.date.today())
  

data["timestamp"] = pd.to_datetime(data["timestamp"])
filtered_data = data[data["severity"] == severity_level]

# Filter by category
if category != "All":
    filtered_data = filtered_data[filtered_data["category"] == category]
    
  # Filter by date
filtered_data = filtered_data[
    (filtered_data['timestamp'].dt.date >= start_date) &
    (filtered_data['timestamp'].dt.date <= end_date)
]

st.divider()
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Incidents", len(filtered_data))
col2.metric("Closed", len(filtered_data[filtered_data['status']=='Closed']))
col3.metric("Resolved", len(filtered_data[filtered_data['status']=='Resolved']))
col4.metric("In Progress", len(filtered_data[filtered_data['status']=='In Progress']))
col5.metric("Open", len(filtered_data[filtered_data['status']=='Open']))
st.divider()

col1, col2,col3 = st.columns(3)

with col1:
    st.subheader(f"Cyber Incidents with severity level: {severity_level}")
    st.bar_chart(filtered_data["category"].value_counts())

with col2:
    st.subheader("Trend of Incidents")
    st.line_chart(filtered_data, x="timestamp", y="category")

with col3:
    st.subheader("Distribution")
    fig_pie = px.pie(filtered_data, names='category')
    st.plotly_chart(fig_pie,use_container_width=True)

st.subheader("Filtered Data")
st.dataframe(filtered_data)
