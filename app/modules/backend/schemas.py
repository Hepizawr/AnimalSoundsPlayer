from pydantic import BaseModel


class JsonModel(BaseModel):
    animal: str
