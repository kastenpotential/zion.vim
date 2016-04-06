" standard vim configurations

" highlight search results
set hlsearch
" display first serach result while typing
set incsearch
" case insensitive search
set ignorecase
" do case sensitive search if searchword contains uppercase char
set smartcase 
" enable line numbering
set number
" show cursor position
set ruler
" use system clipboard for copy and paste
set clipboard=unnamedplus
" dont wirte the anoying backup files! thats what git is for!
set nobackup
set nowritebackup
set noswapfile
" dont't wrap long lines
set nowrap
" default behaviour of new windows and buffers
set splitbelow
set splitright
" enable syntax highlighting 
syntax on
" allow cursor to move beyond last char
set virtualedit=onemore
" show matching parenthesis 
set showmatch
" show list instead of just completing
set wildmenu
" Command <Tab> completion, list matches, then longest common part, then all.
set wildmode=list:longest,full
" expand tabs
set tabstop=4 shiftwidth=4 
" let backspace delete indent
set softtabstop=4
" make backspaces more powerfull
set backspace=indent,eol,start
" allow backspace, left, right to move beyond EOL
set whichwrap=b,s,<,>,[,]
" display tabs i a nice way
" http://unicode-suche.de/unicode-namesearch.pl?term=VERTICAL
" set listchars=tab:>-,trail:-
" AltGr+I = →
" nice chars:⋮ ⋯ ⋰  ⋱ ⁞┊ ⁞┋ │ ┃ ├→ → … ܅
set list
set listchars=tab:→\ ,trail:܅
" copy and paste in command line
cnoremap <MiddleMouse> <C-R>+
cnoremap <C-V> <C-R>+



