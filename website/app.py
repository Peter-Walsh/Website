from flask import Flask
from flask import render_template
from flask import url_for

from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(40), unique=True, nullable=False)
    description = db.Column(db.String(200))
    l1 = db.Column(db.String(100))
    l2 = db.Column(db.String(100))
    l3 = db.Column(db.String(100))
    link = db.Column(db.String(50), unique=True, nullable=False)

    def __str__(self):
        return "Project name: " + self.name + "\n" \
               "\tid: " + str(self.id) + "\n" \
               "\tdescription: " + self.description + "\n" \
               "\tl1: " + self.l1 + "\n" \
               "\tl2: " + self.l2 + "\n" \
               "\tl3: " + self.l3 + "\n" \
               "\tlink: " + self.link + "\n"


@app.route("/projects")
def index_projects():

    context = {}

    for project in Project.query.all():
        context[project.id] = {"name": project.name, "description": project.description,
        "l1": project.l1, "l2": project.l2, "l3": project.l3, "link": project.link}

    return render_template("projects.html", context=context)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
