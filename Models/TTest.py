from typing import List, Optional
from pydantic import BaseModel


class TTestModel(BaseModel):
    significanceLevel: float = 0.05
    tTestValues: List[List[float]]
