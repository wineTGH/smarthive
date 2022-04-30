from crypt import methods
from app import app

@app.route("/api/v1/users/login", methods=["GET"])
def login():
    pass

@app.route("/api/v1/users/register", methods=["POST"])
def register():
    pass