from typing import List, Optional
from pydantic import BaseModel


class TTestModel(BaseModel):
    significanceLevel: float = 0.5
    tTestValues: List[List[float]]
