import json


def load_candidates():
    with open('candidates.json') as file:
        data = json.load(file)
    return data


def main_page():
    res = ""
    for i in load_candidates():
        res += f'''
        Имя кандидата - {i['name']}
        Позиция кандидата - {i['position']}
        Навыки - {i['skills']}
'''
    return f'<pre>{res}</pre>'


def get_by_pk(pk):
    return [i for i in load_candidates() if pk == i['pk']]


def get_by_skill(skill_name):
    return [i for i in load_candidates() if skill_name.lower() in i['skills'].lower()]
