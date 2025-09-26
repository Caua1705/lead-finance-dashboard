from src.data.repositories.courses_repository import CoursesRepository

class CoursesServices():
    def __init__(self, repo: CoursesRepository):
        self.repo = repo

    def obter_cursos_unicos(self):
        return self.repo.get_cursos()