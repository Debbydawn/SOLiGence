import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np 

# Load cryptocurrency price data
data = pd.read_csv('crypto_prices.csv')


side_bars = st.sidebar.radio("Navigation", ["Home","About Us","Dataset","Visualizations","Predictions"])

if side_bars == "Home":
    st.header("SOLiGence")
    st.write("Solent Intelligence (SOLiGence) is a leading financial multinational organisation that deals with stock and shares, saving and investments.")
    import streamlit as st

    # Streamlit app
    st.title('Welcome to SOLiGence')
    st.write("Your Intelligent Coin Trading Platform")

    # Logo
    # st.image('your_logo.png', width=200)

    # Brief Description
    st.write("Empower your cryptocurrency trading decisions with AI-driven insights and real-time data.")

    # Call to Action (CTA) Button
    if st.button("Get Started"):
        st.write("Let's explore the world of cryptocurrency trading together!")

        # Background Image
        st.image('sal.jpg', use_column_width=True)
        if 'section' not in st.session_state:
            st.session_state.section = "Home"
        # Quick Links
        # st.write("Quick Links:")
        # if st.button("About Us"):
        #     st.session_state.section = "About Us"  # Set the section to "About Us"

        # if st.button("Dataset"):
        #     st.session_state.section = "Dataset"  # Set the section to "Dataset"

        # if st.button("Visualizations"):
        #     st.session_state.section = "Visualizations"  # Set the section to "Visualizations"

        # if st.button("Predictions"):
        #     st.session_state.section = "Predictions"  # Set the section to "Predictions"



        # News and Updates
        st.write("News and Updates:")
        st.info("Stay tuned for the latest updates and trends in the cryptocurrency market!")

        # Testimonials
        st.write("What Our Users Say:")
        st.write("The SOLiGence app transformed how I approach cryptocurrency trading. Highly recommended!")

        # Contact Information
        st.write("Contact Us:")
        st.write("For inquiries, email us at info@soligence.com")

        # Social Media Links
        st.write("Connect with Us:")
        st.markdown("[Twitter](https://twitter.com/SOLiGenceApp) [LinkedIn](https://linkedin.com/company/soligence)")

        # Privacy and Disclaimer
        st.write("Privacy Policy | Disclaimer")
        
        # Sidebar sections
        # with st.sidebar.expander("About Us", expanded=(st.session_state.section == "About Us")):
        #     st.write("Welcome to the About Us section!")
        # # You can add content related to "About Us" here
        #     st.title("About Solent Intelligence Ltd.")
        #     st.write("The scale of this organization's operation is impressive, with millions of subscribers and over 150 billion pounds worth of investments. This emphasizes the substantial influence that data-driven decisions can have on managing such a significant amount of assets. The app's focus on implementing an Intelligent Coin Trading (IST) platform, specifically tailored for crypto coin predictions, resonates deeply with me. The idea of utilizing AI to predict cryptocurrency prices on different timeframes, such as daily, weekly, monthly, and quarterly, truly piques my interest. This approach aligns perfectly with my desire to explore how AI can shape and enhance our daily lives. The app's ability to recommend trading opportunities by analyzing AI-generated predictions showcases the tangible applications of data science in the financial world. Considering a more neutral perspective, while the concept of the app is exciting, there are potential challenges that need to be acknowledged. Cryptocurrency markets are known for their volatility, and even the most sophisticated AI predictions might not always be entirely accurate. Users relying solely on these predictions could face risks if market conditions change unexpectedly.")
       
if side_bars == "About Us":
    st.title("About Solent Intelligence Ltd.")
    st.write("The scale of this organization's operation is impressive, with millions of subscribers and over 150 billion pounds worth of investments. This emphasizes the substantial influence that data-driven decisions can have on managing such a significant amount of assets. The app's focus on implementing an Intelligent Coin Trading (IST) platform, specifically tailored for crypto coin predictions, resonates deeply with me. The idea of utilizing AI to predict cryptocurrency prices on different timeframes, such as daily, weekly, monthly, and quarterly, truly piques my interest. This approach aligns perfectly with my desire to explore how AI can shape and enhance our daily lives. The app's ability to recommend trading opportunities by analyzing AI-generated predictions showcases the tangible applications of data science in the financial world. Considering a more neutral perspective, while the concept of the app is exciting, there are potential challenges that need to be acknowledged. Cryptocurrency markets are known for their volatility, and even the most sophisticated AI predictions might not always be entirely accurate. Users relying solely on these predictions could face risks if market conditions change unexpectedly.")

if side_bars == "Dataset":
    st.header("Crypto Dataset of Five Coins")
    
    # Sidebar options
    st.sidebar.subheader("Dataset Options")
    
    # Sorting
    sort_column = st.sidebar.multiselect("Sort by:", data.columns)
    ascending = st.sidebar.checkbox("Ascending")
    sorted_data = data.sort_values(by=sort_column, ascending=ascending)

    # Filtering
    selected_crypto = st.sidebar.selectbox("Filter by cryptocurrency:", ["All"] + data['Crypto'].unique())
    if "All" not in selected_crypto:
        sorted_data = sorted_data[sorted_data['Crypto'].isin(selected_crypto)]

    # Pagination
    page_size = st.sidebar.number_input("Items per page:", min_value=1, value=10)
    page_number = st.sidebar.number_input("Page number:", min_value=1, value=1)
    start_idx = (page_number - 1) * page_size
    end_idx = start_idx + page_size
    paginated_data = sorted_data.iloc[start_idx:end_idx]

    # Display the dataset using a dataframe
    st.subheader("Dataset Overview")
    st.dataframe(paginated_data)
    
    # Provide an option to show a table view
    show_table = st.checkbox("Show as Table")
    
    # Display the dataset as a table if the checkbox is selected
    if show_table:
        st.subheader("Dataset Table View")
        st.table(paginated_data)






