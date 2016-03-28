" Global mappings for Vim

" get rid of <esc>, use jk instead!
inoremap jk <esc>
vnoremap jk <esc>

" mov through split windows
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" visual shifting (does not exit visual mode)
vnoremap < <gv
vnoremap > >gv

" insert mode enhancements
" delete current line
inoremap <c-d> <esc>ddi
" make word under cursor uppercase
inoremap <c-u> <esc>bvwUi

" For when you forget to sudo.. Really Write the file.
cmap w!! w !sudo tee % >/dev/null

" Copy and Pase, Ctrl+c and Ctrl+v use clipboard
nnoremap <c-v> pl
inoremap <c-v> <esc>pli
vnoremap <c-v> <esc>plv
vnoremap <c-c> y

" map standard commands to leader keys
" :w   ->   ,w
inoremap <leader>w <esc>:w<cr>
nnoremap <leader>w :w<cr>
inoremap <leader>q <esc>:q<cr>
nnoremap <leader>q :q<cr>
inoremap <leader>Q <esc>:q!<cr>
nnoremap <leader>Q :q!<cr>

nnoremap <leader>. :nohl<cr>
inoremap <leader>. <esc>:nohl<cr>i

" toggel all folds recursively
nnoremap <space> zA

