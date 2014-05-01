syntax on

set number
set linebreak
set showbreak=+++
set showmatch
set visualbell

set hlsearch
set smartcase
set autoindent
set shiftwidth=4
set tabstop=4
set smartindent
set softtabstop=4
set undolevels=1000
set backspace=indent,eol,start
set expandtab
set autoindent
set mouse=a

highlight LineNr ctermfg=11
highlight Statement term=bold ctermfg=10
highlight Special term=bold ctermfg=6
highlight PreProc term=underline ctermfg=6
highlight Type term=underline ctermfg=4
highlight Directory term=bold ctermfg=12
highlight WarningMsg term=standout ctermfg=13
highlight Title term=bold ctermfg=13

let vala_comment_strings = 1
let vala_space_errors = 1

execute pathogen#infect()

autocmd vimenter * NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif
