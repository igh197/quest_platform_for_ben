from typing import List

from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from models import get_db
from schemas import QuestCreate, QuestRead, RewardCreate, RewardRead
from crud import Crud

app = FastAPI

router = APIRouter()


@router.post(path='/quest/create/{reward_id}', response_model=QuestCreate, status_code=status.HTTP_201_CREATED)
def create_quest(reward_id: int, quest: QuestCreate, db: Session = Depends(get_db)):

    return Crud.create_quest(db=db, quest=quest, reward_id=reward_id)


@router.get(path="/quest/{quest_id}", response_model=QuestRead, status_code=status.HTTP_200_OK)
def get_quest(quest_id: int, db: Session = Depends(get_db)):
    return Crud.get_quest(db=db, quest_id=quest_id)


@router.put(path='/quest/update/{quest_id}', response_model=QuestCreate)
def update_quest(quest_id: int, quest_update: QuestCreate, db: Session = Depends(get_db)):
    db_quest = Crud.update_quest(db=db, quest_id=quest_id, quest_update=quest_update)
    if db_quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    return db_quest


@router.post(path='/reward/create', response_model=RewardCreate, status_code=status.HTTP_201_CREATED)
def create_reward(reward: RewardCreate, db: Session = Depends(get_db)):
    return Crud.create_reward(db=db, reward=reward)


@router.get(path="/reward/{reward_id}", response_model=RewardRead, status_code=status.HTTP_200_OK)
def get_quest(reward_id: int, db: Session = Depends(get_db)):
    return Crud.get_reward(db=db, reward_id=reward_id)


@router.put(path='/reward/update/{reward_id}', response_model=RewardCreate)
def update_quest(reward_id: int, reward_update: RewardCreate, db: Session = Depends(get_db)):
    db_reward = Crud.update_reward(db=db, reward_id=reward_id, reward_update=reward_update)
    if db_reward is None:
        raise HTTPException(status_code=404, detail="Reward not found")
    return db_reward


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, reload=True)
