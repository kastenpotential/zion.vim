
" Executes the content of the current buffer in the internal
" python3 interpreter.
function! zion#python#ExecBufferInternalPython3()
	py3 exec("\n".join(vim.current.buffer))
endfunction

function! zion#python#ToggleBoolean()
	:normal! "zyiw
	let src = @z
	let dst = src
	if src ==# 'True'
		let dst = 'False'
	elseif src ==# 'False'
		let dst = 'True'
	elseif src ==# 'true'
		let dst = 'false'
	elseif src ==# 'false'
		let dst = 'true'
	endif
	echom src . ' => ' . dst
	execute ':normal ciw'.dst
	normal b
endfunction

" True False False False true false true false
nnoremap <leader>! :call zion#python#ToggleBoolean()<cr>
