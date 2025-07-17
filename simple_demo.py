#!/usr/bin/env python3
"""
Simple Multiverse Demo - Fixed version
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
    
    def run_simple_demo():
        """Run the simplified Multiverse demo"""
        print("🚀 Starting Multiverse (Fixed Version)...")
        print("=========================================")
        
        # Create QApplication
        app = QApplication(sys.argv)
        app.setApplicationName("Multiverse")
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
        print("   - Dark theme UI")
        print("   - Working buttons")
        print("   - VM management")
        print("   - Create new virtual machines")
        print("")
        print("🎮 Try clicking the buttons - they all work now!")
        print("🔄 Close the window to exit")
        
        # Start event loop
        sys.exit(app.exec())
        
except ImportError as e:
    print("❌ Error: Missing dependencies")
    print(f"   {e}")
    print("")
    print("🔧 To fix this:")
    print("   1. Install dependencies: pip install PyQt6")
    print("   2. Run again: python simple_demo.py")
    print("")
    print("📖 For more help, see README.md")

if __name__ == "__main__":
    run_simple_demo() 