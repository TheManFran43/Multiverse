#!/usr/bin/env python3
"""
Simple test script for Multiverse
Tests basic functionality without complex dependencies
"""

import sys
from pathlib import Path

# Add src directory to path
SRC_PATH = Path(__file__).parent / "src"
sys.path.insert(0, str(SRC_PATH))

# Use absolute imports

def test_imports():
    """Test if all modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        from ui.main_window import MainWindow
        print("✅ MainWindow imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import MainWindow: {e}")
        return False
        
    try:
        from ui.neumorphic_style import NeumorphicStyle
        print("✅ NeumorphicStyle imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import NeumorphicStyle: {e}")
        return False
        
    try:
        from utils.animation_manager import AnimationManager
        print("✅ AnimationManager imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import AnimationManager: {e}")
        return False
        
    try:
        from vm.vm_manager import VMManager
        print("✅ VMManager imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import VMManager: {e}")
        return False
        
    try:
        from os_templates.nectaros import NectarOSTemplate
        print("✅ NectarOSTemplate imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import NectarOSTemplate: {e}")
        return False
        
    return True

def test_pyqt():
    """Test PyQt6 availability"""
    print("\n🔍 Testing PyQt6...")
    
    try:
        from PyQt6.QtWidgets import QApplication
        from PyQt6.QtCore import Qt
        print("✅ PyQt6 imported successfully")
        return True
    except ImportError as e:
        print(f"❌ PyQt6 not available: {e}")
        print("💡 Install with: pip install PyQt6")
        return False

def test_basic_functionality():
    """Test basic functionality"""
    print("\n⚙️ Testing basic functionality...")
    
    try:
        from vm.vm_manager import VMManager
        vm_manager = VMManager()
        print("✅ VM Manager created successfully")
        
        # Test template
        template = vm_manager.get_template("nectaros")
        if template:
            print("✅ NectarOS template loaded successfully")
        else:
            print("❌ Failed to load NectarOS template")
            return False
            
        # Test VM creation
        test_config = {
            "name": "Test VM",
            "os_template": "NectarOS",
            "memory": 2,
            "storage": 20
        }
        
        success = vm_manager.create_vm(test_config)
        if success:
            print("✅ Test VM created successfully")
        else:
            print("❌ Failed to create test VM")
            return False
            
        # Clean up
        vm_manager.delete_vm("Test VM")
        print("✅ Test VM cleaned up")
        
        return True
        
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Multiverse Application Test")
    print("=" * 40)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed")
        return False
        
    # Test PyQt
    if not test_pyqt():
        print("\n❌ PyQt6 not available")
        return False
        
    # Test basic functionality
    if not test_basic_functionality():
        print("\n❌ Basic functionality tests failed")
        return False
        
    print("\n🎉 All tests passed!")
    print("✅ The application should work correctly")
    print("\nTo run the full application:")
    print("  python demo.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 