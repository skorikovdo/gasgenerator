from ..database import Base


class Token(Base):
    """
    user_id - идентификатор пользователя
    refresh_token - рефреш токен
    """
    __tablename__ = "session"
