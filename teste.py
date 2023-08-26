from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox

class ComboBoxApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ComboBox Example")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.combo_box = QComboBox()
        layout.addWidget(self.combo_box)

        self.add_button = QPushButton("Add Item")
        self.add_button.clicked.connect(self.add_item)
        layout.addWidget(self.add_button)

        central_widget.setLayout(layout)

    def add_item(self):
        new_item = "New Item"  # You can replace this with user input
        user_data = "UserData"  # You can replace this with any data you want

        self.combo_box.addItem(new_item, user_data)

if __name__ == "__main__":
    app = QApplication([])
    window = ComboBoxApp()
    window.show()
    app.exec()
