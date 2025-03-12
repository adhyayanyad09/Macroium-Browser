import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Macroium Browser")
        self.setGeometry(100, 100, 1200, 800)

        # Create a QWebEngineView widget to display the web page
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))  # Default page

        # Set the browser widget as the central widget of the window
        self.setCentralWidget(self.browser)

        # Create the navigation bar (Back, Forward, Reload, Address Bar)
        self.navbar = QToolBar()
        self.addToolBar(self.navbar)

        # Back Button
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        self.navbar.addAction(back_button)

        # Forward Button
        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        self.navbar.addAction(forward_button)

        # Reload Button
        reload_button = QAction('Reload', self)
        reload_button.triggered.connect(self.browser.reload)
        self.navbar.addAction(reload_button)

        # Address Bar
        self.url_bar = QLineEdit(self)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.navbar.addWidget(self.url_bar)

        # Update address bar when navigating to a new page
        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_url(self):
        """Navigate to the URL typed in the address bar."""
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        """Update the address bar with the current URL."""
        self.url_bar.setText(q.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleBrowser()
    window.show()
    sys.exit(app.exec_())
