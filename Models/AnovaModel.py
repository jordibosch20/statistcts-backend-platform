from typing import List
from pydantic import BaseModel


class AnovaModel(BaseModel):
    significanceLevel: float
    anovaValues: List[List[float]]
