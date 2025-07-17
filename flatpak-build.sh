#!/bin/bash

# Multiverse Flatpak Build Script
echo "🚀 Building Multiverse Flatpak Package"
echo "======================================"

# Check if flatpak-builder is installed
if ! command -v flatpak-builder &> /dev/null; then
    echo "❌ flatpak-builder not found"
    echo "Install with: sudo apt install flatpak-builder"
    exit 1
fi

# Check if required runtimes are installed
echo "📦 Checking Flatpak runtimes..."
flatpak install org.gnome.Platform//45 org.gnome.Sdk//45 --user -y

# Build the Flatpak
echo "🔨 Building Flatpak package..."
flatpak-builder --force-clean --user build com.github.themanfran43.multiverse.yml

if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    echo ""
    echo "📦 To install locally:"
    echo "   flatpak-builder --user --install --force-clean build com.github.themanfran43.multiverse.yml"
    echo ""
    echo "🚀 To run the app:"
    echo "   flatpak run com.github.themanfran43.multiverse"
    echo ""
    echo "📤 To create a bundle for distribution:"
    echo "   flatpak-builder --repo=repo --force-clean build com.github.themanfran43.multiverse.yml"
    echo "   flatpak build-bundle repo multiverse.flatpak com.github.themanfran43.multiverse"
else
    echo "❌ Build failed!"
    exit 1
fi 