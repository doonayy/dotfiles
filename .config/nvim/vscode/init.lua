-- init.lua

require "options"
require "keymaps"
require "lazy-config"

if vim.g.vscode then

    vim.cmd[[source $HOME/.config/nvim/vscode/settings.vim]]
-- Optional plugin
--    vim.cmd[[source $HOME/.config/nvim/vscode/easymotion-config.vim]]

else

    require "alpha-config"
    require "autopairs-config"
    require "bufferline-config"
    require "git-config"
    require "hop-config"
    require "indentline-config"
    require "lualine-config"
    require "lsp-config"
    require "nvim-tree-config"
    require "telescope-config"
    require "toggleterm-config"
    require "treesitter-config"
    require "undotree-config"
    require "whichkey"

end