import streamlit as st
import pymysql

# Function to connect to MySQL database


def create_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='#jyO2irmay.',
        database='university',  # Change to your database name
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# Function to fetch company details from the database


def get_company_details(company_id):
    connection = create_connection()
    try:
        with connection.cursor() as cursor:
            query = f"SELECT * FROM Companies WHERE CompanyID = {company_id}"
            cursor.execute(query)
            return cursor.fetchone()
    finally:
        connection.close()

# Function to fetch job roles and placements from the database


def get_job_roles_and_placements(company_id):
    connection = create_connection()
    try:
        with connection.cursor() as cursor:
            query = f"""
                SELECT JobRoles.RoleName, JobRoles.EligibilityCriteria, JobRoles.Salary, Placements.NumberOfStudents
                FROM JobRoles
                LEFT JOIN Placements ON JobRoles.JobRoleID = Placements.JobRoleID
                WHERE JobRoles.CompanyID = {company_id}
            """
            cursor.execute(query)
            return cursor.fetchall()
    finally:
        connection.close()

# Streamlit App


def main():
    st.title("Campus Placement Information")

    # Page layout
    page = st.sidebar.selectbox("Select a Company", [
                                "Google", "Microsoft", "Amazon", "McKinsey & Company", "J.P. Morgan Chase"])

    # Display company logo (placeholder image URLs)
    company_logo_urls = {
        "Google": "https://example.com/google_logo.png",
        "Microsoft": "https://example.com/microsoft_logo.png",
        "Amazon": "https://example.com/amazon_logo.png",
        "McKinsey & Company": "https://example.com/mckinsey_logo.png",
        "J.P. Morgan Chase": "https://example.com/jpmorgan_logo.png",
    }
    company_logo_url = company_logo_urls.get(
        page, "https://example.com/default_logo.png")
    st.image(company_logo_url, width=150)

    # View details option
    if st.button("View Details"):
        company_id_mapping = {
            "Google": 1,
            "Microsoft": 2,
            "Amazon": 3,
            "McKinsey & Company": 4,
            "J.P. Morgan Chase": 5,
        }
        company_id = company_id_mapping.get(page, 1)

        # Fetch company details from the database
        company_details = get_company_details(company_id)

        # Fetch job roles and placements from the database
        job_roles_and_placements = get_job_roles_and_placements(company_id)

        # Display company details
        st.markdown(f"## {page}")
        st.subheader("Description:")
        st.write(company_details.get("Description"))

        # Display job roles and placements
        st.subheader("Job Roles and Placements:")
        for role in job_roles_and_placements:
            st.markdown(f"### {role['RoleName']}")
            st.write(
                f"**Eligibility Criteria:** {role['EligibilityCriteria']}")
            st.write(f"**Salary:** {role['Salary']}")
            st.write(
                f"**Previous Year Statistics (Number of Students):** {role['NumberOfStudents']}")


if __name__ == "__main__":
    main()
