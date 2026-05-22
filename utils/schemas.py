from pydantic import BaseModel

class CustomerSchema(BaseModel):
    id: str
    name: str
    email: str
    tenant_id: str