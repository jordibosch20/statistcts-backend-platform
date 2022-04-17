from Models.AnovaModel import AnovaModel
from Models.TTest import TTestModel
from anova import Anova
from ttest import TTest
from pydantic import BaseModel
from fastapi import FastAPI
from typing import List, Optional
import json
import tempfile
from fastapi.responses import RedirectResponse, FileResponse


import uvicorn
from fastapi import FastAPI, Form, Header
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"hello_world": 'hello_world'}


@app.post("/ttest")
async def computeHypothesis(tTestModel: TTestModel):
    (statistic, pvalue) = TTest.generateStatistics(tTestModel.tTestValues)
    return {'tTest': pvalue, 'statistic': statistic}


@app.post("/anova")
async def computeHypothesis(anovaModel: AnovaModel):
    Anova.generateBoxPlot(anovaModel.anovaValues)
    tmpdir = tempfile.gettempdir()
    return FileResponse(tmpdir + '/anova.png', media_type='image/png')
    # return {'anova': anovaModel}


"""
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
 """
