# Create by olala7846@gmail.com
# Entry point for my GAE

from flask import Flask, request, render_template
from content import index_content

app = Flask(__name__)
app.config['DEBUG'] = True
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print "index content:"
    print index_content
    return render_template('index.html', content=index_content)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
