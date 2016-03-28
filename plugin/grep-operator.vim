" grep operator

nnoremap <leader>g :set operatorfunc=GrepOperator<cr>g@
vnoremap <leader>g :<c-u>call GrepOperator(visualmode())<cr>

function! GrepOperator(type)
    "echom "type: " . a:type
    let saved_unnamed_register = @@
    if a:type ==# 'v'
        normal! `<v`>y
    elseif a:type ==# 'char'
        normal! `[v`]y
    else
        return
    endif

    " echom shellescape(@@)
    silent execute "grep! -R " . shellescape(@@) . " ."
    copen

    let @@ = saved_unnamed_register
endfunction

" 
" viw<leader>g: Visually select a word, then grep for it.
" <leader>g4w: Grep for the next four words.
" <leader>gt;: Grep until semicolon.
" <leader>gi[: Grep inside square brackets.



function! RunScript() abort
    let ft = &filetype
    if ft ==? 'vim'
        execute 'w'
        echom expand('%:p')  . ' sourced. 8xxix3'
        execute 'source %'
    elseif ft ==? 'python'
        echom 'python not implemented yet'
    else
        echom 'Unknonw Filetype: ' . ft
    endif
endfunction

" nnoremap <F5> :call RunScript()<cr>
" inoremap <F5> <esc>:call RunScript()<cr>


