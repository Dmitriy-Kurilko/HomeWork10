from flask import Flask
from utils import *

app = Flask(__name__)


@app.route('/')
def print_all_candidates():
    return main_page(load_candidates())


@app.route('/candidates/<int:pk>')
def print_candidate_by_pk(pk):
    return f'<img src="({get_by_pk(pk)["picture"]})">\n{main_page(load_candidates()[pk-1])}'


@app.route('/skills/<skill>')
def print_candidates_by_skill(skill):
    return main_page(get_by_skill(skill))

app.run()
