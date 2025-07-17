"""
Theme manager for Multiverse application
Handles application-wide styling and theming
"""

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSettings


class ThemeManager:
    """Manages application theming and styling"""
    
    def __init__(self):
        self.settings = QSettings("Multiverse", "Theme")
        self.current_theme = "dark_neumorphic"
        
    def apply_dark_neumorphic_theme(self, app: QApplication):
        """Apply dark neumorphic theme to the application"""
        # Set application-wide properties
        app.setProperty("theme", "dark_neumorphic")
        
        # Apply global stylesheet
        global_style = """
        /* Global application styles */
        * {
            font-family: 'Segoe UI', 'SF Pro Display', 'Ubuntu', sans-serif;
        }
        
        QToolTip {
            background: #2a2a2a;
            border: 1px solid #404040;
            border-radius: 8px;
            color: #ffffff;
            padding: 8px;
            font-size: 12px;
        }
        
        QMenu {
            background: #2a2a2a;
            border: 1px solid #404040;
            border-radius: 8px;
            color: #ffffff;
            padding: 5px;
        }
        
        QMenu::item {
            padding: 8px 15px;
            border-radius: 4px;
        }
        
        QMenu::item:selected {
            background: #4a9eff;
        }
        
        QMessageBox {
            background: #1a1a1a;
            color: #ffffff;
        }
        
        QMessageBox QPushButton {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #3a3a3a, stop:1 #2a2a2a);
            border: 1px solid #404040;
            border-radius: 8px;
            padding: 8px 16px;
            color: #ffffff;
            font-size: 14px;
        }
        
        QMessageBox QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #4a9eff, stop:1 #3a8eef);
            border-color: #4a9eff;
        }
        
        QInputDialog {
            background: #1a1a1a;
            color: #ffffff;
        }
        
        QInputDialog QLineEdit {
            background: #2a2a2a;
            border: 1px solid #404040;
            border-radius: 8px;
            padding: 8px;
            color: #ffffff;
        }
        
        QInputDialog QLineEdit:focus {
            border-color: #4a9eff;
        }
        """
        
        app.setStyleSheet(global_style)
        
        # Save theme preference
        self.settings.setValue("theme", self.current_theme)
        
    def get_theme_colors(self):
        """Get the current theme color palette"""
        return {
            'bg_primary': '#1a1a1a',
            'bg_secondary': '#2a2a2a',
            'bg_tertiary': '#3a3a3a',
            'text_primary': '#ffffff',
            'text_secondary': '#b0b0b0',
            'text_muted': '#808080',
            'accent': '#4a9eff',
            'accent_hover': '#5aaeff',
            'success': '#4ade80',
            'warning': '#fbbf24',
            'error': '#f87171',
            'border': '#404040',
            'shadow_dark': '#0a0a0a',
            'shadow_light': '#4a4a4a'
        }
        
    def get_current_theme(self):
        """Get the current theme name"""
        return self.current_theme
        
    def set_theme(self, theme_name: str):
        """Set a new theme"""
        self.current_theme = theme_name
        self.settings.setValue("theme", theme_name)
        
    def load_saved_theme(self):
        """Load the saved theme preference"""
        saved_theme = self.settings.value("theme", "dark_neumorphic")
        self.current_theme = saved_theme
        return saved_theme 