import sys

from PyQt6.QtWidgets import QApplication

from src.main_windows import MainWindow


def main() -> int:
    """Entry point for tp4."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
