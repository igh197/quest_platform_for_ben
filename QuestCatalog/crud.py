from sqlalchemy.orm import Session


from models import Reward,Quests
from schemas import QuestCreate, QuestRead, RewardCreate


class Crud:
    def create_quest(self,reward_id: int, quest: QuestCreate, db: Session):
        db_quest = Quests(**quest.dict(), owner_id=reward_id)
        db.add(db_quest)
        db.commit()
        db.refresh(db_quest)
        return db_quest

    def get_quest(self,quest_id: int, db: Session):
        return db.query(Quests).filter(Quests.quest_id == quest_id).first()

    def update_quest(self,quest_id: int, quest_update: QuestCreate, db: Session):
        db_quest = db.query(Quests).filter(Quests.quest_id == quest_id).first()
        if not db_quest:
            return None
        for key, value in quest_update.dict(exclude_unset=True).items():
            setattr(db_quest, key, value)
        db.commit()
        db.refresh(db_quest)
        return db_quest

    def create_reward(self,reward: RewardCreate, db: Session):
        db_reward = Reward(**reward.dict())
        db.add(db_reward)
        db.commit()
        db.refresh(db_reward)
        return db_reward

    def get_reward(self,reward_id: int, db: Session):
        return db.query(Reward).filter(Reward.reward_id == reward_id).first()

    def update_reward(self,reward_id: int, reward_update: RewardCreate, db: Session):
        db_reward = db.query(Reward).filter(Reward.reward_id == reward_id).first()
        if not db_reward:
            return None
        for key, value in reward_update.dict(exclude_unset=True).items():
            setattr(db_reward, key, value)
        db.commit()
        db.refresh(db_reward)
        return db_reward
