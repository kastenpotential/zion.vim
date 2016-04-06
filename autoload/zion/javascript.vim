

function! zion#javascript#GetUnderCursor()
	" search in single quotes
	normal! \<LeftMouse>
	normal "zyi'
	return @z
endfunction


function! zion#javascript#GotoDefinition()
	let search=zion#javascript#GetUnderCursor()
	if exists('g:ag_mapping_message')
		let s:old_msg=g:ag_mapping_message
	else
		let s:old_msg=0
	endif
	let g:ag_mapping_message=0
	echom search
	silent! execute 'Ag "Ext.define.*' . search . '"'
	" let results = len(getloclist(0))
	let results = len(getqflist())
	if results == 1
		" silent! execute 'cc 1'
		execute 'cclose'
 		echom 'Goto Definition: ' . search
	endif
	if results == 0
		echom 'No Definition found: ' . search
	endif
	let g:ag_mapping_message=s:old_msg
endfunction

" Ext.define('protel.air.system.controller') asdfasf
" asfasdf 'my words' asdfasfd


" nnoremap <C-LeftMouse> <LeftMouse>:call zion#javascript#GotoDefinition()<cr>
" nnoremap <C-LeftRelease> <LeftMouse>:call zion#javascript#GotoDefinition()<cr>
" map <C-LeftMouse> <silent> echo ""
" map <C-]> silent! echo ""


" Ext.create('protel.air.system.controller') asdfasf

" cnoremap <MiddleMouse> <C-R>+
" cnoremap <C-V> <C-R>+


