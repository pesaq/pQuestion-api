from pydantic import BaseModel, conint, constr

class QuestionBase(BaseModel):
    title: constr(min_length=10, max_length=50)
    content: constr(min_length=15, max_length=800)

class AnswerBase(BaseModel):
    text: constr(min_length=5, max_length=800)

class QuestionRead(BaseModel):
    id: conint(ge=0, le=2_147_483_647)

class QuestionsRead(BaseModel):
    limit: conint(ge=1, le=100) = 20