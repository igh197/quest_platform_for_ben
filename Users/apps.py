from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import User, get_db
from schemas import UserCreate, UserRead, UserLogin
from config import settings
from passlib.context import CryptContext
import requests
app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Settings(BaseModel):
    authjwt_secret_key: str = settings.JWT_SECRET_KEY


@AuthJWT.load_config
def get_config():
    return Settings()


@app.post('/signup', response_model=UserRead, status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.user_name == user.user_name).first():
        raise HTTPException(status_code=409, detail="User already exists")
    hashed_password = pwd_context.hash(user.password)
    new_user = User(user_name=user.user_name, password=hashed_password, gold=20, diamond=0, status=0)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{user_id}')
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.user_id == user_id).first()


@app.put('/user/{user_id}')
async def update_user(user_id: int,update_user_info:UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if not db_user:
        return None
    for key, value in update_user_info.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post('/login')
def login(form_data: UserLogin, db: Session = Depends(get_db),
                Authorize: AuthJWT = Depends()):
    user = db.query(User).filter(User.user_name == form_data.user_name).first()
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    elif user.status == -1:
        raise HTTPException(status_code=401, detail="You are banned")
    user.login_trial += 1
    if user.login_trial ==3 or user.login_trial ==6:
        requests.post('http://127.0.0.1:8000/quest_checker/%s' % user.user_id)
    else:
        requests.post('http://127.0.0.1:8000/quest_checker/%s' % user.user_id,data='not claimed')
    db.commit()
    access_token = Authorize.create_access_token(subject=user.user_id)
    return {"access_token": access_token}


@app.get('/protected', response_model=UserRead)
async def protected(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    current_user_id = Authorize.get_jwt_subject()
    user = await db.query(User).filter(User.id == current_user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, reload=True)
