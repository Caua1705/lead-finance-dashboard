from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from src.config.ui_config import URL_SUPABASE

class Base(DeclarativeBase):
    pass

engine = create_engine(
    URL_SUPABASE,
    connect_args={"sslmode": "require"}  
)

Sessionlocal = sessionmaker(engine, autoflush=False)