"""
Restaurant Food Ordering System - Main GUI Application
A complete menu management, order tracking, and feedback system using MongoDB Atlas
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from database import Database
from datetime import datetime


class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Food Ordering System")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f0f0f0")

        # Initialize database
        self.db = Database()

        # Connection status
        self.connected = False

        # Create main UI
        self.create_header()
        self.create_connection_frame()
        self.create_main_content()

        # Center window
        self.center_window()

    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_header(self):
        """Create header section"""
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        title = tk.Label(
            header_frame,
            text="🍽️ Restaurant Food Ordering System",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title.pack(pady=20)

    def create_connection_frame(self):
        """Create MongoDB connection section"""
        conn_frame = tk.Frame(self.root, bg="#ecf0f1", height=60)
        conn_frame.pack(fill=tk.X, padx=20, pady=10)

        self.conn_status_label = tk.Label(
            conn_frame,
            text="⚠️ Not Connected to MongoDB Atlas",
            font=("Arial", 11),
            bg="#ecf0f1",
            fg="#e74c3c"
        )
        self.conn_status_label.pack(side=tk.LEFT, padx=10)

        self.connect_btn = tk.Button(
            conn_frame,
            text="Connect to MongoDB",
            command=self.connect_to_mongodb,
            bg="#3498db",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=8,
            cursor="hand2"
        )
        self.connect_btn.pack(side=tk.RIGHT, padx=10)

    def create_main_content(self):
        """Create main content area with tabs"""
        # Create notebook (tabbed interface)
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', font=('Arial', 11, 'bold'), padding=[20, 10])

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Create tabs
        self.create_menu_tab()
        self.create_order_tab()
        self.create_feedback_tab()

        # Disable tabs initially
        self.toggle_tabs(False)

    def toggle_tabs(self, enable):
        """Enable or disable tabs based on connection status"""
        state = 'normal' if enable else 'disabled'
        for i in range(self.notebook.index('end')):
            self.notebook.tab(i, state=state)

    # ============ CONNECTION ============

    def connect_to_mongodb(self):
        """Connect to MongoDB Atlas"""
        success, message = self.db.connect()
        if success:
            self.connected = True
            self.conn_status_label.config(
                text="✅ Connected to MongoDB Atlas",
                fg="#27ae60"
            )
            self.connect_btn.config(
                text="Disconnect",
                command=self.disconnect_from_mongodb,
                bg="#e74c3c"
            )
            self.toggle_tabs(True)
            messagebox.showinfo("Success", message)
            # Load initial data
            self.refresh_menu_list()
            self.refresh_order_list()
            self.refresh_feedback_list()
        else:
            messagebox.showerror("Connection Error", message)

    def disconnect_from_mongodb(self):
        """Disconnect from MongoDB"""
        self.db.disconnect()
        self.connected = False
        self.conn_status_label.config(
            text="⚠️ Not Connected to MongoDB Atlas",
            fg="#e74c3c"
        )
        self.connect_btn.config(
            text="Connect to MongoDB",
            command=self.connect_to_mongodb,
            bg="#3498db"
        )
        self.toggle_tabs(False)
        messagebox.showinfo("Disconnected", "Disconnected from MongoDB Atlas")

    # ============ MENU MANAGEMENT TAB ============

    def create_menu_tab(self):
        """Create menu management tab"""
        menu_tab = tk.Frame(self.notebook, bg="white")
        self.notebook.add(menu_tab, text="📋 Menu Management")

        # Split into left and right panels
        left_panel = tk.Frame(menu_tab, bg="white", width=400)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        left_panel.pack_propagate(False)

        right_panel = tk.Frame(menu_tab, bg="white")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left Panel - Add/Edit Form
        form_label = tk.Label(
            left_panel,
            text="Add/Edit Menu Item",
            font=("Arial", 14, "bold"),
            bg="white"
        )
        form_label.pack(pady=10)

        # Form fields
        tk.Label(left_panel, text="Item Name:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=10)
        self.menu_name_entry = tk.Entry(left_panel, font=("Arial", 10))
        self.menu_name_entry.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(left_panel, text="Category:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=10)
        self.menu_category_combo = ttk.Combobox(
            left_panel,
            values=["Appetizer", "Main Course", "Dessert", "Beverage", "Side Dish"],
            font=("Arial", 10),
            state="readonly"
        )
        self.menu_category_combo.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(left_panel, text="Price (₹):", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=10)
        self.menu_price_entry = tk.Entry(left_panel, font=("Arial", 10))
        self.menu_price_entry.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(left_panel, text="Description:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=10)
        self.menu_desc_text = tk.Text(left_panel, height=4, font=("Arial", 10))
        self.menu_desc_text.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.menu_available_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            left_panel,
            text="Available",
            variable=self.menu_available_var,
            bg="white",
            font=("Arial", 10)
        ).pack(anchor=tk.W, padx=10, pady=5)

        # Buttons
        button_frame = tk.Frame(left_panel, bg="white")
        button_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Button(
            button_frame,
            text="Add Item",
            command=self.add_menu_item,
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        tk.Button(
            button_frame,
            text="Update Item",
            command=self.update_menu_item,
            bg="#f39c12",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_menu_form,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        # Right Panel - Menu List
        list_label = tk.Label(
            right_panel,
            text="Menu Items List",
            font=("Arial", 14, "bold"),
            bg="white"
        )
        list_label.pack(pady=10)

        # Search bar
        search_frame = tk.Frame(right_panel, bg="white")
        search_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(search_frame, text="Search:", bg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.menu_search_entry = tk.Entry(search_frame, font=("Arial", 10))
        self.menu_search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        tk.Button(
            search_frame,
            text="Search",
            command=self.search_menu,
            bg="#3498db",
            fg="white",
            font=("Arial", 9, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            search_frame,
            text="Refresh",
            command=self.refresh_menu_list,
            bg="#16a085",
            fg="white",
            font=("Arial", 9, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)

        # Treeview for menu items
        tree_frame = tk.Frame(right_panel, bg="white")
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        scrollbar = tk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.menu_tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "Name", "Category", "Price", "Available"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=self.menu_tree.yview)

        self.menu_tree.heading("ID", text="ID")
        self.menu_tree.heading("Name", text="Name")
        self.menu_tree.heading("Category", text="Category")
        self.menu_tree.heading("Price", text="Price (₹)")
        self.menu_tree.heading("Available", text="Available")

        self.menu_tree.column("ID", width=200)
        self.menu_tree.column("Name", width=150)
        self.menu_tree.column("Category", width=100)
        self.menu_tree.column("Price", width=80)
        self.menu_tree.column("Available", width=80)

        self.menu_tree.pack(fill=tk.BOTH, expand=True)
        self.menu_tree.bind('<ButtonRelease-1>', self.on_menu_select)

        # Action buttons
        action_frame = tk.Frame(right_panel, bg="white")
        action_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Button(
            action_frame,
            text="Delete Selected",
            command=self.delete_menu_item,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)

        self.selected_menu_id = None

    def add_menu_item(self):
        """Add new menu item"""
        name = self.menu_name_entry.get().strip()
        category = self.menu_category_combo.get()
        price = self.menu_price_entry.get().strip()
        description = self.menu_desc_text.get("1.0", tk.END).strip()
        available = self.menu_available_var.get()

        if not all([name, category, price]):
            messagebox.showwarning("Validation Error", "Please fill all required fields!")
            return

        try:
            float(price)
        except ValueError:
            messagebox.showerror("Invalid Price", "Please enter a valid price!")
            return

        success, message = self.db.add_menu_item(name, category, price, description, available)
        if success:
            messagebox.showinfo("Success", message)
            self.clear_menu_form()
            self.refresh_menu_list()
        else:
            messagebox.showerror("Error", message)

    def update_menu_item(self):
        """Update selected menu item"""
        if not self.selected_menu_id:
            messagebox.showwarning("No Selection", "Please select a menu item to update!")
            return

        name = self.menu_name_entry.get().strip()
        category = self.menu_category_combo.get()
        price = self.menu_price_entry.get().strip()
        description = self.menu_desc_text.get("1.0", tk.END).strip()
        available = self.menu_available_var.get()

        if not all([name, category, price]):
            messagebox.showwarning("Validation Error", "Please fill all required fields!")
            return

        try:
            float(price)
        except ValueError:
            messagebox.showerror("Invalid Price", "Please enter a valid price!")
            return

        success, message = self.db.update_menu_item(
            self.selected_menu_id, name, category, price, description, available
        )
        if success:
            messagebox.showinfo("Success", message)
            self.clear_menu_form()
            self.refresh_menu_list()
        else:
            messagebox.showerror("Error", message)

    def delete_menu_item(self):
        """Delete selected menu item"""
        if not self.selected_menu_id:
            messagebox.showwarning("No Selection", "Please select a menu item to delete!")
            return

        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this menu item?"):
            success, message = self.db.delete_menu_item(self.selected_menu_id)
            if success:
                messagebox.showinfo("Success", message)
                self.clear_menu_form()
                self.refresh_menu_list()
            else:
                messagebox.showerror("Error", message)

    def search_menu(self):
        """Search menu items"""
        search_term = self.menu_search_entry.get().strip()
        if not search_term:
            self.refresh_menu_list()
            return

        success, items = self.db.search_menu_items(search_term)
        if success:
            self.populate_menu_tree(items)
        else:
            messagebox.showerror("Error", items)

    def refresh_menu_list(self):
        """Refresh menu items list"""
        success, items = self.db.get_all_menu_items()
        if success:
            self.populate_menu_tree(items)
        else:
            messagebox.showerror("Error", items)

    def populate_menu_tree(self, items):
        """Populate menu treeview with items"""
        self.menu_tree.delete(*self.menu_tree.get_children())
        for item in items:
            self.menu_tree.insert("", tk.END, values=(
                str(item["_id"]),
                item["name"],
                item["category"],
                f"₹{item['price']:.2f}",
                "Yes" if item["availability"] else "No"
            ))

    def on_menu_select(self, event):
        """Handle menu item selection"""
        selection = self.menu_tree.selection()
        if selection:
            item = self.menu_tree.item(selection[0])
            values = item['values']
            self.selected_menu_id = values[0]

            # Fetch full details
            success, menu_item = self.db.get_menu_item_by_id(self.selected_menu_id)
            if success and menu_item:
                self.menu_name_entry.delete(0, tk.END)
                self.menu_name_entry.insert(0, menu_item["name"])

                self.menu_category_combo.set(menu_item["category"])

                self.menu_price_entry.delete(0, tk.END)
                self.menu_price_entry.insert(0, str(menu_item["price"]))

                self.menu_desc_text.delete("1.0", tk.END)
                self.menu_desc_text.insert("1.0", menu_item.get("description", ""))

                self.menu_available_var.set(menu_item["availability"])

    def clear_menu_form(self):
        """Clear menu form"""
        self.menu_name_entry.delete(0, tk.END)
        self.menu_category_combo.set("")
        self.menu_price_entry.delete(0, tk.END)
        self.menu_desc_text.delete("1.0", tk.END)
        self.menu_available_var.set(True)
        self.selected_menu_id = None

    # ============ ORDER TRACKING TAB ============

    def create_order_tab(self):
        """Create order tracking tab"""
        order_tab = tk.Frame(self.notebook, bg="white")
        self.notebook.add(order_tab, text="🛒 Order Tracking")

        # Split into left and right panels
        left_panel = tk.Frame(order_tab, bg="white", width=400)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        left_panel.pack_propagate(False)

        right_panel = tk.Frame(order_tab, bg="white")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left Panel - Create Order Form
        form_label = tk.Label(
            left_panel,
            text="Create New Order",
            font=("Arial", 14, "bold"),
            bg="white"
        )
        form_label.pack(pady=10)

        # Customer details
        tk.Label(left_panel, text="Customer Name:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=10)
        self.order_customer_entry = tk.Entry(left_panel, font=("Arial", 10))
        self.order_customer_entry.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(left_panel, text="Phone:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=10)
        self.order_phone_entry = tk.Entry(left_panel, font=("Arial", 10))
        self.order_phone_entry.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(left_panel, text="Order Items (one per line):", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=10)
        self.order_items_text = tk.Text(left_panel, height=6, font=("Arial", 10))
        self.order_items_text.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(left_panel, text="Total Amount (₹):", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=10)
        self.order_total_entry = tk.Entry(left_panel, font=("Arial", 10))
        self.order_total_entry.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(left_panel, text="Payment Method:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=10)
        self.order_payment_combo = ttk.Combobox(
            left_panel,
            values=["Cash", "Card", "UPI", "Online"],
            font=("Arial", 10),
            state="readonly"
        )
        self.order_payment_combo.pack(fill=tk.X, padx=10, pady=(0, 10))

        # Buttons
        button_frame = tk.Frame(left_panel, bg="white")
        button_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Button(
            button_frame,
            text="Create Order",
            command=self.create_order,
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_order_form,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        # Right Panel - Orders List
        list_label = tk.Label(
            right_panel,
            text="Orders List",
            font=("Arial", 14, "bold"),
            bg="white"
        )
        list_label.pack(pady=10)

        # Search bar
        search_frame = tk.Frame(right_panel, bg="white")
        search_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(search_frame, text="Search:", bg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.order_search_entry = tk.Entry(search_frame, font=("Arial", 10))
        self.order_search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        tk.Button(
            search_frame,
            text="Search",
            command=self.search_orders,
            bg="#3498db",
            fg="white",
            font=("Arial", 9, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            search_frame,
            text="Refresh",
            command=self.refresh_order_list,
            bg="#16a085",
            fg="white",
            font=("Arial", 9, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)

        # Treeview for orders
        tree_frame = tk.Frame(right_panel, bg="white")
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        scrollbar = tk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.order_tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "Customer", "Phone", "Total", "Status", "Date"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=self.order_tree.yview)

        self.order_tree.heading("ID", text="Order ID")
        self.order_tree.heading("Customer", text="Customer")
        self.order_tree.heading("Phone", text="Phone")
        self.order_tree.heading("Total", text="Total (₹)")
        self.order_tree.heading("Status", text="Status")
        self.order_tree.heading("Date", text="Date")

        self.order_tree.column("ID", width=200)
        self.order_tree.column("Customer", width=120)
        self.order_tree.column("Phone", width=100)
        self.order_tree.column("Total", width=80)
        self.order_tree.column("Status", width=100)
        self.order_tree.column("Date", width=150)

        self.order_tree.pack(fill=tk.BOTH, expand=True)

        # Action buttons
        action_frame = tk.Frame(right_panel, bg="white")
        action_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(action_frame, text="Update Status:", bg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.order_status_combo = ttk.Combobox(
            action_frame,
            values=["Pending", "Preparing", "Ready", "Delivered", "Cancelled"],
            font=("Arial", 9),
            state="readonly",
            width=15
        )
        self.order_status_combo.pack(side=tk.LEFT, padx=5)

        tk.Button(
            action_frame,
            text="Update Status",
            command=self.update_order_status,
            bg="#f39c12",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            action_frame,
            text="Delete Selected",
            command=self.delete_order,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)

        self.selected_order_id = None

    def create_order(self):
        """Create new order"""
        customer_name = self.order_customer_entry.get().strip()
        phone = self.order_phone_entry.get().strip()
        items_text = self.order_items_text.get("1.0", tk.END).strip()
        total = self.order_total_entry.get().strip()
        payment_method = self.order_payment_combo.get()

        if not all([customer_name, phone, items_text, total, payment_method]):
            messagebox.showwarning("Validation Error", "Please fill all fields!")
            return

        try:
            float(total)
        except ValueError:
            messagebox.showerror("Invalid Amount", "Please enter a valid total amount!")
            return

        # Parse items
        items = [item.strip() for item in items_text.split('\n') if item.strip()]

        success, message = self.db.create_order(customer_name, phone, items, total, payment_method)
        if success:
            messagebox.showinfo("Success", message)
            self.clear_order_form()
            self.refresh_order_list()
        else:
            messagebox.showerror("Error", message)

    def update_order_status(self):
        """Update order status"""
        selection = self.order_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select an order to update!")
            return

        new_status = self.order_status_combo.get()
        if not new_status:
            messagebox.showwarning("No Status", "Please select a status!")
            return

        item = self.order_tree.item(selection[0])
        order_id = item['values'][0]

        success, message = self.db.update_order_status(order_id, new_status)
        if success:
            messagebox.showinfo("Success", message)
            self.refresh_order_list()
        else:
            messagebox.showerror("Error", message)

    def delete_order(self):
        """Delete selected order"""
        selection = self.order_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select an order to delete!")
            return

        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this order?"):
            item = self.order_tree.item(selection[0])
            order_id = item['values'][0]

            success, message = self.db.delete_order(order_id)
            if success:
                messagebox.showinfo("Success", message)
                self.refresh_order_list()
            else:
                messagebox.showerror("Error", message)

    def search_orders(self):
        """Search orders"""
        search_term = self.order_search_entry.get().strip()
        if not search_term:
            self.refresh_order_list()
            return

        success, orders = self.db.search_orders(search_term)
        if success:
            self.populate_order_tree(orders)
        else:
            messagebox.showerror("Error", orders)

    def refresh_order_list(self):
        """Refresh orders list"""
        success, orders = self.db.get_all_orders()
        if success:
            self.populate_order_tree(orders)
        else:
            messagebox.showerror("Error", orders)

    def populate_order_tree(self, orders):
        """Populate order treeview"""
        self.order_tree.delete(*self.order_tree.get_children())
        for order in orders:
            date_str = order["order_date"].strftime("%Y-%m-%d %H:%M")
            self.order_tree.insert("", tk.END, values=(
                str(order["_id"]),
                order["customer_name"],
                order["phone"],
                f"₹{order['total_amount']:.2f}",
                order["status"],
                date_str
            ))

    def clear_order_form(self):
        """Clear order form"""
        self.order_customer_entry.delete(0, tk.END)
        self.order_phone_entry.delete(0, tk.END)
        self.order_items_text.delete("1.0", tk.END)
        self.order_total_entry.delete(0, tk.END)
        self.order_payment_combo.set("")

    # ============ FEEDBACK TAB ============

    def create_feedback_tab(self):
        """Create customer feedback tab"""
        feedback_tab = tk.Frame(self.notebook, bg="white")
        self.notebook.add(feedback_tab, text="⭐ Customer Feedback")

        # Split into left and right panels
        left_panel = tk.Frame(feedback_tab, bg="white", width=400)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        left_panel.pack_propagate(False)

        right_panel = tk.Frame(feedback_tab, bg="white")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left Panel - Submit Feedback Form
        form_label = tk.Label(
            left_panel,
            text="Submit Feedback",
            font=("Arial", 14, "bold"),
            bg="white"
        )
        form_label.pack(pady=10)

        tk.Label(left_panel, text="Customer Name:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=10)
        self.feedback_name_entry = tk.Entry(left_panel, font=("Arial", 10))
        self.feedback_name_entry.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(left_panel, text="Email:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=10)
        self.feedback_email_entry = tk.Entry(left_panel, font=("Arial", 10))
        self.feedback_email_entry.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(left_panel, text="Rating (1-5):", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=10)
        self.feedback_rating_scale = tk.Scale(
            left_panel,
            from_=1,
            to=5,
            orient=tk.HORIZONTAL,
            bg="white",
            font=("Arial", 10)
        )
        self.feedback_rating_scale.set(5)
        self.feedback_rating_scale.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(left_panel, text="Comments:", bg="white", font=("Arial", 10)).pack(anchor=tk.W, padx=10)
        self.feedback_comments_text = tk.Text(left_panel, height=8, font=("Arial", 10))
        self.feedback_comments_text.pack(fill=tk.X, padx=10, pady=(0, 10))

        # Buttons
        button_frame = tk.Frame(left_panel, bg="white")
        button_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Button(
            button_frame,
            text="Submit Feedback",
            command=self.submit_feedback,
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_feedback_form,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        # Right Panel - Feedback List
        list_label = tk.Label(
            right_panel,
            text="Customer Feedback",
            font=("Arial", 14, "bold"),
            bg="white"
        )
        list_label.pack(pady=10)

        # Statistics frame
        stats_frame = tk.Frame(right_panel, bg="#ecf0f1", relief=tk.RIDGE, borderwidth=2)
        stats_frame.pack(fill=tk.X, padx=10, pady=5)

        self.avg_rating_label = tk.Label(
            stats_frame,
            text="Average Rating: N/A",
            font=("Arial", 11, "bold"),
            bg="#ecf0f1"
        )
        self.avg_rating_label.pack(pady=10)

        # Refresh button
        tk.Button(
            right_panel,
            text="Refresh Feedback",
            command=self.refresh_feedback_list,
            bg="#16a085",
            fg="white",
            font=("Arial", 9, "bold"),
            cursor="hand2"
        ).pack(pady=5)

        # Treeview for feedback
        tree_frame = tk.Frame(right_panel, bg="white")
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        scrollbar = tk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.feedback_tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "Customer", "Email", "Rating", "Date"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=self.feedback_tree.yview)

        self.feedback_tree.heading("ID", text="Feedback ID")
        self.feedback_tree.heading("Customer", text="Customer")
        self.feedback_tree.heading("Email", text="Email")
        self.feedback_tree.heading("Rating", text="Rating")
        self.feedback_tree.heading("Date", text="Date")

        self.feedback_tree.column("ID", width=200)
        self.feedback_tree.column("Customer", width=120)
        self.feedback_tree.column("Email", width=150)
        self.feedback_tree.column("Rating", width=80)
        self.feedback_tree.column("Date", width=150)

        self.feedback_tree.pack(fill=tk.BOTH, expand=True)
        self.feedback_tree.bind('<ButtonRelease-1>', self.on_feedback_select)

        # Action buttons
        action_frame = tk.Frame(right_panel, bg="white")
        action_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Button(
            action_frame,
            text="View Details",
            command=self.view_feedback_details,
            bg="#3498db",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            action_frame,
            text="Delete Selected",
            command=self.delete_feedback,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)

        self.selected_feedback_id = None

    def submit_feedback(self):
        """Submit customer feedback"""
        customer_name = self.feedback_name_entry.get().strip()
        email = self.feedback_email_entry.get().strip()
        rating = self.feedback_rating_scale.get()
        comments = self.feedback_comments_text.get("1.0", tk.END).strip()

        if not all([customer_name, email, comments]):
            messagebox.showwarning("Validation Error", "Please fill all fields!")
            return

        success, message = self.db.add_feedback(customer_name, email, rating, comments)
        if success:
            messagebox.showinfo("Success", "Thank you for your feedback!")
            self.clear_feedback_form()
            self.refresh_feedback_list()
        else:
            messagebox.showerror("Error", message)

    def delete_feedback(self):
        """Delete selected feedback"""
        selection = self.feedback_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select feedback to delete!")
            return

        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this feedback?"):
            item = self.feedback_tree.item(selection[0])
            feedback_id = item['values'][0]

            success, message = self.db.delete_feedback(feedback_id)
            if success:
                messagebox.showinfo("Success", message)
                self.refresh_feedback_list()
            else:
                messagebox.showerror("Error", message)

    def view_feedback_details(self):
        """View detailed feedback"""
        selection = self.feedback_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select feedback to view!")
            return

        item = self.feedback_tree.item(selection[0])
        feedback_id = item['values'][0]

        success, feedback = self.db.get_feedback_by_id(feedback_id)
        if success and feedback:
            details = f"Customer: {feedback['customer_name']}\n"
            details += f"Email: {feedback['email']}\n"
            details += f"Rating: {feedback['rating']}/5 ⭐\n"
            details += f"Date: {feedback['feedback_date'].strftime('%Y-%m-%d %H:%M')}\n\n"
            details += f"Comments:\n{feedback['comments']}"

            messagebox.showinfo("Feedback Details", details)
        else:
            messagebox.showerror("Error", "Failed to retrieve feedback details")

    def refresh_feedback_list(self):
        """Refresh feedback list"""
        success, feedback_list = self.db.get_all_feedback()
        if success:
            self.populate_feedback_tree(feedback_list)
            # Update average rating
            success, stats = self.db.get_average_rating()
            if success:
                avg = stats.get('average_rating', 0)
                total = stats.get('total_feedback', 0)
                self.avg_rating_label.config(
                    text=f"Average Rating: {avg:.2f} ⭐ ({total} reviews)"
                )
        else:
            messagebox.showerror("Error", feedback_list)

    def populate_feedback_tree(self, feedback_list):
        """Populate feedback treeview"""
        self.feedback_tree.delete(*self.feedback_tree.get_children())
        for feedback in feedback_list:
            date_str = feedback["feedback_date"].strftime("%Y-%m-%d %H:%M")
            self.feedback_tree.insert("", tk.END, values=(
                str(feedback["_id"]),
                feedback["customer_name"],
                feedback["email"],
                f"{feedback['rating']}/5 ⭐",
                date_str
            ))

    def on_feedback_select(self, event):
        """Handle feedback selection"""
        selection = self.feedback_tree.selection()
        if selection:
            item = self.feedback_tree.item(selection[0])
            self.selected_feedback_id = item['values'][0]

    def clear_feedback_form(self):
        """Clear feedback form"""
        self.feedback_name_entry.delete(0, tk.END)
        self.feedback_email_entry.delete(0, tk.END)
        self.feedback_rating_scale.set(5)
        self.feedback_comments_text.delete("1.0", tk.END)


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
