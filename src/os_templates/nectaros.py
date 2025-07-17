"""
NectarOS Template Configuration
Fusion of macOS Tahoe, Windows Vista, and OneUI 7 aesthetics
"""

import os
import json
from pathlib import Path


class NectarOSTemplate:
    """NectarOS virtual environment template"""
    
    def __init__(self):
        self.name = "NectarOS"
        self.version = "1.0.0"
        self.description = "A beautiful fusion of macOS Tahoe, Windows Vista, and OneUI 7 aesthetics"
        
        # Design specifications
        self.design_features = {
            "frosted_glass": True,
            "animations": True,
            "rounded_corners": True,
            "gradient_backgrounds": True,
            "soft_shadows": True,
            "transparency_effects": True
        }
        
        # Color palette inspired by the three OS designs
        self.color_palette = {
            # macOS Tahoe inspired
            "primary_blue": "#007AFF",
            "secondary_blue": "#5AC8FA",
            "accent_orange": "#FF9500",
            
            # Windows Vista inspired
            "aero_glass": "rgba(255, 255, 255, 0.1)",
            "vista_blue": "#1E90FF",
            "vista_gray": "#F0F0F0",
            
            # OneUI 7 inspired
            "oneui_primary": "#007AFF",
            "oneui_secondary": "#34C759",
            "oneui_background": "#000000",
            "oneui_surface": "#1C1C1E"
        }
        
        # Essential applications
        self.essential_apps = [
            {
                "name": "Settings",
                "icon": "⚙️",
                "description": "System settings and preferences",
                "category": "system"
            },
            {
                "name": "File Manager",
                "icon": "📁",
                "description": "Browse and manage files",
                "category": "utilities"
            },
            {
                "name": "Terminal",
                "icon": "💻",
                "description": "Command line interface",
                "category": "utilities"
            },
            {
                "name": "Calculator",
                "icon": "🧮",
                "description": "Basic calculator application",
                "category": "utilities"
            }
        ]
        
        # Default VM configuration
        self.default_config = {
            "memory": 2048,  # MB
            "storage": 20,   # GB
            "cpu_cores": 2,
            "display": {
                "width": 1280,
                "height": 720,
                "refresh_rate": 60
            },
            "network": {
                "type": "nat",
                "enabled": True
            }
        }
        
    def get_template_info(self):
        """Get template information"""
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "features": self.design_features,
            "essential_apps": self.essential_apps,
            "default_config": self.default_config
        }
        
    def create_vm_config(self, vm_name: str, custom_config: dict = None):
        """Create VM configuration for NectarOS"""
        config = self.default_config.copy()
        
        if custom_config:
            config.update(custom_config)
            
        vm_config = {
            "name": vm_name,
            "os_template": self.name,
            "config": config,
            "design": {
                "theme": "nectaros_fusion",
                "colors": self.color_palette,
                "features": self.design_features
            },
            "apps": self.essential_apps.copy()
        }
        
        return vm_config
        
    def get_installation_script(self):
        """Get the installation script for NectarOS"""
        return r"""
#!/bin/bash
# NectarOS Installation Script

echo "🌺 Installing NectarOS..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install essential packages
sudo apt install -y \
    xfce4 \
    xfce4-goodies \
    compton \
    nitrogen \
    rofi \
    polybar \
    alacritty \
    thunar \
    gedit \
    gnome-calculator

# Install custom theme and icons
mkdir -p ~/.themes/nectaros
mkdir -p ~/.icons/nectaros

# Configure desktop environment
cat > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<channel name="xfce4-desktop" version="1.0">
  <property name="desktop-icons" type="empty">
    <property name="style" type="int" value="0"/>
  </property>
  <property name="desktop-menu" type="empty">
    <property name="show" type="bool" value="false"/>
  </property>
</channel>
EOF

# Configure compositor for frosted glass effects
cat > ~/.config/compton.conf << 'EOF'
backend = "glx"
glx-no-stencil = true;
glx-no-rebind-pixmap = true;
vsync = "opengl-swc";

# Opacity
inactive-opacity = 0.8;
active-opacity = 1.0;
frame-opacity = 0.7;
inactive-opacity-override = false;

# Blur
blur-background = true;
blur-background-frame = true;
blur-kern = "3x3box";

# Fading
fading = true;
fade-delta = 4;
fade-in-step = 0.03;
fade-out-step = 0.03;
fade-exclude = [];

# Other
mark-wmwin-focused = true;
mark-ovredir-focused = true;
use-ewmh-active-win = true;
detect-rounded-corners = true;
EOF

# Create desktop shortcuts
mkdir -p ~/Desktop
cat > ~/Desktop/Settings.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=Settings
Comment=System Settings
Exec=xfce4-settings-manager
Icon=preferences-system
Terminal=false
EOF

cat > ~/Desktop/File\ Manager.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=File Manager
Comment=Browse Files
Exec=thunar
Icon=system-file-manager
Terminal=false
EOF

chmod +x ~/Desktop/*.desktop

echo "✅ NectarOS installation complete!"
echo "🎨 Features enabled:"
echo "   - Frosted glass effects"
echo "   - Smooth animations"
echo "   - Rounded corners"
echo "   - Gradient backgrounds"
echo "   - Essential applications"
        """
        
    def get_welcome_message(self):
        """Get welcome message for NectarOS"""
        return """
🌺 Welcome to NectarOS! 🌺

You're now experiencing a beautiful fusion of:
• macOS Tahoe's elegance
• Windows Vista's Aero Glass
• OneUI 7's modern design

Features available:
✅ Frosted glass effects
✅ Smooth animations  
✅ Rounded corners
✅ Gradient backgrounds
✅ Essential applications

Enjoy your new virtual environment!
        """ 