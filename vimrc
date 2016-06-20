"vim: filetype=vim

" disable old vi stuff
set nocompatible

"--- VUNDLE-PLUGIN -----------------------------------------------------------

" disable filetype for vundle
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" https://github.com/VundleVim/Vundle.vim
" :help vundle
Plugin 'VundleVim/Vundle.vim'
" https://github.com/ctrlpvim/ctrlp.vim
Plugin 'ctrlpvim/ctrlp.vim'
" https://github.com/vim-airline/vim-airline
" :help airline
Plugin 'vim-airline/vim-airline'
" https://github.com/vim-airline/vim-airline-themes
Plugin 'vim-airline/vim-airline-themes'
" https://github.com/tpope/vim-fugitive
Plugin 'tpope/vim-fugitive'
" https://github.com/Valloric/YouCompleteMe
" :help youcompleteme
" Plugin 'Valloric/YouCompleteMe'
" https://github.com/Shougo/neocomplete.vim
Plugin 'Shougo/neocomplete.vim'
Plugin 'Shougo/neco-syntax'
Plugin 'Shougo/neco-vim'
" https://github.com/suan/vim-instant-markdown
Plugin 'suan/vim-instant-markdown'
" https://github.com/tpope/vim-markdown
Plugin 'tpope/vim-markdown'
" https://github.com/pangloss/vim-javascript
" Plugin 'pangloss/vim-javascript'
" https://github.com/scrooloose/syntastic
Plugin 'scrooloose/syntastic'
" https://github.com/myint/syntastic-extras
Plugin 'myint/syntastic-extras'
" https://github.com/scrooloose/nerdtree
Plugin 'scrooloose/nerdtree'
" https://github.com/jistr/vim-nerdtree-tabs
Plugin 'jistr/vim-nerdtree-tabs'
" https://github.com/dkprice/vim-easygrep
" sudo apt-get install silversearcher-ag
" Plugin 'dkprice/vim-easygrep'
" https://github.com/ggreer/the_silver_searcher
" https://github.com/rking/ag.vim
Plugin 'rking/ag.vim'
" https://github.com/dyng/ctrlsf.vim
Plugin 'dyng/ctrlsf.vim'
" https://github.com/terryma/vim-multiple-cursors
Plugin 'terryma/vim-multiple-cursors'
" https://github.com/Shougo/unite.vim
" Plugin 'Shougo/unite.vim'
" https://github.com/SirVer/ultisnips
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'
Plugin 'Shougo/vimproc'
Plugin 'Shougo/vimshell.vim'
" https://github.com/vim-scripts/pythoncomplete
Plugin 'vim-scripts/pythoncomplete'
" Plugin 'ervandew/supertab'
" MY PLUGIN SHOULD BE THE LAST ONE !!!
Plugin 'kastenpotential/zion.vim'
call vundle#end()

" enable filetype after vundle
filetype plugin indent on

"--- STANDARD-VIM ------------------------------------------------------------

" map leader key
let mapleader = ","
let maplocalleader = ","
" enable mouse integration
set mouse=nvi
" set vi language to english
language en_US.utf8
" default encodig utf
set encoding=utf-8
" enable nice colors
set t_Co=256
" use nicer fonts
" workaround, airline will not load fonts in my config!
let g:use_patch_fonts = 1
let g:airline_powerline_fonts = 1

" and a nice font
if has("gui_running") && g:use_patch_fonts
        set guifont=DejaVu\ Sans\ Mono\ for\ Powerline\ 11
endif
" colors zenburn
colors zion

" let g:neocomplete#enable_at_startup = 1
py3 << EOF
# import pyvim.core
# pv = pyvim.core.init()
EOF

