---

# Django Shop Project

This project is developed to create an online store using Django.

## Description

The project consists of several main applications:

### Products

#### Views

- `IndexView`: Displays the main page of the store.
- `ProductsListView`: Displays a list of products with pagination and the ability to filter by categories.
- `add_basket`: Adds a product to the user's basket.
- `delete_basket`: Removes a product from the user's basket.

#### Models

- `Products`: Model to store information about products.
- `ProductsCategory`: Model to store product categories.
- `Basket`: Model to store items in users' baskets.

### Users

#### Views

- `UserLoginView`: View for user login.
- `UserRegistrationView`: View for user registration.
- `UserProfileView`: View for updating user profiles.
- `EmailVerificationView`: View for email verification for users.

#### Models

- `User`: Django built-in model to store user information.
- `EmailVerification`: Model to store information about email verification for users.

### Orders

#### Views

- `OrderSuccessView`: View for successful order payment.
- `OrderCancelView`: View for canceled order payment.
- `OrderCreateView`: View for creating orders.
- `OrdersDetailsView`: View for displaying order details.

#### Models

- `OrderForm`: Form for creating orders.

### API

#### ViewSets

- `ProductModelViewSet`: ViewSet for managing products (CRUD operations).
- `BasketModelViewSet`: ViewSet for managing the basket (accessible only for authenticated users).

## Dependencies

The project is developed using Django and has dependencies on third-party libraries such as:

- Django
- Django Rest Framework

## Running the Project

1. Ensure that you have Python and Django installed.
2. Clone the project repository: `git clone https://github.com/BalakaMd/online-store`
3. Install dependencies by running: `pip install -r requirements.txt`.
4. Apply migrations: `python manage.py migrate`.
5. Run the server: `python manage.py runserver`.

## Access

- Main store page: `/products/`
- Administrator page: `/admin/`

## User Authentication

Users can authenticate via GitHub using OAuth.

## API Endpoints

- `/api/products/`: Endpoint for managing products.
- `/api/basket/`: Endpoint for managing the basket.

---
