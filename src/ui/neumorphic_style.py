"""
Neumorphic styling for Multiverse application
Dark theme with soft shadows and depth effects (PyQt6 compatible)
"""

class NeumorphicStyle:
    """Neumorphic styling class for dark theme"""
    
    def __init__(self):
        # Color palette for dark neumorphic design
        self.colors = {
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
        
    def get_main_window_style(self):
        """Get the main window stylesheet (PyQt6 compatible)"""
        return f"""
        QMainWindow {{
            background-color: {self.colors['bg_primary']};
            color: {self.colors['text_primary']};
            font-family: 'SF Pro Display', 'Ubuntu', 'Segoe UI', sans-serif;
        }}
        
        /* Sidebar */
        #sidebar {{
            background-color: {self.colors['bg_secondary']};
            border-right: 2px solid {self.colors['border']};
            border-radius: 0px;
        }}
        
        #app-title {{
            font-size: 24px;
            font-weight: bold;
            color: {self.colors['accent']};
            margin: 10px 0;
            padding: 10px;
        }}
        
        #nav-button {{
            background-color: {self.colors['bg_tertiary']};
            border: 1px solid {self.colors['border']};
            border-radius: 8px;
            padding: 12px 15px;
            margin: 5px 0;
            color: {self.colors['text_primary']};
            font-size: 14px;
            font-weight: 500;
            text-align: left;
        }}
        
        #nav-button:hover {{
            background-color: {self.colors['accent']};
            border-color: {self.colors['accent']};
            color: white;
        }}
        
        #nav-button:pressed {{
            background-color: {self.colors['accent_hover']};
            border-color: {self.colors['accent_hover']};
        }}
        
        #create-vm-button {{
            background-color: {self.colors['success']};
            border: none;
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
            color: white;
            font-size: 14px;
            font-weight: bold;
        }}
        
        #create-vm-button:hover {{
            background-color: #5aee90;
        }}
        
        /* Content Area */
        #content-area {{
            background-color: {self.colors['bg_primary']};
            border-radius: 0px;
        }}
        
        #content-header {{
            font-size: 28px;
            font-weight: bold;
            color: {self.colors['text_primary']};
            margin: 10px 0;
        }}
        
        #content-scroll {{
            background-color: transparent;
            border: none;
        }}
        
        #content-scroll QWidget {{
            background-color: transparent;
        }}
        
        /* Welcome Section */
        #welcome-section {{
            background-color: {self.colors['bg_secondary']};
            border: 1px solid {self.colors['border']};
            border-radius: 12px;
            padding: 20px;
        }}
        
        #welcome-title {{
            font-size: 26px;
            font-weight: bold;
            color: {self.colors['accent']};
            margin-bottom: 10px;
        }}
        
        #welcome-subtitle {{
            font-size: 16px;
            color: {self.colors['text_secondary']};
            line-height: 1.4;
        }}
        
        /* Quick Actions */
        #quick-actions {{
            background-color: {self.colors['bg_secondary']};
            border: 1px solid {self.colors['border']};
            border-radius: 12px;
            padding: 20px;
        }}
        
        #quick-action-button {{
            background-color: {self.colors['bg_tertiary']};
            border: 1px solid {self.colors['border']};
            border-radius: 8px;
            padding: 15px;
            color: {self.colors['text_primary']};
            font-size: 14px;
            font-weight: 500;
            min-height: 60px;
        }}
        
        #quick-action-button:hover {{
            background-color: {self.colors['accent']};
            border-color: {self.colors['accent']};
            color: white;
        }}
        
        /* VM Section */
        #vm-section {{
            background-color: {self.colors['bg_secondary']};
            border: 1px solid {self.colors['border']};
            border-radius: 12px;
            padding: 20px;
        }}
        
        #section-title {{
            font-size: 20px;
            font-weight: bold;
            color: {self.colors['text_primary']};
            margin-bottom: 15px;
        }}
        
        /* Scrollbar Styling */
        QScrollBar:vertical {{
            background-color: {self.colors['bg_secondary']};
            width: 12px;
            border-radius: 6px;
        }}
        
        QScrollBar::handle:vertical {{
            background-color: {self.colors['border']};
            border-radius: 6px;
            min-height: 20px;
        }}
        
        QScrollBar::handle:vertical:hover {{
            background-color: {self.colors['accent']};
        }}
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0px;
        }}
        
        /* VM Card Styling */
        #vm-card {{
            background-color: {self.colors['bg_tertiary']};
            border: 1px solid {self.colors['border']};
            border-radius: 12px;
            padding: 15px;
        }}
        
        #vm-card:hover {{
            border-color: {self.colors['accent']};
        }}
        
        #vm-name {{
            font-size: 18px;
            font-weight: bold;
            color: {self.colors['text_primary']};
        }}
        
        #vm-os {{
            font-size: 14px;
            color: {self.colors['text_secondary']};
        }}
        
        #vm-resource {{
            font-size: 12px;
            color: {self.colors['text_muted']};
        }}
        
        #vm-status-running {{
            color: {self.colors['success']};
            font-weight: bold;
            font-size: 12px;
        }}
        
        #vm-status-stopped {{
            color: {self.colors['error']};
            font-weight: bold;
            font-size: 12px;
        }}
        
        #vm-status-paused {{
            color: {self.colors['warning']};
            font-weight: bold;
            font-size: 12px;
        }}
        
        #vm-progress {{
            background-color: {self.colors['bg_primary']};
            border: 1px solid {self.colors['border']};
            border-radius: 8px;
            text-align: center;
            color: {self.colors['text_primary']};
        }}
        
        #vm-progress::chunk {{
            background-color: {self.colors['accent']};
            border-radius: 7px;
        }}
        
        #vm-start-button, #vm-stop-button, #vm-settings-button {{
            background-color: {self.colors['bg_secondary']};
            border: 1px solid {self.colors['border']};
            border-radius: 6px;
            padding: 8px 12px;
            color: {self.colors['text_primary']};
            font-size: 12px;
            font-weight: 500;
        }}
        
        #vm-start-button:hover {{
            background-color: {self.colors['success']};
            border-color: {self.colors['success']};
            color: white;
        }}
        
        #vm-stop-button:hover {{
            background-color: {self.colors['error']};
            border-color: {self.colors['error']};
            color: white;
        }}
        
        #vm-settings-button:hover {{
            background-color: {self.colors['accent']};
            border-color: {self.colors['accent']};
            color: white;
        }}
        """ 