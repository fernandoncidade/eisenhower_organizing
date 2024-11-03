import sys
import json
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem,
                               QMessageBox, QComboBox)
from PySide6.QtCore import Qt


class EisenhowerMatrixApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matriz de Eisenhower - Organização de Estudos")
        self.setGeometry(100, 100, 600, 500)

        self.initUI()
        self.load_tasks()

    def initUI(self):
        main_layout = QVBoxLayout()

        # Input fields
        input_layout = QHBoxLayout()

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Adicione uma tarefa...")
        input_layout.addWidget(self.task_input)

        self.quadrant_selector = QComboBox(self)
        self.quadrant_selector.addItems([
            "Importante e Urgente",
            "Importante, mas Não Urgente",
            "Não Importante, mas Urgente",
            "Não Importante e Não Urgente"
        ])
        input_layout.addWidget(self.quadrant_selector)

        add_button = QPushButton("Adicionar Tarefa")
        add_button.clicked.connect(self.add_task)
        input_layout.addWidget(add_button)

        main_layout.addLayout(input_layout)

        # Quadrants
        quadrant_layout = QHBoxLayout()

        # Quadrant 1
        quadrant1_layout = QVBoxLayout()
        quadrant1_label = QLabel("Importante e Urgente")
        self.quadrant1_list = QListWidget()
        self.add_placeholder(self.quadrant1_list, "1º Quadrante")
        quadrant1_layout.addWidget(quadrant1_label)
        quadrant1_layout.addWidget(self.quadrant1_list)

        # Quadrant 2
        quadrant2_layout = QVBoxLayout()
        quadrant2_label = QLabel("Importante, mas Não Urgente")
        self.quadrant2_list = QListWidget()
        self.add_placeholder(self.quadrant2_list, "2º Quadrante")
        quadrant2_layout.addWidget(quadrant2_label)
        quadrant2_layout.addWidget(self.quadrant2_list)

        # Quadrant 3
        quadrant3_layout = QVBoxLayout()
        quadrant3_label = QLabel("Não Importante, mas Urgente")
        self.quadrant3_list = QListWidget()
        self.add_placeholder(self.quadrant3_list, "3º Quadrante")
        quadrant3_layout.addWidget(quadrant3_label)
        quadrant3_layout.addWidget(self.quadrant3_list)

        # Quadrant 4
        quadrant4_layout = QVBoxLayout()
        quadrant4_label = QLabel("Não Importante e Não Urgente")
        self.quadrant4_list = QListWidget()
        self.add_placeholder(self.quadrant4_list, "4º Quadrante")
        quadrant4_layout.addWidget(quadrant4_label)
        quadrant4_layout.addWidget(self.quadrant4_list)

        # Add layouts to main layout
        quadrant_layout.addLayout(quadrant1_layout)
        quadrant_layout.addLayout(quadrant2_layout)
        quadrant_layout.addLayout(quadrant3_layout)
        quadrant_layout.addLayout(quadrant4_layout)

        main_layout.addLayout(quadrant_layout)

        # Main widget setup
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Connect double click to delete item
        self.quadrant1_list.itemDoubleClicked.connect(lambda item: self.remove_task(item, self.quadrant1_list))
        self.quadrant2_list.itemDoubleClicked.connect(lambda item: self.remove_task(item, self.quadrant2_list))
        self.quadrant3_list.itemDoubleClicked.connect(lambda item: self.remove_task(item, self.quadrant3_list))
        self.quadrant4_list.itemDoubleClicked.connect(lambda item: self.remove_task(item, self.quadrant4_list))

    def add_placeholder(self, list_widget, text):
        placeholder_item = QListWidgetItem(text)
        placeholder_item.setFlags(placeholder_item.flags() & ~Qt.ItemIsSelectable)
        placeholder_item.setForeground(Qt.gray)
        list_widget.addItem(placeholder_item)

    def add_task(self):
        task_text = self.task_input.text().strip()
        if not task_text:
            QMessageBox.warning(self, "Erro", "A tarefa não pode estar vazia.")
            return

        selected_quadrant = self.quadrant_selector.currentIndex()

        # Remove placeholder if present
        if self.quadrant1_list.count() == 1 and self.quadrant1_list.item(0).foreground() == Qt.gray:
            self.quadrant1_list.clear()
        if self.quadrant2_list.count() == 1 and self.quadrant2_list.item(0).foreground() == Qt.gray:
            self.quadrant2_list.clear()
        if self.quadrant3_list.count() == 1 and self.quadrant3_list.item(0).foreground() == Qt.gray:
            self.quadrant3_list.clear()
        if self.quadrant4_list.count() == 1 and self.quadrant4_list.item(0).foreground() == Qt.gray:
            self.quadrant4_list.clear()

        # Add task to the correct quadrant list
        task_item = QListWidgetItem(task_text)
        if selected_quadrant == 0:
            self.quadrant1_list.addItem(task_item)
        elif selected_quadrant == 1:
            self.quadrant2_list.addItem(task_item)
        elif selected_quadrant == 2:
            self.quadrant3_list.addItem(task_item)
        elif selected_quadrant == 3:
            self.quadrant4_list.addItem(task_item)

        self.task_input.clear()
        self.save_tasks()

    def remove_task(self, item, list_widget):
        reply = QMessageBox.question(
            self, "Remover Tarefa", f"Deseja remover a tarefa '{item.text()}'?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            list_widget.takeItem(list_widget.row(item))
            if list_widget.count() == 0:
                self.add_placeholder(list_widget, "Quadrante Vazio")
            self.save_tasks()

    def save_tasks(self):
        tasks = {
            "quadrant1": [self.quadrant1_list.item(i).text() for i in range(self.quadrant1_list.count()) if self.quadrant1_list.item(i).foreground() != Qt.gray],
            "quadrant2": [self.quadrant2_list.item(i).text() for i in range(self.quadrant2_list.count()) if self.quadrant2_list.item(i).foreground() != Qt.gray],
            "quadrant3": [self.quadrant3_list.item(i).text() for i in range(self.quadrant3_list.count()) if self.quadrant3_list.item(i).foreground() != Qt.gray],
            "quadrant4": [self.quadrant4_list.item(i).text() for i in range(self.quadrant4_list.count()) if self.quadrant4_list.item(i).foreground() != Qt.gray],
        }
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
                if tasks["quadrant1"]:
                    self.quadrant1_list.clear()
                    for task in tasks["quadrant1"]:
                        self.quadrant1_list.addItem(QListWidgetItem(task))

                if tasks["quadrant2"]:
                    self.quadrant2_list.clear()
                    for task in tasks["quadrant2"]:
                        self.quadrant2_list.addItem(QListWidgetItem(task))

                if tasks["quadrant3"]:
                    self.quadrant3_list.clear()
                    for task in tasks["quadrant3"]:
                        self.quadrant3_list.addItem(QListWidgetItem(task))

                if tasks["quadrant4"]:
                    self.quadrant4_list.clear()
                    for task in tasks["quadrant4"]:
                        self.quadrant4_list.addItem(QListWidgetItem(task))
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EisenhowerMatrixApp()
    window.show()
    sys.exit(app.exec())
