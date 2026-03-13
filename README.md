# Restaurant Food Ordering System
### MongoDB + Python Integration Project

---

## 📋 Problem Statement

Modern restaurants need an efficient digital system to manage their operations. This project addresses the following challenges:

1. **Menu Management**: Difficult to maintain and update menu items manually
2. **Order Tracking**: No systematic way to track customer orders and their status
3. **Customer Feedback**: Lack of organized feedback collection system
4. **Data Persistence**: Need for reliable cloud-based data storage
5. **User Interface**: Requirement for easy-to-use interface for restaurant staff

**Solution:** A comprehensive desktop application built with Python and MongoDB Atlas that provides menu management, order tracking, and customer feedback capabilities with a user-friendly GUI.

---

## 🎯 Project Objectives

- Apply MongoDB concepts in real-world restaurant management
- Develop hands-on skills in NoSQL database design and querying
- Create a practical CRUD application with Python and MongoDB
- Implement cloud-based data storage using MongoDB Atlas
- Build an intuitive GUI using Tkinter for easy operation

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────┐
│    Tkinter GUI (Frontend)          │
│  - Menu Management Tab              │
│  - Order Tracking Tab               │
│  - Customer Feedback Tab            │
└──────────────┬──────────────────────┘
               │
               │ pymongo
               ▼
┌─────────────────────────────────────┐
│   Database Module (database.py)    │
│  - Connection Management            │
│  - CRUD Operations                  │
│  - Query Functions                  │
└──────────────┬──────────────────────┘
               │
               │ MongoDB Driver
               ▼
┌─────────────────────────────────────┐
│    MongoDB Atlas (Cloud)            │
│  - menu collection                  │
│  - orders collection                │
│  - feedback collection              │
└─────────────────────────────────────┘
```

---

## 🗂️ Database Collections

### 1. Menu Collection
- Stores menu items with name, category, price, description, and availability
- Supports CRUD operations for menu management
- Searchable by name and category

### 2. Orders Collection
- Tracks customer orders with order details and status
- Order status: Pending → Preparing → Ready → Delivered
- Searchable by customer name and phone number

### 3. Feedback Collection
- Stores customer feedback with ratings (1-5 stars)
- Calculates average rating using aggregation
- Timestamped for tracking feedback trends

For detailed schema information, see [DATABASE_DESIGN.md](DATABASE_DESIGN.md)

---

## ⚙️ Features

### 📋 Menu Management
- ✅ Add new menu items with details
- ✅ View all menu items in organized list
- ✅ Update item details (price, availability, description)
- ✅ Delete menu items
- ✅ Search menu by name or category
- ✅ Toggle item availability status

### 🛒 Order Tracking
- ✅ Create new customer orders
- ✅ Track order status (Pending, Preparing, Ready, Delivered, Cancelled)
- ✅ View all orders with customer details
- ✅ Update order status in real-time
- ✅ Search orders by customer name or phone
- ✅ Delete orders (admin function)
- ✅ Support multiple payment methods (Cash, Card, UPI, Online)

### ⭐ Customer Feedback
- ✅ Submit customer feedback with ratings
- ✅ View all feedback with ratings
- ✅ Calculate and display average rating
- ✅ View detailed feedback comments
- ✅ Delete feedback (admin function)
- ✅ Real-time feedback statistics

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- MongoDB Atlas account (free tier available)
- Internet connection

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- `pymongo` - MongoDB driver for Python
- `dnspython` - DNS toolkit (required for MongoDB Atlas connection)
- `pillow` - Image library for Tkinter (optional)

### Step 2: Configure MongoDB Atlas

1. **Create MongoDB Atlas Account**
   - Visit https://www.mongodb.com/cloud/atlas
   - Sign up for a free account

2. **Create a Cluster**
   - Click "Build a Cluster"
   - Choose FREE tier (M0 Sandbox)
   - Select your preferred region
   - Click "Create Cluster"

3. **Create Database User**
   - Go to "Database Access"
   - Click "Add New Database User"
   - Create username and password
   - Set privileges to "Read and Write to any database"

4. **Configure Network Access**
   - Go to "Network Access"
   - Click "Add IP Address"
   - Select "Allow Access from Anywhere" (0.0.0.0/0) for testing
   - Click "Confirm"

5. **Get Connection String**
   - Go to "Clusters"
   - Click "Connect"
   - Choose "Connect your application"
   - Copy the connection string
   - Format: `mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority`

### Step 3: Update Configuration

Edit `config.py` and replace with your connection details:

```python
MONGO_URI = "mongodb+srv://your_username:your_password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "restaurant_system"
```

**Important:** Replace `your_username`, `your_password`, and `cluster0.xxxxx` with your actual credentials.

### Step 4: Load Sample Data (Optional)

To populate the database with test data:

```bash
python load_sample_data.py
```

This will add:
- 15 sample menu items
- 5 sample orders
- 7 sample feedback entries

### Step 5: Run the Application

```bash
python restaurant_app.py
```

---

## 🖥️ User Interface Guide

### Main Window
- **Header**: Application title and branding
- **Connection Panel**: MongoDB connection status and connect/disconnect button
- **Tabs**: Three main modules (Menu Management, Order Tracking, Customer Feedback)

### Menu Management Tab
**Left Panel:**
- Form to add/edit menu items
- Fields: Name, Category, Price, Description, Availability
- Buttons: Add Item, Update Item, Clear

**Right Panel:**
- List of all menu items in table format
- Search functionality
- Double-click to select and edit
- Delete button for removing items

### Order Tracking Tab
**Left Panel:**
- Form to create new orders
- Fields: Customer Name, Phone, Items, Total Amount, Payment Method
- Buttons: Create Order, Clear

**Right Panel:**
- List of all orders with status
- Search by customer name or phone
- Status update dropdown (Pending → Preparing → Ready → Delivered)
- Delete button for removing orders

### Customer Feedback Tab
**Left Panel:**
- Form to submit feedback
- Fields: Customer Name, Email, Rating (1-5), Comments
- Buttons: Submit Feedback, Clear

**Right Panel:**
- Statistics panel showing average rating
- List of all feedback entries
- View Details button to see full comments
- Delete button for removing feedback

---

## 🔧 MongoDB Queries Used

### Insert Operations
```python
# Add menu item
menu_collection.insert_one({
    "name": "Pizza",
    "category": "Main Course",
    "price": 299,
    "description": "Delicious pizza",
    "availability": True,
    "created_at": datetime.now()
})
```

### Read Operations
```python
# Get all menu items
menu_collection.find()

