"""
Quick UI Test - Run this to see the interface without MongoDB
"""

import tkinter as tk
from tkinter import ttk

def create_test_window():
    root = tk.Tk()
    root.title("Restaurant Food Ordering System - UI Test")
    root.geometry("1200x700")
    root.configure(bg="#f0f0f0")

    # Header
    header_frame = tk.Frame(root, bg="#2c3e50", height=80)
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

    # Connection frame
    conn_frame = tk.Frame(root, bg="#ecf0f1", height=60)
    conn_frame.pack(fill=tk.X, padx=20, pady=10)

    conn_label = tk.Label(
        conn_frame,
        text="⚠️ This is a UI test - MongoDB not connected",
        font=("Arial", 11),
        bg="#ecf0f1",
        fg="#e74c3c"
    )
    conn_label.pack(side=tk.LEFT, padx=10)

    test_button = tk.Button(
        conn_frame,
        text="UI Test Mode",
        bg="#95a5a6",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8
    )
    test_button.pack(side=tk.RIGHT, padx=10)

    # Tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    # Menu Tab
    menu_tab = tk.Frame(notebook, bg="white")
    notebook.add(menu_tab, text="📋 Menu Management")

    menu_label = tk.Label(
        menu_tab,
        text="✅ Menu Management UI\n\nThis tab will show menu items.\nYou can add, edit, delete, and search items.",
        font=("Arial", 14),
        bg="white",
        fg="#2c3e50"
    )
    menu_label.pack(pady=100)

    # Order Tab
    order_tab = tk.Frame(notebook, bg="white")
    notebook.add(order_tab, text="🛒 Order Tracking")

    order_label = tk.Label(
        order_tab,
        text="✅ Order Tracking UI\n\nThis tab will show customer orders.\nYou can create orders and update their status.",
        font=("Arial", 14),
        bg="white",
        fg="#2c3e50"
    )
    order_label.pack(pady=100)

    # Feedback Tab
    feedback_tab = tk.Frame(notebook, bg="white")
    notebook.add(feedback_tab, text="⭐ Customer Feedback")

    feedback_label = tk.Label(
        feedback_tab,
        text="✅ Customer Feedback UI\n\nThis tab will show customer reviews and ratings.\nAverage rating is calculated automatically.",
        font=("Arial", 14),
        bg="white",
        fg="#2c3e50"
    )
    feedback_label.pack(pady=100)

    # Info label
    info_label = tk.Label(
        root,
        text="📝 This is just a UI test. To use the full app, setup MongoDB Atlas and run restaurant_app.py",
        font=("Arial", 10),
        bg="#f0f0f0",
        fg="#7f8c8d"
    )
    info_label.pack(pady=10)

    print("\n" + "="*60)
    print("✅ UI TEST WINDOW OPENED!")
    print("="*60)
    print("\nThe application window should be visible on your screen.")
    print("This is just a preview - the real app needs MongoDB Atlas.")
    print("\nTo use the full application:")
    print("1. Setup MongoDB Atlas (see MONGODB_ATLAS_SETUP.md)")
    print("2. Update config.py with your connection string")
    print("3. Run: python restaurant_app.py")
    print("\nClose the window to exit this test.")
    print("="*60 + "\n")

    root.mainloop()

if __name__ == "__main__":
    create_test_window()
