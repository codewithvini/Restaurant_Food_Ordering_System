# MongoDB Queries Reference
## Restaurant Food Ordering System

This document contains all MongoDB queries used in the application with examples and screenshots.

---

## Connection to MongoDB Atlas

### Python Code
```python
from pymongo import MongoClient

# Connection string
MONGO_URI = "mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"

# Create client
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

# Test connection
client.admin.command('ping')

# Get database
db = client['restaurant_system']

# Get collections
menu_collection = db['menu']
orders_collection = db['orders']
feedback_collection = db['feedback']
```

---

## 1. MENU MANAGEMENT QUERIES

### INSERT - Add Menu Item

**Python Code:**
```python
from datetime import datetime

menu_item = {
    "name": "Margherita Pizza",
    "category": "Main Course",
    "price": 299.0,
    "description": "Classic pizza with tomato sauce, mozzarella, and basil",
    "availability": True,
    "created_at": datetime.now()
}

result = menu_collection.insert_one(menu_item)
print(f"Inserted ID: {result.inserted_id}")
```

**MongoDB Shell Equivalent:**
```javascript
db.menu.insertOne({
    name: "Margherita Pizza",
    category: "Main Course",
    price: 299.0,
    description: "Classic pizza with tomato sauce, mozzarella, and basil",
    availability: true,
    created_at: new Date()
})
```

**Expected Output:**
```
Inserted ID: 65f1234567890abcdef12345
```

---

### SELECT - View All Menu Items

**Python Code:**
```python
# Get all menu items
items = list(menu_collection.find())

for item in items:
    print(f"ID: {item['_id']}")
    print(f"Name: {item['name']}")
    print(f"Category: {item['category']}")
    print(f"Price: ₹{item['price']}")
    print(f"Available: {item['availability']}")
    print("-" * 50)
```

**MongoDB Shell Equivalent:**
```javascript
db.menu.find()
```

**Sample Output:**
```
ID: 65f1234567890abcdef12345
Name: Margherita Pizza
Category: Main Course
Price: ₹299.0
Available: True
--------------------------------------------------
ID: 65f1234567890abcdef12346
Name: Chicken Tikka
Category: Appetizer
Price: ₹249.0
Available: True
--------------------------------------------------
```

---

### SELECT - Find Specific Menu Item

**Python Code:**
```python
from bson.objectid import ObjectId

# Find by ID
item_id = "65f1234567890abcdef12345"
item = menu_collection.find_one({"_id": ObjectId(item_id)})

print(f"Found: {item['name']}")
print(f"Price: ₹{item['price']}")
```

**MongoDB Shell Equivalent:**
```javascript
db.menu.findOne({_id: ObjectId("65f1234567890abcdef12345")})
```

---

### UPDATE - Update Menu Item

**Python Code:**
```python
from bson.objectid import ObjectId
from datetime import datetime

item_id = "65f1234567890abcdef12345"

update_data = {
    "$set": {
        "price": 349.0,
        "description": "Updated description - Premium pizza",
        "updated_at": datetime.now()
    }
}

result = menu_collection.update_one(
    {"_id": ObjectId(item_id)},
    update_data
)

print(f"Modified count: {result.modified_count}")
```

**MongoDB Shell Equivalent:**
```javascript
db.menu.updateOne(
    {_id: ObjectId("65f1234567890abcdef12345")},
    {
        $set: {
            price: 349.0,
            description: "Updated description - Premium pizza",
            updated_at: new Date()
        }
    }
)
```

**Output:**
```
Modified count: 1
```

---

### DELETE - Remove Menu Item

**Python Code:**
```python
from bson.objectid import ObjectId

item_id = "65f1234567890abcdef12345"

result = menu_collection.delete_one({"_id": ObjectId(item_id)})

print(f"Deleted count: {result.deleted_count}")
```

**MongoDB Shell Equivalent:**
```javascript
db.menu.deleteOne({_id: ObjectId("65f1234567890abcdef12345")})
```

**Output:**
```
Deleted count: 1
```

---

### SEARCH - Find Menu Items by Name or Category

**Python Code:**
```python
search_term = "pizza"

items = list(menu_collection.find({
    "$or": [
        {"name": {"$regex": search_term, "$options": "i"}},
        {"category": {"$regex": search_term, "$options": "i"}}
    ]
}))

print(f"Found {len(items)} items matching '{search_term}'")
for item in items:
    print(f"- {item['name']} ({item['category']})")
```

**MongoDB Shell Equivalent:**
```javascript
db.menu.find({
    $or: [
        {name: {$regex: "pizza", $options: "i"}},
        {category: {$regex: "pizza", $options: "i"}}
    ]
})
```

