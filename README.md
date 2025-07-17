# Multiverse - Virtual OS Hub 🚀

Welcome to Multiverse! This is a beginner-friendly application that lets you create and manage virtual machines with custom operating system environments. Think of it as a "hub" where you can run different operating systems inside your computer.

## ✨ What is Multiverse?

Multiverse is an application that:
- **Runs on macOS, Linux, and Windows** (yes, it works on your Mac!)
- Creates beautiful virtual machines with custom designs
- Has a modern dark interface with soft, elegant shadows
- Lets you explore different operating system styles

## 🎨 Features

- **Dark Neumorphic UI**: Modern, elegant interface with soft shadows and depth
- **Virtual Machine Management**: Create, manage, and run multiple VM environments
- **Custom OS Environments**: Pre-configured operating system templates
- **Cross-Platform**: Works on macOS, Linux, and Windows
- **Beginner Friendly**: Easy-to-use interface with clear instructions

## 🌟 Current Virtual OS

### NectarOS
- **Design**: A beautiful fusion of macOS Tahoe, Windows Vista, and OneUI 7 aesthetics
- **Features**: Frosted glass effects, smooth animations
- **Apps Included**: Settings, File Manager (more coming soon!)

## 📋 What You Need

### For macOS Users:
- macOS 10.15 (Catalina) or newer
- Python 3.8 or newer
- Homebrew (for easy installation)

### For Linux Users:
- Ubuntu 20.04+ or similar
- Python 3.8+
- QEMU/KVM (for virtualization)

### For Windows Users:
- Windows 10 or newer
- Python 3.8+
- WSL2 (Windows Subsystem for Linux) recommended

## 🚀 Getting Started (Beginner Guide)

### Step 0: Set up Git Repository (Recommended)
```bash
# Make the setup script executable
chmod +x setup_git.sh

# Run the Git setup script
./setup_git.sh
```

This will:
- Initialize a Git repository
- Create your first commit
- Guide you through creating a GitHub repository

### Step 1: Install Python
First, make sure you have Python installed:

**On macOS:**
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python
```

**On Windows:**
Download Python from [python.org](https://www.python.org/downloads/)

**On Linux:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Step 2: Download Multiverse
```bash
# Download the project
git clone https://github.com/TheManFran43/Multiverse.git
cd Multiverse
```

### Step 3: Install Dependencies
```bash
# Install Python packages
pip install -r requirements.txt
```

### Step 4: Run Multiverse!
```bash
# Run the main application
python main.py

# Or run the demo version
python demo.py
```

That's it! 🎉

## 🛠️ For Advanced Users

### System Dependencies (Linux only):
If you're on Linux and want full VM functionality:
```bash
sudo apt update
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
sudo usermod -a -G libvirt $USER
```

### Troubleshooting:
- **"Python not found"**: Make sure Python is installed and in your PATH
- **"Module not found"**: Run `pip install -r requirements.txt` again
- **"Permission denied"**: On Linux, make sure you're in the libvirt group

## 🎯 How to Use

1. **Launch Multiverse** - Run `python main.py`
2. **Create a New VM** - Click "Create New VM" button
3. **Choose NectarOS** - Select from available templates
4. **Configure Settings** - Set memory, storage, etc.
5. **Launch & Enjoy** - Start your virtual environment!

## 📁 Project Structure
```
multiverse/
├── main.py                 # Start here! 🚀
├── src/
│   ├── ui/                 # User interface
│   ├── vm/                 # Virtual machine stuff
│   ├── os_templates/       # OS designs
│   └── utils/              # Helper functions
├── resources/              # Icons and themes
├── templates/              # VM templates
└── docs/                   # Documentation
```

## 🤝 Need Help?

- **New to coding?** Start with the "Getting Started" section above
- **Stuck?** Check the troubleshooting section
- **Found a bug?** Create an issue on GitHub
- **Want to contribute?** We welcome beginners! See CONTRIBUTING.md

## 📄 License

MIT License - feel free to use and modify!

---

**Made with ❤️ for beginners and pros alike!**

## Usage

1. Launch Multiverse
2. Select "Create New VM" to set up a new virtual environment
3. Choose from available OS templates (starting with NectarOS)
4. Configure VM settings and launch
5. Manage your virtual environments from the main hub

## Development

### Project Structure
```
multiverse/
├── main.py                 # Main application entry point
├── src/
│   ├── ui/                 # User interface components
│   ├── vm/                 # Virtual machine management
│   ├── os_templates/       # OS environment templates
│   └── utils/              # Utility functions
├── resources/              # Icons, themes, and assets
├── templates/              # VM and OS templates
└── docs/                   # Documentation
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For issues and feature requests, please use the GitHub issue tracker. 