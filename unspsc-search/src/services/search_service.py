import pandas as pd
import difflib
import os
import time
from typing import List, Tuple

# Add common acronyms and their expansions

ACRONYMS = {
    # Microscopy & Imaging
    'sem': 'scanning electron microscope',
    'tem': 'transmission electron microscope',
    'afm': 'atomic force microscope',
    'stm': 'scanning tunneling microscope',
    'xrd': 'x-ray diffractometer',
    'xrf': 'x-ray fluorescence spectrometer',
    'wdx': 'wavelength dispersive x-ray spectrometer',
    'edx': 'energy dispersive x-ray spectrometer',
    'saxs': 'small angle x-ray scattering',
    'fe-SEM': 'field emission scanning electron microscope',
    'xps': 'x-ray photoelectron spectrometer',
    'eds': 'energy dispersive spectroscopy',
    'feg': 'field emission gun',
    'ccd': 'charge-coupled device',

    # Spectroscopy
    'uv-vis': 'ultraviolet-visible spectrophotometer',
    'ftir': 'fourier-transform infrared spectrometer',
    'nmr': 'nuclear magnetic resonance spectrometer',
    'raman': 'raman spectrometer',
    'aes': 'atomic emission spectrometer',
    'aAS': 'atomic absorption spectrometer',
    'icp': 'inductively coupled plasma spectrometer',
    'icp-ms': 'inductively coupled plasma mass spectrometer',
    'icp-oes': 'inductively coupled plasma optical emission spectrometer',
    'tof': 'time-of-flight mass spectrometer',

    # Chromatography & Separation
    'gc': 'gas chromatograph',
    'lc': 'liquid chromatograph',
    'hplc': 'high performance liquid chromatography',
    'uhplc': 'ultra high performance liquid chromatography',
    'gcms': 'gas chromatograph mass spectrometer',
    'lcms': 'liquid chromatograph mass spectrometer',
    'cec': 'capillary electrochromatography',
    'ms': 'mass spectrometer',

    # Thermal Analysis
    'tga': 'thermogravimetric analyzer',
    'dsc': 'differential scanning calorimeter',
    'dma': 'dynamic mechanical analyzer',
    'tsa': 'thermal shock analyzer',

    # Industrial & Process Equipment
    'plc': 'programmable logic controller',
    'vfd': 'variable frequency drive',
    'scada': 'supervisory control and data acquisition',
    'dcs': 'distributed control system',
    'hvac': 'heating ventilation and air conditioning',
    'cfd': 'computational fluid dynamics',
    'pcr': 'polymerase chain reaction machine',
    'autoclave': 'high-pressure sterilization chamber',
    'furnace': 'high-temperature heating unit',
    'reactor': 'chemical reaction vessel',
    'centrifuge': 'rotational separation device',
    'spectrometer': 'general device for measuring spectra',
    'balance': 'precision weighing scale',
    'ph meter': 'device for measuring pH',
    'titrator': 'automated titration system',
    'viscometer': 'device for measuring viscosity',
    'densitometer': 'device for measuring density',
    'colorimeter': 'device for measuring color intensity',
    'laser': 'light amplification by stimulated emission of radiation',
    'led': 'light emitting diode',
    'lcd': 'liquid crystal display',
    'ups': 'uninterruptible power supply',
    'rpm': 'revolutions per minute (motor speed)',
}

def expand_query(query: str) -> List[str]:
    """Expand search query to include acronym definitions and variations"""
    query = query.lower().strip()
    queries = [query]
    
    # Handle hyphenated terms
    if '-' in query:
        queries.append(query.replace('-', ' '))
    
    # Handle common variations
    variations = []
    for q in queries:
        # Add acronym expansion if it exists
        if q in ACRONYMS:
            variations.append(ACRONYMS[q])
        
        # Add variations without spaces
        if ' ' in q:
            variations.append(q.replace(' ', ''))
        
        # Add individual words
        variations.extend(q.split())
        
        # Add common suffixes
        if not q.endswith(('s', 'er', 'or')):
            variations.extend([q + 's', q + 'er', q + 'or'])
    
    queries.extend(variations)
    
    # Remove duplicates while preserving order
    seen = set()
    return [x for x in queries if not (x in seen or seen.add(x))]

def load_unspsc_data():
    """Load UNSPSC codes from CSV file with better path handling"""
    try:
        # Try multiple possible file paths
        possible_paths = [
            os.path.join(os.path.dirname(__file__), '..', 'data', 'unspsc_codes.csv'),
            os.path.join('src', 'data', 'unspsc_codes.csv'),
            os.path.join('data', 'unspsc_codes.csv'),
        ]
        
        # Try each path until we find the file
        for file_path in possible_paths:
            if os.path.exists(file_path):
                print(f"Loading data from: {file_path}")  # Debug info
                df = pd.read_csv(file_path)
                print(f"Loaded {len(df)} rows")  # Debug info
                return df
                
        raise FileNotFoundError(f"Could not find unspsc_codes.csv in any of: {possible_paths}")
        
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        print(f"Current working directory: {os.getcwd()}")  # Debug info
        return None

def search_unspsc_codes(query: str, unspsc_data: pd.DataFrame, timeout: int = 5, max_results: int = 20) -> List[Tuple[str, str]]:
    """Search UNSPSC codes with improved matching and timeout"""
    if unspsc_data is None or not query:
        return []
    
    try:
        start_time = time.time()
        query = query.lower().strip()
        matches = []

        # Priority 1: Direct acronym matches
        if query in ACRONYMS:
            expanded = ACRONYMS[query].lower()
            mask = unspsc_data['Description'].str.lower().str.contains(expanded, na=False)
            matches.extend([
                (2.0, row['Code'], row['Description']) 
                for _, row in unspsc_data[mask].iterrows()
            ])
            
            # Return all matches up to max_results for acronyms
            if matches:
                return [(code, desc) for _, code, desc in sorted(matches, reverse=True)[:max_results]]

        # Check timeout before continuing
        if time.time() - start_time > timeout:
            raise TimeoutError("Search took too long")

        # Priority 2: Fuzzy matching if needed
        if len(matches) < max_results:
            for _, row in unspsc_data.iterrows():
                if time.time() - start_time > timeout:
                    break
                
                desc = str(row['Description']).lower()
                score = difflib.SequenceMatcher(None, query, desc).ratio()
                if score > 0.4:
                    matches.append((score, row['Code'], row['Description']))

        # Sort and return top matches up to max_results
        matches.sort(reverse=True)
        seen = set()
        results = []
        for _, code, desc in matches:
            if code not in seen:
                results.append((code, desc))
                seen.add(code)
                if len(results) >= max_results:
                    break

        return results

    except Exception as e:
        print(f"Error during search: {str(e)}")
        return []

def main_search_function(query: str, max_results: int = 5) -> List[Tuple[str, str]]:
    """Main function to handle search requests"""
    unspsc_data = load_unspsc_data()
    if unspsc_data is None:
        print("No data loaded")
        return []
        
    results = search_unspsc_codes(query, unspsc_data, max_results=max_results)
    print(f"Found {len(results)} results for query: {query}")
    return results
