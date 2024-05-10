from flask import Flask, render_template, redirect, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session


@app.route("/")
def main():
    return redirect('index', 301)

app.run('127.0.0.1', 3000)  
