from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table, select
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, func

# Define the metadata
metadata = MetaData()
engine = create_engine("sqlite:///restu.db")

Base = declarative_base(metadata=metadata)

restaurant_customer = Table(
    'restaurant_customer',
    Base.metadata,
    Column('customer_id', Integer, ForeignKey('customers.id'), primary_key=True),
    Column('restaurant_id', Integer, ForeignKey('restaurants.id'), primary_key=True),
    extend_existing=True,
)

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    customers = relationship('Customer', secondary=restaurant_customer, back_populates='restaurants')

    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_reviews(self, session):
        return session.query(Review).filter(Review.restaurant_id == self.id).all()
    
    def get_customers(self, session):
       
        customer_ids = session.query(Review.customer_id).filter(Review.restaurant_id == self.id).all()
        return [session.query(Customer).get(customer_id[0]) for customer_id in customer_ids]

    @classmethod
    def fanciest(cls, session):       
        return session.query(cls).order_by(cls.price.desc()).first()       
   
   
    def __repr__(self):
        return f"Restraunt name: {self.name} {self.price} "
    
    
    def all_reviews(self, session):        
        review_strings = []
        for review in self.get_reviews(session):
            customer_full_name = review.customer(session).full_name()
            star_rating = review.rating
            review_str = f"Review for {self.name} by {customer_full_name}: {star_rating} stars."
            review_strings.append(review_str)
        return review_strings
            
        
       

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    restaurants = relationship('Restaurant', secondary=restaurant_customer, back_populates='customers')
    
    def __init__(self, first_name, last_name):
        self.first_name =first_name
        self.last_name = last_name
        
        
    def reviews(self, session):        
        return session.query(Review).filter(Review.customer_id == self.id).all()
 
    
    def get_restaurants(self, session):
        restaurant_ids = session.query(Review.restaurant_id).filter(Review.customer_id == self.id).all()
        return [session.query(Restaurant).get(restaurant_id[0]) for restaurant_id in restaurant_ids]
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def favorite(self, session):
    
        max_rating = session.query(func.max(Review.rating)).filter_by(customer_id=self.id).scalar()
        if max_rating is not None:
            favorite_review = session.query(Review).filter_by(customer_id=self.id, rating=max_rating).first()
            if favorite_review:
                return favorite_review.restaurant
        return None
    
    def add_reviews(self, rating, comments, restaurant_id, customer_id, session):
        rev= Review(rating= rating, comments=comments, restaurant_id=restaurant_id, customer_id=customer_id)
        session.add(rev)
        session.commit()
        return rev
    
    def delete_reviews(self, restaurant, session):
         session.query(Review).filter(
            (Review.customer_id == self.id) & ( Review.restaurant_id == restaurant.id)
        ).delete()
         session.commit() 


   
     
    def __repr__ (self):
        return f"Customer: {self.first_name}, {self.last_name}"
    
 

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rating =Column(Integer(), nullable=False)
    comments = Column(String())
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)

    def __init__(self, rating, comments, customer_id, restaurant_id):
        self.rating =rating
        self.comments =comments
        self.customer_id =customer_id
        self.restaurant_id = restaurant_id

    
    def customer(self, session):
        return session.query(Customer).filter_by(id=self.customer_id).first()

   
    def restaurant(self, session):
        return session.query(Restaurant).filter_by(id=self.restaurant_id).first()
    
    def full_review(self,session):        
        restaurant_name = self.restaurant(session).name  
        customer_full_name = self.customer(session).full_name() 
        star_rating = self.rating 
        review_str = f"Review for {restaurant_name} by {customer_full_name}: {star_rating} stars."
        return review_str
        
        
        

    def __repr__ (self):
        return f"Review: {self.rating}, {self.comments}, {self.customer_id},  {self.restaurant_id} "


