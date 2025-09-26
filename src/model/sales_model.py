from src.data.db_connection import Base
from sqlalchemy import String, Integer, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Vendas(Base):
    __tablename__ = "vendas"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id"), nullable=False)
    
    valor_total: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    forma_pagamento: Mapped[str] = mapped_column(String(20), nullable=False)
    parcelas: Mapped[int] = mapped_column(Integer)
    data_venda: Mapped[datetime] = mapped_column(DateTime)
    responsavel_venda: Mapped[str] = mapped_column(String(100), nullable=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"),nullable=False)


    cliente = relationship("Clientes", backref="vendas")
    curso = relationship("Cursos", backref="vendas")
