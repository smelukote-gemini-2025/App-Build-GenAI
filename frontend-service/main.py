import os
from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# It's good practice to get the backend service URL from an environment variable
# This allows you to easily change it without redeploying the container
# For local testing, you might hardcode it, but for Cloud Run, ENV vars are best.
RETRIEVAL_SERVICE_URL = os.environ.get('RETRIEVAL_SERVICE_URL', 'http://retrieval-service-default-url.run.app')
# Replace 'http://retrieval-service-default-url.run.app' with the actual
# URL of your deployed retrieval-service, or ensure you set the ENV var.


@app.route('/')
def index():
    retrieval_data = "No data yet."
    error_message = None

    try:
        # Example: Making a request to your retrieval service
        # You might pass parameters based on user input or other logic
        response = requests.get(f"{RETRIEVAL_SERVICE_URL}/data") # Assuming /data endpoint on retrieval-service
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        retrieval_data = response.json() # Assuming the retrieval service returns JSON
    except requests.exceptions.ConnectionError:
        error_message = f"Could not connect to retrieval service at {RETRIEVAL_SERVICE_URL}. Is it running?"
    except requests.exceptions.Timeout:
        error_message = "Request to retrieval service timed out."
    except requests.exceptions.RequestException as e:
        error_message = f"Error calling retrieval service: {e}"
    except ValueError: # Catches JSONDecodeError if response is not valid JSON
        error_message = f"Retrieval service returned non-JSON data: {response.text}"

    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Frontend Service</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 2em; }
            pre { background-color: #eee; padding: 1em; border-radius: 5px; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>Welcome to the Frontend Service!</h1>
        <p>This service is running on Google Cloud Run.</p>

        <h2>Data from Retrieval Service:</h2>
        {% if error_message %}
            <p class="error">{{ error_message }}</p>
        {% else %}
            <pre>{{ retrieval_data }}</pre>
        {% endif %}

        <p>You can modify this code to build out your full frontend application.</p>
    </body>
    </html>
    """
    return render_template_string(html_template, retrieval_data=retrieval_data, error_message=error_message)

if __name__ == '__main__':
    # Cloud Run expects the application to listen on PORT environment variable
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)

