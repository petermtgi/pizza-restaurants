from server.config import db
from sqlalchemy.orm import relationship

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = relationship('RestaurantPizza', cascade='all, delete', backref='restaurant')
