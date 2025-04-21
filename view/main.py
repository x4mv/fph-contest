import sys
import random
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class TablaDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FPH CONTEST WORKFLOW")
        self.setGeometry(200, 200, 800, 600)

        layout = QVBoxLayout()

        # Crear la tabla con 3 filas y 2 columnas
        self.tabla = QTableWidget(6, 5)

        # Agregar encabezados
        self.tabla.setHorizontalHeaderLabels(["Nro","Nombre", "Categoria", "Nacimiento", "Equipo"])

        # Insertar datos
        self.tabla.setItem(0, 0, QTableWidgetItem("1"))
        self.tabla.setItem(0, 1, QTableWidgetItem("Sergio"))
        self.tabla.setItem(0, 2, QTableWidgetItem("77"))
        self.tabla.setItem(0, 3, QTableWidgetItem("2003"))
        self.tabla.setItem(0, 4, QTableWidgetItem("FPH"))


        layout.addWidget(self.tabla)
        self.setLayout(layout)
        

if __name__ == "__main__":
    app = QApplication([])
    ventana = TablaDemo()
    ventana.show()
    app.exec()