from app import app

@app.route("/api/v1/test")
def test():
    return 'test'