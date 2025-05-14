local terminal_setup = {
  shells = {
    zsh = {
      [".zshrc"] = true,
      themes = {}
    },
    fish = {
      ["config.fish"] = true
    },
    bash = {
      [".bashrc"] = true
    }
  },
  prompts = {
    ["oh-my-posh"] = {
      themes = {}
    },
    powerlevel10k = {
      [".p10k.zsh"] = true
    },
    starship = {
      ["starship.toml"] = true
    }
  },
  tools = {
    fzf = {},
    bat = {},
    exa = {},
    tldr = {}
  },
  fonts = {
    ["nerd-fonts-install.md"] = true
  }
}

return terminal_setup
