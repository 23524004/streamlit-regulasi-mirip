import streamlit as st
import sys
import os
import gdown
import urllib.request
from io import StringIO
import gzip
from io import TextIOWrapper

# Add the src folder to sys.path
sys.path.append(os.path.join(os.getcwd(), 'src'))  # Make sure 'src' folder is in sys.path

# Now import GraphTraversal from query.py in src/
from query import GraphTraversal
import networkx as nx

# Define Google Drive file ID and local file name
GDRIVE_FILE_ID = '1OCJfBAsNrGDS1egvmO4oyOcbVkiCUd'
GRAPH_FILE_PATH = 'cached_graph.graphml'

def download_graph_if_not_exists():
    if not os.path.exists(GRAPH_FILE_PATH):
        url = f"https://drive.google.com/uc?id={GDRIVE_FILE_ID}"
        st.info("Downloading large graph file from Google Drive. This may take a moment...")
        gdown.download(url, GRAPH_FILE_PATH, quiet=False)
    else:
        st.info("Using cached graph file.")

# Download the graph file before anything else
# download_graph_if_not_exists()

# Define DROPBOX ---- ORIGINAL FILE GAGAL ,  STREAMLIT NYA GA KUAT
# Define DROPBOX ---- COMPRESSED DULU
GRAPH_FILE_URL = "https://www.dropbox.com/scl/fi/izf9byjr9lr4ci9hm5jcr/50_noThresh_entity_zfinal_graph.gz?rlkey=gt1n65a5jj49q187o304tx9ls&st=e8ah17ug&dl=1"
@st.cache_data(show_spinner="Loading graphx...")
def load_compressed_graphml_from_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            with gzip.GzipFile(fileobj=response) as gz:
                with TextIOWrapper(gz, encoding='utf-8') as f:
                    return nx.read_graphml(f)
    except Exception as e:
        st.error(f"Failed to load graph: {e}")
        return None
# @st.cache_data(show_spinner="Loading large graph file...")
# def load_graph_from_dropbox(url):
#     try:
#         with urllib.request.urlopen(url) as response:
#             data = response.read().decode('utf-8')
#             return nx.read_graphml(StringIO(data))
#     except Exception as e:
#         st.error(f"Failed to load graph: {e}")
#         return None



def perform_search(query):    
    graph = load_compressed_graphml_from_url(GRAPH_FILE_URL)
    if graph is None or len(graph.nodes) == 0:
        st.error("Graph file could not be loaded or is empty.")
        return []
    # Load the graph
    # graph = nx.read_graphml(GRAPH_FILE_PATH)
    # if graph is None or len(graph.nodes) == 0:
    #     st.error("Graph file could not be loaded or is empty.")
    #     return

    # Define traversal parameters
    similarity_threshold = 0.1
    max_depth = 2

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
    formatted_results = []
    seen_results = set()
    
    for result in results:
        from_node = result.get('from_node', 'Unknown')
        to_node = result.get('to_node', 'Unknown')
        relation = result.get('relation', 'N/A')
        similarity_score = result.get('similarity_score', 'N/A')
        isi = result.get('isi', 'N/A')

        formatted_result = f"""
        <div class="result">
            <div class="result-header">
                <strong>{to_node}</strong>
            </div>
            <div class="content">
                <strong>{isi}</strong> 
            </div>
        </div>
        """
        
        # Only unique result
        if formatted_result not in seen_results:
            formatted_results.append(formatted_result)
            seen_results.add(formatted_result)

    return formatted_results

# Streamlit layout
st.markdown("""
    <style>
        body {
            background-color: black;
        }
        .result {
            background-color: #f9f9f9;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .result-header {
            font-size: 18px;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 8px;
        }
        .result-body {
            font-size: 16px;
            margin: 10px 0;
            color: #555;
        }
        .similarity-score {
            color: #4CAF50;
            font-weight: bold;
        }
        .relation {
            font-style: italic;
            color: #777;
        }
        .content {
            font-size: 14px;
            color: #333;
            word-wrap: break-word;
        }
        .header {
            text-align: center;
            color: #eb6a6a;
            font-size: 36px;
            margin-bottom: 30px;
        }
        .search-box {
            padding: 10px;
            font-size: 18px;
            border-radius: 5px;
            border: 2px solid #4CAF50;
            width: 100%;
            height: 60px;
        }
    </style>
""", unsafe_allow_html=True)

# Header of the application
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
            for result in formatted_results:
                st.markdown(result, unsafe_allow_html=True)
        else:
            st.markdown('<div class="results">No results found.</div>', unsafe_allow_html=True)
