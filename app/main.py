import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ------------------ PAGE CONFIG ------------------
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# ------------------ STYLING ------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0A1F44, #203a43, #2c5364);
}
section[data-testid="stSidebar"] {
    background-color: #1c1f26;
}
</style>
""", unsafe_allow_html=True)

# ------------------ SESSION STATE ------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = None

# ------------------ LANDING PAGE ------------------
def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.rerun()

def landing_page():
    st.title("Swift Wheels")
    st.subheader("AI-Powered Dispatching & Tracking Platform")

    st.markdown("""
    Swift Wheels is a smart logistics management platform designed to help
    warehouse dispatchers, drivers, and clients efficiently manage freight
    operations through real-time tracking and an AI-assisted chatbot.
    """)

    st.markdown("### Login As")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Dispatcher Login"):
            st.session_state.logged_in = True
            st.session_state.role = "Dispatcher"

    with col2:
        if st.button("Driver Login"):
            st.session_state.logged_in = True
            st.session_state.role = "Driver"

    with col3:
        if st.button("Client Login"):
            st.session_state.logged_in = True
            st.session_state.role = "Client"

# ------------------ DISPATCHER PANEL ------------------
def dispatcher_panel():
    st.sidebar.title("Dispatcher Panel")
    choice = st.sidebar.radio(
        "Navigate",
        ["Dashboard", "Dispatch Chatbot", "Trip Tracking", "Proof of Payment", "Customer Feedback", "About System"]
    )
    # choice = st.sidebar.radio(
    #     "Browse System Features",
    #     [
    #         "View Dashboard",
    #         "Trip Tracking",
    #         "Monitor Statistics",
    #         "Dispatch Chatbot",
    #         "Payment Management",
    #         "Ratings & Feedback",
    #         "About System"
    #     ]
    # )

    if choice == "Dashboard":
        st.header("Dispatch Operations Dashboard")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Active Trips", "40", "+5")
        col2.metric("Active Drivers", "12", "+1")
        col3.metric("Completed Trips", "250", "+8")
        col4.metric("On-Time Delivery (%)", "89.5%", "+0.5%")

        trip_data = {
            "Category": ["Active", "Completed", "Delayed", "Cancelled"],
            "Count": [40, 150, 20, 5]
        }
        df = pd.DataFrame(trip_data)
        st.plotly_chart(px.bar(df, x="Category", y="Count"), use_container_width=True)
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
            'Status': ['Completed', 'Completed', 'Completed', 'Completed']}
        df = pd.DataFrame({
            "Category": ["Active", "Completed", "Delayed"],
            "Count": [40, 150, 20]
        })
        st.plotly_chart(px.bar(df, x="Category", y="Count"), use_container_width=True)
        active_trips_df = pd.DataFrame(ls_active_trips)
        pending_trips_df = pd.DataFrame(ls_pending_trips)
        completed_trips_df = pd.DataFrame(ls_completed_trips)

        st.subheader("Active Trips")
        st.dataframe(active_trips_df)

        st.subheader("Pending Trips")
        st.dataframe(pending_trips_df)

        st.subheader("Completed Trips")
        st.dataframe(completed_trips_df)
    elif choice == "Dispatch Chatbot":
        st.header("Operational Dispatch Chatbot")

        chatbot_responses = {
            "where is truck 12": "Truck 12 is near Jhelum. ETA: 1 hour 20 minutes.",
            "show active trips": "There are currently 40 active trips.",
            "driver status": "12 drivers active, 3 on leave.",
            "what is the status of trip 102": "Trip 102 is ongoing. ETA: 1:00 PM.",
            "track my shipment": "Shipment is near Jhelum. ETA: 1 hour 20 minutes.",
            "show pending payments": "There are 3 pending payments.",
            "payment status trip 101": "Payment for Trip 101 is verified.",
            "has payment for trip 101 been verified": "Yes, payment for Trip 101 is verified.",
            "show driver rating for ali ahmed": "Ali Ahmed has an average rating of 4.6 stars."

        }

        query = st.text_area("Enter dispatcher query")
        if st.button("Query System"):
            st.success(chatbot_responses.get(
                query.lower().strip(),
                "Query not recognized. Please rephrase."
            ))

    elif choice == "Trip Tracking":
        st.header("Real-Time Trip Tracking")
        st.map(pd.DataFrame(
            np.random.randn(50, 2) / [50, 50] + [33.6844, 73.0479],
            columns=["lat", "lon"]
        ))
        st.dataframe(pd.DataFrame({
            "Trip ID": [101, 102],
            "Driver": ["Ali Ahmed", "Abdul Haq"],
            "Status": ["Ongoing", "Pending"],
            "ETA": ["1:00 PM", "3:30 PM"]
        }))
        st.success("Tracking 2 drivers!")
        st.button("View Trip Details")
        st.button("Update Trip Status")
        st.button("Track Trip")


    elif choice == "Proof of Payment":
        st.header("Electronic Proof of Payment")
        file = st.file_uploader("Upload payment proof", type=["pdf", "png", "jpg"])
        if file:
            st.success("Payment proof uploaded successfully.")
        st.info("Verify Payment Record | View Proof of Payment")
        st.dataframe(pd.DataFrame({
            "Trip ID": [101, 102],
            "Driver": ["Ali Ahmed", "Abdul Haq"],
            "Status": ["Ongoing", "Pending"],
            "Payment": ["Received", "Processed"]
        }))
        st.button("View Proof of Payment")

    elif choice == "Customer Feedback":
        st.header("Customer Feedback")
        st.text_area("View or record customer feedback")
        st.button("Save")
        st.subheader("Rate Driver")

        rating = st.radio(
            "Select Rating",
            ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
            horizontal=True
        )

        st.write(f"You selected: {len(rating)} star(s)")

        if st.button("Submit Rating"):
            st.success("Driver rating submitted successfully.")

    elif choice == "About System":
        st.markdown("Swift Wheels supports freight dispatch operations in Pakistan.")
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

    # ------------------ DRIVER PANEL ------------------
def driver_panel():
    st.sidebar.title("Driver Functions")
    choice = st.sidebar.radio(
        "Navigate",
        ["View Trip Status", "Send GPS Location"]
    )

    if choice == "View Trip Status":
        st.info("Trip ID: 102 | Status: Ongoing | ETA: 1:00 PM")

    elif choice == "Send GPS Location":
        st.success("GPS location sent to dispatcher.")

# ------------------ CLIENT PANEL ------------------
def client_panel():
    st.sidebar.title("Client Panel")
    choice = st.sidebar.radio("Navigate", ["Track Trip", "Submit Feedback"])

    if choice == "Track Trip":
        st.header("Track Your Shipment")
        st.map(pd.DataFrame(
            np.random.randn(30, 2) / [50, 50] + [33.6844, 73.0479],
            columns=["lat", "lon"]
        ))

    elif choice == "Submit Feedback":
        feedback = st.text_area("Enter feedback")
        if st.button("Submit"):
            st.success("Thank you for your feedback.")

# ------------------ MAIN ROUTER ------------------
if not st.session_state.logged_in:
    landing_page()
else:
    st.sidebar.success(f"Logged in as {st.session_state.role}")

    # LOGOUT BUTTON (VISIBLE TO ALL ROLES)
    if st.sidebar.button("Logout"):
        logout()

    if st.session_state.role == "Dispatcher":
        dispatcher_panel()
    elif st.session_state.role == "Driver":
        driver_panel()
    elif st.session_state.role == "Client":
        client_panel()

# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt 
# import plotly.express as px
# # from streamlit_extras.switch_page_button import switch_page 

# st.title("Swift Wheels")
# st.subheader("Solution For Dispatch Management")
# st.sidebar.title("Navigation")
# st.sidebar.header("Go to")
# # st.sidebar.radio("Sections", ["Dashboard", "Chat Bot", "Upload Proof", "Trip Tracking", "Customer Feedback", "About Us"])
# choice =st.sidebar.radio("Sections", ["Dashboard", "Chat Bot", "Upload Proof", "Trip Tracking", "Customer Feedback", "About Us"])
# # st.sidebar.markdown("""
# # -[Home](#) -[About](#) - [Contact](#)
# # """)
# # st.subheader("Welcome to Swift Wheels!")
# ###1 . Dashboard 
# # 2. Chat Bot
# #  3. upload proof(as mentioned in the scope doc) 
# # 4. trip tracking
# # 5.customer feedback
# # 6.About US
# if choice == "Dashboard":
#     st.header("Dispatch Management Dashboard")
#     col1,col2,col3,col4=st.columns(4)
#     with col1:
#         st.metric("Total Rides", "70", "5.2%")   
#     with col2:
#         st.metric("Active Drivers", "12", "1.3%")              
#     with col3:
#         st.metric("Completed Trips", "250", "3.8%")
#     with col4:
#         st.metric("Customer Satisfaction", "89.5%", "0.5%")
    
