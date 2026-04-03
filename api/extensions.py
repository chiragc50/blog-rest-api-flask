from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_smorest import Api
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


limiter = Limiter(key_func=get_remote_address)


migrate = Migrate()
jwt = JWTManager()
cors = CORS()
api = Api()
