"""
Database connection and operations module
Handles MongoDB Atlas connection and CRUD operations
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
import config
from datetime import datetime


class Database:
    def __init__(self):
        """Initialize MongoDB connection"""
        self.client = None
        self.db = None
        self.menu_collection = None
        self.orders_collection = None
        self.feedback_collection = None

    def connect(self):
        """Establish connection to MongoDB Atlas"""
        try:
            self.client = MongoClient(config.MONGO_URI, serverSelectionTimeoutMS=5000)
            # Test connection
            self.client.admin.command('ping')

            # Get database and collections
            self.db = self.client[config.DATABASE_NAME]
            self.menu_collection = self.db[config.MENU_COLLECTION]
            self.orders_collection = self.db[config.ORDERS_COLLECTION]
            self.feedback_collection = self.db[config.FEEDBACK_COLLECTION]

            return True, "Connected to MongoDB Atlas successfully!"
        except (ConnectionFailure, ServerSelectionTimeoutError) as e:
            return False, f"Failed to connect to MongoDB: {str(e)}"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def disconnect(self):
        """Close MongoDB connection"""
        if self.client:
            self.client.close()

    # ============ MENU MANAGEMENT ============

    def add_menu_item(self, name, category, price, description, availability=True):
        """Add a new menu item"""
        try:
            menu_item = {
                "name": name,
                "category": category,
                "price": float(price),
                "description": description,
                "availability": availability,
                "created_at": datetime.now()
            }
            result = self.menu_collection.insert_one(menu_item)
            return True, f"Menu item added successfully with ID: {result.inserted_id}"
        except Exception as e:
            return False, f"Error adding menu item: {str(e)}"

    def get_all_menu_items(self):
        """Retrieve all menu items"""
        try:
            items = list(self.menu_collection.find())
            return True, items
        except Exception as e:
            return False, f"Error retrieving menu items: {str(e)}"

    def get_menu_item_by_id(self, item_id):
        """Retrieve a specific menu item by ID"""
        try:
            from bson.objectid import ObjectId
            item = self.menu_collection.find_one({"_id": ObjectId(item_id)})
            return True, item
        except Exception as e:
            return False, f"Error retrieving menu item: {str(e)}"

    def update_menu_item(self, item_id, name, category, price, description, availability):
        """Update an existing menu item"""
        try:
            from bson.objectid import ObjectId
            update_data = {
                "$set": {
                    "name": name,
                    "category": category,
                    "price": float(price),
                    "description": description,
                    "availability": availability,
                    "updated_at": datetime.now()
                }
            }
            result = self.menu_collection.update_one(
                {"_id": ObjectId(item_id)},
                update_data
            )
            if result.modified_count > 0:
                return True, "Menu item updated successfully!"
            else:
                return False, "No changes made or item not found."
        except Exception as e:
            return False, f"Error updating menu item: {str(e)}"

    def delete_menu_item(self, item_id):
        """Delete a menu item"""
        try:
            from bson.objectid import ObjectId
            result = self.menu_collection.delete_one({"_id": ObjectId(item_id)})
            if result.deleted_count > 0:
                return True, "Menu item deleted successfully!"
            else:
                return False, "Item not found."
        except Exception as e:
            return False, f"Error deleting menu item: {str(e)}"

    def search_menu_items(self, search_term):
        """Search menu items by name or category"""
        try:
            items = list(self.menu_collection.find({
                "$or": [
                    {"name": {"$regex": search_term, "$options": "i"}},
                    {"category": {"$regex": search_term, "$options": "i"}}
                ]
            }))
            return True, items
        except Exception as e:
            return False, f"Error searching menu items: {str(e)}"

    # ============ ORDER TRACKING ============

    def create_order(self, customer_name, phone, items, total_amount, payment_method):
        """Create a new order"""
        try:
            order = {
                "customer_name": customer_name,
                "phone": phone,
                "items": items,
                "total_amount": float(total_amount),
                "payment_method": payment_method,
                "status": "Pending",
                "order_date": datetime.now()
            }
            result = self.orders_collection.insert_one(order)
            return True, f"Order created successfully with ID: {result.inserted_id}"
        except Exception as e:
            return False, f"Error creating order: {str(e)}"

    def get_all_orders(self):
        """Retrieve all orders"""
        try:
            orders = list(self.orders_collection.find().sort("order_date", -1))
            return True, orders
        except Exception as e:
            return False, f"Error retrieving orders: {str(e)}"

    def get_order_by_id(self, order_id):
        """Retrieve a specific order by ID"""
        try:
            from bson.objectid import ObjectId
            order = self.orders_collection.find_one({"_id": ObjectId(order_id)})
            return True, order
        except Exception as e:
            return False, f"Error retrieving order: {str(e)}"

    def update_order_status(self, order_id, status):
        """Update order status"""
        try:
            from bson.objectid import ObjectId
            result = self.orders_collection.update_one(
                {"_id": ObjectId(order_id)},
                {"$set": {"status": status, "updated_at": datetime.now()}}
            )
            if result.modified_count > 0:
                return True, f"Order status updated to {status}!"
            else:
                return False, "Order not found or status unchanged."
        except Exception as e:
            return False, f"Error updating order status: {str(e)}"

    def delete_order(self, order_id):
        """Delete an order"""
        try:
            from bson.objectid import ObjectId
            result = self.orders_collection.delete_one({"_id": ObjectId(order_id)})
            if result.deleted_count > 0:
                return True, "Order deleted successfully!"
            else:
                return False, "Order not found."
        except Exception as e:
            return False, f"Error deleting order: {str(e)}"

    def search_orders(self, search_term):
        """Search orders by customer name or phone"""
        try:
            orders = list(self.orders_collection.find({
                "$or": [
                    {"customer_name": {"$regex": search_term, "$options": "i"}},
                    {"phone": {"$regex": search_term, "$options": "i"}}
                ]
            }).sort("order_date", -1))
            return True, orders
        except Exception as e:
            return False, f"Error searching orders: {str(e)}"

    # ============ CUSTOMER FEEDBACK ============

    def add_feedback(self, customer_name, email, rating, comments):
        """Add customer feedback"""
        try:
            feedback = {
                "customer_name": customer_name,
                "email": email,
                "rating": int(rating),
                "comments": comments,
                "feedback_date": datetime.now()
            }
            result = self.feedback_collection.insert_one(feedback)
            return True, f"Feedback submitted successfully with ID: {result.inserted_id}"
        except Exception as e:
            return False, f"Error submitting feedback: {str(e)}"

    def get_all_feedback(self):
        """Retrieve all feedback"""
        try:
            feedback_list = list(self.feedback_collection.find().sort("feedback_date", -1))
            return True, feedback_list
        except Exception as e:
            return False, f"Error retrieving feedback: {str(e)}"

    def get_feedback_by_id(self, feedback_id):
        """Retrieve specific feedback by ID"""
        try:
            from bson.objectid import ObjectId
            feedback = self.feedback_collection.find_one({"_id": ObjectId(feedback_id)})
            return True, feedback
        except Exception as e:
            return False, f"Error retrieving feedback: {str(e)}"

    def delete_feedback(self, feedback_id):
        """Delete feedback"""
        try:
            from bson.objectid import ObjectId
            result = self.feedback_collection.delete_one({"_id": ObjectId(feedback_id)})
            if result.deleted_count > 0:
                return True, "Feedback deleted successfully!"
            else:
                return False, "Feedback not found."
        except Exception as e:
            return False, f"Error deleting feedback: {str(e)}"

    def get_average_rating(self):
        """Get average rating from all feedback"""
        try:
            pipeline = [
                {
                    "$group": {
                        "_id": None,
                        "average_rating": {"$avg": "$rating"},
                        "total_feedback": {"$sum": 1}
                    }
                }
            ]
            result = list(self.feedback_collection.aggregate(pipeline))
            if result:
                return True, result[0]
            else:
                return True, {"average_rating": 0, "total_feedback": 0}
        except Exception as e:
            return False, f"Error calculating average rating: {str(e)}"