**Output:**
```
Found 2 items matching 'pizza'
- Margherita Pizza (Main Course)
- Pepperoni Pizza (Main Course)
```

---

### FILTER - Get Available Items Only

**Python Code:**
```python
available_items = list(menu_collection.find({"availability": True}))

print(f"Available items: {len(available_items)}")
```

**MongoDB Shell Equivalent:**
```javascript
db.menu.find({availability: true})
```

---

### SORT - Get Menu Items by Price

**Python Code:**
```python
# Sort by price ascending
items = list(menu_collection.find().sort("price", 1))

# Sort by price descending
items = list(menu_collection.find().sort("price", -1))

for item in items:
    print(f"{item['name']}: ₹{item['price']}")
```

**MongoDB Shell Equivalent:**
```javascript
// Ascending
db.menu.find().sort({price: 1})

// Descending
db.menu.find().sort({price: -1})
```

---

## 2. ORDER TRACKING QUERIES

### INSERT - Create Order

**Python Code:**
```python
from datetime import datetime

order = {
    "customer_name": "Rahul Sharma",
    "phone": "9876543210",
    "items": ["Margherita Pizza", "Cold Coffee"],
    "total_amount": 418.0,
    "payment_method": "UPI",
    "status": "Pending",
    "order_date": datetime.now()
}

result = orders_collection.insert_one(order)
print(f"Order created with ID: {result.inserted_id}")
```

**MongoDB Shell Equivalent:**
```javascript
db.orders.insertOne({
    customer_name: "Rahul Sharma",
    phone: "9876543210",
    items: ["Margherita Pizza", "Cold Coffee"],
    total_amount: 418.0,
    payment_method: "UPI",
    status: "Pending",
    order_date: new Date()
})
```

---

### SELECT - View All Orders

**Python Code:**
```python
# Get all orders sorted by date (newest first)
orders = list(orders_collection.find().sort("order_date", -1))

for order in orders:
    print(f"Order ID: {order['_id']}")
    print(f"Customer: {order['customer_name']}")
    print(f"Phone: {order['phone']}")
    print(f"Total: ₹{order['total_amount']}")
    print(f"Status: {order['status']}")
    print(f"Date: {order['order_date']}")
    print("-" * 50)
```

**MongoDB Shell Equivalent:**
```javascript
db.orders.find().sort({order_date: -1})
```

---

### UPDATE - Update Order Status

**Python Code:**
```python
from bson.objectid import ObjectId
from datetime import datetime

order_id = "65f1234567890abcdef12346"
new_status = "Delivered"

result = orders_collection.update_one(
    {"_id": ObjectId(order_id)},
    {
        "$set": {
            "status": new_status,
            "updated_at": datetime.now()
        }
    }
)

print(f"Order status updated to: {new_status}")
```

**MongoDB Shell Equivalent:**
```javascript
db.orders.updateOne(
    {_id: ObjectId("65f1234567890abcdef12346")},
    {
        $set: {
            status: "Delivered",
            updated_at: new Date()
        }
    }
)
```

---

### DELETE - Remove Order

**Python Code:**
```python
from bson.objectid import ObjectId

order_id = "65f1234567890abcdef12346"

result = orders_collection.delete_one({"_id": ObjectId(order_id)})
print(f"Deleted {result.deleted_count} order(s)")
```

**MongoDB Shell Equivalent:**
```javascript
db.orders.deleteOne({_id: ObjectId("65f1234567890abcdef12346")})
```

---

### SEARCH - Find Orders by Customer

**Python Code:**
```python
search_term = "Rahul"

orders = list(orders_collection.find({
    "$or": [
        {"customer_name": {"$regex": search_term, "$options": "i"}},
        {"phone": {"$regex": search_term, "$options": "i"}}
    ]
}).sort("order_date", -1))

print(f"Found {len(orders)} order(s) for '{search_term}'")
for order in orders:
    print(f"- {order['customer_name']} - ₹{order['total_amount']} - {order['status']}")
```

**MongoDB Shell Equivalent:**
```javascript
db.orders.find({
    $or: [
        {customer_name: {$regex: "Rahul", $options: "i"}},
        {phone: {$regex: "Rahul", $options: "i"}}
    ]
}).sort({order_date: -1})
```

---

### FILTER - Get Orders by Status

**Python Code:**
```python
status = "Pending"

orders = list(orders_collection.find({"status": status}))

print(f"Orders with status '{status}': {len(orders)}")
```

**MongoDB Shell Equivalent:**
```javascript
db.orders.find({status: "Pending"})
```

---

## 3. CUSTOMER FEEDBACK QUERIES

### INSERT - Submit Feedback

