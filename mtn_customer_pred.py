import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_card import card
import plotly.express as px


# PAGE CONFIG
st.set_page_config(
page_title='MTN CUSTOMER CHURN PREDICTION APP',
page_icon="🤖",
layout="wide"
)
model = joblib.load("Mtn_customer_churn_model.pkl")


# CUSTOM CSS
st.markdown("""
<style>
.main {
background-color: #0E1117;
backgroundColor="#e61c06ff"
}

h1, h2, h3 {
color: white;
}

.stMetric {
background-color: #1E1E1E;
padding: 15px;
border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR MENU
with st.sidebar:
                selected = option_menu(
                menu_title="Navigation",
                options=["Dataset", "Prediction", "Analysis"],
                icons=["Data", "cpu", "bar-chart"],
                menu_icon="cast",
                default_index=0,
                )

# HOME PAGE
if selected == "Dataset":                
                        st.title('🤖MTN Customer Churn Prediction APP')
                        st.subheader('This apps tells you  about mtn customer chun')
                        st.subheader('Check the dataset below')
                        st.markdown("## MTN Customer Dataset")
                        df = pd.read_csv('mtn_customer_churn.csv')
                        st.dataframe(df)


                    
# PREDICTION PAGE
elif selected == "Prediction":

                            st.title("🎯 MTN CUSTOMER PREDICTION APP")
                            st.subheader('Enter Details to predict the risk of customer churning')
                                            
                            col1, col2 = st.columns(2)

                            with col1:
                                    Age = st.number_input('Customer Age?', min_value=18, max_value=85, value=18)
                                    State = st.selectbox('Customer State', options=[
                                        'Kwara', 'Abuja (FCT)', 'Sokoto', 'Gombe', 'Oyo', 'Plateau',
                                        'Jigawa', 'Imo', 'Bauchi', 'Ondo', 'Kebbi', 'Adamawa', 'Yobe',
                                        'Anambra', 'Cross River', 'Kogi', 'Osun', 'Kano', 'Benue',
                                        'Rivers', 'Enugu', 'Borno', 'Edo', 'Kaduna', 'Abia', 'Ekiti',
                                        'Bayelsa', 'Delta', 'Zamfara', 'Akwa Ibom', 'Nasarawa', 'Taraba',
                                        'Niger', 'Katsina', 'Lagos'
                                    ])

                                    MTN_Device = st.selectbox('Customer MTN Device', options=['4G Router', 'Mobile SIM Card', '5G Broadband Router', 'Broadband MiFi'])

                                    Gender = st.selectbox('Customer Gender', options=['Male', 'Female'])

                                    Customer_review = st.selectbox('Customer Review', options=['Fair', 'Poor', 'Good', 'Excellent', 'Very Good'])
                                    tenure = st.number_input('Customer Tenure (Months)', min_value=0, max_value=200, value=0)



                            with col2:
                                    Unit_Price = st.number_input('Cost of Data Plan', min_value=0, max_value=500000, value=0)
                                    Number_of_Times_Purchased = st.number_input('Number of Times Purchased', min_value=0, max_value=20, value=0)
                                    Total_Revenue = st.number_input('Total Monthly Revenue', min_value=1, max_value=350000, value=1)
                                    Data_usage = st.number_input('Custormers Data Usage in Gigabyte(gb)', min_value=1, max_value=350000, value=1)
                                    Subscription_Plan = st.selectbox(
                                        'Customer Subscription Plan',
                                        options=[
                                            '165GB Monthly Plan', '12.5GB Monthly Plan', '150GB FUP Monthly Unlimited',
                                            '1GB+1.5mins Daily Plan', '30GB Monthly Broadband Plan', '10GB+10mins Monthly Plan',
                                            '25GB Monthly Plan', '7GB Monthly Plan', '1.5TB Yearly Broadband Plan',
                                            '65GB Monthly Plan', '120GB Monthly Broadband Plan', '300GB FUP Monthly Unlimited',
                                            '60GB Monthly Broadband Plan', '500MB Daily Plan', '3.2GB 2-Day Plan',
                                            '20GB Monthly Plan', '2.5GB 2-Day Plan', '450GB 3-Month Broadband Plan',
                                            '200GB Monthly Broadband Plan', '1.5GB 2-Day Plan', '16.5GB+10mins Monthly Plan'
                                        ]
                                    )

                                # Mappings
                                    Gender_mapping = {'Male': 1, 'Female': 0}
                                    state_mapping = {
                                    'Kwara': 1, 'Abuja (FCT)': 2, 'Sokoto': 3, 'Gombe': 4, 'Oyo': 5, 'Plateau': 6,
                                    'Jigawa': 7, 'Imo': 8, 'Bauchi': 9, 'Ondo': 10, 'Kebbi': 11, 'Adamawa': 12, 'Yobe': 13,
                                    'Anambra': 14, 'Cross River': 15, 'Kogi': 16, 'Osun': 17, 'Kano': 18, 'Benue': 19,
                                    'Rivers': 20, 'Enugu': 21, 'Borno': 22, 'Edo': 23, 'Kaduna': 24, 'Abia': 25, 'Ekiti': 26,
                                    'Bayelsa': 27, 'Delta': 28, 'Zamfara': 29, 'Akwa Ibom': 30, 'Nasarawa': 31, 'Taraba': 32,
                                    'Niger': 33, 'Katsina': 34, 'Lagos': 35
                                }

                                    mtn_device_mapping = {
                                            '4G Router': 1,
                                            'Mobile SIM Card': 2,
                                            '5G Broadband Router': 3,
                                            'Broadband MiFi': 4
                                        }

                                    customer_review_mapping = {
                                            'Fair': 1,
                                            'Poor': 2,
                                            'Good': 3,
                                            'Excellent': 4,
                                            'Very Good': 5
                                        }

                                    subscription_plan_mapping = {
                                            '165GB Monthly Plan': 1,
                                            '12.5GB Monthly Plan': 2,
                                            '150GB FUP Monthly Unlimited': 3,
                                            '1GB+1.5mins Daily Plan': 4,
                                            '30GB Monthly Broadband Plan': 5,
                                            '10GB+10mins Monthly Plan': 6,
                                            '25GB Monthly Plan': 7,
                                            '7GB Monthly Plan': 8,
                                            '1.5TB Yearly Broadband Plan': 9,
                                            '65GB Monthly Plan': 10,
                                            '120GB Monthly Broadband Plan': 11,
                                            '300GB FUP Monthly Unlimited': 12,
                                            '60GB Monthly Broadband Plan': 13,
                                            '500MB Daily Plan': 14,
                                            '3.2GB 2-Day Plan': 15,
                                            '20GB Monthly Plan': 16,
                                            '2.5GB 2-Day Plan': 17,
                                            '450GB 3-Month Broadband Plan': 18,
                                            '200GB Monthly Broadband Plan': 19,
                                            '1.5GB 2-Day Plan': 20,
                                            '16.5GB+10mins Monthly Plan': 21
                                        }

                                    # Map categorical variables to numerical
                                    Gender_map = Gender_mapping[Gender]
                                    state_map = state_mapping[State]
                                    subscription_plan_map = subscription_plan_mapping[Subscription_Plan]
                                    customer_review_map = customer_review_mapping[Customer_review]
                                    mtn_device_map = mtn_device_mapping[MTN_Device]

                                            # Log transform Total Revenue
                                    Total_Revenue_log = np.log1p(Total_Revenue)

                                    if st.button('🔮 Predict Customer Churn'):
                                        features = [
                                            [
                                                Age,
                                                state_map,
                                                subscription_plan_map,
                                                customer_review_map,
                                                mtn_device_map,
                                                Total_Revenue_log,
                                                Gender_map,
                                                Unit_Price,
                                                Number_of_Times_Purchased,
                                                tenure,
                                                Data_usage
                                            ]
                                        ]
                                        prediction = model.predict(features)
                                        probability = model.predict_proba(features)[0][1]

                                        if prediction[0] == 1:
                                            card(
                                                title="Prediction",
                                                text = f"🚩 Customer is likely to churn! Probability: {round(probability * 100, 2)}%")
                                            st.metric(f"🚩 Customer is likely to churn! ", f"Probability: {round(probability * 100, 2)}%")

                                        else:
                                            card(
                                                title="Prediction",
                                                text= f"✅ Customer is unlikely to churn! Probability: {round(probability * 100, 2)}%")
                                            style_metric_cards()
                                            st.metric(f"✅ Customer is unlikely to churn!", f"Probability: {round(probability * 100, 2)}%")
                                            
                                        
                              
elif selected == "Analysis":
                            st.title("📊 MTN Customer Analytics PAGE")

                            # PLOTLY CHART
                            st.markdown("## MTN Customer Dataset")
                            df = pd.read_csv('mtn_customer_churn.csv')
                            st.dataframe(df)

                            plt.figure(figsize=(10,5))
                            st.markdown("## Age Distribution")
                            fig = px.histogram(df['Age'], x="Age", nbins=20, title="Customer Age Distribution")
                            #fig = px.bar(df['Age'], x="Age", title="Customer Age Distribution")

                            st.plotly_chart(fig, use_container_width=True)
                            
                        
                            st.markdown("## MTN Customer Dataset")
                           

                            # 2. AGE DISTRIBUTION (Already Plotly)
                            #st.markdown("## Age Distribution")
                            #fig_age = px.histogram(df, x="Age", nbins=20, title="Customer Age Distribution",) 
                            #st.plotly_chart(fig_age, use_container_width=True)
                            st.markdown("---")

                            # 3. GEOGRAPHIC DISTRIBUTION
                            st.markdown("## Customers State")
                            state_counts = df['State'].value_counts().reset_index()
                            state_counts.columns = ['State', 'Number of Customers']
                            fig_state = px.bar(state_counts, x='State', y='Number of Customers', 
                                            title='Customer Distribution by State',
                                            color='Number of Customers')
                            st.plotly_chart(fig_state, use_container_width=True)
                            st.markdown("---")

                            # 4. DEVICE USAGE
                            st.markdown("## Device Usage")
                            fig_device = px.histogram(df, x='MTN Device', title='Device Usage',
                                                    color='MTN Device')
                            st.plotly_chart(fig_device, use_container_width=True)
                            st.markdown("---")

                            # 5. GENDER DISTRIBUTION
                            st.markdown("## Gender Distribution")
                            fig_gender = px.pie(df, names='Gender', title='Gender Distribution', hole=0.4)
                            st.plotly_chart(fig_gender, use_container_width=True)
                            st.markdown("---")

                            # 6. SATISFACTION RATE
                            st.markdown("## Satisfaction Rate")
                            fig_sat = px.histogram(df, x='Satisfaction Rate', nbins=10, 
                                                title='Customer Satisfaction Rate',
                                                color_discrete_sequence=['green'])
                            st.plotly_chart(fig_sat, use_container_width=True)
                            st.markdown("---")

                            # 7. CUSTOMER TENURE
                            st.markdown("## Customer Tenure")
                            fig_tenure = px.histogram(df, x='Customer Tenure in months', nbins=20, 
                                                    title='Customer Tenure Distribution',
                                                    labels={'Customer Tenure in months': 'Months'})
                            st.plotly_chart(fig_tenure, use_container_width=True)
                            st.markdown("---")

                            # 8. SUBSCRIPTION PLANS
                            st.markdown("## Subscription Plans")
                            plan_counts = df['Subscription Plan'].value_counts().reset_index()
                            fig_plan = px.bar(plan_counts, x='Subscription Plan', y='count', 
                                            title='Subscription Plan Popularity',
                                            color='Subscription Plan')
                            st.plotly_chart(fig_plan, use_container_width=True)
                            st.markdown("---")

                            # 10. CHURN ANALYSIS
                            st.markdown("## Churn Analysis")
                            fig_churn = px.pie(df, names='Customer Churn Status', title='Customer Churn Status',
                                            color_discrete_map={'Yes':'red', 'No':'blue'})
                            st.plotly_chart(fig_churn, use_container_width=True)
                            st.info("Lots of customer are still using MTN; only a few have left.")
                            st.markdown("---")

                            # 11. REASONS FOR CHURN
                            st.markdown("## Reasons for Churn")
                            # Filtering out rows where churn might be null or reasons are missing
                            churn_reasons = df[df['Reasons for Churn'].notna()]
                            fig_reasons = px.bar(churn_reasons['Reasons for Churn'].value_counts().reset_index(), 
                                                y='Reasons for Churn', x='count', orientation='h',
                                                title='Reasons for Customer Churn',
                                                labels={'count': 'Number of Customers', 'Reasons for Churn': 'Reason'})
                            st.plotly_chart(fig_reasons, use_container_width=True)
                            