/* --------------------- macOS ------------------------- */
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Oh My Posh via Homebrew
brew install oh-my-posh

# Optional: Install a Nerd Font (e.g., Meslo)
brew tap homebrew/cask-fonts
brew install --cask font-meslo-lg-nerd-font

# Ensure profile exists
if (!(Test-Path -Path $PROFILE)) {
  New-Item -ItemType File -Path $PROFILE -Force
}

# Add this to your PowerShell profile (~/.config/powershell/Microsoft.PowerShell_profile.ps1)
Add-Content -Path $PROFILE -Value @'
oh-my-posh init pwsh --config "$(brew --prefix)/etc/oh-my-posh/themes/jandedobbeleer.omp.json" | Invoke-Expression
Set-PoshPrompt -Theme jandedobbeleer
'@

# Reload profile
. $PROFILE