

function! zion#javascript#GetUnderCursor()
	" search in single quotes
	normal! \<LeftMouse>
	normal "zyi'
	return @z
endfunction


function! zion#javascript#GotoDefinition()
	let search=zion#javascript#GetUnderCursor()
	echom search
	execute 'Ag "Ext.define.*' . search . '"'
endfunction

" Ext.define('protel.air.system.controller') asdfasf
" asfasdf 'my words' asdfasfd

nnoremap <A-LeftRelease> :call zion#javascript#GotoDefinition()<cr>


" Ext.create('protel.air.system.controller') asdfasf

cnoremap <MiddleMouse> <C-R>+
cnoremap <C-V> <C-R>+


