from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password = db.Column(db.String(100), index=True)
	
	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.username)
		
class Order(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	userNick = db.Column(db.String(64))
	numberStation = db.Column(db.Integer, db.ForeignKey('station.id'))
	idGame = db.Column(db.Integer, db.ForeignKey('game.id'))
	dateOrder = db.Column(db.Date)
	orderFrom = db.Column(db.Date)
	orderTo = db.Column(db.Date)
	price = db.Column(db.Float)
	numberStationRel = db.relationship('Station', back_populates='station')
	idGameRel = db.relationship('Game', back_populates='game')
	
class Station(db.Model):
	id = db.Column(db.Integer, primary_key=True) 
	stationType = db.Column(db.String(15))
	coordX = db.Column(db.Integer)
	coordY = db.Column(db.Integer)
	numberOfSeats = db.Column(db.Integer)
	pricePerHour = db.Column(db.Float)
	station = db.relationship('Order',back_populates='numberStationRel')
	
class Game(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	gameType = db.Column(db.String(15))
	gameName = db.Column(db.String(60))
	gamePrice = db.Column(db.Float)
	game= db.relationship('Order', back_populates='idGameRel')
	
class Bar(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(20))
	name = db.Column(db.String(60))
	pricePerUnit = db.Column(db.Float)
	
class Admin(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password = db.Column(db.String(100), index=True)
	