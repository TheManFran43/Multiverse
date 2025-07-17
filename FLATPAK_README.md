# Multiverse Flatpak Guide

This guide will help you build and publish Multiverse as a Flatpak app on Flathub.

## 🚀 Quick Start

### 1. Install Flatpak Build Tools
```bash
# Ubuntu/Debian
sudo apt install flatpak flatpak-builder

# Fedora
sudo dnf install flatpak flatpak-builder

# Arch
sudo pacman -S flatpak flatpak-builder
```

### 2. Build the Flatpak
```bash
# Make the build script executable
chmod +x flatpak-build.sh

# Run the build script
./flatpak-build.sh
```

### 3. Test Locally
```bash
# Install the app locally
flatpak-builder --user --install --force-clean build com.github.themanfran43.multiverse.yml

# Run the app
flatpak run com.github.themanfran43.multiverse
```

## 📦 Publishing to Flathub

### 1. Create App Icon
Replace `resources/icons/multiverse.png` with a real 256x256 PNG icon.

### 2. Update Manifest
Edit `com.github.themanfran43.multiverse.yml`:
- Update SHA256 hashes for dependencies
- Verify all URLs are correct
- Test the build locally

### 3. Submit to Flathub
1. Fork the [Flathub repository](https://github.com/flathub/flathub)
2. Add your app manifest to the `apps` directory
3. Create a pull request
4. Wait for review and approval

### 4. Flathub Requirements
- ✅ App ID follows reverse domain name notation
- ✅ Desktop file is properly configured
- ✅ App icon is included
- ✅ Manifest is valid
- ✅ App works in sandboxed environment
- ✅ No proprietary dependencies

## 🔧 Customization

### App Metadata
- **Name**: Multiverse
- **Description**: Virtual OS Hub with dark neumorphic design
- **Categories**: System, Virtualization
- **Keywords**: virtual, machine, vm, os, hub

### Permissions
The app requests these permissions:
- Network access (for updates)
- Home directory access (for VM storage)
- Audio (for VM audio)
- Graphics (for VM display)

## 🐛 Troubleshooting

### Build Issues
```bash
# Clean build directory
rm -rf build/

# Check Flatpak runtime
flatpak list --runtime

# Install missing runtime
flatpak install org.gnome.Platform//45 org.gnome.Sdk//45
```

### Runtime Issues
```bash
# Check app logs
flatpak run --command=sh com.github.themanfran43.multiverse
journalctl --user -f

# Test permissions
flatpak run --env=FLATPAK_DEBUG=1 com.github.themanfran43.multiverse
```

## 📋 Checklist for Flathub

- [ ] App builds successfully
- [ ] App runs in sandboxed environment
- [ ] Desktop file is properly configured
- [ ] App icon is 256x256 PNG
- [ ] Manifest follows Flathub guidelines
- [ ] No proprietary dependencies
- [ ] App works without network access
- [ ] App handles permissions gracefully
- [ ] Documentation is complete
- [ ] License is compatible

## 🎯 Next Steps

1. **Test thoroughly** on different Linux distributions
2. **Create app icon** using GIMP, Inkscape, or similar
3. **Update manifest** with correct SHA256 hashes
4. **Submit to Flathub** via pull request
5. **Monitor feedback** and update as needed

## 📚 Resources

- [Flathub Documentation](https://docs.flathub.org/)
- [Flatpak Builder Guide](https://docs.flatpak.org/en/latest/building.html)
- [App Stream Guidelines](https://www.freedesktop.org/software/appstream/docs/)
- [Flathub Review Process](https://github.com/flathub/flathub/wiki/App-Requirements)

---

**Good luck with your Flathub submission! 🚀** 