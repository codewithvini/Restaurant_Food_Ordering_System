# 🚀 Install & Run - Restaurant Food Ordering System

## ✅ **YOUR WEB APP IS READY!**

---

## 📦 **Step 1: Install Flask (30 seconds)**

```bash
pip install -r requirements.txt
```

This installs:
- Flask 3.0.0 (web framework)
- pymongo 4.6.1 (MongoDB driver)
- dnspython 2.4.2 (required for MongoDB Atlas)
- Werkzeug 3.0.1 (Flask dependency)

---

## ⚙️ **Step 2: Setup MongoDB Atlas (10 minutes)**

### Quick Setup:

1. **Go to:** https://mongodb.com/cloud/atlas

2. **Sign up** (free account)

3. **Create cluster:**
   - Click "Build a Database"
   - Choose **FREE** (M0 Sandbox)
   - Select region closest to you
   - Click "Create"

4. **Create database user:**
   - Go to "Database Access"
   - Click "Add New Database User"
   - Username: `restaurant_user`
   - Password: (create a simple password, save it!)
   - Privileges: "Atlas admin"

5. **Whitelist IP:**
   - Go to "Network Access"
   - Click "Add IP Address"
   - Click "Allow Access from Anywhere" (0.0.0.0/0)
   - Confirm

6. **Get connection string:**
   - Go back to "Database"
   - Click "Connect" on your cluster
   - Choose "Connect your application"
   - Copy the connection string

7. **Update config.py:**

```python
MONGO_URI = "mongodb+srv://restaurant_user:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
```

Replace:
- `restaurant_user` with your username
- `YOUR_PASSWORD` with your password
- `cluster0.xxxxx` with your cluster address

---

## 🎲 **Step 3: Load Sample Data (Optional - 30 seconds)**

```bash
python load_sample_data.py
```

This adds:
- 15 menu items
- 5 sample orders
- 7 customer feedback entries

---

## 🌐 **Step 4: Run the Web Application**

```bash
python app.py
```

You should see:
```
============================================================
🍽️  Restaurant Food Ordering System
============================================================

🌐 Starting web server...
✅ Connected to MongoDB Atlas successfully!

📍 Access the application at:
   → http://localhost:5000
   → http://127.0.0.1:5000
```

---

## 🖥️ **Step 5: Open in Browser**

Open your web browser and go to:

```
http://localhost:5000
```

You should see a beautiful website with:
- 🏠 Home page
- 📊 Dashboard
- 📋 Menu Management
- 🛒 Order Tracking
- ⭐ Customer Feedback

---

## 🎯 **Quick Test:**

1. **Go to Menu page:** http://localhost:5000/menu
2. **Click "Add New Item"**
3. **Fill the form:**
   - Name: Test Pizza
   - Category: Main Course
   - Price: 399
   - Description: Delicious test pizza
4. **Click "Save"**
5. **You should see it in the table!** ✅

---

## 🐛 **Troubleshooting:**

### Problem: "Port already in use"
```bash
# Find and kill the process
lsof -i :5000
kill -9 <PID>
```

### Problem: "MongoDB connection failed"
- Check your `config.py` has the correct connection string
- Verify MongoDB Atlas cluster is running
- Check IP is whitelisted (0.0.0.0/0)
- Make sure password doesn't have special characters

### Problem: "Module not found: flask"
```bash
pip install -r requirements.txt
```

### Problem: "Template not found"
```bash
# Make sure you're in the right directory
cd /home/yash/Restaurant_Food_Ordering_System
python app.py
```

---

## 📸 **For Your Assignment:**

Take screenshots of:
1. Home page
2. Dashboard with stats
3. Menu page with items
4. Add item modal
5. Orders page
6. Create order modal
7. Feedback page
8. Submit feedback modal

---

## 🎉 **Success Checklist:**

- [ ] Flask installed
- [ ] MongoDB Atlas account created
- [ ] Cluster created (FREE M0)
- [ ] Database user created
- [ ] IP whitelisted (0.0.0.0/0)
- [ ] Connection string copied
- [ ] config.py updated
- [ ] Sample data loaded
- [ ] App running: `python app.py`
- [ ] Browser opened: http://localhost:5000
- [ ] Can see home page
- [ ] Can navigate all pages
- [ ] Can add menu items
- [ ] Can create orders
- [ ] Can submit feedback

---

## 💡 **Pro Tips:**

1. **Keep Terminal Open:** Don't close the terminal where `python app.py` is running
2. **Auto-Reload:** Flask auto-reloads when you save files (debug mode)
3. **View Logs:** All requests appear in the terminal
4. **Stop Server:** Press `Ctrl+C` in terminal
5. **Restart Server:** Run `python app.py` again

---

## 🌐 **All URLs:**

| Page | URL |
|------|-----|
| Home | http://localhost:5000/ |
| Dashboard | http://localhost:5000/dashboard |
| Menu | http://localhost:5000/menu |
| Orders | http://localhost:5000/orders |
| Feedback | http://localhost:5000/feedback |

---

## 📚 **Need More Help?**

Read these files:
1. **WEB_APP_GUIDE.md** - Complete web app documentation
2. **MONGODB_ATLAS_SETUP.md** - Detailed MongoDB setup
3. **RUN_WEB_APP.txt** - Quick reference

---

## ✨ **What You Have:**

✅ Professional web application
✅ Beautiful Bootstrap 5 UI
✅ Real-time CRUD operations
✅ Cloud MongoDB integration
✅ RESTful API architecture
✅ Mobile-responsive design
✅ Production-ready code
✅ Perfect for your assignment!

---

## 🚀 **Start Now!**

```bash
# 1. Install
pip install -r requirements.txt

# 2. Update config.py with MongoDB URI

# 3. Load data
python load_sample_data.py

# 4. Run
python app.py

# 5. Open: http://localhost:5000
```

**Your restaurant website is ready to go live! 🎊**
