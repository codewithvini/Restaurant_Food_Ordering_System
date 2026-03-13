# 🌐 Web Application Guide
## Restaurant Food Ordering System - Flask Web App

**Congratulations! Your project is now a full web application!** 🎉

---

## 🚀 Quick Start

### Step 1: Install Flask Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `Flask` - Web framework
- `pymongo` - MongoDB driver
- `dnspython` - Required for MongoDB Atlas
- `Werkzeug` - Flask dependency

### Step 2: Setup MongoDB Atlas

**IMPORTANT:** You must setup MongoDB Atlas first!

1. Follow **[MONGODB_ATLAS_SETUP.md](MONGODB_ATLAS_SETUP.md)**
2. Update `config.py` with your connection string

### Step 3: Load Sample Data (Optional)

```bash
python load_sample_data.py
```

### Step 4: Run the Web Application

```bash
python app.py
```

### Step 5: Open in Browser

```
http://localhost:5000
```

or

```
http://127.0.0.1:5000
```

---

## 🌐 Application URLs

| Page | URL | Description |
|------|-----|-------------|
| **Home** | http://localhost:5000/ | Landing page with overview |
| **Dashboard** | http://localhost:5000/dashboard | Statistics and quick actions |
| **Menu Management** | http://localhost:5000/menu | Add, edit, delete menu items |
| **Order Tracking** | http://localhost:5000/orders | Create and track orders |
| **Customer Feedback** | http://localhost:5000/feedback | View and submit feedback |

---

## 📱 Features

### ✅ Menu Management
- ➕ Add new menu items
- ✏️ Edit existing items
- 🗑️ Delete items
- 🔍 Search menu
- 💰 Update prices
- ✅ Toggle availability

### ✅ Order Tracking
- 📝 Create new orders
- 👁️ View all orders
- 🔄 Update order status (Pending → Preparing → Ready → Delivered)
- 🔍 Search by customer
- 💳 Multiple payment methods
- 🗑️ Delete orders

### ✅ Customer Feedback
- ⭐ Submit feedback with ratings (1-5 stars)
- 📊 View average rating
- 💬 Read all reviews
- 🗑️ Delete feedback

### ✅ Dashboard
- 📊 Statistics (menu items, orders, feedback count)
- ⭐ Average rating display
- 🚀 Quick action buttons
- 📈 Real-time data

---

## 🎨 User Interface

### Modern Design Features:
- ✅ Bootstrap 5 responsive design
- ✅ Beautiful gradient hero section
- ✅ Animated cards and buttons
- ✅ Icons from Bootstrap Icons
- ✅ Modal dialogs for forms
- ✅ Professional color scheme
- ✅ Mobile-friendly layout

---

## 🔌 API Endpoints

### Menu API
```
GET    /api/menu              - Get all menu items
POST   /api/menu              - Add new item
PUT    /api/menu/<id>         - Update item
DELETE /api/menu/<id>         - Delete item
GET    /api/menu/search?q=    - Search menu
```

### Orders API
```
GET    /api/orders                  - Get all orders
POST   /api/orders                  - Create order
PUT    /api/orders/<id>/status      - Update status
DELETE /api/orders/<id>             - Delete order
GET    /api/orders/search?q=        - Search orders
```

### Feedback API
```
GET    /api/feedback          - Get all feedback
POST   /api/feedback          - Submit feedback
DELETE /api/feedback/<id>     - Delete feedback
GET    /api/feedback/stats    - Get statistics
```

---

## 📂 Project Structure

```
Restaurant_Food_Ordering_System/
├── app.py                    # Flask web application
├── database.py               # Database operations
├── config.py                 # MongoDB configuration
├── load_sample_data.py       # Sample data loader
├── requirements.txt          # Dependencies
│
├── templates/                # HTML templates
│   ├── base.html            # Base template
│   ├── index.html           # Home page
│   ├── dashboard.html       # Dashboard
│   ├── menu.html            # Menu management
│   ├── orders.html          # Order tracking
│   ├── feedback.html        # Feedback system
│   ├── 404.html             # Error page
│   └── 500.html             # Error page
│
└── static/                   # Static files
    └── css/
        └── style.css        # Custom styles
```

