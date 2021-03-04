from models import app, db, User
from flask import jsonify, request, redirect, url_for

@app.route("/")
def home():
  return jsonify(message="Welcome to my api")

@app.route("/users", methods=["GET", "POST"])
def user_index_create():
  if request.method == "GET":
    # get all users
    users = User.query.all()
    print(type(users[0]))
    results = [user.to_dict() for user in users]
    return jsonify(results)
  if request.method == "POST":
    # create a user
    new_user = User(name=request.form["name"], email=request.form["email"], bio=request.form["bio"])
    db.session.add(new_user)
    db.session.commit()
    print(new_user)
    return jsonify(new_user.to_dict())

@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def user_show_update_delete(id):
  if request.method == "GET":
    # get a user
    user = User.query.get(id)
    if user:
      return jsonify(user.to_dict())
    else:
      return jsonify(message="There is no user here")
  if request.method == "PUT":
    # get a user
    user = User.query.get(id)
    if user:
      # update user
      for key, value in request.form.items():
        print(f"💥 {key}: {value}")
        setattr(user, key, value)
      db.session.commit()
      return jsonify(user.to_dict())
    else: 
      return jsonify(message="There is no user here")
  if request.method == "DELETE":
    # delete a user
    user = User.query.get(id)
    if user:
      db.session.delete(user)
      db.session.commit()
      return jsonify(message="successful deletion")
    else:
      return jsonify(message="no user here")

if __name__ == "__main__":
  app.run()