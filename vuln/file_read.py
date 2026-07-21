import os
from flask import Flask, request, abort

app = Flask(__name__)

ALLOWED_CONFIGS = {
    "app.conf",
    "db.conf",
    "logging.conf",
}


def read_config(filename):
    """Read configuration file."""
    base_dir = os.path.abspath('/configs')

    if not filename or filename not in ALLOWED_CONFIGS:
        raise ValueError("Invalid config name")

    filepath = os.path.abspath(os.path.join(base_dir, filename))
    if os.path.commonpath([base_dir, filepath]) != base_dir:
        raise ValueError("Invalid config path")

    with open(filepath, 'r') as f:
        return f.read()


@app.route('/config')
def config_route():
    try:
        return read_config(request.args.get('name'))
    except ValueError:
        abort(400, description="Invalid config name")
