from pydantic import BaseSettings


class Settings(BaseSettings):
    JWT_SECRET_KEY: str = 'a9d1df2ce17f60a1cbddf52c964c80695f77202b646af1cb0d70a5124944d48c6160d4c163aedc82873015ab887de7a7c3882c71e5296b380b7fbf4fa99b232d'  # 반드시 강력한 키로 변경하세요.


settings = Settings()
