def _get_mock_volkswagen_data():
    """Returns a hardcoded string of financial data for Volkswagen."""
    return """
    - Company: Volkswagen AG
    - Ticker: VOW3.DE
    - Stock Price: €120.50
    - Market Cap: €75.8B
    - P/E Ratio: 5.6
    - Annual Revenue (2023): €279.2B
    - Net Income (2023): €14.8B
    """.strip()

def get_financial_data(company_name: str):
    """
    Retrieves financial data for a given company.
    """
    if "volkswagen" in company_name.lower():
        return _get_mock_volkswagen_data()
    return f"Financial data for {company_name} not found."