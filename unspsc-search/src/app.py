import streamlit as st
from services.search_service import main_search_function

def main():
    # Configure page
    st.set_page_config(
        page_title="UNSPSC Code Search",
        page_icon="🔍",
        layout="wide"
    )
    
    # Initialize session state for results count
    if 'show_results' not in st.session_state:
        st.session_state.show_results = 5
    
    # Main UI
    st.title("UNSPSC Code Search")
    st.subheader("Search for equipment codes and descriptions")
    
    # Create search input with placeholder
    search_query = st.text_input(
        "Enter product description:",
        placeholder="Example: SEM or microscope"
    )
    
    if search_query:
        with st.spinner('Searching...'):
            try:
                # Get results with current count
                results = main_search_function(query=search_query, 
                                            max_results=st.session_state.show_results)
                
                if results:
                    total_found = len(results)
                    st.success(f"Found {total_found} matches")
                    
                    # Create a container for results
                    with st.container():
                        for code, description in results:
                            col1, col2 = st.columns([1, 3])
                            with col1:
                                st.code(code, language=None)
                            with col2:
                                st.markdown(f"**{description}**")
                            st.divider()
                        
                        # Create columns for buttons
                        col1, col2 = st.columns(2)
                        
                        # Show "Load More" button if there might be more results
                        if total_found >= st.session_state.show_results:
                            if col1.button("Show More Results", key="more"):
                                st.session_state.show_results += 5
                                st.rerun()
                        
                        # Show "Show Less" button if showing more than initial amount
                        if st.session_state.show_results > 5:
                            if col2.button("Show Less", key="less"):
                                st.session_state.show_results = 5
                                st.rerun()
                else:
                    st.warning("No matches found. Try a different search term.")
            
            except Exception as e:
                st.error(f"An error occurred during search: {str(e)}")

if __name__ == "__main__":
    main()
