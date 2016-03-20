" echom "zion ftplugin vim loaded."

" Open the buffer with {name} if exists or create it with {type}.
" call OpenSameBuffer('__Color__Preview__', 'split')
function! OpenSameBuffer(name, type)
    let win = bufwinnr(a:name)
    if win > -1
        execute win . "wincmd w"
    else
        execute a:type . " " . a:name
    endif
endfunction


function! ClearBuffer()
    normal! ggdG
endfunction

function! GetCurrentBuffer()
    return bufnr('%')
endfunction

function! GotoWindow(nr)
    execute a:nr . "wincmd w"
endfunction


function! ShowHighlightPreview()
    "let win_nr = GetCurrentBuffer()
    " get content of current line
    let line = getline(".")
    "echom "line: " . line
    " get the second word
    let save_z = @z
    let cursor_pos = getpos(".")
    normal! ^w"zyw
    call setpos('.', cursor_pos)
    let group_name = @z
    " echom ">>>" . @z
    let @z = save_z
    
    " goto preview window
    call OpenSameBuffer("__ColorPreview__", "split")
    call ClearBuffer()
    setlocal filetype=colorpreview
    setlocal buftype=nofile
    setlocal nonumber
    let preview_text = [
        \ "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod",
        \ "tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At",
        \ "vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,",
        \ "no sea takimata sanctus est Lorem ipsum dolor sit amet."
        \ ]
    call append(0, line)
    call append(2, preview_text)
    execute "syntax match " . group_name . "/.*/"
    " call GotoWindow(win_nr)
endfunction




" Show preview of highlighting
nnoremap <buffer> <localleader>h
    \ :call ShowHighlightPreview()<cr>


