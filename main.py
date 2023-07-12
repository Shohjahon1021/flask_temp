from flask import Flask, render_template
from jinja2 import Template




app = Flask(__name__)

html_tem = Template('''
<html>
<head>
    <title>{{title}}</title>
</head>
<body>
    <h1>{{content}}</h1>
                    
    <a href="home">home</a>
    <a href="about">about</a>
    <a href="contact">contact</a>
    <a href="help">help</a>
</body>
</html>
''')
                    
@app.route('/home')
@app.route('/')
def home():
    title = "Home"
    content = "This is Home page"
    return render_template('home.html')

@app.route('/about')
def about():
    title = "About"
    content = "This is About page"
    return html_tem.render(title=title,content=content)

@app.route('/contact')
def contact():
    title = "Contact"
    content = "This is Contact page"
    return html_tem.render(title=title,content=content)

@app.route('/help')
def help():
    title = "Help"
    content = "This is Help page"
    return html_tem.render(title=title,content=content)

app.run(debug=True)