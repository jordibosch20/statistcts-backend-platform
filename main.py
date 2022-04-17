import mimetypes
from anova import generateBoxPlot
from ttest import generateStatistics
from parseInput import parseInput
from flask import jsonify, Flask, make_response, send_file
from flask_cors import CORS
import functions_framework
import tempfile

app = Flask(__name__)
CORS(app)


def requestFlight(request):
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@functions_framework.http
def hello_http(request):
    if request.method == 'OPTIONS':
        return requestFlight(request)

    l1 = parseInput(request)
    anovaValues = l1['anovaValues']
    generateBoxPlot(anovaValues)

    import anova
    tmpdir = tempfile.gettempdir()
    response = send_file(tmpdir + '/anova.png', mimetype='blob')
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@functions_framework.http
def hello_t_test(request):
    if request.method == 'OPTIONS':
        return requestFlight(request)

    l1 = parseInput(request)
    tTestValues = l1['tTestValues']
    (statistic, pvalue) = generateStatistics(tTestValues)
    response = make_response(
        jsonify(
            {'statistic': statistic, 'pvalue': pvalue}
        ))
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response
