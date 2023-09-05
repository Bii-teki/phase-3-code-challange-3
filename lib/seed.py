from faker import Faker
import random
from faker import Faker  # Import the Faker class

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import Base, Restaurant, Customer, Review

if __name__ == "__main__":
    engine = create_engine("sqlite:///restu.db")
    # Create the tables in the database
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.query(Review).delete()

    fake = Faker()  # Create an instance of the Faker class



# generate fake restaurant
restaurants =[]
for i in range(25):
    restaurant = Restaurant(name=fake.company(), price=random.randint(10, 50))
    session.add(restaurant)
    session.commit()
    restaurants.append(restaurant)

# creating customers
customers = []
for i in range(25):
    customer = Customer(first_name=fake.first_name(), last_name=fake.last_name())

    session.add(customer)
    session.commit()
    customers.append(customer)

# create reviews
reviews = []
for customer in customers:
    review = Review(
        rating= random.randint(0,5),
        comments= fake.paragraph(nb_sentences=3),
        customer_id=customer.id,
        restaurant_id=restaurants[random.randint(0, len(restaurants)-1)].id
    )
    
    session.add(review)
    session.commit()
    
    reviews.append(review)


# Retrieve a specific review
review = session.query(Review).filter_by(id=1).first()

if review is not None:
    # Get the associated Customer and Restaurant instances
    customer_instance = review.customer(session)
    restaurant_instance = review.restaurant(session)

    # Commit the changes to the database
    session.commit()
else:
    # Handle the case where the review does not exist
    print("Review with ID 1 does not exist.")
session.commit()


restaurant = session.query(Restaurant).filter_by(id=1).first()
if restaurant is not None:
    restaurant_reviews = restaurant.get_reviews(session)
    restaurant_customers = restaurant.get_customers(session)
    # print(restaurant_customers)
    # print (restaurant_reviews)
    
else:
    print("Restaurant with ID 1 does not exist.")
session.commit()

customer = session.query(Customer).filter_by(id=5).first()
if customer is not None:
    custom = customer.reviews(session)
    restaurants_reviewed = customer.get_restaurants(session)
    print(custom)
    print(restaurants_reviewed)
else:
    print("No customer found")
    
    
customer = session.query(Customer).filter_by(id=1).first()  
if customer is not None:
    cust = customer.full_name()
    print(cust)
else:
    print("No Customer found")    



customer = session.query(Customer).filter_by(id=1).first()

if customer:
    favorite_restaurant = customer.favorite(session)
    if favorite_restaurant:
        print(f"{customer.full_name()} has a favorite restaurant:")       
    else:
        print(f"{customer.full_name()} has no favorite restaurant.")
else:
    print("Customer not found.")



new_customer = Customer(first_name='Peters', last_name='Williams')
session.add(new_customer)
session.commit()
new_review = new_customer.add_reviews(5, "Mambo freshii" , 4, new_customer.id, session)
session.commit()
print(new_review)




customer = session.get(Customer, 12)
restaurant = session.get(Restaurant, 8)
customer.delete_reviews(restaurant, session)
session.commit()


# review = Review(
#     rating=5,  # Replace with the actual rating
#     comments="Mambo ni matatu",  # Replace with the actual comments
#     restaurant_id=6,  # Replace with the associated restaurant
#     customer_id=4  # Replace with the associated customer
# )
# formatted_review = review.full_review()
# print(formatted_review)


fanciest = Restaurant.fanciest(session)
if fanciest:
    print(f"The fanciest restaurant is {fanciest.name} with a price of {fanciest.price}")
else:
    print("No restaurants found.")
    

restaurant = session.query(Restaurant).get(5)  
reviews = restaurant.all_reviews()
for review in reviews:
    print(review)    