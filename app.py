import streamlit as st

# Function to simulate a search
def perform_search(query):
    # Example search logic (you can modify this)
    return f"Results for '{query}':\n- Result 1\n- Result 2\n- Result 3"

# Streamlit UI layout
st.title("Search Application")

# Textbox for user input
search_query = st.text_input("Enter your search query:")

# Button to trigger the search
if st.button("Search") or search_query:
    if search_query:
        results = perform_search(search_query)
        st.write(results)
    else:
        st.write("Please enter a query.")
