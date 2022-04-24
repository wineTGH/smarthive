from app import app

#Возращение средних значений данных со всех ульев
@app.route("/api/v1/hive/state", methods=['GET'])
def states():
    return 'state all'

# Возвращение значений данных с конкретного улья
@app.route("/api/v1/hive/state/<int:index>", methods=['GET'])
def state(index: int):
    return f'state {index}'