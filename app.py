from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/eduskills')
def education():
    return render_template('eduskills.html')

@app.route('/projects')
def project():
    return render_template('projects.html')

@app.route('/contact')
def conact():
    return render_template('contact.html')


if __name__ == '__main__':  
    app.run(debug=True)