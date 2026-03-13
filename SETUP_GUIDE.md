# Quick Setup Guide
## Restaurant Food Ordering System

Follow these steps to get your application up and running quickly!

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Install Python Dependencies (1 min)

Open terminal in the project directory and run:
```bash
pip install -r requirements.txt
```

### Step 2: Setup MongoDB Atlas (2 min)

1. Go to https://www.mongodb.com/cloud/atlas
2. Click "Try Free" and create an account
3. Create a FREE cluster (M0 Sandbox)
4. While cluster is creating:
   - Go to "Database Access" → Create a database user
   - Username: `restaurant_user`
   - Password: Choose a strong password (save it!)
   - Privileges: "Atlas admin"

5. Go to "Network Access" → Add IP Address
   - Click "Allow Access from Anywhere"
   - Or add your current IP address

6. Once cluster is ready, click "Connect"
   - Choose "Connect your application"
   - Copy the connection string

### Step 3: Configure Application (1 min)

1. Open `config.py` in a text editor
2. Replace the MONGO_URI with your connection string:
```python
MONGO_URI = "mongodb+srv://restaurant_user:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
```
**Important**: Replace `YOUR_PASSWORD` and `cluster0.xxxxx` with your actual values!

3. Save the file

### Step 4: Load Sample Data (30 seconds)

```bash
python load_sample_data.py
```

You should see:
```
✅ Connected successfully!
📋 Loading sample menu items...
  ✓ Added: Margherita Pizza
  ✓ Added: Chicken Tikka
  ...
✅ Sample data loaded successfully!
```

### Step 5: Run the Application (30 seconds)

```bash
python restaurant_app.py
```

1. Click "Connect to MongoDB" button
2. If successful, you'll see "✅ Connected to MongoDB Atlas"
3. Start using the application!

---

## 🎯 Testing Your Application

### Test Menu Management
1. Go to "📋 Menu Management" tab
2. Try adding a new item:
   - Name: "Test Pizza"
   - Category: "Main Course"
   - Price: 399
   - Description: "Test item"
   - Click "Add Item"

3. You should see it appear in the list on the right!

### Test Order Tracking
1. Go to "🛒 Order Tracking" tab
2. Create a test order:
   - Customer Name: "Test Customer"
   - Phone: "1234567890"
   - Items: "Pizza\nCold Coffee"
   - Total: 500
   - Payment: "UPI"
   - Click "Create Order"

3. Update the status using the dropdown

### Test Customer Feedback
1. Go to "⭐ Customer Feedback" tab
2. Submit test feedback:
   - Name: "Test User"
   - Email: "test@example.com"
   - Rating: 5 (use slider)
   - Comments: "Great food!"
   - Click "Submit Feedback"

3. Check the average rating updates!

---

## 📸 Taking Screenshots for Assignment

### Required Screenshots

1. **MongoDB Atlas Dashboard**
   - Show your cluster
   - Show database and collections

2. **Connection Screen**
   - Before connection (⚠️ Not Connected)
   - After connection (✅ Connected)

3. **Menu Management**
   - Add menu item form filled
   - Menu items list
   - Update operation
   - Delete operation

4. **Order Tracking**
   - Create order form
   - Orders list with different statuses
   - Status update

5. **Customer Feedback**
   - Submit feedback form
   - Feedback list with ratings
   - Average rating display

### How to Take Screenshots

**Windows**: Press `Windows + Shift + S`
**Mac**: Press `Cmd + Shift + 4`
**Linux**: Press `PrtScn` or use Screenshot tool

Save all screenshots in a `screenshots/` folder for your assignment.

---

## 🔍 Verify MongoDB Atlas Data

### Using MongoDB Compass (Optional)

1. Download MongoDB Compass: https://www.mongodb.com/products/compass
2. Install and open it
3. Paste your connection string
4. Connect and browse your collections

### Using Atlas Web Interface

1. Go to your cluster in MongoDB Atlas
2. Click "Collections"
3. You should see:
   - `restaurant_system` database
   - `menu`, `orders`, `feedback` collections
