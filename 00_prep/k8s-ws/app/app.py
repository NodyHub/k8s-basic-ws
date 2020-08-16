from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get DB connection string
    DB_CON_STRING = os.getenv('DB_CON_STRING')

    # Create directory listing
    LIST_DIR = os.getenv('LIST_DIR')
    dir_listing = "\n".join([ "%s/%s" % (LIST_DIR, x) for x in os.listdir(LIST_DIR)])
    
    return 'DB connection string: %s\nDirectory listing for "%s":\n%s' % (DB_CON_STRING, LIST_DIR, dir_listing)
