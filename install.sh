#!/bin/bash

# Multiverse Installation Script
# Supports macOS, Linux, and Windows (via WSL)

echo "🚀 Installing Multiverse - Virtual OS Hub"
echo "=========================================="

# Detect operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
    echo "📱 Detected: macOS"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
    echo "🐧 Detected: Linux"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    OS="windows"
    echo "🪟 Detected: Windows"
else
    echo "❌ Unsupported operating system: $OSTYPE"
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "Please install Python 3.8+ from https://python.org"
    exit 1
fi

PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "✅ Python $PYTHON_VERSION found"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed"
    echo "Please install pip3"
    exit 1
fi

echo "✅ pip3 found"

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Python dependencies installed successfully"
else
    echo "❌ Failed to install Python dependencies"
    exit 1
fi

# Platform-specific setup
case $OS in
    "macos")
        echo "🍎 macOS specific setup..."
        
        # Check if Homebrew is installed
        if ! command -v brew &> /dev/null; then
            echo "📦 Installing Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        
        # Install additional dependencies if needed
        echo "✅ macOS setup complete"
        ;;
        
    "linux")
        echo "🐧 Linux specific setup..."
        
        # Check if running as root
        if [ "$EUID" -eq 0 ]; then
            echo "⚠️  Running as root - this is not recommended"
        fi
        
        # Install system dependencies
        if command -v apt &> /dev/null; then
            echo "📦 Installing system dependencies (Ubuntu/Debian)..."
            sudo apt update
            sudo apt install -y python3-venv python3-pip
        elif command -v dnf &> /dev/null; then
            echo "📦 Installing system dependencies (Fedora)..."
            sudo dnf install -y python3-pip python3-venv
        elif command -v pacman &> /dev/null; then
            echo "📦 Installing system dependencies (Arch)..."
            sudo pacman -S --noconfirm python-pip python-virtualenv
        else
            echo "⚠️  Package manager not detected - please install dependencies manually"
        fi
        
        # Optional: Install QEMU/KVM for full VM functionality
        read -p "🤔 Install QEMU/KVM for full virtual machine support? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            if command -v apt &> /dev/null; then
                sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
                sudo usermod -a -G libvirt $USER
                echo "✅ QEMU/KVM installed"
                echo "⚠️  Please log out and back in for group changes to take effect"
            else
                echo "⚠️  QEMU/KVM installation not supported on this distribution"
            fi
        fi
        
        echo "✅ Linux setup complete"
        ;;
        
    "windows")
        echo "🪟 Windows specific setup..."
        echo "⚠️  Running on Windows - consider using WSL2 for better performance"
        echo "✅ Windows setup complete"
        ;;
esac

# Create desktop shortcut (Linux/macOS)
if [[ "$OS" == "linux" || "$OS" == "macos" ]]; then
    read -p "🤔 Create desktop shortcut? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        if [[ "$OS" == "linux" ]]; then
            # Linux desktop shortcut
            cat > ~/Desktop/Multiverse.desktop << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Multiverse
Comment=Virtual OS Hub
Exec=python3 $(pwd)/main.py
Icon=$(pwd)/resources/icons/multiverse.png
Terminal=false
Categories=System;
EOF
            chmod +x ~/Desktop/Multiverse.desktop
            echo "✅ Desktop shortcut created"
        elif [[ "$OS" == "macos" ]]; then
            # macOS app bundle (simplified)
            echo "📱 macOS app creation not implemented yet"
            echo "   Run with: python3 main.py"
        fi
    fi
fi

echo ""
echo "🎉 Installation complete!"
echo "========================="
echo ""
echo "To run Multiverse:"
echo "  python3 main.py"
echo ""
echo "Features available:"
echo "  ✅ Dark neumorphic UI"
echo "  ✅ NectarOS template"
echo "  ✅ Virtual machine management"
echo "  ✅ Cross-platform support"
echo ""
echo "For help, see README.md"
echo ""
echo "Enjoy exploring the Multiverse! 🌟" 