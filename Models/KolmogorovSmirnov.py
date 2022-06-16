from typing import List
from pydantic import BaseModel


class KolmogorovSmirnovModel(BaseModel):
    kolmogorovSmirnovValues: List[List[float]]
