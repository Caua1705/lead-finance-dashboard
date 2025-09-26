from src.data.db_connection import Base
from sqlalchemy import String,Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB

class HistoricoIA(Base):
    __tablename__ = "historico_ia_principal"
    
    id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    session_id:Mapped[str] = mapped_column(String(50))
    message: Mapped[dict] = mapped_column(JSONB, nullable=False)
    cliente_id:Mapped[int] = mapped_column(ForeignKey("clientes.id"),nullable=True)

    cliente = relationship("Clientes",backref="historico_ia_principal")