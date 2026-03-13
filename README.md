# EasyBuy - E-Commerce Platform

A full-featured e-commerce platform built with Django 5.2, featuring multi-vendor support, user authentication, shopping cart, checkout process, and admin management.

## 🚀 Features

### For Customers
- **User Authentication**: Register, Login, OTP verification
- **Product Browsing**: Browse by category, subcategory, brand, price range
- **Product Details**: View product variants, images, prices, stock status
- **Shopping Cart**: Add/remove items, update quantities
- **Checkout**: Address selection, payment method, order confirmation
- **Order Management**: View orders, cancel orders
- **Wishlist**: Save favorite products

### For Sellers
- **Seller Registration**: Apply to become a seller
- **Product Management**: Add products with variants, images, pricing
- **Inventory Management**: Track stock quantities
- **Order Management**: View and manage orders

### For Admins
- **Category Management**: Create and manage categories/subcategories
- **Seller Approval**: Approve or reject seller applications
- **Product Approval**: Approve or reject seller products
- **User Management**: View and manage users

## 📁 Project Structure

```
BESTBUY/
├── easybuy/
│   ├── core/              # Core app - users, categories, addresses
│   │   ├── models.py     # User, Address, Category, SubCategory, etc.
│   │   ├── views.py      # Authentication, category views
│   │   ├── urls.py       # Core URL patterns
│   │   └── decorators.py # Role-based access control
│   │
│   ├── user/             # Customer app - shopping, orders
│   │   ├── models.py     # Cart, Order, OrderItem
│   │   ├── views.py      # Product views, cart, checkout
│   │   └── urls.py       # User URL patterns
│   │
│   ├── seller/           # Seller app - products, inventory
│   │   ├── models.py     # Product, ProductVariant, ProductImage
│   │   ├── views.py      # Seller dashboard, product management
│   │   ├── forms.py     # Product forms
│   │   └── urls.py       # Seller URL patterns
│   │
│   ├── easybuy_admin/    # Admin app
│   │   ├── views.py      # Admin dashboard, approvals
│   │   └── urls.py       # Admin URL patterns
│   │
│   └── templates/        # HTML templates
│       ├── core/         # Base templates, home, categories
│       ├── user/         # User-facing templates
│       ├── seller/       # Seller dashboard templates
│       ├── admin/        # Admin panel templates
│       └── includes/     # Reusable components
│
├── images/               # Media files (product images, profiles)
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## 🛠️ Tech Stack

- **Backend**: Django 5.2 (Python)
- **Database**: SQLite3
- **Frontend**: HTML, CSS (Tailwind), JavaScript
- **Authentication**: Django Auth with OTP verification
- **Email**: SMTP Gmail

## ⚙️ Installation

### Prerequisites
- Python 3.10+
- Django 5.2

### Setup

1. **Clone the repository**
   ```bash
   cd BESTBUY/project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📱 User Roles

| Role | Description | Access |
|------|-------------|--------|
| CUSTOMER | Regular buyers | Browse, Cart, Checkout, Orders |
| SELLER | Product vendors | Dashboard, Products, Orders |
| ADMIN | Platform admins | Full control |

## 🛒 Shopping Flow

1. **Browse Products** → Home, Categories, Search
2. **View Product** → Select variant, Add to Cart
3. **Cart** → Update quantities, Remove items
4. **Checkout** → Select address, Payment method
5. **Order** → View in "My Orders"

## 📄 API Endpoints

### User URLs
| Endpoint | Description |
|----------|-------------|
| `/user/products/<slug>/` | Product detail |
| `/user/new_arrivals/` | New arrivals |
| `/user/category/<slug>/` | Category products |
| `/user/cart/` | Shopping cart |
| `/user/checkout/` | Checkout page |
| `/user/orders/` | User orders |
| `/user/addtocart/<id>/` | Add to cart (AJAX) |
| `/user/buy_now/<id>/` | Buy now |

### Seller URLs
| Endpoint | Description |
|----------|-------------|
| `/seller/dashboard/` | Seller dashboard |
| `/seller/add_product/` | Add new product |
| `/seller/inventory/` | Product inventory |
| `/seller/orders/` | Seller orders |

### Admin URLs
| Endpoint | Description |
|----------|-------------|
| `/admin/dashboard/` | Admin dashboard |
| `/admin/all_sellers/` | All sellers |
| `/admin/approve_product/<id>/` | Approve product |
| `/admin/reject_product/<id>/` | Reject product |

## 🔧 Management Commands

```bash
# Add product images
python manage.py add_product_images

# Download product images
python manage.py download_product_images
```

## 📦 Key Models

### Core App
- **User**: Custom user with roles (ADMIN, SELLER, CUSTOMER)
- **Address**: User delivery addresses
- **Category/SubCategory**: Product categories
- **Otp**: OTP verification

### Seller App
- **SellerProfile**: Seller information and status
- **Product**: Products with approval system
- **ProductVariant**: Product variants (size, color, etc.)
- **ProductImage**: Product images

### User App
- **Cart/CartItem**: Shopping cart
- **Order/OrderItem**: Customer orders

## 🎨 Templates

The project uses Tailwind CSS for styling with:
- Responsive design (mobile, tablet, desktop)
- Dark mode support
- Custom color scheme (primary green, terracotta accent)

## 📝 Configuration

Key settings in `settings.py`:
- **DEBUG**: Development mode
- **ALLOWED_HOSTS**: Host whitelist
- **MEDIA_ROOT**: Image storage location
- **Email**: SMTP configuration for Gmail

## 🔐 Security

- Role-based access control via decorators
- CSRF protection
- Password validation
- Email OTP verification

## 📄 License

This project is for educational purposes.

## 👥 Credits

Built with Django, Tailwind CSS, and Material Symbols.

ADMIN:

Username: admin

Password: admin123

SELLERS:

Username: seller1, seller2, seller3

Password: seller123

CUSTOMERS:

Username: customer1, customer2

Password: customer123