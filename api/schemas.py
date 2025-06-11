import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_serializer


class PostSchema(BaseModel):
    id: int
    headline: str
    text: str
    created_at: datetime.datetime
    user_id: int

    model_config = ConfigDict(from_attributes=True)

    @field_serializer("created_at")
    def serialize_datetime(self, value: datetime, _info):
        return value.strftime("%d.%m.%Y %H:%M:%S")


class PostIn(BaseModel):
    headline: str
    text: str


class PostOutMessage(BaseModel):
    message: str


class PostUpdate(BaseModel):
    headline: Optional[str] = None
    text: Optional[str] = None
