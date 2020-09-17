# token-toggle

Vim plugin to quickly toggle frequently used pairs of tokens.   

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

Then run the following command in Vim:  
    
    :PlugInstall

Or you can also use other plugin managers:  

+ [Vundle](https://github.com/VundleVim/Vundle.vim)
+ [neobundle](https://github.com/Shougo/neobundle.vim)
+ [pathogen](https://github.com/tpope/vim-pathogen)

## Usage

When cursor is on the target token, run the following command
    
    :TokenToggle

------

# token-toggle

这是一款用于快速切换常用成对标识符的 Vim 插件。  

## 当前支持切换的标识符

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

标识符切换时，会在大小写及首字母大写等方面遵循被替换标识符的格式。  

## 安装

如果你使用插件管理器的是 [vim-plug](https://github.com/junegunn/vim-plug)，你可以直接在你的 `vimrc` 文件中加入下面这一行：  
    
    Plug 'JonnieWayy/token-toggle'

然后在 Vim 中运行如下命令：  
    
    :PlugInstall

或者你也可以使用其他的插件管理器：  

+ [Vundle](https://github.com/VundleVim/Vundle.vim)
+ [neobundle](https://github.com/Shougo/neobundle.vim)
+ [pathogen](https://github.com/tpope/vim-pathogen)

## 用法

当光标位于想要切换的标识符之上时，运行如下命令：  
    
    :TokenToggle
