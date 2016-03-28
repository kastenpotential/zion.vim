" python filetype plugin, called on every ft=python

noremap <buffer> <F5> <esc>:w<cr>:call zion#python#ExecBufferInternalPython3()<cr>

setlocal foldmethod=indent foldlevelstart=1

