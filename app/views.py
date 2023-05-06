from datetime import datetime
from .models import *
from .forms import *
from flask import Flask, render_template, redirect, url_for
from . import app, db

@app.route('/<url_name>', methods=['GET', 'POST'])
def global_func(url_name):
    if url_name == "get_url":
        form = UrlForm()
        if form.is_submitted():
            form_model = Urls()
            form_model.url = form.url.data
            form_model.username = 0
            db.session.add(form_model)
            db.session.commit()
            
        return render_template("index.html", form = form)
    elif url_name == "regis":
        form = Regis()
        if form.is_submitted():
            form_model = User()
            form_model.username = form.username.data
            form_model.password = form.password.data
            form_model.email = form.email.data
            
            db.session.add(form_model)
            db.session.commit()
            
        return render_template("regis.html", form=form)
    elif url_name == "auth":
        form = Auth()
        if form.is_submitted():
            form.username = form.username.data
            form.password = form.password.data
            
            db.session.add(form)
            db.session.commit()
        return render_template("auth.html", form=form)
    else:
        return render_template("urls.html")
        
    
    
    

    
    
    