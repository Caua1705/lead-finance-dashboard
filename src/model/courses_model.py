from src.data.db_connection import Base
from sqlalchemy import String,Integer,DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Cursos(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50),nullable=False)
    cidade:  Mapped[str] = mapped_column(String(50))
    data_inicio:  Mapped[datetime] = mapped_column(DateTime,nullable=False)
    data_fim:  Mapped[datetime] = mapped_column(DateTime,nullable=False)