

# SQLAlchemy Migrations and Object Relationships Project
## Introduction

This project focuses on working with SQLAlchemy, a popular Object Relational Mapping (ORM) library for Python. We will perform database schema migrations, define object relationships, and implement various methods to interact with our models, including classes like Restaurant, Customer, and Review. This README will guide you through the tasks and deliverables.
Prerequisites

Before diving into the project, ensure you have the following in place:

   ### SQLAlchemy installed.
    Initial Restaurant and Customer models, database tables, and sample data.
    A reviews table created via migration, including columns to establish relationships with Restaurant and Customer, as well as a star_rating column to store review ratings.

## Migration

    Create a migration for the reviews table with the necessary columns to establish relationships with Restaurant and Customer. Include a star_rating column to store review ratings.

### Object Relationship Methods
#### Review Class

    customer(): Returns the Customer instance associated with this review.
    restaurant(): Returns the Restaurant instance associated with this review.

#### Restaurant Class

    reviews(): Returns a collection of all the reviews for the restaurant.
    customers(): Returns a collection of all the customers who reviewed the restaurant.

#### Customer Class

    reviews(): Returns a collection of all the reviews that the customer has left.
    restaurants(): Returns a collection of all the restaurants that the customer has reviewed.

## Aggregate and Relationship Methods
#### Customer Class

    full_name(): Returns the full name of the customer, with the first name and last name concatenated.
    favorite_restaurant(): Returns the restaurant instance with the highest star rating from this customer.
    add_review(restaurant, rating): Creates a new review for the specified restaurant with the given rating.
    delete_reviews(restaurant): Removes all reviews by the customer for a specific restaurant.

#### Review Class

    full_review(): Returns a formatted review string, e.g., "Review for {restaurant name} by {customer's full name}: {review star_rating} stars."

#### Restaurant Class

    fanciest(): Returns one restaurant instance with the highest price.
    all_reviews(): Returns a list of strings with all the reviews for this restaurant, formatted as specified.

## Usage

    Create database tables and initial data using migrations and the seeds.py file.
    Implement methods and test them in the console using sample data.
    Follow the suggested order of tasks, but feel free to adapt based on your preference.
    Ensure methods work as expected and test thoroughly before proceeding.
    Refactor code for clean and maintainable organization.

This project does not include automated tests, so manual testing in the console is crucial. Prioritize functionality over clean code initially, and refactor for best practices once everything works.
License

This project is open-source and available under the MIT License.
