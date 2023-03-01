from PyQt5.QtCore import QProcess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit

app = QApplication([])

button_w = 270
button_h = 116
window_w = 1080
window_h = 720
filepath_w = 700
filepath_h = 25
output_w = 500
output_h = 500

# window
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setFixedSize(window_w, window_h)

# button
button = QPushButton('RUN', window)
button.setFixedSize(button_w, button_h)
button.setGeometry((window_w-button_w)//2, 0, button_w, button_h)

# filepath
filepath = QTextEdit(window)
filepath.setFixedSize(filepath_w, filepath_h)
filepath.setPlaceholderText('Filepath')
filepath.setGeometry((window_w-filepath_w)//2, 150, filepath_w, filepath_h)

# output
output = QTextEdit(window)
output.setFixedSize(output_w, output_h)
output.setReadOnly(True)
output.setGeometry((window_w-output_w)//2, 190, output_w, output_h)

def runPython():
    p = QProcess()
    params = []
    python = 'python3'
    params.append(filepath.toPlainText())
    p.start(python, params)
    p.waitForFinished()
    output.setText(p.readAllStandardOutput().data().decode('utf-8'))

button.clicked.connect(runPython)


window.show()
app.exec()