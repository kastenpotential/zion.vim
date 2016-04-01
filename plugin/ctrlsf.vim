
" grep text in single quotes
nnoremap <leader>g "zyi':exec ":CtrlSF ".@z.""<cr>
" open file in single quotes
nnoremap <leader>p "zyi':exec ":CtrlP ". join(split(@z, '.'), '' ).""<cr>
nnoremap <F3> :CtrlSFToggle<cr>


nnoremap <C-S-F> :CtrlSF -I<space>


