from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from app import db, Project

key_terms_extractor = {
    "name": "Key-Terms-Extraction",
    "description": "Attempts to identify the subject of several news articles using Python's"
                   " nltk and sklearn libraries. At the moment, it produces 5 key-terms per news articles that should"
                   " give us a feel for what the subject of the article is about.",
    "learned": [
        "Intro to NLP in Python using nltk and sklearn",
        "NLP preprocessing; tokenization, lemmatization, POS-tagging, etc.",
        "Calculating TF-IDF scores using sklearn",
    ],
    "link": "https://github.com/Peter-Walsh/Key-Terms-Extractor"
}

phone_book = {
    "name": "Phone Book",
    "description": "This project essentially just sorts and searches through a massive phone book using a variety"
                   " of basic searching and sorting algorithms as well as a hash table. The goal was for me to "
                   "reinforce what I was learning in my data structures and algorithms course, and to see Big-O in action",
    "learned": [
        "Big-O notation, and it's affect on the runtime of algorithms",
        "Implementation of hashtables (chaining method)",
        "Implementation of basic searching/sorting algorithms"
    ],
    "link": "https://github.com/Peter-Walsh/PhoneBook"
}

basic_calculator = {
    "name": "Basic Calculator",
    "description": "A simple calculator that allows you to perform the 4 basic arithmetic operations as well"
                   "as exponentiation. Also allows users to declare and use variables in their expressions.",
    "learned": [
        "Converting infix expressions to postfix expressions",
        "Simple data structures (lists, stacks, queues)",
        "Regular expressions in Python"
    ],
    "link": "https://github.com/Peter-Walsh/Calculator"
}

weather_app = {
    "name": "Weather-app",
    "description": "Simple web application that gets and displays the weather at any location in the world. You"
                   " essentially just enter the name of the location in the search bar, the locations name and a"
                   " description of the weather will pop up on the screen.",
    "learned": [
        "Flask, Flask-SQLAlchemy",
        "Experience working with an API (open weather api)",
        "Basic HTTP requests (GET, POST, DELETE, etc.)",
    ],
    "link": "https://github.com/Peter-Walsh/Weather-App"
}

# web_calender = {
#     "name": "Web-Calender",
#     "description": "Simple REST service using Flask and Flask"
#
# }


PROJECTS = [key_terms_extractor, weather_app, phone_book, basic_calculator]


def add_projects_to_database():

    for p in PROJECTS:
        project = Project(name=p['name'], description=p['description'],
                          l1=p['learned'][0], l2=p['learned'][1], l3=p['learned'][2],
                          link=p['link'])
        db.session.add(project)

    db.session.commit()


def db_test():
    db.create_all()

    name = "Key-Terms-Extractor"
    description = "In this project I took several news articles and extracted a few " \
                  "key words from each article to try and figure out what the article was about."
    l1 = "Intro to NLP in Python using nltk and sklearn"
    l2 = "NLP preprocessing; tokenization, lemmatization, POS-tagging, etc."
    l3 = ""
    l4 = ""
    l5 = ""

    link = "https://github.com/Peter-Walsh/Key-Terms-Extractor"

    # db.session.add(Project(name=name, description=description, l1=l1, l2=l2, l3=l3, l4=l4, l5=l5, link=link))
    # db.session.commit()

    display_projects()


def add_project():
    project_name = add_project_name()
    project_description = add_project_description()
    learned = add_project_learned()
    project_link = add_project_link()

    try:
        project = Project(name=project_name, description=project_description,
                          l1=learned[0], l2=learned[1], l3=learned[2], l4=learned[3], l5=learned[4],
                          link=project_link)

        db.session.add(project)
        db.session.commit()
        print("Project successfully uploaded to database!")
    except IntegrityError:
        print("Project failed to upload to database. Please check that the name of the project and the "
              "link unique!")


def add_project_name():
    project_name = input("Please enter the name of the project: ")
    return project_name.strip()


def add_project_description():
    project_description = input("Please enter a brief description of the project: ")
    return project_description.replace("\n", "").strip()


def add_project_learned():
    learned = ["", "", "", "", ""]

    run = True
    i = 0
    while i < len(learned) and run:
        next = input("Please describe something you learned. If nothing else, type, 'Done': ")
        if next.lower() == 'done':
            run = False
        else:
            learned[i] = next
        i += 1

    return learned


def add_project_link():
    project_link = input("Please enter the link to the code repository of the project: ")
    return project_link.strip()


def display_projects():
    for project in Project.query.all():
        print(project)


if __name__ == "__main__":
    db.drop_all()
    db.create_all()

    add_projects_to_database()
    display_projects()
