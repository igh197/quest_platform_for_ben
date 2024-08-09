from pydantic import BaseModel



class RewardCreate(BaseModel):
    reward_name: int
    reward_item: str
    reward_qty: int


class RewardRead(BaseModel):
    reward_id: int
    reward_name: int
    reward_item: str
    reward_qty: int


class QuestCreate(BaseModel):
    auto_claim: bool
    streak: int
    duplication: int
    name: str
    owner_id: int
    description: str


class QuestRead(BaseModel):
    quest_id: int
    auto_claim: bool
    streak: int
    duplication: int
    name: str
    owner_id: int
    description: str
