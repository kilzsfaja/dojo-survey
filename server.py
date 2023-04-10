from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "123survey"

#dojo survey input page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

#results page
@app.route("/process", methods=["POST"])
def process():
    name = request.form["form_name"]
    location = request.form["form_location"]
    language = request.form["form_language"]
    comments = request.form["form_comments"]
#name conditional
    if not name:
        message = "Please provide your name to fill out survey."
        return render_template("index.html", message = message)


    session["name"] = name
    session["location"] = location
    session["language"] = language
    session["comments"] = comments
    return redirect("/result")

# process center
@app.route("/result", methods=["GET", "POST"])
def results():
    name = session["name"]
    location = session["location"]
    language = session["language"]
    comments = session["comments"]
    return render_template("result.html", name = name, location = location , language = language, comments = comments)

if __name__ == "__main__":
    app.run(debug = True)


#COME BACK AND ADD IF STATEMENT, NO NAME, NO PROCEEDING

# **********************

#   Method: GET
#   grabbing everything in a list
#   URL: make it plural ex: "/todos"
#   Function: get_all_todos()
#             get_todos()

#   Method: GET
#   grabbing ONE of a particular list
#   URL: "/todo/<int:id>"
#        "/user/<int:id>"
#   Function: get_todo_by_id(id)
#             get_todo(id)

#   Method: GET
#   Displaying a form that will eventually refer to a list
#   URL: "/todo/form"
#   Function: display_todo_form()

#   Method: POST
#   Create a new item of a list
#   URL: "/todo/add"
#        "/todo/new"
#   Function: create_todo_list()
#             add_todo()
#             new_todo()

#   Method: POST-PUT
#   Updating an existing item of a list
#   URL: "/todo/update/<int:id>"
#        "/todo/edit/<int:id>"
#   Function: update_todo(id)
#             edit_todo(id)

#   Method: POST - DELETE
#   Deleting an existing item of a list
#   URL: "/todo/remove/<int:id>"
#        "/todo/delete/<int:id>"
#   Function: remove_todo(id)
#             delete_todo(id)

# **********************