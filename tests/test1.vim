" echom Test1()


function! Test1()
py3 << EOF
import vim

print(vim.current.window.cursor)
vim.command("return 'hello'")

EOF
endfunction


function! MoveLineUp()
py3 << EOF
import vim

row, col = vim.current.window.cursor
row -= 1
col -= 1
if row > 0:
	vim.current.buffer[row-1], vim.current.buffer[row] = vim.current.buffer[row], vim.current.buffer[row-1]
	vim.current.window.cursor = row, col
vim.command("return 'hello'")

EOF
endfunction


py3 << EOF

from pyvim import pv

def move_line_up(visible=False):
	win = pv.window()
	row, col = win.getCursorPos()
	mode = vim.eval("mode(1)")
	start = vim.current.range.start
	end = vim.current.range.end
	print(win, row, mode, start, end)
	if row > 0:
		for row in range(start, end+1):
			win.buffer[row-1], win.buffer[row] = win.buffer[row], win.buffer[row-1]
		win.setCursorPos(start-1, col)
		#vim.current.range(start-1, end-1)
		if visible:
			vim.command("normal! V{}G".format(end))

def move_line_down(visible=False):
	win = pv.window()
	row, col = win.getCursorPos()
	start = vim.current.range.start
	end = vim.current.range.end
	print(win, row, start, end)
	if row < len(win.buffer)-1:
		for row in range(start, end+1):
			win.buffer[row+1], win.buffer[row] = win.buffer[row], win.buffer[row+1]
		win.setCursorPos(end+1, col)
		#vim.current.range(start-1, end-1)
		if visible:
			vim.command("normal! V{}G".format(start+2))

EOF

nnoremap <A-Down> :py3 move_line_down(False)<cr>

vnoremap <A-Down> :py3 move_line_down(True)<cr>




nnoremap <A-Up> :py3 move_line_up(False)<cr>
vnoremap <A-Up> :py3 move_line_up(True)<cr>
nnoremap <A-1> echom "hello a"<cr>

