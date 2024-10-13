from flask import Flask, render_template, url_for, request, session, redirect


from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'ecobuddykey'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Retrieve the ECOBUDDY NAME from the form
        ecobuddy_name = request.form['ecobuddy_name']
        # Store it in the session
        session['ecobuddy_name'] = ecobuddy_name
        # Redirect to the index page
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/index')
def index():
    ecobuddy_name = session.get('ecobuddy_name', 'Your EcoBuddy')
    return render_template('index.html', ecobuddy_name=ecobuddy_name)

@app.route('/death')
def death():
    return render_template('death.html')

@app.route('/death')
def death():
    # Optionally, clear the session or perform other cleanup
    session.clear()
    return render_template('death.html')

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/input', methods=['POST'])
def input():
    if request.method == 'POST':
        # Retrieve the ECOBUDDY NAME from the form
        quest = request.form['question']
        # Store it in the session
        session['question'] = quest
        # Redirect to the index page
        return redirect(url_for('index'))
    
>>>>>>> 7479c929ca16f5a16bb49e7fae4be8fba5a84430
