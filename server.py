from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from auth.auth import require_auth, validator

from db.config import test_connect

from api.crypto_blueprint import crypto_blueprint
from api.cyber_blueprint import cyber_blueprint
from api.econ_blueprint import econ_blueprint
from api.scythe_blueprint import scythe_blueprint
from yminer.service import yminer_service

from ynosisPoem import ping as yeet

# Initialize flask API, db connection, rate limiting 
app = Flask(__name__)
limiter = Limiter(
  key_func=get_remote_address
)
limiter.limit("10/minute")(crypto_blueprint)
limiter.limit("10/minute")(cyber_blueprint)
limiter.limit("10/minute")(econ_blueprint)
limiter.limit("10/minute")(scythe_blueprint)
app.register_blueprint(crypto_blueprint)
app.register_blueprint(cyber_blueprint)
app.register_blueprint(econ_blueprint)
app.register_blueprint(scythe_blueprint)

# TODO: finalize ynosis api authentication and authorization
#require_auth.register_token_validator(validator)

# test database connections 
test_connect()
yminer_service()

@app.route('/yeet')
def ping():
    return yeet, 200
    

if __name__ == "__main__":
    app.run()
    
    
    
