from pydantic import BaseModel

class SankeyDataModel(BaseModel):
    sources:    list[int]
    targets:    list[int]
    values:     list[int]
    colors:     list[str]