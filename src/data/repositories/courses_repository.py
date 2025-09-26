from sqlalchemy.orm import Session
from sqlalchemy import select
from src.model.courses_model import Cursos

class CoursesRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_cursos(self):
        cursos = self.db.execute(
            select(Cursos.nome)
            .distinct()
            .order_by(Cursos.nome)
            ).scalars().all()
        return cursos
    
    