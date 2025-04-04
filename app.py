import streamlit as st

def perform_search(query):
    # Simulating a search action. Modify this logic based on your real search.
    if query.lower() == "python":
        return "Results for 'python':\n- Python Docs\n- Python Tutorial\n- Python Courses"
    else:
        return f"Results for '{query}':\n- No results found."

# Streamlit UI layout
st.title("Search Application")

# Textbox for user input
search_query = st.text_input("Enter your search query:")

# Trigger search if button is clicked or 'Enter' is pressed
if st.button("Search") or search_query:
    if search_query:
        results = perform_search(search_query)
        st.write(results)
    else:
        st.write("Please enter a search query.")
