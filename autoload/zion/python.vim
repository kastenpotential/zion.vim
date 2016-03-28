
" Executes the content of the current buffer in the internal
" python3 interpreter.
function zion#python#ExecBufferInternalPython3()
	py3 exec("\n".join(vim.current.buffer))
endfunction