**Python Code:**
```python
from datetime import datetime

feedback = {
    "customer_name": "Priya Patel",
    "email": "priya@example.com",
    "rating": 5,
    "comments": "Excellent food and service! The pizza was amazing.",
    "feedback_date": datetime.now()
}

result = feedback_collection.insert_one(feedback)
print(f"Feedback submitted with ID: {result.inserted_id}")
```

**MongoDB Shell Equivalent:**
```javascript
db.feedback.insertOne({
    customer_name: "Priya Patel",
    email: "priya@example.com",
    rating: 5,
    comments: "Excellent food and service! The pizza was amazing.",
    feedback_date: new Date()
})
```

---

### SELECT - View All Feedback

**Python Code:**
```python
# Get all feedback sorted by date (newest first)
feedback_list = list(feedback_collection.find().sort("feedback_date", -1))

for feedback in feedback_list:
    print(f"Customer: {feedback['customer_name']}")
    print(f"Email: {feedback['email']}")
    print(f"Rating: {feedback['rating']}/5 ⭐")
    print(f"Comments: {feedback['comments']}")
    print(f"Date: {feedback['feedback_date']}")
    print("-" * 50)
```

**MongoDB Shell Equivalent:**
```javascript
db.feedback.find().sort({feedback_date: -1})
```

---

### DELETE - Remove Feedback

**Python Code:**
```python
from bson.objectid import ObjectId

feedback_id = "65f1234567890abcdef12347"

result = feedback_collection.delete_one({"_id": ObjectId(feedback_id)})
print(f"Deleted {result.deleted_count} feedback(s)")
```

**MongoDB Shell Equivalent:**
```javascript
db.feedback.deleteOne({_id: ObjectId("65f1234567890abcdef12347")})
```

---

### AGGREGATION - Calculate Average Rating

**Python Code:**
```python
pipeline = [
    {
        "$group": {
            "_id": None,
            "average_rating": {"$avg": "$rating"},
            "total_feedback": {"$sum": 1},
            "max_rating": {"$max": "$rating"},
            "min_rating": {"$min": "$rating"}
        }
    }
]

result = list(feedback_collection.aggregate(pipeline))

if result:
    stats = result[0]
    print(f"Average Rating: {stats['average_rating']:.2f}/5")
    print(f"Total Feedback: {stats['total_feedback']}")
    print(f"Highest Rating: {stats['max_rating']}")
    print(f"Lowest Rating: {stats['min_rating']}")
```

**MongoDB Shell Equivalent:**
```javascript
db.feedback.aggregate([
    {
        $group: {
            _id: null,
            average_rating: {$avg: "$rating"},
            total_feedback: {$sum: 1},
            max_rating: {$max: "$rating"},
            min_rating: {$min: "$rating"}
        }
    }
])
```

**Output:**
```
Average Rating: 4.43/5
Total Feedback: 7
Highest Rating: 5
Lowest Rating: 3
```

---

### AGGREGATION - Count Feedback by Rating

**Python Code:**
```python
pipeline = [
    {
        "$group": {
            "_id": "$rating",
            "count": {"$sum": 1}
        }
    },
    {
        "$sort": {"_id": -1}
    }
]

result = list(feedback_collection.aggregate(pipeline))

print("Feedback distribution:")
for item in result:
    print(f"{item['_id']} stars: {item['count']} reviews")
```

**MongoDB Shell Equivalent:**
```javascript
db.feedback.aggregate([
    {
        $group: {
            _id: "$rating",
            count: {$sum: 1}
        }
    },
    {
        $sort: {_id: -1}
    }
])
```

**Output:**
```
Feedback distribution:
5 stars: 4 reviews
4 stars: 2 reviews
3 stars: 1 reviews
```

---

## 4. ADVANCED QUERIES

### Count Documents in Each Collection

**Python Code:**
```python
menu_count = menu_collection.count_documents({})
orders_count = orders_collection.count_documents({})
feedback_count = feedback_collection.count_documents({})

print(f"Menu Items: {menu_count}")
print(f"Orders: {orders_count}")
print(f"Feedback: {feedback_count}")
```

**MongoDB Shell Equivalent:**
```javascript
db.menu.countDocuments({})
db.orders.countDocuments({})
db.feedback.countDocuments({})
```

---

### Get Recent Orders (Last 7 Days)

**Python Code:**
```python
from datetime import datetime, timedelta

seven_days_ago = datetime.now() - timedelta(days=7)

recent_orders = list(orders_collection.find({
    "order_date": {"$gte": seven_days_ago}
}).sort("order_date", -1))

print(f"Orders in last 7 days: {len(recent_orders)}")
```

