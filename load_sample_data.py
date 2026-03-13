"""
Script to load sample data into MongoDB Atlas
Use this to populate the database with test data
"""

from database import Database
from datetime import datetime, timedelta
import random


def load_sample_data():
    """Load sample menu items, orders, and feedback"""
    db = Database()

    print("Connecting to MongoDB Atlas...")
    success, message = db.connect()
    if not success:
        print(f"Connection failed: {message}")
        return

    print("✅ Connected successfully!")

    # Sample Menu Items
    print("\n📋 Loading sample menu items...")
    menu_items = [
        ("Margherita Pizza", "Main Course", 299, "Classic pizza with tomato sauce, mozzarella, and basil", True),
        ("Chicken Tikka", "Appetizer", 249, "Grilled chicken marinated in Indian spices", True),
        ("Pasta Alfredo", "Main Course", 329, "Creamy pasta with parmesan cheese", True),
        ("Caesar Salad", "Appetizer", 179, "Fresh romaine lettuce with Caesar dressing", True),
        ("Chocolate Lava Cake", "Dessert", 149, "Warm chocolate cake with molten center", True),
        ("Mango Lassi", "Beverage", 89, "Refreshing yogurt-based mango drink", True),
        ("French Fries", "Side Dish", 99, "Crispy golden fries", True),
        ("Paneer Butter Masala", "Main Course", 279, "Cottage cheese in rich tomato gravy", True),
        ("Ice Cream Sundae", "Dessert", 129, "Vanilla ice cream with chocolate sauce", True),
        ("Cold Coffee", "Beverage", 119, "Chilled coffee with ice cream", True),
        ("Spring Rolls", "Appetizer", 159, "Crispy vegetable rolls", True),
        ("Garlic Bread", "Side Dish", 109, "Toasted bread with garlic butter", True),
        ("Biryani", "Main Course", 349, "Aromatic rice with spices and vegetables", True),
        ("Brownie", "Dessert", 139, "Rich chocolate brownie", True),
        ("Green Tea", "Beverage", 69, "Healthy green tea", True),
    ]

    for name, category, price, description, available in menu_items:
        success, msg = db.add_menu_item(name, category, price, description, available)
        if success:
            print(f"  ✓ Added: {name}")
        else:
            print(f"  ✗ Failed to add {name}: {msg}")

    # Sample Orders
    print("\n🛒 Loading sample orders...")
    orders = [
        {
            "customer_name": "Rahul Sharma",
            "phone": "9876543210",
            "items": ["Margherita Pizza", "Cold Coffee"],
            "total_amount": 418,
            "payment_method": "UPI",
            "status": "Delivered"
        },
        {
            "customer_name": "Priya Patel",
            "phone": "9876543211",
            "items": ["Chicken Tikka", "Biryani", "Mango Lassi"],
            "total_amount": 687,
            "payment_method": "Cash",
            "status": "Pending"
        },
        {
            "customer_name": "Amit Kumar",
            "phone": "9876543212",
            "items": ["Pasta Alfredo", "Garlic Bread", "Chocolate Lava Cake"],
            "total_amount": 587,
            "payment_method": "Card",
            "status": "Preparing"
        },
        {
            "customer_name": "Sneha Reddy",
            "phone": "9876543213",
            "items": ["Caesar Salad", "Spring Rolls", "Green Tea"],
            "total_amount": 407,
            "payment_method": "Online",
            "status": "Ready"
        },
        {
            "customer_name": "Vikram Singh",
            "phone": "9876543214",
            "items": ["Paneer Butter Masala", "French Fries", "Ice Cream Sundae"],
            "total_amount": 507,
            "payment_method": "UPI",
            "status": "Delivered"
        },
    ]

    for order in orders:
        success, msg = db.create_order(
            order["customer_name"],
            order["phone"],
            order["items"],
            order["total_amount"],
            order["payment_method"]
        )
        if success:
            # Update status
            order_id = msg.split("ID: ")[1]
            db.update_order_status(order_id, order["status"])
            print(f"  ✓ Created order for: {order['customer_name']}")
        else:
            print(f"  ✗ Failed to create order: {msg}")

    # Sample Feedback
    print("\n⭐ Loading sample feedback...")
    feedback_list = [
        {
            "customer_name": "Rahul Sharma",
            "email": "rahul@example.com",
            "rating": 5,
            "comments": "Excellent food and service! The pizza was amazing."
        },
        {
            "customer_name": "Priya Patel",
            "email": "priya@example.com",
            "rating": 4,
            "comments": "Good food, but delivery took a bit longer than expected."
        },
        {
            "customer_name": "Amit Kumar",
            "email": "amit@example.com",
            "rating": 5,
            "comments": "Best pasta I've ever had! Will definitely order again."
        },
        {
            "customer_name": "Sneha Reddy",
            "email": "sneha@example.com",
            "rating": 4,
            "comments": "Fresh salad and great taste. Loved the spring rolls."
        },
        {
            "customer_name": "Ananya Gupta",
            "email": "ananya@example.com",
            "rating": 5,
            "comments": "Outstanding! The paneer butter masala was delicious."
        },
        {
            "customer_name": "Rohan Joshi",
            "email": "rohan@example.com",
            "rating": 3,
            "comments": "Food was okay, but could be better seasoned."
        },
        {
            "customer_name": "Kavya Menon",
            "email": "kavya@example.com",
            "rating": 5,
            "comments": "Amazing desserts! The lava cake was perfect."
        },
    ]

    for feedback in feedback_list:
        success, msg = db.add_feedback(
            feedback["customer_name"],
            feedback["email"],
            feedback["rating"],
            feedback["comments"]
        )
        if success:
            print(f"  ✓ Added feedback from: {feedback['customer_name']}")
        else:
            print(f"  ✗ Failed to add feedback: {msg}")

    print("\n✅ Sample data loaded successfully!")
    print("\nDatabase Statistics:")

    # Get statistics
    success, menu_items = db.get_all_menu_items()
    print(f"  - Menu Items: {len(menu_items) if success else 0}")

    success, orders = db.get_all_orders()
    print(f"  - Orders: {len(orders) if success else 0}")

    success, feedback = db.get_all_feedback()
    print(f"  - Feedback: {len(feedback) if success else 0}")

    success, stats = db.get_average_rating()
    if success and stats:
        print(f"  - Average Rating: {stats.get('average_rating', 0):.2f}/5")

    db.disconnect()
    print("\n🔌 Disconnected from MongoDB Atlas")


if __name__ == "__main__":
    print("=" * 60)
    print("Restaurant Food Ordering System - Sample Data Loader")
    print("=" * 60)
    load_sample_data()
