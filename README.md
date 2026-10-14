# E-Commerce Backend - Django + DRF + JWT

A complete scalable E-Commerce backend built with Django Rest Framework.

### Tech Stack
- Django, Django Rest Framework
- Simple JWT for Authentication
- SQLite (can be switched to Postgres)
- Role: User, Admin

### Setup

1. Clone
```bash
git clone <repo>
cd ecommerce
```

2. Venv
```bash
python -m venv venv
source venv/bin/activate  # windows: venv\Scripts\activate
pip install django djangorestframework djangorestframework-simplejwt
```

3. Migrate & Create Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

4. Run
```bash
python manage.py runserver
```

Admin: http://127.0.0.1:8000/admin/
API: http://127.0.0.1:8000/api/

### Authentication

All protected APIs need header:
`Authorization: Bearer <access_token>`

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | /api/register/ | Signup |
| POST | /api/token/ | Login, get token |
| POST | /api/token/refresh/ | Refresh token |

### Product & Category

| Method | Endpoint | Permission | Desc |
| :--- | :--- | :--- | :--- |
| GET | /api/products/ | AllowAny | List all products |
| POST | /api/products/ | IsAuthenticated | Create (Admin) |
| GET | /api/categories/ | AllowAny | List categories |

### Cart - User Isolated

| Method | Endpoint | Desc |
| :--- | :--- | :--- |
| GET | /api/cart/ | My cart items |
| POST | /api/cart/add/ | Add to cart - Body: {"product":1,"quantity":2} |
| DELETE | /api/cart/remove/<id>/ | Remove item |

System Design: User A cannot see User B cart. `request.user` filter used. `get_or_create` for idempotent add.

### Order - Cart to Order Flow

| Method | Endpoint | Desc |
| :--- | :--- | :--- |
| POST | /api/orders/create/ | Create order from cart, cart will be cleared |
| GET | /api/orders/my/ | My order history |

Order Model:
- Order = user, total_price, is_paid, created_at
- OrderItem = order, product, quantity, price (price snapshot at order time)

### Admin Panel Features

- Category, Product, Cart, Order management
- OrderInline shows items inside order
- Product search enabled for fast selection

### Future Scope
- Payment Gateway (Razorpay/Stripe) integration with `is_paid`
- Stock decrement on order
- Order status: Pending, Shipped, Delivered

Made for Learning & Interviews.
