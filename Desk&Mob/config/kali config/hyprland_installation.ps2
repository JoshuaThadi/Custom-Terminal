# Variables
$kaliUser = "yourUsername"
$kaliHost = "192.168.x.x"  # Change to your Kali machine's IP
$scriptPath = "C:\Users\you\hyprland-setup.sh"

# Create Bash Script Content
$setupScript = @"
#!/bin/bash
sudo apt update && sudo apt full-upgrade -y

sudo apt install -y \
  build-essential cmake git libwayland-dev libx11-dev \
  libxcb-composite0-dev libxcb-xinput-dev libxkbcommon-dev \
  libpixman-1-dev libxrender-dev ninja-build libinput-dev \
  libxcb1-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-image0-dev \
  libxcb-keysyms1-dev libxcb-randr0-dev libxcb-util0-dev \
  libxcb-xinerama0-dev libxcb-xkb-dev meson wayland-protocols \
  wayland-utils xdg-desktop-portal-wlr unzip waybar rofi wlogout \
  dunst swww kitty lxappearance papirus-icon-theme \
  fonts-jetbrains-mono fonts-firacode grim slurp

cd ~
git clone https://github.com/hyprwm/Hyprland
cd Hyprland
make all
sudo make install

mkdir -p ~/.config/{hypr,waybar,wlogout,rofi,wallpapers,scripts}

cat <<EOF > ~/.config/hypr/hyprland.conf
exec-once = waybar &
exec-once = dunst &
exec-once = swww init &
exec-once = swww img ~/wallpapers/your_wallpaper.jpg

input {
  kb_layout = us
}

general {
  gaps_in = 5
  gaps_out = 10
  border_size = 2
  col.active_border = rgba(ffb86cff)
  col.inactive_border = rgba(44475a99)
}

decoration {
  rounding = 10
}

monitor=,preferred,auto,1
EOF

echo "exec Hyprland" > ~/.xinitrc
"@

# Save to file
$setupScript | Out-File -Encoding ASCII -FilePath $scriptPath

# Copy to Kali (needs OpenSSH client installed)
scp $scriptPath "$kaliUser@$kaliHost:/home/$kaliUser/hyprland-setup.sh"

# SSH and run
ssh "$kaliUser@$kaliHost" "chmod +x ~/hyprland-setup.sh && bash ~/hyprland-setup.sh"
