# Deploy Restaurant Food Ordering System to Render

## Complete Step-by-Step Guide (Using GitHub Desktop)

---

## Part 1: Prepare Your Project (5 minutes)

### Step 1: Create `.gitignore` file

Create a file named `.gitignore` in your project folder with this content:

```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.env
.DS_Store
```

This prevents unnecessary files from being uploaded to GitHub.

---

### Step 2: Create `render.yaml` (Optional but recommended)

Create a file named `render.yaml` in your project folder:

```yaml
services:
  - type: web
    name: restaurant-system
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

---

## Part 2: Upload to GitHub Using GitHub Desktop (10 minutes)

### Step 1: Download GitHub Desktop

1. Go to: https://desktop.github.com/
2. Download and install GitHub Desktop
3. Sign in with your GitHub account (create one if needed at https://github.com)

---

### Step 2: Create Repository in GitHub Desktop

1. Open GitHub Desktop
2. Click **"File"** → **"Add Local Repository"**
3. Click **"Choose..."** and select your project folder:
   ```
   /home/yash/Restaurant_Food_Ordering_System
   ```
4. If it says "not a Git repository", click **"create a repository"**
5. Fill in:
   - **Name:** `restaurant-food-ordering-system`
   - **Description:** `Restaurant Food Ordering System with Flask and MongoDB`
   - **Local Path:** (should already be filled)
   - Check **"Initialize this repository with a README"** (optional)
6. Click **"Create Repository"**

---

### Step 3: Commit Your Files

1. You'll see all your files listed in GitHub Desktop
2. In the bottom left corner:
   - **Summary:** Type `Initial commit - Restaurant System`
   - **Description:** (optional) `Flask web app with MongoDB Atlas`
3. Click **"Commit to main"**

---

### Step 4: Publish to GitHub

1. Click **"Publish repository"** button at the top
2. Uncheck **"Keep this code private"** (or keep it checked if you want it private)
3. Click **"Publish Repository"**
4. Wait for upload to complete (may take 1-2 minutes)

---

### Step 5: Verify on GitHub

1. In GitHub Desktop, click **"View on GitHub"** button
2. Your browser will open showing your repository
3. You should see all your files listed
4. Copy the repository URL (looks like: `https://github.com/YOUR_USERNAME/restaurant-food-ordering-system`)

---

## Part 3: Deploy to Render (10 minutes)

### Step 1: Sign Up for Render

1. Go to: https://render.com
2. Click **"Get Started"**
3. Sign up with your **GitHub account** (easiest method)
4. Authorize Render to access your GitHub

---

### Step 2: Create New Web Service

1. Click **"New +"** button at the top
2. Select **"Web Service"**
3. You'll see your GitHub repositories listed
4. Find **"restaurant-food-ordering-system"** and click **"Connect"**

---

### Step 3: Configure Web Service

Fill in these settings:

**Basic Settings:**
- **Name:** `restaurant-system` (or any name you want)
- **Region:** Choose closest to you (e.g., Oregon, Frankfurt, Singapore)
- **Branch:** `main`
- **Root Directory:** Leave empty
- **Runtime:** `Python 3`

**Build & Deploy:**
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python app.py`

**Instance Type:**
- Select **"Free"** (Free tier - $0/month)

---

### Step 4: Add Environment Variables (IMPORTANT!)

Scroll down to **"Environment Variables"** section:

Click **"Add Environment Variable"** and add these:

1. **Key:** `PYTHON_VERSION`
   **Value:** `3.11.0`

2. **Key:** `PORT`
   **Value:** `5000`

3. **Key:** `MONGO_URI`
   **Value:** `mongodb+srv://restaurant_user:Restaurant2026@restaurantcluster.sn4qrzm.mongodb.net/?retryWrites=true&w=majority&appName=RestaurantCluster`

---

### Step 5: Create Web Service

1. Click **"Create Web Service"** button at the bottom
2. Render will start building your app (takes 2-5 minutes)
3. You'll see logs showing the build process

---

