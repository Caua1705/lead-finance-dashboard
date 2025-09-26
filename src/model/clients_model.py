from src.data.db_connection import Base
from sqlalchemy import String,Integer,DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Clientes(Base):
    __tablename__ = "clientes"
    
    id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50),nullable=False)
    telefone: Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    email: Mapped[str] = mapped_column(String(50),unique=True)
    cpf: Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    perfil_cliente: Mapped[str] = mapped_column(String(50))
    cidade: Mapped[str] = mapped_column(String(50))
    data_criacao: Mapped[datetime] = mapped_column(DateTime)
    status_qualificacao: Mapped[str] = mapped_column(String(50))
    idade: Mapped[int] = mapped_column(Integer)
    forma_pagamento_preferida: Mapped[str] = mapped_column(String(50))
    etapa_atendimento: Mapped[str] = mapped_column(String(50))
    tipo_inscricao: Mapped[str] = mapped_column(String(50))
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"),nullable=False)

    curso = relationship("Cursos", backref="clientes")