---

## 💻 Technology Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.8+ |
| **Web Framework** | Flask 3.0.0 |
| **Database** | MongoDB Atlas (Cloud) |
| **Database Driver** | pymongo 4.6.1 |
| **Frontend** | HTML5, CSS3, JavaScript |
| **CSS Framework** | Bootstrap 5.3.0 |
| **Icons** | Bootstrap Icons |
| **JavaScript Library** | jQuery 3.6.0 |

---

## 🔧 Configuration

### MongoDB Configuration (config.py)

```python
# Your MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"

# Database name
DATABASE_NAME = "restaurant_system"

# Collection names
MENU_COLLECTION = "menu"
ORDERS_COLLECTION = "orders"
FEEDBACK_COLLECTION = "feedback"
```

### Flask Configuration (app.py)

```python
# Flask runs on port 5000 by default
app.run(debug=True, host='0.0.0.0', port=5000)

# debug=True: Auto-reload on code changes
# host='0.0.0.0': Accessible from any IP
# port=5000: Default Flask port
```

---

## 🌍 Deployment Options

### Option 1: Local Development (Current)
```bash
python app.py
# Access at: http://localhost:5000
```

### Option 2: Deploy to Render.com (Free)

1. Create `render.yaml`:
```yaml
services:
  - type: web
    name: restaurant-system
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
```

2. Add `gunicorn` to requirements.txt
3. Push to GitHub
4. Connect to Render
5. Deploy!

### Option 3: Deploy to Railway (Free)

1. Push code to GitHub
2. Go to https://railway.app
3. Create new project
4. Connect GitHub repo
5. Add environment variables
6. Deploy!

### Option 4: Deploy to Heroku

1. Create `Procfile`:
```
web: gunicorn app:app
```

2. Push to Heroku:
```bash
heroku login
heroku create restaurant-system
git push heroku main
```

### Option 5: Deploy to PythonAnywhere

1. Upload files to PythonAnywhere
2. Create web app
3. Configure WSGI file
4. Set up virtualenv
5. Reload web app

---

## 🔒 Security Considerations

### For Development (Current)
- ✅ Debug mode enabled for easy development
- ✅ Host set to 0.0.0.0 for network access
- ⚠️ Secret key is hardcoded (OK for development)

### For Production (Future)
- ❌ Disable debug mode
- ✅ Use environment variables for secrets
- ✅ Add authentication system
- ✅ Implement CORS properly
- ✅ Add rate limiting
- ✅ Use HTTPS

Example production config:
```python
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['DEBUG'] = False
```

---

## 🐛 Troubleshooting

### Issue 1: Port Already in Use

**Error:**
```
OSError: [Errno 98] Address already in use
```

**Solution:**
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process
kill -9 <PID>

# Or use different port
python app.py  # Edit app.py to change port
```

---

### Issue 2: MongoDB Connection Failed

**Error:**
```
ServerSelectionTimeoutError
```

**Solution:**
1. Check internet connection
2. Verify MongoDB Atlas connection string in `config.py`
3. Check IP whitelist in MongoDB Atlas
4. Ensure cluster is active

---

### Issue 3: Template Not Found

**Error:**
```
TemplateNotFound: index.html
```

**Solution:**
```bash
# Ensure templates folder exists
ls templates/

# Run from project root directory
cd /home/yash/Restaurant_Food_Ordering_System
python app.py
```

---

### Issue 4: Module Not Found

**Error:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
pip install -r requirements.txt
# or
pip install Flask pymongo dnspython
```

---

## 📸 Taking Screenshots

For your assignment, capture:

