from flask import Flask
from markupsafe import escape
import requests
from flask import request
from faker import Faker
import csv

fake = Faker()

app = Flask(__name__)


@app.route('/')
def hello_teacher():
    greeting = 'Hello, Yaroslav! This is my homework. Use to check:' \
               '<br>/requirements/' \
               '<br>/generate-users/<br>/mean/<br>/space/'
    return greeting


if __name__ == '__main__':
    app.run()


@app.route('/requirements/')
def show_req():
    req = ''
    with open('/home/serg/PycharmProjects/flaskProject/requirements.txt', 'r') as f:
        for l in f.readlines():
            req += l.replace('\n', '<br>')
    return req


@app.route('/generate-users/')
def generate_users():
    users = ''
    n = request.args.get('n', default=100, type=int)
    for _ in range(n):
        m = fake.name().lower().replace(' ', '<br>')
        users += m + '@mail.com <br>'
    return users


@app.route('/mean/')
def mean():
    h, w, c = 0, 0, 0
    l = []
    with open('/home/serg/Загрузки/hw.csv') as f:
        reader = csv.reader(f)
        for line in f:
            l.append([x for x in line.split()])
    del l[0]
    for i in l:
        h1 = i[1]
        h1 = h1[:-2]
        h += float(h1)
        c += 1

    for i in l:
        w1 = i[2]
        w += float(w1)

    H = round((h / c) * 2.5, 2)
    W = round((w / c) * 0.45, 2)
    return f'{H} -- средний рост \ {W} -- средний вес'


@app.route('/space/')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    r = r.json()
    q = str(r.get("number"))
    return q
