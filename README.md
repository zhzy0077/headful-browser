# headful-browser

Head for headless browser - A Python proxy server that connects to a remote Chrome instance via Chrome DevTools Protocol and displays web pages in an iframe.

## Features

- 🌐 Connect to remote Chrome debug instance
- 📱 Simple web interface for entering URLs
- 🖼️ Display loaded pages in an iframe
- 🔧 Configurable Chrome debug host and port
- 🚀 Built with Flask and Chrome DevTools Protocol

## Prerequisites

- Python 3.8 or higher
- Chrome/Chromium running with remote debugging enabled

## Installation

1. Clone the repository:
```bash
git clone https://github.com/zhzy0077/headful-browser.git
cd headful-browser
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Setup Chrome Remote Debugging

You need to start Chrome with remote debugging enabled. Use one of the following methods:

### Linux/Mac:
```bash
google-chrome --remote-debugging-port=9229 --user-data-dir=/tmp/chrome-debug
```

### Windows:
```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9229 --user-data-dir=C:\temp\chrome-debug
```

### Docker (Chromium):
```bash
docker run -d -p 9229:9229 zenika/alpine-chrome --no-sandbox --remote-debugging-address=0.0.0.0 --remote-debugging-port=9229
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Enter a URL in the input field and click "Load Page" to view it through the remote Chrome instance.

## Configuration

You can configure the application using environment variables:

- `CHROME_DEBUG_HOST`: Chrome debug host (default: `localhost`)
- `CHROME_DEBUG_PORT`: Chrome debug port (default: `9229`)
- `FLASK_HOST`: Flask server host (default: `0.0.0.0`)
- `FLASK_PORT`: Flask server port (default: `5000`)

Example:
```bash
export CHROME_DEBUG_HOST=192.168.1.100
export CHROME_DEBUG_PORT=9229
python app.py
```

## How It Works

1. User enters a URL in the web interface
2. Flask server receives the request
3. Server connects to Chrome via Chrome DevTools Protocol (CDP)
4. Chrome loads the requested URL
5. Server retrieves the HTML content from Chrome
6. Content is displayed in an iframe on the user's browser

## Project Structure

```
headful-browser/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web interface
└── README.md          # This file
```

## License

This project is open source and available under the MIT License.
