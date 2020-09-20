

#### Requirements  ####
# Install Qt5 (for the operating system, not Python)
# pip install PyQt5
# pip install PySide2
# pip install ts3

import sys
import ts3

from PySide2.QtWidgets import (QAction, QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit)


class SonzoTS3CommanderWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)


class HelpWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.helpText = QTextEdit()
        self.helpText.setReadOnly(True)
        self.loadPage()
        layout = QVBoxLayout()
        layout.addWidget(self.helpText)
        self.setLayout(layout)
        self.setGeometry(300, 300, 350, 350)


    def loadPage(self):
        with open("help.html", "r") as fp:
            html = fp.read()
        self.helpText.setHtml(html)


class AboutWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.aboutText = QTextEdit()
        self.aboutText.setReadOnly(True)
        self.loadPage()
        layout = QVBoxLayout()
        layout.addWidget(self.aboutText)
        self.setLayout(layout)
        self.setGeometry(300, 300, 350, 250)


    def loadPage(self):
        with open("about.html", "r") as fp:
            html = fp.read()
        self.aboutText.setHtml(html)


class SonzoTS3CommanderWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Sonzosoft - TS3 Commander")
        self.initUI()
        self.help = HelpWindow()
        self.about = AboutWindow()


    def initUI(self):
        self.initMainMenu()
        self.statusBar()


    def initMainMenu(self):
        quitAction = QAction("&Quit", self)
        quitAction.setShortcut("Ctrl+Q")
        quitAction.setStatusTip("Exit")
        quitAction.triggered.connect(self.close_application)

        connectAction = QAction("&Connect", self)
        connectAction.setShortcut("Ctrl+C")
        connectAction.setStatusTip("Connect to server")
        connectAction.triggered.connect(self.connect_to_server)

        helpAction = QAction("&Help", self)
        helpAction.setShortcut("Ctrl+H")
        helpAction.setStatusTip("Help")
        helpAction.triggered.connect(self.open_help)

        aboutAction = QAction("&About", self)
        aboutAction.setShortcut("Ctrl+A")
        aboutAction.setStatusTip("About")
        aboutAction.triggered.connect(self.open_about)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(quitAction)

        connectMenu = mainMenu.addMenu("&Connect")
        connectMenu.addAction(connectAction)

        helpMenu = mainMenu.addMenu("&Help")
        helpMenu.addAction(helpAction)
        helpMenu.addAction(aboutAction)


    def open_help(self):
        #dlg = QDialog(self)
        self.help.setWindowTitle("TS3 Commander - Help")
        #help = HelpWindow()
        self.help.show()


    def open_about(self):
        self.about.setWindowTitle("TS3 Commander - About")
        #help = HelpWindow()
        self.about.show()


    def connect_to_server(self):
        pass


    def close_application(self):
        QApplication.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = SonzoTS3CommanderWidget()
    window = SonzoTS3CommanderWindow(widget)
    window.resize(400, 500)
    window.show()

    sys.exit(app.exec_())


