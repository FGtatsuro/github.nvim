github.nvim
==================================================

[![Build Status](https://travis-ci.org/FGtatsuro/github.nvim.svg?branch=master)](https://travis-ci.org/FGtatsuro/github.nvim)

Neovim plugin to see a file on current buffer via Github WebUI.

Requirements
------------

The dependencies on other softwares/libraries for this project. 
This software may work even if these requirements aren't met, but the behavior on that case can't be supported officially.

- Neovim (>= 0.5.x)
- Python (>= 3.8.x)

Installation
------------

1. Create a directory to put this plugin.

```bash
$ mkdir -p ~/.config/nvim/bundle
```

2. Clone this project under step1's directory.

```bash
$ git clone git@github.com:FGtatsuro/github.nvim.git ~/.config/nvim/bundle/github.nvim
```

3. Add a directory of cloned this project to `$runtimepath`.

```vim
" Your vimrc
let &runtimepath.=','.$HOME.'/.config/nvim/bundle/github.nvim'
```

4. Update plugin info.

```vim
# In Neovim
:UpdateRemotePlugins
:qa!
```

How to
------

Development
-----------

1. Start Neovim with `NVIM_PYTHON_LOG_FILE` and `NVIM_PYTHON_LOG_FILE`, you can check logs of Neovim.

```bash
# FYI: https://github.com/neovim/python-client/blob/master/docs/usage/remote-plugins.rst
$ NVIM_PYTHON_LOG_LEVEL=DEBUG NVIM_PYTHON_LOG_FILE=./github.log nvim -u tests/vimrc
```

2. Update the remote plugin manifest and restart Neovim. After that, please check futures of your plugin.

```
# In Neovim
:UpdateRemotePlugins
:qa!

...

$ (Same command to step1)
:(Run plugin's command/function/mapping and so on)
```
