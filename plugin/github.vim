if exists("g:loaded_github")
  finish
endif
let g:loaded_github = 1

" Probably, save_cpo logic isn't needed because Neovim is always "nocompatible"
" FYI:
"   https://neovim.io/doc/user/usr_41.html#41.11
"   https://neovim.io/doc/user/vim_diff.html#'compatible'

" FYI: https://neovim.io/doc/user/options.html#'tabstop'
" vim: tabstop=8 shiftwidth=2 softtabstop=2
