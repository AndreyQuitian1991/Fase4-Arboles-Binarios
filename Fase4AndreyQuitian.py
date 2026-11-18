"""
PHASE 4 - BINARY SEARCH TREE
Student: Anderson Andrey Quitian Perez
Course: Data Structures - 301305
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# ==================================================
# BINARY TREE NODE
# ==================================================

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ==================================================
# BINARY SEARCH TREE
# ==================================================

class BinarySearchTree:

    def __init__(self, max_levels=4):
        self.root = None
        self.max_levels = max_levels

    def insert(self, value):

        if self.root is None:
            self.root = TreeNode(value)
            return True

        current = self.root
        level = 1

        while True:

            if value == current.value:
                return False

            if value < current.value:

                if current.left is None:

                    if level + 1 > self.max_levels:
                        raise ValueError(
                            "The tree cannot exceed four levels."
                        )

                    current.left = TreeNode(value)
                    return True

                current = current.left

            else:

                if current.right is None:

                    if level + 1 > self.max_levels:
                        raise ValueError(
                            "The tree cannot exceed four levels."
                        )

                    current.right = TreeNode(value)
                    return True

                current = current.right

            level += 1

    def search(self, value):

        current = self.root

        while current is not None:

            if value == current.value:
                return True

            elif value < current.value:
                current = current.left

            else:
                current = current.right

        return False

    def preorder(self):

        result = []

        def visit(node):
            if node is not None:
                result.append(node.value)
                visit(node.left)
                visit(node.right)

        visit(self.root)
        return result

    def inorder(self):

        result = []

        def visit(node):
            if node is not None:
                visit(node.left)
                result.append(node.value)
                visit(node.right)

        visit(self.root)
        return result

    def postorder(self):

        result = []

        def visit(node):
            if node is not None:
                visit(node.left)
                visit(node.right)
                result.append(node.value)

        visit(self.root)
        return result

    def clear(self):
        self.root = None


# ==================================================
# LOGIN WINDOW
# ==================================================

class LoginWindow:

    def __init__(self, root):

        self.root = root

        self.root.title("Fase4AndreyQuitian - Login")
        self.root.geometry("520x430")
        self.root.resizable(False, False)
        self.root.configure(bg="#142536")

        self.create_widgets()

    def create_widgets(self):

        frame = tk.Frame(
            self.root,
            bg="#142536"
        )
        frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

        tk.Label(
            frame,
            text="BINARY SEARCH TREE",
            font=("Arial", 22, "bold"),
            fg="#35C6D8",
            bg="#142536"
        ).pack(pady=(25, 12))

        tk.Label(
            frame,
            text="Fase4AndreyQuitian",
            font=("Arial", 15, "bold"),
            fg="white",
            bg="#142536"
        ).pack(pady=6)

        tk.Label(
            frame,
            text="Student: Anderson Andrey Quitian Perez",
            font=("Arial", 10),
            fg="#D5DEE7",
            bg="#142536"
        ).pack(pady=6)

        tk.Label(
            frame,
            text="Course: Data Structures - 301305",
            font=("Arial", 10),
            fg="#D5DEE7",
            bg="#142536"
        ).pack(pady=6)

        tk.Label(
            frame,
            text="Date: " + datetime.now().strftime("%d/%m/%Y"),
            font=("Arial", 10),
            fg="#D5DEE7",
            bg="#142536"
        ).pack(pady=6)

        tk.Label(
            frame,
            text="Enter password:",
            font=("Arial", 11, "bold"),
            fg="white",
            bg="#142536"
        ).pack(pady=(25, 8))

        self.password_entry = tk.Entry(
            frame,
            show="*",
            font=("Arial", 13),
            justify="center",
            width=25
        )
        self.password_entry.pack(ipady=6)
        self.password_entry.focus()

        tk.Button(
            frame,
            text="LOGIN",
            font=("Arial", 11, "bold"),
            bg="#16A6BD",
            fg="white",
            activebackground="#12899D",
            command=self.validate_login,
            width=18,
            cursor="hand2"
        ).pack(pady=22)

        self.root.bind(
            "<Return>",
            lambda event: self.validate_login()
        )

    def validate_login(self):

        password = self.password_entry.get()

        if password == "UNAD":

            messagebox.showinfo(
                "Access granted",
                "Welcome to Binary Search Tree!"
            )

            for widget in self.root.winfo_children():
                widget.destroy()

            MainWindow(self.root)

        else:

            messagebox.showerror(
                "Access denied",
                "Incorrect password. Please try again."
            )

            self.password_entry.delete(0, tk.END)
            self.password_entry.focus()


# ==================================================
# MAIN APPLICATION
# ==================================================

class MainWindow:

    def __init__(self, root):

        self.root = root
        self.tree = BinarySearchTree(max_levels=4)
        self.highlighted_value = None

        self.root.title(
            "Fase4AndreyQuitian - Binary Search Tree"
        )

        self.root.configure(bg="#142536")
        self.root.minsize(850, 650)

        try:
            self.root.state("zoomed")
        except tk.TclError:
            self.root.geometry("1200x800")

        self.create_interface()

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.exit_application
        )

        self.root.bind(
            "<Return>",
            lambda event: self.add_node()
        )

        self.root.after(150, self.update_interface)

    # --------------------------------------------------
    # CREATE INTERFACE
    # --------------------------------------------------

    def create_interface(self):

        main_frame = tk.Frame(
            self.root,
            bg="#142536"
        )
        main_frame.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=10
        )

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(2, weight=5, minsize=260)
        main_frame.grid_rowconfigure(3, weight=2, minsize=145)

        # HEADER

        header = tk.Frame(
            main_frame,
            bg="#142536"
        )
        header.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0, 10)
        )

        header.grid_columnconfigure(0, weight=1)

        tk.Label(
            header,
            text="BINARY SEARCH TREE",
            font=("Arial", 22, "bold"),
            fg="#35C6D8",
            bg="#142536"
        ).grid(row=0, column=0, sticky="w")

        tk.Label(
            header,
            text="Data Structures - 301305",
            font=("Arial", 10),
            fg="white",
            bg="#142536"
        ).grid(row=0, column=1, sticky="e")

        # CONTROL PANEL

        controls = tk.LabelFrame(
            main_frame,
            text="Controls",
            font=("Arial", 11, "bold"),
            fg="white",
            bg="#20394D",
            bd=1
        )
        controls.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(0, 12)
        )

        controls.grid_columnconfigure(1, weight=1)

        tk.Label(
            controls,
            text="Enter an integer:",
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#20394D"
        ).grid(
            row=0,
            column=0,
            padx=12,
            pady=15
        )

        self.value_entry = tk.Entry(
            controls,
            font=("Arial", 12),
            justify="center",
            width=12
        )
        self.value_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=12,
            sticky="w"
        )

        tk.Button(
            controls,
            text="Add Node",
            command=self.add_node,
            bg="#16A6BD",
            fg="white",
            font=("Arial", 10, "bold"),
            width=11,
            cursor="hand2"
        ).grid(row=0, column=2, padx=5, pady=12)

        tk.Button(
            controls,
            text="Search Node",
            command=self.search_node,
            bg="#16A6BD",
            fg="white",
            font=("Arial", 10, "bold"),
            width=12,
            cursor="hand2"
        ).grid(row=0, column=3, padx=5, pady=12)

        tk.Button(
            controls,
            text="Clear",
            command=self.clear_tree,
            bg="#B77A1D",
            fg="white",
            font=("Arial", 10, "bold"),
            width=9,
            cursor="hand2"
        ).grid(row=0, column=4, padx=5, pady=12)

        tk.Button(
            controls,
            text="Exit",
            command=self.exit_application,
            bg="#B33A3A",
            fg="white",
            font=("Arial", 10, "bold"),
            width=9,
            cursor="hand2"
        ).grid(
            row=0,
            column=5,
            padx=12,
            pady=12,
            sticky="e"
        )

        # TREE PANEL

        tree_frame = tk.LabelFrame(
            main_frame,
            text="Panel 1 - Binary Search Tree",
            font=("Arial", 11, "bold"),
            fg="white",
            bg="#20394D",
            bd=1
        )
        tree_frame.grid(
            row=2,
            column=0,
            sticky="nsew",
            pady=(0, 12)
        )

        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        self.tree_canvas = tk.Canvas(
            tree_frame,
            bg="#F0F5FA",
            highlightthickness=0
        )
        self.tree_canvas.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=8,
            pady=8
        )

        self.tree_canvas.bind(
            "<Configure>",
            lambda event: self.draw_tree()
        )

        # TRAVERSAL PANELS

        traversal_frame = tk.Frame(
            main_frame,
            bg="#142536"
        )
        traversal_frame.grid(
            row=3,
            column=0,
            sticky="nsew"
        )

        for column in range(3):
            traversal_frame.grid_columnconfigure(
                column,
                weight=1,
                uniform="panels"
            )

        traversal_frame.grid_rowconfigure(0, weight=1)

        self.preorder_canvas = self.create_traversal_panel(
            traversal_frame,
            "Panel 2 - Preorder",
            0
        )

        self.inorder_canvas = self.create_traversal_panel(
            traversal_frame,
            "Panel 3 - Inorder",
            1
        )

        self.postorder_canvas = self.create_traversal_panel(
            traversal_frame,
            "Panel 4 - Postorder",
            2
        )

        # STATUS BAR

        self.status_label = tk.Label(
            main_frame,
            text="Ready. Enter an integer to begin.",
            font=("Arial", 9),
            fg="#D5DEE7",
            bg="#142536",
            anchor="w"
        )
        self.status_label.grid(
            row=4,
            column=0,
            sticky="ew",
            pady=(8, 0)
        )

    # --------------------------------------------------
    # CREATE TRAVERSAL PANEL
    # --------------------------------------------------

    def create_traversal_panel(self, parent, title, column):

        panel = tk.LabelFrame(
            parent,
            text=title,
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#20394D",
            bd=1
        )
        panel.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=5
        )

        panel.grid_rowconfigure(0, weight=1)
        panel.grid_columnconfigure(0, weight=1)

        canvas = tk.Canvas(
            panel,
            bg="#F0F5FA",
            highlightthickness=0,
            height=125
        )
        canvas.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=6,
            pady=6
        )

        return canvas

    # --------------------------------------------------
    # GET AND VALIDATE INPUT
    # --------------------------------------------------

    def get_input_value(self):

        raw_value = self.value_entry.get().strip()

        if not raw_value:
            messagebox.showwarning(
                "Missing value",
                "Please enter an integer."
            )
            self.value_entry.focus()
            return None

        try:
            return int(raw_value)

        except ValueError:

            messagebox.showerror(
                "Invalid input",
                "Please enter a valid integer."
            )

            self.value_entry.delete(0, tk.END)
            self.value_entry.focus()

            return None

    # --------------------------------------------------
    # ADD NODE
    # --------------------------------------------------

    def add_node(self):

        value = self.get_input_value()

        if value is None:
            return

        try:

            inserted = self.tree.insert(value)

            if not inserted:

                messagebox.showwarning(
                    "Duplicate value",
                    "This value already exists in the tree."
                )

                self.value_entry.delete(0, tk.END)
                self.value_entry.focus()
                return

            self.highlighted_value = None

            self.update_interface()

            self.status_label.config(
                text=f"Node {value} added successfully."
            )

            self.value_entry.delete(0, tk.END)
            self.value_entry.focus()

        except ValueError as error:

            messagebox.showerror(
                "Level limit reached",
                str(error)
            )

            self.value_entry.delete(0, tk.END)
            self.value_entry.focus()

    # --------------------------------------------------
    # SEARCH NODE
    # --------------------------------------------------

    def search_node(self):

        value = self.get_input_value()

        if value is None:
            return

        if self.tree.search(value):

            self.highlighted_value = value

            self.update_interface()

            messagebox.showinfo(
                "Search result",
                f"Node {value} was found in the tree."
            )

            self.status_label.config(
                text=f"Node {value} found successfully."
            )

        else:

            self.highlighted_value = None

            self.update_interface()

            messagebox.showwarning(
                "Search result",
                f"Node {value} does not exist in the tree."
            )

            self.status_label.config(
                text=f"Node {value} was not found."
            )

        self.value_entry.delete(0, tk.END)
        self.value_entry.focus()

    # --------------------------------------------------
    # DRAW MAIN TREE
    # --------------------------------------------------

    def draw_tree(self):

        canvas = self.tree_canvas
        canvas.delete("all")

        width = canvas.winfo_width()
        height = canvas.winfo_height()

        if width < 100 or height < 100:
            return

        if self.tree.root is None:

            canvas.create_text(
                width / 2,
                height / 2,
                text="The tree is empty. Add a node to begin.",
                font=("Arial", 14, "bold"),
                fill="#667788"
            )
            return

        radius = 19

        vertical_gap = (height - 90) / 3
        vertical_gap = max(45, vertical_gap)

        positions = {}

        def calculate_positions(node, depth, path):

            if node is None:
                return

            x = width * (path + 0.5) / (2 ** depth)
            y = 40 + depth * vertical_gap

            positions[node.value] = (x, y)

            calculate_positions(
                node.left,
                depth + 1,
                path * 2
            )

            calculate_positions(
                node.right,
                depth + 1,
                path * 2 + 1
            )

        calculate_positions(self.tree.root, 0, 0)

        # Draw connections first.

        def draw_connections(node):

            if node is None:
                return

            x, y = positions[node.value]

            for child in (node.left, node.right):

                if child is not None:

                    child_x, child_y = positions[child.value]

                    canvas.create_line(
                        x,
                        y + radius,
                        child_x,
                        child_y - radius,
                        fill="#526B80",
                        width=2
                    )

                    draw_connections(child)

        draw_connections(self.tree.root)

        # Draw nodes over the connections.

        for value, (x, y) in positions.items():

            if value == self.highlighted_value:
                color = "#E5A32B"
            else:
                color = "#16A6BD"

            canvas.create_oval(
                x - radius,
                y - radius,
                x + radius,
                y + radius,
                fill=color,
                outline="#142536",
                width=2
            )

            canvas.create_text(
                x,
                y,
                text=str(value),
                fill="white",
                font=("Arial", 10, "bold")
            )

    # --------------------------------------------------
    # DRAW BOTTOM TRAVERSAL PANELS
    # --------------------------------------------------

    def draw_traversal_panel(self, canvas, values):

        canvas.delete("all")

        width = canvas.winfo_width()
        height = canvas.winfo_height()

        if width < 50 or height < 40:
            return

        if not values:
            canvas.create_text(
                width / 2,
                height / 2,
                text="No nodes available.",
                font=("Arial", 10, "bold"),
                fill="#142536"
            )
            return

        # Each traversal is displayed as a connected visual sequence.
        count = len(values)
        margin = 14
        usable_width = max(1, width - 2 * margin)
        step = usable_width / count
        radius = min(14, step * 0.38, max(7, height * 0.20))
        center_y = height / 2

        centers = [
            margin + step * (index + 0.5)
            for index in range(count)
        ]

        # Draw arrows before drawing the nodes.

        for index in range(count - 1):
            canvas.create_line(
                centers[index] + radius,
                center_y,
                centers[index + 1] - radius,
                center_y,
                fill="#526B80",
                width=2,
                arrow=tk.LAST,
                arrowshape=(7, 8, 3)
            )

        # Draw the nodes in traversal order.

        for index, value in enumerate(values):
            x = centers[index]

            canvas.create_oval(
                x - radius,
                center_y - radius,
                x + radius,
                center_y + radius,
                fill="#16A6BD",
                outline="#142536",
                width=1.5
            )

            font_size = 9 if radius >= 11 else 7

            canvas.create_text(
                x,
                center_y,
                text=str(value),
                fill="white",
                font=("Arial", font_size, "bold")
            )

    # --------------------------------------------------
    # UPDATE TRAVERSAL PANELS
    # --------------------------------------------------

    def update_traversals(self):

        self.draw_traversal_panel(
            self.preorder_canvas,
            self.tree.preorder()
        )

        self.draw_traversal_panel(
            self.inorder_canvas,
            self.tree.inorder()
        )

        self.draw_traversal_panel(
            self.postorder_canvas,
            self.tree.postorder()
        )

    # --------------------------------------------------
    # UPDATE INTERFACE
    # --------------------------------------------------

    def update_interface(self):

        self.draw_tree()
        self.update_traversals()

    # --------------------------------------------------
    # CLEAR TREE
    # --------------------------------------------------

    def clear_tree(self):

        if self.tree.root is None:

            messagebox.showinfo(
                "Clear tree",
                "The tree is already empty."
            )
            return

        confirmation = messagebox.askyesno(
            "Clear tree",
            "Are you sure you want to delete all nodes?"
        )

        if confirmation:

            self.tree.clear()
            self.highlighted_value = None

            self.update_interface()

            self.status_label.config(
                text="The tree has been cleared."
            )

            self.value_entry.delete(0, tk.END)
            self.value_entry.focus()

    # --------------------------------------------------
    # EXIT APPLICATION
    # --------------------------------------------------

    def exit_application(self):

        confirmation = messagebox.askyesno(
            "Exit application",
            "Are you sure you want to close the application?"
        )

        if confirmation:
            self.root.destroy()


# ==================================================
# MAIN PROGRAM
# ==================================================

if __name__ == "__main__":

    root = tk.Tk()

    application = LoginWindow(root)

    root.mainloop()