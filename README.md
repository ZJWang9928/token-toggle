# token-toggle

Vim plugin to toggle frequently used pairs of tokens.   

## List of current supported token

| No. | Token1 | Token2 |
|-----|--------|--------|
| 1   | true   | false  |
| 2   | ==     | !=     |
| 3   | >      | <=     |
| 4   | <      | >=     |
| 5   | \+     | \-     |
| 6   | \*     | /      |
| 7   | yes    | no     |
| 8   | on     | off    |
| 9   | 1      | 0      |

The toggled Token will follow the format of the given token, e.g. upper/lower case, capitalization, etc..  

## Installation

If you use [vim-plug](https://github.com/junegunn/vim-plug), you can just add the following line to your `vimrc` file:  
    
    Plug 'JonnieWayy/token-toggle'

Then run the following command in vim:  
    
    :PlugInstall

Or you can also use other plugin managers:  

+ [Vundle](https://github.com/VundleVim/Vundle.vim)
+ [neobundle](https://github.com/Shougo/neobundle.vim)
+ [pathogen](https://github.com/tpope/vim-pathogen)

## Usage

When cursor is on the target token, run the following command
    
    :TokenToggle
