from models.movie import Movie as MovieModel
from schemas.movie import Movie



class MovieServices():
    def __init__(self, db) -> None:
        self.db = db


    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_movies_by_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    
    def create_movie(self, movie:Movie):
        new_movie = MovieModel(**movie.dict()):
        self.db.add(new_movie)
        self.db.commit()
        return  //// Aca quedamos ayer.