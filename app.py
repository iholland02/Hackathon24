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

if __name__ == "__main__":
    app.run(debug=True)
