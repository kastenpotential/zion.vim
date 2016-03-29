
" populate location list so that you can jump to errors
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:syntastic_javascript_checkers = ['jshint', 'jscs']


nnoremap <C-F> :lnext<cr>
nnoremap <C-B> :lprev<cr>

