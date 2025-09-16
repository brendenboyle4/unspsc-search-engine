class SearchModel:
    def __init__(self, unspsc_data):
        self.unspsc_data = unspsc_data

    def search(self, query):
        # Normalize the query for better matching
        normalized_query = self.normalize_query(query)
        results = self.find_relevant_codes(normalized_query)
        return results

    def normalize_query(self, query):
        # Implement normalization logic (e.g., lowercasing, removing special characters)
        return query.lower().strip()

    def find_relevant_codes(self, normalized_query):
        # Implement logic to find relevant UNSPSC codes based on the normalized query
        relevant_codes = []
        for code, description in self.unspsc_data.items():
            if normalized_query in description.lower():
                relevant_codes.append((code, description))
        return relevant_codes