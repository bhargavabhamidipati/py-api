from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from palindrome.routes import palindrome
import logging
from config.config import SWAGGER_URL, API_URL, LOGGING_LEVEL, SWAGGER_UI_CONFIG, URL_PREFIX

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=LOGGING_LEVEL)

# Initialize Swagger UI blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config=SWAGGER_UI_CONFIG
)

# Register blueprints
app.register_blueprint(swaggerui_blueprint)
app.register_blueprint(palindrome, url_prefix=URL_PREFIX)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    #app.run(debug=True, host='0.0.0.0', port=5000)
