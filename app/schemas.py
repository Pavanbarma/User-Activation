from pydantic import BaseModel, Field, SecretStr

class UserActivity(BaseModel):
    user_name: str
    event: SecretStr = Field(
        json_schema_extra={
        "event_type": "page_view",
        "timestamp": "2025-05-15T10:12:00Z",
        "metadata": {
        "page": "/home",
        "browser": "Chrome"
            }
        }
    )

    class Config:
        orm_mode = True