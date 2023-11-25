import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Define a custom stylesheet for the main window
        style_sheet = """
            QMainWindow {
                background-color: #2E2E2E;
                color: #FFFFFF;
            }
            # ... (style definitions for various widgets)
        """
        self.setStyleSheet(style_sheet)

        # Set up the main web browser view
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Set application icon
        app_icon = QIcon('browser_icon.png')  # Replace with the path to your icon image
        self.setWindowIcon(app_icon)

        # Create a navigation toolbar and add buttons for back, forward, reload, home
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Create a URL bar for typing and displaying URLs
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Connect signals to update URL bar when the page is changed
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        # Navigate to the home page (Google in this case)
        self.browser.setUrl(QUrl('https://www.google.com/'))

    def navigate_to_url(self):
        # Navigate to the URL entered in the URL bar
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        # Update the URL bar when the page is changed
        self.url_bar.setText(q.toString())

if __name__ == "__main__":
    # Create and run the application
    app = QApplication(sys.argv)
    QApplication.setApplicationName("Browser") #Feel free to change you browser title
    window = MainWindow()
    app.exec_()
