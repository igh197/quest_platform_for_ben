import datetime

import requests
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from models import get_db
from schemas import UserQuestRewardBase

app = FastAPI

router = APIRouter()


@router.post('/quest_checker/{user_id}/{quest_id}', response_model=UserQuestRewardBase, status_code=status.HTTP_201_CREATED)
def user_quest_reward_create(user_id: int, claim: str,db: Session = Depends(get_db)):
    db_uqr = UserQuestRewardBase(user_id=user_id, status=claim, date=datetime.date)
    db.add(db_uqr)
    db.commit()
    db.refresh(db_uqr)
    return db_uqr
