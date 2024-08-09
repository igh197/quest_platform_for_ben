import datetime

from pydantic import BaseModel


class UserQuestRewardBase(BaseModel):
    uqr_id: int
    status: str
    date: datetime.date
    user_id: int
    quest_id:int