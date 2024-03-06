import streamlit as st

# Function to fetch company details from the database
def fetch_company_details(symbol):
    conn = sqlite3.connect('company_profiles.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM companies WHERE symbol=?', (symbol,))
    company_details = cursor.fetchone()
    conn.close()
    return company_details

# Display company symbols and descriptions
st.title("Company Information Portal")

selected_company_symbol = st.selectbox("Select a company symbol:", options=["A", "B"])  # Replace with symbols fetched from database

if st.button("View Details"):
    # Fetch details from the database
    company_details = fetch_company_details(selected_company_symbol)
    if company_details:
        st.subheader(selected_company_symbol)
        st.write("**Description:**", company_details[2])
        st.write("**Job Roles:**", company_details[3])
        st.write("**Eligibility Criteria:**", company_details[4])
        st.write("**Past Placement Statistics:**", company_details[5])
    else:
        st.write("Company details not found.")
