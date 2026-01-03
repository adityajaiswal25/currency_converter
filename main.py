# Simple Currency Converter Web App
# This script creates a Flask web application that serves a frontend HTML page
# and provides an API endpoint for currency conversion.

from flask import Flask, request, jsonify, render_template_string, Response
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# API key and base URL for exchange rate service
# Get API key from environment variable, fallback to None if not set
api_key = os.getenv('EXCHANGE_RATE_API_KEY')
if not api_key:
    raise ValueError("EXCHANGE_RATE_API_KEY environment variable is not set. Please set it in your .env file or environment.")

base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

def get_exchange_rates(base_currency):
    """
    Fetch exchange rates for a given base currency from the API.

    Args:
        base_currency (str): The base currency code (e.g., 'USD').

    Returns:
        dict: Dictionary of conversion rates, or empty dict if error.
    """
    url = f"{base_url}{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('conversion_rates', {})
    else:
        print("Error fetching exchange rates")
        return {}

def convert_currency(amount, from_currency, to_currency):
    """
    Convert an amount from one currency to another.

    Args:
        amount (float): The amount to convert.
        from_currency (str): Source currency code.
        to_currency (str): Target currency code.

    Returns:
        float or None: Converted amount, or None if conversion fails.
    """
    rates = get_exchange_rates(from_currency)
    if to_currency in rates:
        return amount * rates[to_currency]
    else:
        return None

@app.route('/')
def home():
    """
    Serve the main HTML page for the currency converter.
    """
    # Read the HTML content from index.html file
    index_path = os.path.join(os.path.dirname(__file__), 'index.html')
    with open(index_path, 'r') as f:
        html_content = f.read()
    return render_template_string(html_content)

@app.route('/rates', methods=['GET'])
def get_rates():
    """
    API endpoint to get exchange rates from a base currency to multiple target currencies.
    
    Query parameters:
    - base: Base currency code (default: 'USD')
    - currencies: Comma-separated list of target currencies (optional)
    
    Returns JSON response with rates for specified currencies.
    """
    base_currency = request.args.get('base', 'USD').upper()
    currencies_str = request.args.get('currencies', '')
    
    rates = get_exchange_rates(base_currency)
    
    if not rates:
        return jsonify({'error': 'Failed to fetch exchange rates'}), 500
    
    # If specific currencies requested, filter the rates
    if currencies_str:
        target_currencies = [c.strip().upper() for c in currencies_str.split(',')]
        filtered_rates = {curr: rates.get(curr) for curr in target_currencies if curr in rates}
        return jsonify({
            'base': base_currency,
            'rates': filtered_rates
        })
    
    # Return all rates if no specific currencies requested
    return jsonify({
        'base': base_currency,
        'rates': rates
    })

@app.route('/convert', methods=['POST'])
def convert():
    """
    API endpoint to handle currency conversion requests.

    Expects JSON data with 'amount', 'from_currency', and 'to_currency'.
    Returns JSON response with conversion result or error message.
    """
    data = request.get_json()
    amount = data.get('amount')
    from_currency = data.get('from_currency')
    to_currency = data.get('to_currency')

    if not all([amount, from_currency, to_currency]):
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        amount = float(amount)
        result = convert_currency(amount, from_currency.upper(), to_currency.upper())
        if result is not None:
            return jsonify({
                'original_amount': amount,
                'from_currency': from_currency.upper(),
                'converted_amount': round(result, 2),
                'to_currency': to_currency.upper()
            })
        else:
            return jsonify({'error': 'Conversion not possible. Check currency codes.'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid amount format'}), 400

@app.route('/robots.txt')
def robots_txt():
    """
    Serve robots.txt for SEO purposes.
    """
    robots_content = """User-agent: *
Allow: /
Sitemap: {}/sitemap.xml
""".format(request.url_root.rstrip('/'))
    return Response(robots_content, mimetype='text/plain')

@app.route('/sitemap.xml')
def sitemap_xml():
    """
    Serve sitemap.xml for SEO purposes.
    """
    base_url = request.url_root.rstrip('/')
    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{base_url}/</loc>
    <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>"""
    return Response(sitemap_content, mimetype='application/xml')

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
