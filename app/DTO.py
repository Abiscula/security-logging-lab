from pydantic import BaseModel

class LoginRequest(BaseModel):
  username: str
  password: str

class ActionRequest(BaseModel):
  action: str