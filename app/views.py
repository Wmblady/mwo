from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .models import User

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	#w pythonie False i True pisze sie z duzej litery, klucze w slowniku musza byc w ciapkach jesli sa zwyklymi stringami inaczej szuka zmiennej
	#mockTables symuluja odpowiedz z bazy
	mockTables = [{"id": 1, "consoleType": False, "xAxis": 3, "yAxis": 4, "seats": 5, "price": 10}, {"id": 2, "consoleType": True, "xAxis": 2, "yAxis": 2, "seats": 3, "price": 12}]
	
	#to co w srodku [] buduje tablice zlozona z wartosci yAxis z kazdego stolu, potem max zwraca z tego maksymalna wartosc
	yRange = max([table["yAxis"] for table in mockTables])
	xRange = max([table["xAxis"] for table in mockTables])
	
	#na poczatku tworze calego grida
	#_ oznacza ze olewam iterator i nie przypisuje go do zadnej zmiennej
	#range(k, n) oznacza stworzenie tablicy [k, ..., n - 1]
	gridTables = [[{"isTable": False} for _ in range(0, xRange)] for _ in range(0, yRange)]
	for table in mockTables:
		#dodawanie nowego klucza w pythonie wyglada tak, ze wystarczy zrobic tab['nowy klucz']
		gridTables[table['yAxis'] - 1][table['xAxis'] - 1]['table'] = table
		gridTables[table['yAxis'] - 1][table['xAxis'] - 1]['isTable'] = True
		
	#wszystkie dane sa przekazywane w momencie renderowania templatki, jesli chcemy cos dociagnac to za pomoca flaska trzeba na nowo wyrenderowac strone z tego co wiem, na razie tak probujmy
	#jesli trzeba bedzie zmienic to cos poszukam
	return render_template('index.html', tables=gridTables)
