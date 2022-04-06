from .movie import MovieApi, MoviesApi
from .user import UserApi, UsersApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(MoviesApi, '/movies')
    api.add_resource(MovieApi, '/movies/<id>')
    
    api.add_resource(UsersApi, '/users')
    api.add_resource(UserApi, '/users/<id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')