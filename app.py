"""Main Flask application for headful browser proxy."""
from flask import Flask, render_template, request, jsonify
import pychrome
import config

app = Flask(__name__)

# Global browser instance
browser = None


def get_browser():
    """Get or create browser connection."""
    global browser
    if browser is None:
        try:
            browser = pychrome.Browser(
                url=f"http://{config.CHROME_DEBUG_HOST}:{config.CHROME_DEBUG_PORT}"
            )
        except Exception as e:
            print(f"Error connecting to Chrome: {e}")
            return None
    return browser


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/load_url', methods=['POST'])
def load_url():
    """Load a URL in the remote Chrome instance and return the page content."""
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        # Ensure URL has a scheme
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        # Get browser instance
        browser_instance = get_browser()
        if not browser_instance:
            return jsonify({'error': 'Could not connect to Chrome debug instance'}), 500
        
        # Create a new tab
        tab = browser_instance.new_tab()
        
        # Start the tab
        tab.start()
        
        # Navigate to the URL
        tab.Page.enable()
        tab.Page.navigate(url=url)
        
        # Wait for page to load
        tab.wait(5)
        
        # Get the page content
        result = tab.Runtime.evaluate(expression="document.documentElement.outerHTML")
        html_content = result.get('result', {}).get('value', '')
        
        # Close the tab
        tab.stop()
        browser_instance.close_tab(tab)
        
        return jsonify({
            'success': True,
            'url': url,
            'content': html_content
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/proxy_url')
def proxy_url():
    """Proxy a URL for iframe display."""
    url = request.args.get('url')
    if not url:
        return "No URL provided", 400
    
    # Ensure URL has a scheme
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        # Get browser instance
        browser_instance = get_browser()
        if not browser_instance:
            return "Could not connect to Chrome debug instance", 500
        
        # Create a new tab
        tab = browser_instance.new_tab()
        
        # Start the tab
        tab.start()
        
        # Navigate to the URL
        tab.Page.enable()
        tab.Page.navigate(url=url)
        
        # Wait for page to load
        tab.wait(5)
        
        # Get the page content
        result = tab.Runtime.evaluate(expression="document.documentElement.outerHTML")
        html_content = result.get('result', {}).get('value', '')
        
        # Close the tab
        tab.stop()
        browser_instance.close_tab(tab)
        
        return html_content
        
    except Exception as e:
        return f"Error loading page: {str(e)}", 500


if __name__ == '__main__':
    app.run(
        host=config.FLASK_HOST,
        port=config.FLASK_PORT,
        debug=True
    )
