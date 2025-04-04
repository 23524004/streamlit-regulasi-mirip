import streamlit as st
from time import sleep

# Function to simulate a search
def perform_search(query):
    # Simulate a loading time
    sleep(1)
    # Example search logic (you can modify this)
    if query.lower() == "python":
        return "Results for 'python':\n- Python Docs\n- Python Tutorial\n- Python Courses"
    elif query.lower() == "streamlit":
        return "Results for 'streamlit':\n- Streamlit Docs\n- Streamlit Tutorial"
    else:
        return f"Results for '{query}':\n- No results found."

# Custom CSS to style elements (like search box, button, etc.)
st.markdown("""
    <style>
        .search-box {
            padding: 10px;
            font-size: 18px;
            border-radius: 5px;
            border: 2px solid #4CAF50;
            width: 100%;
            max-width: 600px;
        }
        .search-button {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            font-size: 18px;
        }
        .search-button:hover {
            background-color: #45a049;
        }
        .header {
            text-align: center;
            color: #333;
            font-size: 36px;
        }
        .results {
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit layout
st.markdown('<div class="header">Search Application</div>', unsafe_allow_html=True)

# Create a search box with custom CSS
search_query = st.text_input("Enter your search query:", "", key="search", placeholder="Search for Python, Streamlit, etc.", help="Type your search query and hit Enter")

# Use columns for side-by-side layout for button and input box
col1, col2 = st.columns([4, 1])

with col1:
    pass  # Just to keep the layout

with col2:
    # Button to trigger the search
    search_button = st.button("Search", key="search_button", use_container_width=True)

# Trigger search if the button is clicked or the user presses Enter
if search_button or search_query:
    if search_query:
        # Show loading spinner
        with st.spinner("Searching..."):
            results = perform_search(search_query)
            st.markdown(f'<div class="results">{results}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a search query.")
