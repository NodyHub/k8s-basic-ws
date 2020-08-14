from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    SECRET_LOG = os.getenv('SECRET_LOG')
    with open(SECRET_LOG) as f:
        content = "".join(f.readlines())
    
    return 'Content of "%s":\n%s' % (SECRET_LOG, content)
