import mimetypes
from flask import jsonify, Flask, make_response, send_file
from flask_cors import CORS
import functions_framework

app = Flask(__name__)
CORS(app)


@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    print('request_json', request_json)
    print('request_args', request_args)
    if request.method == 'OPTIONS':  # Cors preflight
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response
    response = send_file('static/anova.png', mimetype='blob')
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    import anova
    print('arribat dsps anova')
    return response


@functions_framework.cloud_event
def hello_cloud_event(cloud_event):
    print(
        f"Received event with ID: {cloud_event['id']} and data {cloud_event.data}")