#     st.markdown("---")
#     # st.histogram_data = np.random.randn(1000)
#     # fig, ax = plt.subplots()
#     # ax.hist(st.histogram_data, bins=30, color='skyblue', edgecolor='black')
#     # ax.set_title('Distribution of Trip Durations')  
#     # ax.set_xlabel('Duration (minutes)')
#     # ax.set_ylabel('Frequency')
#     # st.pyplot(fig)
#     # plt.pie_chart_data = pd.Series([70, 20, 10], index=['Completed', 'Ongoing', 'Pending'])
#     # plt.figure(figsize=(6,6))
#     # plt.pie(plt.pie_chart_data, labels=plt.pie_chart_data.index, autopct='%1.1f%%', startangle=140, colors=['#4CAF50', '#FF9800', '#F44336'])   
#     # plt.title('Trip Status Distribution')
#     # st.pyplot(plt)
#     # data = {'Category': ['A', 'B', 'C', 'D'], 'Value': [40, 30, 20, 10]}
#     # df = pd.DataFrame(data)

#     # st.title("Interactive Pie Chart with Plotly")

#     # # Create the pie chart figure
#     # fig = px.pie(df, values='Value', names='Category', title='My Pie Chart')

#     # # Display the chart in Streamlit
#     # st.plotly_chart(fig, use_container_width=True)

