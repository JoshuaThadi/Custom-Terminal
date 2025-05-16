🌀 GNOME Setup Guide for Kali Linux

This guide helps you install and configure the GNOME desktop environment on Kali Linux, including all necessary dependencies, aesthetic customization, and optional tweaks for better performance.

📁 Folder Structure

~/.config/
├── gnome-shell/ # GNOME Shell extensions and settings
├── dconf/ # GNOME configuration database (backups)
├── wallpapers/ # Custom wallpapers
└── scripts/ # Custom user scripts (autostart, tweaks)

⚙️ System Preparation

Update your system


sudo apt update && sudo apt full-upgrade -y
📦 Install GNOME Desktop Environment

Install GNOME Full (Default + Extra Tools)


sudo apt install -y kali-desktop-gnome gnome-core gnome-tweaks gnome-shell-extensions gnome-software gnome-backgrounds
Optional: Install LightDM instead of GDM


sudo apt install lightdm lightdm-gtk-greeter
When prompted, select lightdm as the default display manager.

💡 Optional GNOME Tweaks & Utilities

Install useful tweaks and customization tools

sudo apt install -y \
  gnome-tweaks \
  dconf-editor \
  gnome-shell-extension-manager \
  chrome-gnome-shell \
  gnome-system-monitor \
  gnome-disk-utility \
  gnome-calendar \
  gnome-clocks
🎨 Themes, Icons & Fonts

Enhance GNOME appearance

sudo apt install -y \
  papirus-icon-theme \
  fonts-firacode \
  fonts-jetbrains-mono \
  yaru-theme-gtk \
  yaru-theme-icon \
  lxappearance
🖼️ Set Wallpapers

Add your custom wallpapers


mkdir -p ~/.config/wallpapers
cp /path/to/your/wallpaper.jpg ~/.config/wallpapers/
gsettings set org.gnome.desktop.background picture-uri "file://$HOME/.config/wallpapers/wallpaper.jpg"
⚙️ Configure GNOME with dconf (Optional)

Save and load GNOME settings (backup/restore)

Backup current config:

mkdir -p ~/.config/dconf
dconf dump / > ~/.config/dconf/gnome-settings-backup.ini
Restore config later:

dconf load / < ~/.config/dconf/gnome-settings-backup.ini
🚀 Autostart Custom Apps or Scripts

Create an autostart script

Create ~/.config/scripts/autostart.sh:


#!/bin/bash
# Start apps or scripts at GNOME login
nitrogen --restore &
nm-applet &
Make it executable:


chmod +x ~/.config/scripts/autostart.sh
Then create a .desktop entry in autostart:


mkdir -p ~/.config/autostart
cat <<EOF > ~/.config/autostart/autostart-script.desktop
[Desktop Entry]
Type=Application
Exec=$HOME/.config/scripts/autostart.sh
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Custom Autostart Script
EOF
🧩 Recommended Extensions (via GNOME Extension Manager)

Suggested GNOME Shell Extensions

User Themes

Dash to Dock

Caffeine

Blur My Shell

Clipboard Indicator

Sound Input & Output Device Chooser

Install via Extension Manager or https://extensions.gnome.org

📸 Screenshot Tool

Use GNOME’s built-in screenshot utility or install Flameshot:


sudo apt install flameshot
Bind to Print key:

Settings → Keyboard Shortcuts → Custom Shortcuts
Name: Flameshot
Command: flameshot gui
Shortcut: Print

✅ Final Notes

Open GNOME Tweaks to apply icon/GTK themes, fonts, etc.

Wallpapers are stored in ~/.config/wallpapers

All system settings saved via dconf for easy restoration.

You can install additional GNOME apps via gnome-software.