# Search menu items
menu_collection.find({
    "$or": [
        {"name": {"$regex": search_term, "$options": "i"}},
        {"category": {"$regex": search_term, "$options": "i"}}
    ]
})
```

### Update Operations
```python
# Update menu item
menu_collection.update_one(
    {"_id": ObjectId(item_id)},
    {"$set": {
        "name": "New Name",
        "price": 350,
        "updated_at": datetime.now()
    }}
)
```

### Delete Operations
```python
# Delete menu item
menu_collection.delete_one({"_id": ObjectId(item_id)})
```

### Aggregation Pipeline
```python
# Calculate average rating
feedback_collection.aggregate([
    {
        "$group": {
            "_id": None,
            "average_rating": {"$avg": "$rating"},
            "total_feedback": {"$sum": 1}
        }
    }
])
```

---

## 📸 Screenshots

*(Add screenshots of your running application here after testing)*

1. **Connection Screen**: Shows MongoDB Atlas connection status
2. **Menu Management**: Add, view, update, delete menu items
3. **Order Tracking**: Create and track orders
4. **Customer Feedback**: Submit and view feedback with ratings

---

## 🧪 Testing Checklist

### Menu Management
- [ ] Connect to MongoDB Atlas
- [ ] Add new menu item
- [ ] View all menu items
- [ ] Search menu items by name
- [ ] Update menu item details
- [ ] Delete menu item
- [ ] Toggle item availability

### Order Tracking
- [ ] Create new order
- [ ] View all orders
- [ ] Search orders by customer name
- [ ] Update order status
- [ ] Delete order

### Customer Feedback
- [ ] Submit feedback with rating
- [ ] View all feedback
- [ ] Check average rating calculation
- [ ] View feedback details
- [ ] Delete feedback

### Error Handling
- [ ] Test with invalid MongoDB URI
- [ ] Test with empty form fields
- [ ] Test with invalid data types
- [ ] Test connection timeout

---

## 🎓 Assignment Deliverables

### Required Components
1. ✅ **Problem Statement**: Restaurant management system needs
2. ✅ **Database Design**: Three collections with proper schema
3. ✅ **Sample Data**: 15 menu items, 5 orders, 7 feedback entries
4. ✅ **Queries**: CRUD operations with screenshots
5. ✅ **Conclusions**: Benefits and learnings from the project

### Documentation Structure
```
Restaurant_Food_Ordering_System/
├── config.py              # MongoDB configuration
├── database.py            # Database operations
├── restaurant_app.py      # Main GUI application
├── load_sample_data.py    # Sample data loader
├── requirements.txt       # Dependencies
├── DATABASE_DESIGN.md     # Detailed schema documentation
├── README.md              # This file
└── screenshots/           # Screenshots for assignment (to be added)
```

---

## 📊 Conclusions

### Learning Outcomes

1. **MongoDB Integration**
   - Successfully connected Python application to MongoDB Atlas
   - Implemented CRUD operations using pymongo
   - Used aggregation pipeline for calculating average ratings

2. **NoSQL Database Benefits**
   - Flexible schema allows easy modifications
   - Document model naturally represents real-world entities
   - Cloud-based storage provides reliability and accessibility

3. **Application Development**
   - Built complete desktop application with Tkinter
   - Implemented three major modules with full functionality
   - Created user-friendly interface for restaurant operations

4. **Practical Skills**
   - Database design for real-world scenarios
   - Error handling and validation
   - Data persistence and retrieval
   - GUI development with Python

### MongoDB Advantages for This System

1. **Schema Flexibility**: Easy to add new fields without database migrations
2. **JSON Format**: Natural integration with Python dictionaries
3. **Scalability**: MongoDB Atlas provides automatic scaling
4. **Cloud Storage**: Data accessible from anywhere with internet
5. **Aggregation Framework**: Powerful analytics capabilities
6. **No Complex Joins**: Embedded documents simplify data relationships

### Real-World Applications

This system demonstrates MongoDB's suitability for:
- Restaurant management systems
- E-commerce order tracking
- Customer feedback platforms
- Inventory management
- Food delivery applications

### Future Enhancements

- User authentication and role-based access
- Report generation (daily sales, popular items)
- Email notifications for order status
- Payment gateway integration
- Mobile app version
- Multi-restaurant support

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: Connection timeout to MongoDB Atlas
**Solution**:
- Check internet connection
- Verify IP address is whitelisted in Network Access
- Ensure correct connection string in config.py

**Issue**: Authentication failed
**Solution**:
- Verify username and password are correct
- Check if database user has proper permissions
- Ensure password doesn't contain special characters that need URL encoding

**Issue**: ModuleNotFoundError: No module named 'pymongo'
**Solution**:
```bash
pip install pymongo dnspython
```

**Issue**: GUI window too small or large
**Solution**:
- Adjust window size in `restaurant_app.py`
- Modify `self.root.geometry("1200x700")` to desired dimensions

---

## 📝 Assignment Submission Checklist

- [ ] Problem statement documented
- [ ] Database design document completed
- [ ] Sample data loaded into MongoDB Atlas
- [ ] All CRUD operations tested
- [ ] Screenshots captured for each operation
- [ ] Conclusions written
- [ ] Code properly commented
- [ ] README documentation complete
- [ ] Presentation prepared (2-5 minutes)

---

## 👨‍💻 Developer Information

**Project**: Restaurant Food Ordering System
**Technology Stack**: Python, MongoDB, Tkinter, pymongo
**Course**: Advanced Database with MongoDB (4040233206)
**Assignment Type**: Innovative Assignment
**Semester**: 4, Academic Year: 2025-26

---

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review MongoDB Atlas documentation
3. Verify configuration in config.py
4. Check Python version compatibility

---

## 📄 License

This project is created for educational purposes as part of the Advanced Database with MongoDB course.

---

**Note**: Remember to keep your MongoDB Atlas credentials secure. Never commit sensitive information to version control systems.
