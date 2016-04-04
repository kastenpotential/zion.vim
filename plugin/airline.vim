" configuration for airline


" echom "use_patch_fonts=" . g:use_patch_fonts

if exists("g:use_patch_fonts") && g:use_patch_fonts
	" echom "yes"
	" hide --INSERT-- on command linet
	set noshowmode
	" use nicer fonts if awailable
	let g:airline_powerline_fonts = 1
else
	set showmode
	let g:airline_powerline_fonts = 0
endif

" enable airline statusline
set laststatus=2
let g:airline_theme='bubblegum'

if has("gui_running")
	" enable/disable enhanced tabline.
	let g:airline#extensions#tabline#enabled = 0
	" enable/disable enhanced tabline.
else
	let g:airline#extensions#tabline#enabled = 0
endif

" enable/disable displaying open splits per tab (only when tabs are opened).
let g:airline#extensions#tabline#show_splits = 0

" configure how numbers are displayed in tab mode. >
let g:airline#extensions#tabline#tab_nr_type = 1 " tab number

let g:airline#extensions#tabline#show_close_button = 0
let g:airline#extensions#tabline#show_tab_type = 1
let g:airline#extensions#tabline#show_tab_nr = 1
let g:airline#extensions#tabline#close_symbol = "X"
let g:airline#extensions#tabline#tabs_label = 'tabs'

" rename label for tabs (default: 'tabs') (c)
" let g:airline#extensions#tabline#tabs_label = 'tbak'

let g:airline#extensions#tabline#buffer_idx_mode = 1
"nmap <leader>1 <Plug>AirlineSelectTab1
"nmap <leader>2 <Plug>AirlineSelectTab2
"nmap <leader>3 <Plug>AirlineSelectTab3
"nmap <leader>4 <Plug>AirlineSelectTab4
"nmap <leader>5 <Plug>AirlineSelectTab5
"nmap <leader>6 <Plug>AirlineSelectTab6
"nmap <leader>7 <Plug>AirlineSelectTab7
"nmap <leader>8 <Plug>AirlineSelectTab8
"nmap <leader>9 <Plug>AirlineSelectTab9
"nmap <leader>- <Plug>AirlineSelectPrevTab
"nmap <leader>+ <Plug>AirlineSelectNextTab


