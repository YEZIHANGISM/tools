
" ==========================================
" vim config
" ==========================================

" 修改保存后立刻生效
" autocmd BufWritePost $MYVIMRC source $MYVIMRC

set nocompatible			" 关闭兼容模式

set nu 						" 显示行号
" set cursorline				" 当前行高亮
set showmatch				" 显示括号匹配

set ts=4 					" 设置tab长度为4个空格
set autoindent				" 继承前一行的缩进方式

let mapleader=","			" 快捷键前缀

syntax on 					" 代码高亮
filetype plugin indent on 	" 启用自动补全

call plug#begin('~/.vim/plugged')

" ==========================================
" NERDTree
" ==========================================
Plug 'preservim/nerdtree'
nnoremap <leader>v :NERDTreeFind<CR>

" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

" ==========================================
" color theme
" ==========================================
Plug 'morhetz/gruvbox'

" ==========================================
" vim-easy-align 快速对齐
" ==========================================
" Plug 'junegunn/vim-easy-align'

" ==========================================
" tagbar
" ==========================================
Plug 'majutsushi/tagbar'
nnoremap <leader>t :TagbarToggle<CR>

" ==========================================
" auto-pairs 括号自动补全
" ==========================================
Plug 'jiangmiao/auto-pairs'

" ==========================================
" vim-airline vim状态栏插件
" ==========================================
" Plug 'vim-airline/vim-airline'

" ==========================================
" youcompleteme 代码自动完成
" ==========================================
Plug 'Valloric/YouCompleteMe', {'commit': 'd98f896'}

" ==========================================
" git 文档显示git信息
" ==========================================
" Plug 'airblade/vim-gitgutter'

" ==========================================
" supertab tab补全
" ==========================================
Plug 'vim-scripts/SuperTab'

" ==========================================
" golang
" ==========================================
Plug 'fatih/vim-go', {'tag': '*'}
nnoremap gd :GoDef<CR>
" 代码追踪（gd）
" Plug 'dgryski/vim-godef'

" All of your Plugins must be added before the following line
call plug#end()            " required

" ==========================================
" gruvbox config
" ==========================================
colorscheme gruvbox
set t_Co=256
set background=dark
set guioptions=
set guifont=Monaco:h17
autocmd vimenter ++nested colorscheme gruvbox


" ==========================================
" golang config
" ==========================================
" 函数在同一文件时不打开新窗口
let g:godef_samefile_in_same_window=1
