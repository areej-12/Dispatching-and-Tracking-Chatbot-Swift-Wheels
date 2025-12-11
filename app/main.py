import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px
# from streamlit_extras.switch_page_button import switch_page 

st.title("Swift Wheels")
st.subheader("Solution For Dispatch Management")
st.sidebar.title("Navigation")
st.sidebar.header("Go to")
# st.sidebar.radio("Sections", ["Dashboard", "Chat Bot", "Upload Proof", "Trip Tracking", "Customer Feedback", "About Us"])
choice =st.sidebar.radio("Sections", ["Dashboard", "Chat Bot", "Upload Proof", "Trip Tracking", "Customer Feedback", "About Us"])
# st.sidebar.markdown("""
# -[Home](#) -[About](#) - [Contact](#)
# """)
# st.subheader("Welcome to Swift Wheels!")
###1 . Dashboard 
# 2. Chat Bot
#  3. upload proof(as mentioned in the scope doc) 
# 4. trip tracking
# 5.customer feedback
# 6.About US
if choice == "Dashboard":
    st.header("Dispatch Management Dashboard")
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Total Rides", "70", "5.2%")   
    with col2:
        st.metric("Active Drivers", "12", "1.3%")              
    with col3:
        st.metric("Completed Trips", "250", "3.8%")
    with col4:
        st.metric("Customer Satisfaction", "89.5%", "0.5%")
    
    st.markdown("---")
    # st.histogram_data = np.random.randn(1000)
    # fig, ax = plt.subplots()
    # ax.hist(st.histogram_data, bins=30, color='skyblue', edgecolor='black')
    # ax.set_title('Distribution of Trip Durations')  
    # ax.set_xlabel('Duration (minutes)')
    # ax.set_ylabel('Frequency')
    # st.pyplot(fig)
    # plt.pie_chart_data = pd.Series([70, 20, 10], index=['Completed', 'Ongoing', 'Pending'])
    # plt.figure(figsize=(6,6))
    # plt.pie(plt.pie_chart_data, labels=plt.pie_chart_data.index, autopct='%1.1f%%', startangle=140, colors=['#4CAF50', '#FF9800', '#F44336'])   
    # plt.title('Trip Status Distribution')
    # st.pyplot(plt)
    # data = {'Category': ['A', 'B', 'C', 'D'], 'Value': [40, 30, 20, 10]}
    # df = pd.DataFrame(data)

    # st.title("Interactive Pie Chart with Plotly")

    # # Create the pie chart figure
    # fig = px.pie(df, values='Value', names='Category', title='My Pie Chart')

    # # Display the chart in Streamlit
    # st.plotly_chart(fig, use_container_width=True)

    # # Customize layout (optional)
    # fig.update_layout(
    #     title_font_size=20,
    #     legend_title_text='Categories'
    # )
    # st.plotly_chart(fig) # Show again with layout changes
    ls_active_trips = {
        'Trip ID': [101, 102, 103],
        'Driver': ['Alice', 'Bob', 'Charlie'],
        'Start Time': ['10:00 AM', '10:30 AM', '11:00 AM'],
        'Status': ['Ongoing', 'Ongoing', 'Ongoing']
    }
    ls_pending_trips = {
        'Trip ID': [201, 202],
        'Driver': ['David', 'Eve'],
        'Start Time': ['12:00 PM', '12:30 PM'],
        'Status': ['Pending', 'Pending']
    }
    ls_completed_trips = {
        'Trip ID': [301, 302, 303, 304],
        'Driver': ['Frank', 'Grace', 'Heidi', 'Ivan'],
        'Start Time': ['9:00 AM', '9:30 AM', '10:00 AM', '10:30 AM'],
        'End Time': ['9:30 AM', '10:00 AM', '10:30 AM', '11:00 AM'],
        'Status': ['Completed', 'Completed', 'Completed', 'Completed']      }
    active_trips_df = pd.DataFrame(ls_active_trips)
    pending_trips_df = pd.DataFrame(ls_pending_trips)   
    completed_trips_df = pd.DataFrame(ls_completed_trips)

    st.subheader("Active Trips")
    st.dataframe(active_trips_df)

    st.subheader("Pending Trips")
    st.dataframe(pending_trips_df)

    st.subheader("Completed Trips")
    st.dataframe(completed_trips_df)
elif choice == "Chat Bot":
    st.header("Dispatch Management Chat Bot")
    st.text_area("Chat with the bot:", height=300)
    st.button("Send")
elif choice == "Upload Proof":
    st.header("Upload Proof of Delivery")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        st.success("File uploaded successfully!")
elif choice == "Trip Tracking":
    st.header("Real-time Trip Tracking")
    st.map(pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon']))
elif choice == "Customer Feedback":
    st.header("Customer Feedback")
    feedback = st.text_area("Enter your feedback here:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")
elif choice == "About Us":
    st.header("About Swift Wheels")
    st.markdown("""
    Swift Wheels is dedicated to providing efficient dispatch management solutions for ride-sharing services. Our platform offers real-time tracking, customer feedback integration, and seamless communication tools to enhance the overall experience for both drivers and customers.
    """)
    st.markdown("### Our Team")
    st.markdown("- Areej Arif 2024113")
    st.markdown("- Tuba Hussain 2024XXX")
    st.markdown("- Muhammad Hasan Asif 2024XXX")
    st.markdown("- Muhammad Anas 2024XXX")
    st.markdown("### Contact Us")
    st.markdown("Email: gikigiki@gmail.com")
    st.markdown("Phone: +1-234-567-8901")
    st.markdown("Address: Giki")    
    st.markdown("### Follow Us")
    st.markdown("- [Twitter](#)")   

