# Create by olala7846@gmail.com
# Entry point for my GAE

from flask import Flask, request, render_template
from content import index_content, RESUME_DATA
import markdown as md

app = Flask(__name__)
app.config['DEBUG'] = True
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html', content=index_content)


@app.route('/blog')
def blog():
    """Simple blog entry test page"""
    return render_template('blog.html', content=RESUME_DATA)


@app.route('/markdown')
def markdown():
    """Test markdown"""
    return md.markdown("```var 2+3;```")


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
