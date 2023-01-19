from flask import Flask, redirect, render_template
from jinja2 import Template
import sqlite3


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

conn = sqlite3.connect('comm.db')
cursor = conn.cursor()

conn.commit()

@app.route('/')
def index():
    comments = cursor.execute("SELECT * FROM comm")
    return render_template("index.html", comments=comments)