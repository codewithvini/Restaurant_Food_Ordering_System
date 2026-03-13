"""
Restaurant Food Ordering System - Flask Web Application
Run this with: python app.py
Access at: http://localhost:5000
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from database import Database
from datetime import datetime
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'restaurant_secret_key_2026'

# Initialize database
db = Database()

# Connect to MongoDB when app starts
def connect_db():
    success, message = db.connect()
    if success:
        print("✅ Connected to MongoDB Atlas successfully!")
    else:
        print(f"⚠️ MongoDB connection warning: {message}")
        print("⚠️ Please update config.py with your MongoDB Atlas URI")

# ============ HOME & MAIN ROUTES ============

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Main dashboard"""
    # Get statistics
    success, menu_items = db.get_all_menu_items()
    menu_count = len(menu_items) if success else 0

    success, orders = db.get_all_orders()
    orders_count = len(orders) if success else 0

    success, feedback = db.get_all_feedback()
    feedback_count = len(feedback) if success else 0

    success, stats = db.get_average_rating()
    avg_rating = stats.get('average_rating', 0) if success else 0

    return render_template('dashboard.html',
                         menu_count=menu_count,
                         orders_count=orders_count,
                         feedback_count=feedback_count,
                         avg_rating=avg_rating)

# ============ MENU MANAGEMENT ROUTES ============

@app.route('/menu')
def menu():
    """Menu management page"""
    success, items = db.get_all_menu_items()
    menu_items = items if success else []
    return render_template('menu.html', menu_items=menu_items)

@app.route('/api/menu', methods=['GET'])
def get_menu_items():
    """API: Get all menu items"""
    success, items = db.get_all_menu_items()
    if success:
        # Convert ObjectId to string
        for item in items:
            item['_id'] = str(item['_id'])
            if 'created_at' in item:
                item['created_at'] = item['created_at'].isoformat()
        return jsonify({'success': True, 'data': items})
    return jsonify({'success': False, 'message': items})

@app.route('/api/menu', methods=['POST'])
def add_menu_item():
    """API: Add new menu item"""
    data = request.json
    success, message = db.add_menu_item(
        data['name'],
        data['category'],
        data['price'],
        data['description'],
        data.get('availability', True)
    )
    return jsonify({'success': success, 'message': message})

@app.route('/api/menu/<item_id>', methods=['PUT'])
def update_menu_item(item_id):
    """API: Update menu item"""
    data = request.json
    success, message = db.update_menu_item(
        item_id,
        data['name'],
        data['category'],
        data['price'],
        data['description'],
        data.get('availability', True)
    )
    return jsonify({'success': success, 'message': message})

@app.route('/api/menu/<item_id>', methods=['DELETE'])
def delete_menu_item(item_id):
    """API: Delete menu item"""
    success, message = db.delete_menu_item(item_id)
    return jsonify({'success': success, 'message': message})

@app.route('/api/menu/search', methods=['GET'])
def search_menu():
    """API: Search menu items"""
    search_term = request.args.get('q', '')
    success, items = db.search_menu_items(search_term)
    if success:
        for item in items:
            item['_id'] = str(item['_id'])
            if 'created_at' in item:
                item['created_at'] = item['created_at'].isoformat()
        return jsonify({'success': True, 'data': items})
    return jsonify({'success': False, 'message': items})

# ============ ORDER TRACKING ROUTES ============

@app.route('/orders')
def orders():
    """Order tracking page"""
    success, order_list = db.get_all_orders()
    orders_data = order_list if success else []
    return render_template('orders.html', orders=orders_data)

@app.route('/api/orders', methods=['GET'])
def get_orders():
    """API: Get all orders"""
    success, orders = db.get_all_orders()
    if success:
        for order in orders:
            order['_id'] = str(order['_id'])
            if 'order_date' in order:
                order['order_date'] = order['order_date'].isoformat()
        return jsonify({'success': True, 'data': orders})
    return jsonify({'success': False, 'message': orders})

@app.route('/api/orders', methods=['POST'])
def create_order():
    """API: Create new order"""
    data = request.json
    success, message = db.create_order(
        data['customer_name'],
        data['phone'],
        data['items'],
        data['total_amount'],
        data['payment_method']
    )
    return jsonify({'success': success, 'message': message})

@app.route('/api/orders/<order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    """API: Update order status"""
    data = request.json
    success, message = db.update_order_status(order_id, data['status'])
    return jsonify({'success': success, 'message': message})

@app.route('/api/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    """API: Delete order"""
    success, message = db.delete_order(order_id)
    return jsonify({'success': success, 'message': message})

@app.route('/api/orders/search', methods=['GET'])
def search_orders():
    """API: Search orders"""
    search_term = request.args.get('q', '')
    success, orders = db.search_orders(search_term)
    if success:
        for order in orders:
            order['_id'] = str(order['_id'])
            if 'order_date' in order:
                order['order_date'] = order['order_date'].isoformat()
        return jsonify({'success': True, 'data': orders})
    return jsonify({'success': False, 'message': orders})

# ============ FEEDBACK ROUTES ============

@app.route('/feedback')
def feedback():
    """Feedback page"""
    success, feedback_list = db.get_all_feedback()
    feedbacks = feedback_list if success else []

    success, stats = db.get_average_rating()
    avg_rating = stats.get('average_rating', 0) if success else 0
    total_feedback = stats.get('total_feedback', 0) if success else 0

    return render_template('feedback.html',
                         feedbacks=feedbacks,
                         avg_rating=avg_rating,
                         total_feedback=total_feedback)

@app.route('/api/feedback', methods=['GET'])
def get_feedback():
    """API: Get all feedback"""
    success, feedback_list = db.get_all_feedback()
    if success:
        for fb in feedback_list:
            fb['_id'] = str(fb['_id'])
            if 'feedback_date' in fb:
                fb['feedback_date'] = fb['feedback_date'].isoformat()
        return jsonify({'success': True, 'data': feedback_list})
    return jsonify({'success': False, 'message': feedback_list})

@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """API: Submit feedback"""
    data = request.json
    success, message = db.add_feedback(
        data['customer_name'],
        data['email'],
        data['rating'],
        data['comments']
    )
    return jsonify({'success': success, 'message': message})

@app.route('/api/feedback/<feedback_id>', methods=['DELETE'])
def delete_feedback_item(feedback_id):
    """API: Delete feedback"""
    success, message = db.delete_feedback(feedback_id)
    return jsonify({'success': success, 'message': message})

@app.route('/api/feedback/stats', methods=['GET'])
def get_feedback_stats():
    """API: Get feedback statistics"""
    success, stats = db.get_average_rating()
    if success:
        return jsonify({'success': True, 'data': stats})
    return jsonify({'success': False, 'message': stats})

# ============ ERROR HANDLERS ============

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

# ============ RUN APPLICATION ============

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🍽️  Restaurant Food Ordering System")
    print("="*60)
    print("\n🌐 Starting web server...")

    # Connect to MongoDB
    connect_db()

    print("\n📍 Access the application at:")
    print("   → http://localhost:5000")
    print("   → http://127.0.0.1:5000")
    print("\n⚠️  Make sure MongoDB Atlas is configured in config.py")
    print("\n🛑 Press CTRL+C to stop the server")
    print("="*60 + "\n")

    # Get port from environment variable (for Render deployment) or use 5000 for local
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