4. Click on each to see your data

---

## 🎓 Assignment Report Structure

### Create Your Report in This Order:

1. **Cover Page**
   - Project Title
   - Your Name and Roll Number
   - Course Details
   - Date

2. **Index Page**
   - List all sections with page numbers

3. **Problem Statement**
   - Copy from README.md

4. **Database Design**
   - Copy schema from DATABASE_DESIGN.md
   - Add your own diagrams if possible

5. **Sample Data**
   - Show 3-5 examples from each collection
   - Include screenshots from MongoDB Atlas

6. **Queries with Screenshots**

   **Menu Operations:**
   - INSERT: Adding a menu item (show code + screenshot)
   - SELECT: Viewing all items (show code + screenshot)
   - UPDATE: Updating an item (show code + screenshot)
   - DELETE: Removing an item (show code + screenshot)
   - SEARCH: Searching items (show code + screenshot)

   **Order Operations:**
   - INSERT: Creating an order
   - SELECT: Viewing orders
   - UPDATE: Updating order status
   - DELETE: Removing order

   **Feedback Operations:**
   - INSERT: Submitting feedback
   - SELECT: Viewing feedback
   - AGGREGATE: Average rating calculation

7. **Conclusions**
   - What you learned
   - MongoDB advantages
   - Real-world applications
   - Future enhancements

---

## 💡 Tips for Success

### For Your Presentation (2-5 minutes)

1. **Introduction** (30 sec)
   - Project name and purpose
   - Why MongoDB?

2. **Demo** (2-3 min)
   - Connect to MongoDB
   - Quick demo of each module
   - Show one CRUD operation

3. **Technical Details** (1 min)
   - Database design
   - Key features
   - Technologies used

4. **Conclusion** (30 sec)
   - Learning outcomes
   - Future scope

### Practice Your Demo
- Test everything before presentation
- Keep sample data ready
- Practice timing
- Prepare for common questions:
  - Why MongoDB over MySQL?
  - How does the connection work?
  - What are the main challenges?

---

## 🐛 Common Issues & Quick Fixes

### Issue: Can't connect to MongoDB
**Fix:**
```python
# Check your config.py:
# 1. Is the URI correct?
# 2. Did you replace YOUR_PASSWORD?
# 3. Did you replace cluster0.xxxxx with your cluster name?
```

### Issue: "Authentication failed"
**Fix:**
- Go to MongoDB Atlas → Database Access
- Make sure user exists and password is correct
- Try creating a new user with simple password (no special characters)

### Issue: "No module named 'pymongo'"
**Fix:**
```bash
pip install pymongo dnspython
```

### Issue: Sample data script fails
**Fix:**
- Make sure you can connect manually first
- Check if database user has write permissions
- Try running `python restaurant_app.py` first

---

## ✅ Final Checklist Before Submission

- [ ] Application runs without errors
- [ ] Connected to MongoDB Atlas successfully
- [ ] All CRUD operations working
- [ ] Sample data loaded
- [ ] Screenshots captured (at least 10)
- [ ] Report formatted properly
- [ ] Code properly commented
- [ ] config.py updated with your credentials
- [ ] Tested on the presentation computer
- [ ] Presentation slides ready (if required)
- [ ] Backup of code and screenshots
- [ ] MongoDB Atlas cluster is active

---

## 📧 Getting Help

If something doesn't work:

1. **Check Error Messages**: Read what the error says
2. **Review Configuration**: Most issues are in config.py
3. **Test Internet Connection**: MongoDB Atlas needs internet
4. **Check MongoDB Atlas**: Is your cluster running?
5. **Verify Credentials**: Username and password correct?

---

## 🎉 You're Ready!

If you've completed all steps:
- Your application is running ✅
- MongoDB Atlas is connected ✅
- Sample data is loaded ✅
- You can perform all CRUD operations ✅

**You're ready for your presentation!** 🚀

Good luck with your assignment! 💪
