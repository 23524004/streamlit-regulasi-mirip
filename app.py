import streamlit as st
import sys
import os

# Add the src folder to sys.path
sys.path.append(os.path.join(os.getcwd(), 'src'))  # Make sure 'src' folder is in sys.path

# Now import GraphTraversal from query.py in src/
from query import GraphTraversal
import networkx as nx

# Path to the graph file
GRAPH_FILE_PATH = 'dataset/final_graph.graphml'

def perform_search(query):
    # Load the graph
    graph = nx.read_graphml(GRAPH_FILE_PATH)
    
    # Define traversal parameters
    similarity_threshold = 0.5
    max_depth = 3
    
    # Create a GraphTraversal object
    traversal = GraphTraversal(graph, query, similarity_threshold, max_depth)
    
    # Step 1: Get initial nodes based on query similarity
    initial_nodes = traversal.get_initial_nodes()
    
    # Step 2: Perform the graph traversal starting from the initial nodes
    results = traversal.traverse(initial_nodes)
    
    # Return results
    return results

def format_results_for_display(results):
    """Format the traversal results for displaying in Streamlit"""
    formatted_results = ""
    for result in results:
        formatted_results += f"From Node: {result['from_node']}\n"
        formatted_results += f"To Node: {result['to_node']}\n"
        formatted_results += f"Relation: {result['relation']}\n"
        if result['similarity_score']:
            formatted_results += f"Similarity Score: {result['similarity_score']:.2f}\n"
        if result['isi']:
            formatted_results += f"Content (Isi): {result['isi']}\n"
        formatted_results += "-" * 40 + "\n"
    
    return formatted_results

# Streamlit layout
st.markdown("""
    <style>
        .search-box {
            padding: 10px;
            font-size: 18px;
            border-radius: 5px;
            border: 2px solid #4CAF50;
            width: 100%;
            max-width: 600px;
            min-height:100px;
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

st.markdown('<div class="header">PENCARIAN REGULASI</div>', unsafe_allow_html=True)

# Text input for search query
search_query = st.text_input("", "", key="search", placeholder="Type your query and press Enter", help="Start typing to search...", max_chars=25)

# If the user has entered a query, perform the search
if search_query:
    with st.spinner("Searching..."):
        # Get search results from the graph traversal
        results = perform_search(search_query)
        
        # Format the results for display
        formatted_results = format_results_for_display(results)
        
        # Display the results in Streamlit
        if formatted_results:
            st.markdown(f'<div class="results">{formatted_results}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="results">No results found.</div>', unsafe_allow_html=True)
