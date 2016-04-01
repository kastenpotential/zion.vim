
" populate location list so that you can jump to errors
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 0
let g:syntastic_check_on_open = 0
let g:syntastic_check_on_wq = 0
let g:syntastic_javascript_checkers = ['jshint', 'jscs']
let g:syntastic_python_checkers = ['flake8', 'python3', 'pylint', 'pyflakes', 'pep8']

" sudo pip3 install --upgrade pyflakes
" sudo pip3 install --upgrade pylint
" sudo pip3 install --upgrade pep8


" nnoremap <C-F> :lnext<cr>
" nnoremap <C-B> :lprev<cr>
nnoremap <F4> :SyntasticCheck<cr>:lopen<cr>

