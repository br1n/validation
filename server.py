from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'henlobilo'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit')
def submit():
    return render_template('submit.html')
    

@app.route('/process', methods=['POST'])
def process():
    #name and comments must not be blank
    #name must be longer than 3 characters
    #comments must be longer than 10 characters
    
    form = request.form 
    #actually just a dictionary
    #this allows us to clean our code up and shorten 
    errors = []

    if len(form['name']) < 3:
        errors.append('Name must be at least 3 charaters long')
        

    if len(form['comment']) < 10:
        errors.append('Comment must be longer than 10 characters long')
        
    if len(errors) > 0:
        for error in errors:
            flash(error) #import flash via. flask - init flash html layout (see flask doc.)
        return redirect('/')
    
    else:
        session['name'] = form['name']
        session['location'] = form['location']
        session['language'] = form['language']
        session['comment'] = form['comment']
        session['form'] = request.form
        return redirect('/submit')


app.run(debug=True)

