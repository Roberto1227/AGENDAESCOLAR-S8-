import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QListWidget, QVBoxLayout, QHBoxLayout,
    QMessageBox
)
from PyQt5.QtCore import Qt 

class MiAgendaEscolar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Agenda Escolar ")
        self.setGeometry(100, 100, 400, 400)
        self.init_ui()

    def init_ui(self):
        # Widgets
        self.label_tarea = QLabel("Nombre de la tarea:")
        self.input_tarea = QLineEdit()

        self.label_materia = QLabel("Materia:")
        self.input_materia = QLineEdit()

        self.label_fecha = QLabel("Fecha límite:")
        self.input_fecha = QLineEdit()

        self.boton_agregar = QPushButton("Agregar tarea")
        self.boton_agregar.clicked.connect(self.agregar_tarea)

        self.lista_tareas = QListWidget()
        self.instruccion_doble_click = QLabel("Doble clic en una tarea para marcarla como completada ✅")

        # Layouts
        layout_principal = QVBoxLayout()

        layout_tarea = QHBoxLayout()
        layout_tarea.addWidget(self.label_tarea)
        layout_tarea.addWidget(self.input_tarea)

        layout_materia = QHBoxLayout()
        layout_materia.addWidget(self.label_materia)
        layout_materia.addWidget(self.input_materia)

        layout_fecha = QHBoxLayout()
        layout_fecha.addWidget(self.label_fecha)
        layout_fecha.addWidget(self.input_fecha)

        layout_principal.addLayout(layout_tarea)
        layout_principal.addLayout(layout_materia)
        layout_principal.addLayout(layout_fecha)
        layout_principal.addWidget(self.boton_agregar)
        layout_principal.addWidget(self.instruccion_doble_click)
        layout_principal.addWidget(self.lista_tareas)

        self.setLayout(layout_principal)

        # Doble clic para marcar como completada
        self.lista_tareas.itemDoubleClicked.connect(self.marcar_completada)

    def agregar_tarea(self):
        tarea = self.input_tarea.text()
        materia = self.input_materia.text()
        fecha = self.input_fecha.text()

        if tarea and materia and fecha:
            texto = f"{tarea} | {materia} | {fecha}"
            self.lista_tareas.addItem(texto)
            self.input_tarea.clear()
            self.input_materia.clear()
            self.input_fecha.clear()
            QMessageBox.information(self, "¡Tarea agregada!", "Tu tarea pendiente ha sido registrada")
        else:
            QMessageBox.warning(self, "Campos incompletos", "Por favor llena todos los campos.")

    def marcar_completada(self, item):
        item.setText(f"✅ {item.text()}")
        item.setForeground(Qt.gray)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiAgendaEscolar()
    ventana.show()
    sys.exit(app.exec_())