### Step 6: Wait for Deployment

Watch the logs. You should see:

```
==> Installing dependencies from requirements.txt
==> Successfully installed Flask pymongo dnspython
==> Starting service
✅ Connected to MongoDB Atlas successfully!
📍 Access the application at:
   → http://localhost:5000
```

When you see **"Your service is live"** with a green checkmark, it's ready!

---

## Part 4: Access Your Live Website (1 minute)

### Your Live URL:

Render will give you a URL like:
```
https://restaurant-system.onrender.com
```

or
```
https://restaurant-system-xxxx.onrender.com
```

1. Click on the URL at the top of the Render dashboard
2. Your live website will open in a new tab
3. Test all features:
   - Home page
   - Dashboard
   - Menu management
   - Orders
   - Feedback

---

## Troubleshooting

### Problem: Build fails with "No module named flask"

**Solution:** Make sure `requirements.txt` exists in your project with:
```
Flask==3.0.0
pymongo==4.6.1
dnspython==2.4.2
Werkzeug==3.0.1
```

---

### Problem: "Application failed to start"

**Solution:** Check these:
1. In `app.py`, make sure last lines are:
```python
if __name__ == '__main__':
    connect_db()
    app.run(debug=False, host='0.0.0.0', port=5000)
```

2. Change `debug=True` to `debug=False` for production

---

### Problem: "MongoDB connection failed"

**Solution:**
1. Go to Render dashboard
2. Click **"Environment"** tab
3. Check `MONGO_URI` is correct
4. Go to MongoDB Atlas → Network Access
5. Make sure `0.0.0.0/0` is whitelisted

---

### Problem: Page loads but shows errors

**Solution:**
1. Check Render logs (click "Logs" tab)
2. Look for error messages
3. Most common: missing environment variables

---

## Important Notes

### Free Tier Limitations:

- Service **sleeps after 15 minutes of inactivity**
- First request after sleep takes **30-60 seconds** to wake up
- 750 hours/month free (enough for one service running 24/7)

### Keeping Service Awake (Optional):

Use a service like **UptimeRobot** or **Cron-Job.org** to ping your URL every 10 minutes:
- URL to ping: `https://your-app.onrender.com`
- Interval: 10 minutes

---

## Update Your App Later

When you make changes to your code:

1. **Save changes** in VS Code
2. **Open GitHub Desktop**
3. You'll see changed files listed
4. **Commit changes:**
   - Summary: `Updated feature X`
   - Click "Commit to main"
5. **Push to GitHub:**
   - Click "Push origin" button
6. **Render auto-deploys:**
   - Render detects changes automatically
   - Rebuilds and redeploys (2-3 minutes)
   - No manual action needed!

---

## Success Checklist

- [ ] `.gitignore` file created
- [ ] GitHub Desktop installed
- [ ] Repository created in GitHub Desktop
- [ ] Files committed
- [ ] Repository published to GitHub
- [ ] Render account created
- [ ] Web service created on Render
- [ ] Environment variables added
- [ ] Build completed successfully
- [ ] Service is live (green checkmark)
- [ ] Live URL works
- [ ] Can access all pages
- [ ] Can perform CRUD operations
- [ ] MongoDB data persists

---

## Your Live URLs

After deployment, you'll have:

| Page | URL |
|------|-----|
| Home | https://your-app.onrender.com/ |
| Dashboard | https://your-app.onrender.com/dashboard |
| Menu | https://your-app.onrender.com/menu |
| Orders | https://your-app.onrender.com/orders |
| Feedback | https://your-app.onrender.com/feedback |

---

## For Your Assignment

Take screenshots of:
1. GitHub repository page
2. Render dashboard showing "Live" status
3. Live website home page
4. Live website dashboard
5. Performing CRUD operations on live site

---

## Deployment Summary

```
Local Development → GitHub Desktop → GitHub → Render → Live Website
                    (Version Control) (Cloud)  (Deploy) (Public URL)
```

**Congratulations! Your restaurant system is now live on the internet!**
