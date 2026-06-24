from pydantic import BaseModel

class SankeyDto(BaseModel):
    sources:    list[int]
    targets:    list[int]
    values:     list[int]
    colors:     list[str]