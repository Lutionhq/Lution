import sys
import subprocess
import threading
import time
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

def startweebserver():
    subprocess.Popen(["streamlit", "run", "main.py"])

def main():
    threading.Thread(target=startweebserver, daemon=True).start()
    time.sleep(2)

    app = QApplication(sys.argv)
    browser = QWebEngineView()
    browser.resize(1024, 768)
    browser.setWindowTitle("Lution - Windwon")
    browser.load(QUrl("http://localhost:8501"))
    browser.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
