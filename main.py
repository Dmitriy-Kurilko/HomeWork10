from flask import Flask
from  utils import *

app = Flask('__main__')

@app.route('/')
def print_all_candidates():
    return main_page(load_candidates())

app.run()