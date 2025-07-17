#!/usr/bin/env python3
"""
Multiverse Demo Script
A simple demonstration of the Multiverse application
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

try:
    from PyQt6.QtWidgets import QApplication
    from ui.main_window import MainWindow
    from utils.theme_manager import ThemeManager
    from vm.vm_manager import VMManager
    
    def run_demo():
        """Run the Multiverse demo"""
        print("🚀 Starting Multiverse Demo...")
        print("=================================")
        
        # Create QApplication
        app = QApplication(sys.argv)
        app.setApplicationName("Multiverse Demo")
        app.setApplicationVersion("1.0.0")
        
        # Apply theme
        theme_manager = ThemeManager()
        theme_manager.apply_dark_neumorphic_theme(app)
        
        # Initialize VM manager
        vm_manager = VMManager()
        
        # Create and show main window
        window = MainWindow()
        window.show()
        
        print("✅ Multiverse is running!")
        print("📱 Features available:")
        print("   - Dark neumorphic UI")
        print("   - NectarOS template")
        print("   - VM management interface")
        print("   - Create new virtual machines")
        print("")
        print("🎮 Try clicking 'Create New VM' to see the dialog!")
        print("🔄 Close the window to exit")
        
        # Start event loop
        sys.exit(app.exec())
        
except ImportError as e:
    print("❌ Error: Missing dependencies")
    print(f"   {e}")
    print("")
    print("🔧 To fix this:")
    print("   1. Install dependencies: pip install -r requirements.txt")
    print("   2. Run again: python demo.py")
    print("")
    print("📖 For more help, see README.md")

if __name__ == "__main__":
    run_demo() 