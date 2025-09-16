import streamlit as st
from services.search_service import main_search_function
import os

def main():
    # Configure page
    st.set_page_config(
        page_title="UNSPSC Code Search",
        page_icon="🔍",
        layout="wide"
    )
    
    # Main UI
    st.title("UNSPSC Code Search")
    st.subheader("Search for equipment codes and descriptions")
    
    # Create search input with placeholder
    search_query = st.text_input(
        "Enter product description:",
        placeholder="Example: 'SEM' or 'scanning electron microscope'"
    )
    
    if search_query:
        results = main_search_function(search_query)
        if results:
            st.success(f"Found {len(results)} matches")
            for code, description in results:
                with st.container():
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.code(code)
                    with col2:
                        st.write(description)
                st.divider()
        else:
            st.warning("No matches found")

if __name__ == "__main__":
    main()