1. **Home Page** (http://localhost:5000/)
2. **Dashboard** with statistics
3. **Menu Page** - showing items
4. **Add Menu Item** - modal dialog
5. **Edit Menu Item** - with data
6. **Search Menu** - with results
7. **Orders Page** - showing orders
8. **Create Order** - modal dialog
9. **Update Order Status** - dropdown
10. **Feedback Page** - showing reviews
11. **Submit Feedback** - modal dialog
12. **Average Rating** - display

---

## 🎯 Differences: Desktop vs Web App

| Feature | Desktop (Tkinter) | Web Application (Flask) |
|---------|-------------------|-------------------------|
| **Access** | Single computer | Any device with browser |
| **UI** | Native widgets | HTML/CSS/JavaScript |
| **Deployment** | Executable file | Web server |
| **Updates** | Reinstall required | Instant for all users |
| **Multi-user** | One at a time | Multiple simultaneous |
| **Platform** | OS-dependent | Cross-platform |
| **Internet** | Optional | Required |
| **Portability** | Low | High |
| **Maintenance** | Hard | Easy |
| **Modern Look** | Basic | Professional |

---

## 🎓 For Your Assignment

### Report Updates

Add this section to your report:

**Web Application Features:**
- Built with Flask framework
- RESTful API endpoints
- Responsive Bootstrap 5 UI
- AJAX for real-time updates
- Cloud-based MongoDB integration
- Accessible via URL
- Modern, professional interface
- Mobile-friendly design

### Presentation Updates

Add these points:
- "Deployed as web application using Flask"
- "Accessible from any browser at localhost:5000"
- "Modern UI with Bootstrap 5"
- "RESTful API design"
- "Can be deployed to cloud platforms"

---

## 🚀 Advanced Features (Future)

### Authentication System
```python
from flask_login import LoginManager, login_required

@app.route('/admin')
@login_required
def admin_panel():
    return render_template('admin.html')
```

### API Rate Limiting
```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/menu')
@limiter.limit("100 per hour")
def get_menu():
    pass
```

### File Upload (Menu Images)
```python
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static/images', filename))
```

---

## 📝 Development Tips

### 1. Auto-reload on Changes
Flask debug mode auto-reloads when you edit files!

### 2. View Logs
All requests and errors appear in terminal

### 3. Test API with curl
```bash
# Get menu
curl http://localhost:5000/api/menu

# Add item
curl -X POST http://localhost:5000/api/menu \
  -H "Content-Type: application/json" \
  -d '{"name":"Pizza","category":"Main Course","price":299,"description":"Yummy"}'
```

### 4. Browser DevTools
- F12 to open DevTools
- View Network tab for API calls
- Check Console for JavaScript errors

---

## ✅ Pre-Demo Checklist

Before showing your web app:

- [ ] MongoDB Atlas is connected
- [ ] Sample data is loaded
- [ ] All pages load correctly
- [ ] Can add menu items
- [ ] Can create orders
- [ ] Can submit feedback
- [ ] Search functionality works
- [ ] All CRUD operations tested
- [ ] No console errors
- [ ] Screenshots captured

---

## 🎉 Congratulations!

You now have a **fully functional web application** that:

✅ Runs in a browser with a URL
✅ Has a beautiful, modern interface
✅ Supports all CRUD operations
✅ Connects to cloud MongoDB database
✅ Can be accessed from any device
✅ Is ready for deployment
✅ Perfect for your assignment!

---

## 📞 Next Steps

1. **Run the application:**
   ```bash
   python app.py
   ```

2. **Open in browser:**
   ```
   http://localhost:5000
   ```

3. **Test all features**

4. **Take screenshots**

5. **Deploy (optional):**
   - Render.com
   - Railway.app
   - PythonAnywhere
   - Heroku

6. **Update your presentation** to mention web application features!

---

**Your web app is ready to go live! 🚀**

Access it at: **http://localhost:5000**
