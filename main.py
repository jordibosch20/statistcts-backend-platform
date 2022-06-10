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

import os
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
async def root(item_id):
    return {"hello_world": "hello_world"}


@app.post("/ttest")
async def computeHypothesis(tTestModel: TTestModel):
    (statistic, pvalue) = TTest.generateStatistics(tTestModel.tTestValues)
    return {'tTest': pvalue, 'statistic': statistic}


@app.post("/anova/homocedasticity")
async def homocedasticity(anovaModel: AnovaModel):
    anova = Anova(anovaModel.anovaValues)
    return anova.computeHomocedasticityTest()


@app.post("/anova/normalityComputation")
async def homocedasticity(anovaModel: AnovaModel):
    anova = Anova(anovaModel.anovaValues)
    return anova.computeNormalityTest()


@app.post("/anova/anovaTukey")
async def comptueTukey(anovaModel: AnovaModel):
    anova = Anova(anovaModel.anovaValues)
    return anova.comptueTukey()


@app.post("/anova/anovaComputation")
async def computeAnova(anovaModel: AnovaModel):
    anova = Anova(anovaModel.anovaValues)
    return anova.computeAnova()


@app.post("/anova/{numberImage}")
async def computeHypothesis(numberImage, anovaModel: AnovaModel):
    anova = Anova(anovaModel.anovaValues)
    if (numberImage == 'first'):
        anova.generateBoxPlot()
        tmpdir = tempfile.gettempdir()
        return FileResponse(tmpdir + '/anova.png', media_type='image/png')
    elif(numberImage == 'second'):
        anova.generateNormalityPlot()
        tmpdir = tempfile.gettempdir()
        return FileResponse(tmpdir + '/anova2.png', media_type='image/png')
