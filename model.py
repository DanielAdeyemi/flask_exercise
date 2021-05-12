import json

def load_db():
  with open("app_db.json") as f:
    return json.load(f)

def save_db():
  with open("app_db.json", "w") as f:
    return json.dump(db,f)

db = load_db()
