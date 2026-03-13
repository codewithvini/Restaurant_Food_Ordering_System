"""
Configuration file for MongoDB Atlas connection
Replace the MONGO_URI with your actual MongoDB Atlas connection string
"""

# MongoDB Atlas Configuration
# Format: mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<database>?retryWrites=true&w=majority
MONGO_URI = "mongodb+srv://restaurant_user:Restaurant2026@restaurantcluster.sn4qrzm.mongodb.net/?retryWrites=true&w=majority&appName=RestaurantCluster"

# Database Name
DATABASE_NAME = "restaurant_system"

# Collection Names
MENU_COLLECTION = "menu"
ORDERS_COLLECTION = "orders"
FEEDBACK_COLLECTION = "feedback"
