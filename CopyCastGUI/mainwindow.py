# This Python file uses the following encoding: utf-8
# The tool receives live video stream from 
import os
from pathlib import Path
import io
import socket
import struct
import time
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
# host and port for the sockets
def recv_client():
    host = "172.16.143.147"
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))


    connection = client_socket.makefile('wb')
    try:
        while True:
            image_len = struct.unpack('<L', client_socket.recv(struct.calcsize('<L')))[0]
            if not image_len:
                break
            image_stream = io.BytesIO()
            image_stream.write(client_socket.recv(image_len))
            image_stream.seek(0)
            image = Image.open(image_stream)
            image.show()
            image.verify()
    finally:
        connection.close()
        client_socket.close()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = Path(__file__).resolve().parent / "dialog.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
