
from models.user import User
from sqlalchemy import select
from sqlalchemy.orm import Session

class UserRepo:

    def create_user(
            self, 
            session: Session, 
            username: str, 
            email: str, 
            password_hash: str) -> User:
        
        user = User(
            username=username,
            email=email,
            password_hash=password_hash
        )

        session.add(user)
        session.flush()
        return user

    def get_user_by_id(self, session: Session, user_id: int) -> User | None:
        return session.get(User, user_id)

    def get_user_by_username(self,session: Session, username: str) -> User | None:
        statement = select(User).where(User.username == username)
        return session.scalar(statement)

    def get_user_by_email(self,session: Session, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return session.scalar(statement)
