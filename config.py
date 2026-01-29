"""Configuration for the headful browser proxy."""
import os

# Chrome debug host configuration
CHROME_DEBUG_HOST = os.environ.get('CHROME_DEBUG_HOST', 'localhost')
CHROME_DEBUG_PORT = int(os.environ.get('CHROME_DEBUG_PORT', '9229'))

# Flask server configuration
FLASK_HOST = os.environ.get('FLASK_HOST', '127.0.0.1')
FLASK_PORT = int(os.environ.get('FLASK_PORT', '5000'))