#     # # Customize layout (optional)
#     # fig.update_layout(
#     #     title_font_size=20,
#     #     legend_title_text='Categories'
#     # )
#     # st.plotly_chart(fig) # Show again with layout changes
#     ls_active_trips = {
#         'Trip ID': [101, 102, 103],
#         'Driver': ['Alice', 'Bob', 'Charlie'],
#         'Start Time': ['10:00 AM', '10:30 AM', '11:00 AM'],
#         'Status': ['Ongoing', 'Ongoing', 'Ongoing']
#     }
#     ls_pending_trips = {
#         'Trip ID': [201, 202],
#         'Driver': ['David', 'Eve'],
#         'Start Time': ['12:00 PM', '12:30 PM'],
#         'Status': ['Pending', 'Pending']
#     }
#     ls_completed_trips = {
#         'Trip ID': [301, 302, 303, 304],
#         'Driver': ['Frank', 'Grace', 'Heidi', 'Ivan'],
#         'Start Time': ['9:00 AM', '9:30 AM', '10:00 AM', '10:30 AM'],
#         'End Time': ['9:30 AM', '10:00 AM', '10:30 AM', '11:00 AM'],
#         'Status': ['Completed', 'Completed', 'Completed', 'Completed']      }
#     active_trips_df = pd.DataFrame(ls_active_trips)
#     pending_trips_df = pd.DataFrame(ls_pending_trips)   
#     completed_trips_df = pd.DataFrame(ls_completed_trips)

#     st.subheader("Active Trips")
#     st.dataframe(active_trips_df)

#     st.subheader("Pending Trips")
#     st.dataframe(pending_trips_df)

#     st.subheader("Completed Trips")
#     st.dataframe(completed_trips_df)
# elif choice == "Chat Bot":
#     st.header("Dispatch Management Chat Bot")
#     st.text_area("Chat with the bot:", height=300)
#     st.button("Send")
# elif choice == "Upload Proof":
#     st.header("Upload Proof of Delivery")
#     uploaded_file = st.file_uploader("Choose a file")
#     if uploaded_file is not None:
#         st.success("File uploaded successfully!")
# elif choice == "Trip Tracking":
#     st.header("Real-time Trip Tracking")
#     st.map(pd.DataFrame(
#         np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
#         columns=['lat', 'lon']))
# elif choice == "Customer Feedback":
#     st.header("Customer Feedback")
#     feedback = st.text_area("Enter your feedback here:")
#     if st.button("Submit Feedback"):
#         st.success("Thank you for your feedback!")
# elif choice == "About Us":
#     st.header("About Swift Wheels")
#     st.markdown("""
#     Swift Wheels is dedicated to providing efficient dispatch management solutions for ride-sharing services. Our platform offers real-time tracking, customer feedback integration, and seamless communication tools to enhance the overall experience for both drivers and customers.
#     """)
#     st.markdown("### Our Team")
#     st.markdown("- Areej Arif 2024113")
#     st.markdown("- Tuba Hussain 2024XXX")
#     st.markdown("- Muhammad Hasan Asif 2024XXX")
#     st.markdown("- Muhammad Anas 2024XXX")
#     st.markdown("### Contact Us")
#     st.markdown("Email: gikigiki@gmail.com")
#     st.markdown("Phone: +1-234-567-8901")
#     st.markdown("Address: Giki")    
#     st.markdown("### Follow Us")
#     st.markdown("- [Twitter](#)")   

