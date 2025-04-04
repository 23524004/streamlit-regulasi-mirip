import streamlit as st
from time import sleep

##########################################################
##########################################################
##########################################################
def perform_search(query):
    sleep(1)
    if query.lower() == "python":
        return "Results for 'python':\n- Python Docs\n- Python Tutorial\n- Python Courses"
    elif query.lower() == "streamlit":
        return "Results for 'streamlit':\n- Streamlit Docs\n- Streamlit Tutorial"
    else:
        return f"Results for '{query}':\n- No results found."


##########################################################
##########################################################
##########################################################

# Custom CSS to style elements (like search box, button, etc.)
st.markdown("""
    <style>
        .search-box {
            padding: 20px;
            font-size: 24px;
            border-radius: 10px;
            border: 2px solid #4CAF50;
            width: 100%;
            max-width: 600px;
            height: 60px;
        }
        .header {
            text-align: center;
            color: #eb6a6a;
            font-size: 36px;
            margin-bottom: 30px;
        }
        .results {
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 10px;
            color: #000000;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit layout
st.markdown('<div class="header">PENCARIAN REGULASI</div>', unsafe_allow_html=True)

search_query = st.text_input("", "", key="search", placeholder="Type your query and press Enter", help="Start typing to search...", max_chars=100)

if search_query:
    with st.spinner("Searching..."):
        results = perform_search(search_query)
        st.markdown(f'<div class="results">{results}</div>', unsafe_allow_html=True)




