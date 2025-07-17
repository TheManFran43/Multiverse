#!/usr/bin/env python3
"""
Multiverse - Virtual OS Hub
Main application entry point
"""

import sys
import os
from pathlib import Path
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from ui.main_window import MainWindow
from utils.theme_manager import ThemeManager


def main():
    """Main application entry point"""
    # Create QApplication
    app = QApplication(sys.argv)
    app.setApplicationName("Multiverse")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("Multiverse Team")
    
    # Set application icon
    icon_path = Path(__file__).parent / "resources" / "icons" / "multiverse.png"
    if icon_path.exists():
        app.setWindowIcon(QIcon(str(icon_path)))
    
    # Apply dark neumorphic theme
    theme_manager = ThemeManager()
    theme_manager.apply_dark_neumorphic_theme(app)
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Start event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 