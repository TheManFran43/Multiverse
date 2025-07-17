"""
Neumorphic styling for Multiverse application
Dark theme with soft shadows and depth effects
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
        """Get the main window stylesheet"""
        return f"""
        QMainWindow {{
            background-color: {self.colors['bg_primary']};
            color: {self.colors['text_primary']};
            font-family: 'Segoe UI', 'SF Pro Display', 'Ubuntu', sans-serif;
        }}
        
        /* Sidebar */
        #sidebar {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {self.colors['bg_secondary']}, stop:1 {self.colors['bg_tertiary']});
            border-right: 1px solid {self.colors['border']};
            border-radius: 15px;
            margin: 10px;
            padding: 10px;
        }}
        
        #app-title {{
            font-size: 24px;
            font-weight: bold;
            color: {self.colors['accent']};
            margin: 10px 0;
            padding: 10px;
        }}
        
        #nav-button {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {self.colors['bg_tertiary']}, stop:1 {self.colors['bg_secondary']});
            border: 1px solid {self.colors['border']};
            border-radius: 10px;
            padding: 12px 15px;
            margin: 5px 0;
            color: {self.colors['text_primary']};
            font-size: 14px;
            font-weight: 500;
            text-align: left;
        }}
        
        #nav-button:hover {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {self.colors['accent']}, stop:1 {self.colors['accent_hover']});
            border-color: {self.colors['accent']};
            color: white;
        }}
        
        #nav-button:pressed {{
            background: {self.colors['accent']};
            border-color: {self.colors['accent_hover']};
        }}
        
        #create-vm-button {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {self.colors['success']}, stop:1 #3ade70);
            border: none;
            border-radius: 12px;
            padding: 15px;
            margin: 10px 0;
            color: white;
            font-size: 14px;
            font-weight: bold;
        }}
        
        #create-vm-button:hover {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #5aee90, stop:1 #4ade80);
        }}
        
        /* Content Area */
        #content-area {{
            background: {self.colors['bg_primary']};
            border-radius: 15px;
            margin: 10px;
        }}
        
        #content-header {{
            font-size: 28px;
            font-weight: bold;
            color: {self.colors['text_primary']};
            margin: 10px 0;
        }}
        
        #content-scroll {{
            background: transparent;
            border: none;
        }}
        
        #content-scroll QWidget {{
            background: transparent;
        }}
        
        /* Welcome Section */
        #welcome-section {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 {self.colors['bg_secondary']}, stop:1 {self.colors['bg_tertiary']});
            border: 1px solid {self.colors['border']};
            border-radius: 20px;
            box-shadow: 5px 5px 15px {self.colors['shadow_dark']},
                        -5px -5px 15px {self.colors['shadow_light']};
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
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 {self.colors['bg_secondary']}, stop:1 {self.colors['bg_tertiary']});
            border: 1px solid {self.colors['border']};
            border-radius: 15px;
            box-shadow: 3px 3px 10px {self.colors['shadow_dark']},
                        -3px -3px 10px {self.colors['shadow_light']};
        }}
        
        #quick-action-button {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {self.colors['bg_tertiary']}, stop:1 {self.colors['bg_secondary']});
            border: 1px solid {self.colors['border']};
            border-radius: 12px;
            padding: 15px;
            color: {self.colors['text_primary']};
            font-size: 14px;
            font-weight: 500;
            min-height: 60px;
        }}
        
        #quick-action-button:hover {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {self.colors['accent']}, stop:1 {self.colors['accent_hover']});
            border-color: {self.colors['accent']};
            color: white;
        }}
        
        /* VM Section */
        #vm-section {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 {self.colors['bg_secondary']}, stop:1 {self.colors['bg_tertiary']});
            border: 1px solid {self.colors['border']};
            border-radius: 15px;
            box-shadow: 3px 3px 10px {self.colors['shadow_dark']},
                        -3px -3px 10px {self.colors['shadow_light']};
        }}
        
        #section-title {{
            font-size: 20px;
            font-weight: bold;
            color: {self.colors['text_primary']};
            margin-bottom: 15px;
        }}
        
        /* Scrollbar Styling */
        QScrollBar:vertical {{
            background: {self.colors['bg_secondary']};
            width: 12px;
            border-radius: 6px;
        }}
        
        QScrollBar::handle:vertical {{
            background: {self.colors['border']};
            border-radius: 6px;
            min-height: 20px;
        }}
        
        QScrollBar::handle:vertical:hover {{
            background: {self.colors['accent']};
        }}
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0px;
        }}
        """ 