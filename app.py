import streamlit as st

##########################################################
##########################################################
##########################################################
def perform_search(query):
    if query.lower() == "python":
        return "Results for 'python':\n- Python Docs\n- Python Tutorial\n- Python Courses"
    else:
        return f"Results for '{query}':\n- No results found."


##########################################################
##########################################################
##########################################################

st.title("Pencarian Pasal")

# creates a horizontal line
st.write("---")

# Textbox user input
search_query = st.text_input("Enter search query:")

# Button to trigger the search
if st.button("Search") or search_query:
    if search_query:
        results = perform_search(search_query)
        st.write(results)
    else:
        st.write("Please enter a query.")





