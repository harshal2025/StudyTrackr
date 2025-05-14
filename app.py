from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'you-dont-know-my-secret'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/subjects')
def subjects():
    subjects = ["Physics", "Chemistry", "Maths"]
    return render_template('subjects.html', subjects = subjects)

@app.route('/track', methods = ['GET', 'POST'])
def track():
    if request.method == 'POST':
        physics = float(request.form.get('physics', 0))
        chemistry = float(request.form.get('chemistry', 0))
        maths = float(request.form.get('maths', 0))
        total = physics + chemistry + maths

        session['total'] = total
        flash("Well done! Keep it up 🧠🔥", "success")
        return redirect(url_for('track'))
    
    total = session.get('total', None)
    return render_template('track.html', total = total)

if __name__ == '__main__':
    app.run(debug=True)