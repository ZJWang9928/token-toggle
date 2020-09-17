python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

function! TokenToggle()
py << EndOfPython

from token_toggle import token_toggle

# get token under cursor
token_under_cursor = vim.eval('expand("<cword>")')

if len(token_under_cursor):
    toggled_token = token_toggle(token_under_cursor)
    vim.command('normal viwc%s' % toggled_token)
    vim.command('normal b')

EndOfPython
endfunction

command! TokenToggle call TokenToggle()