if side_bars == "Visualizations":
    st.title('Explore historical cryptocurrency prices.')
    st.header('Cryptocurrency Price Visualization')
    
    
    # Sidebar for user input
    selected_cryptos = st.sidebar.multiselect('Select cryptocurrencies:', data['Crypto'].unique())

    # Filter data for the selected cryptocurrencies
    filtered_data = data[data['Crypto'].isin(selected_cryptos)]

    # Display selected cryptocurrencies' price chart
    if len(selected_cryptos) > 0:
        st.write('Price Chart for Selected Cryptocurrencies')
        plt.figure(figsize=(10, 6))
        
        for crypto in selected_cryptos:
            crypto_data = filtered_data[filtered_data['Crypto'] == crypto]
            plt.plot(crypto_data['Date'], crypto_data['Price'], marker='o', label=crypto)
        
        plt.xticks(rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f'Line graph of Cryptocurrency price in {selected_cryptos}')
        plt.legend()
        st.pyplot(plt)
    else:
        st.write('Select one or more cryptocurrencies from the sidebar to plot.')

    # # Sidebar for user input
    
    # selected_crypto = st.sidebar.selectbox('Select a cryptocurrency:', data['Crypto'].unique())
    
    # # Filter data for the selected cryptocurrency
    # filtered_data = data[data['Crypto'] == selected_crypto]
    # # Display selected cryptocurrency's price chart
    
    # st.write(f'Price Chart for {selected_crypto}')
    # plt.figure(figsize=(10, 6))
    # plt.plot(filtered_data['Date'], filtered_data['Price'], marker='o')
    # plt.xticks(rotation=45)
    # plt.xlabel('Date')
    # plt.ylabel('Price')
    # st.pyplot(plt)


if side_bars == "Predictions":
    st.title('Cryptocurrency Price Volatility Example')
    st.write("Cryptocurrency markets are known for their complexities and volatility.")
   
   # Select cryptocurrencies for prediction
    selected_crypto = st.multiselect("Select cryptocurrencies:", data['Crypto'].unique())
    
    # Prepare data for Linear Regression
    plt.figure(figsize=(10, 6))
    for crypto in selected_crypto:
        crypto_data = data[data['Crypto'] == crypto]
        x = np.array(crypto_data.index).reshape(-1, 1)
        y = crypto_data['Price']

        # Linear Regression model
        lr = LinearRegression()
        lr.fit(x, y)
        predicted = lr.predict(x)

        # Display predicted values and corresponding dates
        st.write(f"Predicted Values and Corresponding Dates for {crypto}:")
        prediction_df = pd.DataFrame({'Date': crypto_data['Date'], 'Predicted Price': predicted})
        st.write(prediction_df)

        # Display scatter plot with Linear Regression line
        plt.scatter(x, y, label=f'Actual Prices ({crypto})')
        plt.plot(x, predicted, label=f'Linear Regression ({crypto})')
    
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.title(f'Cryptocurrency Price Volatility Prediction for {", ".join(selected_crypto)}')
        plt.legend()
        st.pyplot(plt)
   
    # # crypto_data = data[data['Crypto'] == 'Bitcoin']
    # # Select cryptocurrency for prediction
    # selected_crypto = st.selectbox("Select a cryptocurrency:", data['Crypto'].unique())
    # crypto_data = data[data['Crypto'] == selected_crypto]

    # # Prepare data for Linear Regression
    # x = np.array(crypto_data.index).reshape(-1, 1)
    # y = crypto_data['Price']

    # # Linear Regression model
    # lr = LinearRegression()
    # lr.fit(x, y)
    # predicted = lr.predict(x)

    # # Display predicted values and corresponding dates
    # st.write(f"Predicted Values and Corresponding Dates for {selected_crypto}:")
    # prediction_df = pd.DataFrame({'Date': crypto_data['Date'], 'Predicted Price': predicted})
    # st.write(prediction_df)

    # st.write(f"Visualizing Cryptocurrency Price Prediction for {selected_crypto}:")
    # # Display scatter plot with Linear Regression line
    # plt.figure(figsize=(10, 6))
    # plt.scatter(x, y, label='Actual Prices', color='blue')
    # plt.plot(x, predicted, label='Linear Regression', color='red')
    # plt.xlabel('Days')
    # plt.ylabel('Price')
    # plt.title(f'Cryptocurrency Price Volatility Prediction for {selected_crypto}')
    # plt.legend()
    # st.pyplot(plt)
    
    
#     # Prepare data for Linear Regression
#     x = np.array(crypto_data.index).reshape(-1, 1)
#     y = crypto_data['Price']

#     # Linear Regression model
#     lr = LinearRegression()
#     lr.fit(x, y)
#     predicted = lr.predict(x)
    
#    # Display predicted values and corresponding dates
#     st.write("Predicted Values and Corresponding Dates:")
#     st.write(pd.DataFrame({'Date': crypto_data['Date'], 'Predicted Price': predicted}))
    
#     st.write("Let's visualize the limitations of a Linear Regression model.")
#     # Display scatter plot with Linear Regression line
#     plt.figure(figsize=(10, 6))
#     plt.scatter(x, y, label='Actual Prices', color='blue')
#     plt.plot(x, predicted, label='Linear Regression', color='red')
#     plt.xlabel('Days')
#     plt.ylabel('Price')
#     plt.title('Cryptocurrency Price Volatility')
#     plt.legend()
#     st.pyplot(plt)
   
    
