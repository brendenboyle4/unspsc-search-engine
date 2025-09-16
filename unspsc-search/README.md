# UNSPSC Code Search Application

An application to search and find UNSPSC codes using equipment names and acronyms.

## Project Structure

- **src/**: Contains the main application code.
  - **app.py**: The main entry point of the application.
  - **data/**: Contains the dataset of UNSPSC codes.
    - **unspsc_codes.csv**: The CSV file with UNSPSC codes and hierarchies.
  - **models/**: Contains the logic for handling search queries.
    - **search_model.py**: Defines data structures and logic for search handling.
  - **services/**: Contains the search and AI functionalities.
    - **search_service.py**: Functions for searching the UNSPSC dataset.
    - **ai_service.py**: Integrates AI functionalities for enhanced search capabilities.
  - **ui/**: Contains the user interface components.
    - **main_window.py**: Sets up the main application window.
    - **search_widget.py**: Defines the search input field and button.
    - **results_widget.py**: Displays the search results.
  - **utils/**: Contains utility functions for text processing.
    - **text_processing.py**: Functions for processing and normalizing user input.
  
- **tests/**: Contains unit tests for the application.
  - **test_search.py**: Unit tests for the search functionality.

- **requirements.txt**: Lists the dependencies required to run the application.

## Installation

1. Clone this repository:
```bash
git clone <https://github.com/brendenboyle4/unspsc-search-engine>
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Mac/Linux:
```bash
source venv/bin/activate
```

4. Install required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory
2. Run:
```bash
streamlit run src/app.py
```

3. Open your web browser to http://localhost:8501

## Usage

1. Enter equipment name or acronym in the search box
2. View matching UNSPSC codes and descriptions
3. Results are ranked by relevance

## Features

- Acronym recognition (e.g., "SEM" → "Scanning Electron Microscope")
- Fuzzy matching for similar terms
- Detailed equipment descriptions
- Top 5 most relevant results

## Deployment

### Streamlit Cloud Deployment

1. Visit [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Select your repository
4. Deploy settings:
   - Main file path: src/app.py
   - Python version: 3.9
   - Requirements: requirements.txt

Access the deployed app at: https://unspsc-search-engine-dsl3xtt5dign9ymvri8r9o.streamlit.app/

## License

This project is licensed under the MIT License. See the LICENSE file for more details.