**MongoDB Shell Equivalent:**
```javascript
db.orders.find({
    order_date: {$gte: new Date(Date.now() - 7*24*60*60*1000)}
}).sort({order_date: -1})
```

---

### Get Total Sales Amount

**Python Code:**
```python
pipeline = [
    {
        "$match": {"status": "Delivered"}
    },
    {
        "$group": {
            "_id": None,
            "total_sales": {"$sum": "$total_amount"},
            "total_orders": {"$sum": 1}
        }
    }
]

result = list(orders_collection.aggregate(pipeline))

if result:
    stats = result[0]
    print(f"Total Sales: ₹{stats['total_sales']:.2f}")
    print(f"Completed Orders: {stats['total_orders']}")
```

**MongoDB Shell Equivalent:**
```javascript
db.orders.aggregate([
    {
        $match: {status: "Delivered"}
    },
    {
        $group: {
            _id: null,
            total_sales: {$sum: "$total_amount"},
            total_orders: {$sum: 1}
        }
    }
])
```

---

### Get Most Popular Menu Categories

**Python Code:**
```python
pipeline = [
    {
        "$group": {
            "_id": "$category",
            "count": {"$sum": 1},
            "avg_price": {"$avg": "$price"}
        }
    },
    {
        "$sort": {"count": -1}
    }
]

result = list(menu_collection.aggregate(pipeline))

print("Menu categories:")
for item in result:
    print(f"{item['_id']}: {item['count']} items (Avg: ₹{item['avg_price']:.2f})")
```

**MongoDB Shell Equivalent:**
```javascript
db.menu.aggregate([
    {
        $group: {
            _id: "$category",
            count: {$sum: 1},
            avg_price: {$avg: "$price"}
        }
    },
    {
        $sort: {count: -1}
    }
])
```

---

## 5. BULK OPERATIONS

### Insert Multiple Menu Items

**Python Code:**
```python
items = [
    {
        "name": "Item 1",
        "category": "Main Course",
        "price": 299,
        "description": "Description 1",
        "availability": True,
        "created_at": datetime.now()
    },
    {
        "name": "Item 2",
        "category": "Dessert",
        "price": 149,
        "description": "Description 2",
        "availability": True,
        "created_at": datetime.now()
    }
]

result = menu_collection.insert_many(items)
print(f"Inserted {len(result.inserted_ids)} items")
```

**MongoDB Shell Equivalent:**
```javascript
db.menu.insertMany([
    {name: "Item 1", category: "Main Course", price: 299, ...},
    {name: "Item 2", category: "Dessert", price: 149, ...}
])
```

---

### Update Multiple Documents

**Python Code:**
```python
# Update all items in a category
result = menu_collection.update_many(
    {"category": "Dessert"},
    {"$set": {"availability": False}}
)

print(f"Updated {result.modified_count} items")
```

**MongoDB Shell Equivalent:**
```javascript
db.menu.updateMany(
    {category: "Dessert"},
    {$set: {availability: false}}
)
```

---

### Delete Multiple Documents

**Python Code:**
```python
# Delete all unavailable items
result = menu_collection.delete_many({"availability": False})

print(f"Deleted {result.deleted_count} items")
```

**MongoDB Shell Equivalent:**
```javascript
db.menu.deleteMany({availability: false})
```

---

## 6. INDEX OPERATIONS

### Create Indexes for Better Performance

**Python Code:**
```python
# Create text index for search
menu_collection.create_index([("name", "text"), ("category", "text")])

# Create index on order date
orders_collection.create_index([("order_date", -1)])

# Create index on rating
feedback_collection.create_index([("rating", 1)])

print("Indexes created successfully")
```

**MongoDB Shell Equivalent:**
```javascript
// Text index for search
db.menu.createIndex({name: "text", category: "text"})

// Index on order date
db.orders.createIndex({order_date: -1})

// Index on rating
db.feedback.createIndex({rating: 1})
```

---

## Summary of Operations

### CRUD Operations Count

| Collection | INSERT | SELECT | UPDATE | DELETE | SEARCH | AGGREGATE |
|-----------|--------|--------|--------|--------|--------|-----------|
| Menu      | ✅     | ✅     | ✅     | ✅     | ✅     | ✅        |
| Orders    | ✅     | ✅     | ✅     | ✅     | ✅     | ✅        |
| Feedback  | ✅     | ✅     | ❌     | ✅     | ❌     | ✅        |

**Total Unique Queries: 25+**

---

## Notes for Assignment

1. **Screenshots Required**: Take screenshots after running each query
2. **Output Documentation**: Show both the code and the result
3. **MongoDB Compass**: Use Compass to show data visually
4. **Aggregation**: Highlight the aggregation pipeline queries
5. **Performance**: Mention the use of indexes for optimization

---
