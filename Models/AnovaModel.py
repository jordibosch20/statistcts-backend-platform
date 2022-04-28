from typing import List
from pydantic import BaseModel


class AnovaModel(BaseModel):
    significanceLevel: float = 0.05
    anovaValues: List[List[float]]
