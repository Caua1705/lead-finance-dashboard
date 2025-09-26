from src.data.db_connection import Base
from sqlalchemy import String,Integer,DateTime,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Mensagens(Base):
    __tablename__ = "mensagens"
    
    id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    conteudo:Mapped[str] = mapped_column(String(200))
    data_envio:Mapped[DateTime] = mapped_column(DateTime)
    cliente_id:Mapped[int] = mapped_column(ForeignKey("clientes.id"),nullable=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"),nullable=False)


    cliente = relationship("Clientes",backref="mensagens")
    curso = relationship("Cursos", backref="mensagens")