#!/bin/bash

# Git Repository Setup Script for Multiverse
echo "🔧 Setting up Git repository for Multiverse"
echo "============================================"

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed"
    echo "Please install Git from https://git-scm.com/"
    exit 1
fi

echo "✅ Git found"

# Initialize git repository
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi

# Add all files
echo "📦 Adding files to Git..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Multiverse Virtual OS Hub

- Dark neumorphic UI design
- NectarOS template with macOS/Vista/OneUI fusion
- Virtual machine management system
- Cross-platform support (macOS, Linux, Windows)
- Beginner-friendly interface"

echo "✅ Initial commit created"

# Ask if user wants to create GitHub repository
echo ""
echo "🤔 Do you want to create a GitHub repository?"
echo "This will help you share and collaborate on your project."
read -p "Create GitHub repository? (y/n): " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "📋 To create a GitHub repository:"
    echo "1. Go to https://github.com/new"
    echo "2. Repository name: multiverse"
    echo "3. Description: Virtual OS Hub with dark neumorphic design"
    echo "4. Make it Public or Private (your choice)"
    echo "5. Don't initialize with README (we already have one)"
    echo "6. Click 'Create repository'"
    echo ""
    echo "After creating the repository, run these commands:"
    echo "git remote add origin https://github.com/TheManFran43/Multiverse.git"
    echo "git branch -M main"
    echo "git push -u origin main"
else
    echo "✅ Local Git repository is ready!"
    echo "You can create a GitHub repository later if needed."
fi

echo ""
echo "🎉 Git setup complete!"
echo "======================"
echo ""
echo "Your Multiverse project is now under version control!"
echo ""
echo "Next steps:"
echo "1. Install dependencies: pip install -r requirements.txt"
echo "2. Run the app: python main.py"
echo "3. Make changes and commit them: git add . && git commit -m 'Your message'"
echo ""
echo "Happy coding! 🚀" 