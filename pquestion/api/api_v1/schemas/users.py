from pydantic import BaseModel, conint, constr

class UserCreateSchema(BaseModel):
    username: constr(min_length=5, max_length=20)
    password: constr(min_length=8, max_length=255)

class LiteUserSchema(BaseModel):
    id: int
    username: constr(min_length=5, max_length=20)
    is_active: bool

    class Config:
        from_attributes: bool = True