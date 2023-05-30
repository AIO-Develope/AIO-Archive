from flask import Flask, send_from_directory
import logging
from flask import Flask

app = Flask(__name__)

# Disable Flask's default logger
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)



@app.route('/downloads/<code>/<filename>')
def download_file(code, filename):
    folder_path = f'archive/{code}'
    return send_from_directory(folder_path, filename)

if __name__ == '__main__':
    # Set up a custom logger to print the accessible IP and port
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    app.run(host='0.0.0.0', port=80, debug=False)
