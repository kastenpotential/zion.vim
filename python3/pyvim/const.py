# -*- coding: utf-8 -*-
"""
In this module are constants from vim defined for an easier use in python.
Nearly all constants have their name assigned as string.
"""
from enum import Enum


class AutoCommand(Enum):
    """ Vim autocmd events taken from :help autocommand-events """
    # Reading
    BufNewFile = "BufNewFile"  # starting to edit a file that doesn't exist
    BufReadPre = "BufReadPre"  # starting to edit a new buffer, before reading the file
    BufRead = "BufRead"  # starting to edit a new buffer, after reading the file
    BufReadPost = "BufReadPost"  # starting to edit a new buffer, after reading the file
    BufReadCmd = "BufReadCmd"  # before starting to edit a new buffer Cmd-event

    FileReadPre = "FileReadPre"  # before reading a file wit]h a ":read" command
    FileReadPost = "FileReadPost"  # after reading a file with a ":read" command
    FileReadCmd = "FileReadCmd"  # before reading a file with a ":read" command Cmd-event

    FilterReadPre = "FilterReadPre"  # before reading a file from a filter command
    FilterReadPost = "FilterReadPost"  # after reading a file from a filter command

    StdinReadPre = "StdinReadPre"  # before reading from stdin into the buffer
    StdinReadPost = "StdinReadPost"  # After reading from the stdin into the buffer

    # Writing
    BufWrite = "BufWrite"  # starting to write the whole buffer to a file
    BufWritePre = "BufWritePre"  # starting to write the whole buffer to a file
    BufWritePost = "BufWritePost"  # after writing the whole buffer to a file
    BufWriteCmd = "BufWriteCmd"  # before writing the whole buffer to a file Cmd-event

    FileWritePre = "FileWritePre"  # starting to write part of a buffer to a file
    FileWritePost = "FileWritePost"  # after writing part of a buffer to a file
    FileWriteCmd = "FileWriteCmd"  # before writing part of a buffer to a file Cmd-event

    FileAppendPre = "FileAppendPre"  # starting to append to a file
    FileAppendPost = "FileAppendPost"  # after appending to a file
    FileAppendCmd = "FileAppendCmd"  # before appending to a file Cmd-event

    FilterWritePre = "FilterWritePre"  # starting to write a file for a filter command or diff
    FilterWritePost = "FilterWritePost"  # after writing a file for a filter command or diff

    # Buffers
    BufAdd = "BufAdd"  # just after adding a buffer to the buffer list
    BufCreate = "BufCreate"  # just after adding a buffer to the buffer list
    BufDelete = "BufDelete"  # before deleting a buffer from the buffer list
    BufWipeout = "BufWipeout"  # before completely deleting a buffer

    BufFilePre = "BufFilePre"  # before changing the name of the current buffer
    BufFilePost = "BufFilePost"  # after changing the name of the current buffer

    BufEnter = "BufEnter"  # after entering a buffer
    BufLeave = "BufLeave"  # before leaving to another buffer
    BufWinEnter = "BufWinEnter"  # after a buffer is displayed in a window
    BufWinLeave = "BufWinLeave"  # before a buffer is removed from a window

    BufUnload = "BufUnload"  # before unloading a buffer
    BufHidden = "BufHidden"  # just after a buffer has become hidden
    BufNew = "BufNew"  # just after creating a new buffer

    SwapExists = "SwapExists"  # detected an existing swap file

    # Options
    FileType = "FileType"  # when the 'filetype' option has been set
    Syntax = "Syntax"  # when the 'syntax' option has been set
    EncodingChanged = "EncodingChanged"  # after the 'encoding' option has been changed
    TermChanged = "TermChanged"  # after the value of 'term' has changed

    # Startup and exit
    VimEnter = "VimEnter"  # after doing all the startup stuff
    GUIEnter = "GUIEnter"  # after starting the GUI successfully
    GUIFailed = "GUIFailed"  # after starting the GUI failed
    TermResponse = "TermResponse"  # after the terminal response to t_RV is received

    QuitPre = "QuitPre"  # when using `:quit`, before deciding whether to quit
    VimLeavePre = "VimLeavePre"  # before exiting Vim, before writing the viminfo file
    VimLeave = "VimLeave"  # before exiting Vim, after writing the viminfo file

    # Various
    FileChangedShell = "FileChangedShell"  # Vim notices that a file changed since editing started
    FileChangedShellPost = "FileChangedShellPost"  # After handling a file changed since editing started
    FileChangedRO = "FileChangedRO"  # before making the first change to a read-only file

    ShellCmdPost = "ShellCmdPost"  # after executing a shell command
    ShellFilterPost = "ShellFilterPost"  # after filtering with a shell command

    CmdUndefined = "CmdUndefined"  # a user command is used but it isn't defined
    FuncUndefined = "FuncUndefined"  # a user function is used but it isn't defined
    SpellFileMissing = "SpellFileMissing"  # a spell file is used but it can't be found
    SourcePre = "SourcePre"  # before sourcing a Vim script
    SourceCmd = "SourceCmd"  # before sourcing a Vim script Cmd-event

    VimResized = "VimResized"  # after the Vim window size changed
    FocusGained = "FocusGained"  # Vim got input focus
    FocusLost = "FocusLost"  # Vim lost input focus
    CursorHold = "CursorHold"  # the user doesn't press a key for a while
    CursorHoldI = "CursorHoldI"  # the user doesn't press a key for a while in Insert mode
    CursorMoved = "CursorMoved"  # the cursor was moved in Normal mode
    CursorMovedI = "CursorMovedI"  # the cursor was moved in Insert mode

    WinEnter = "WinEnter"  # after entering another window
    WinLeave = "WinLeave"  # before leaving a window
    TabEnter = "TabEnter"  # after entering another tab page
    TabLeave = "TabLeave"  # before leaving a tab page
    CmdwinEnter = "CmdwinEnter"  # after entering the command-line window
    CmdwinLeave = "CmdwinLeave"  # before leaving the command-line window

    InsertEnter = "InsertEnter"  # starting Insert mode
    InsertChange = "InsertChange"  # when typing <Insert> while in Insert or Replace mode
    InsertLeave = "InsertLeave"  # when leaving Insert mode
    InsertCharPre = "InsertCharPre"  # when a character was typed in Insert mode, before

    TextChanged = "TextChanged"  # after a change was made to the text in Normal mode
    TextChangedI = "TextChangedI"  # after a change was made to the text in Insert mode

    ColorScheme = "ColorScheme"  # after loading a color scheme

    RemoteReply = "RemoteReply"  # a reply from a server Vim was received

    QuickFixCmdPre = "QuickFixCmdPre"  # before a quickfix command is run
    QuickFixCmdPost = "QuickFixCmdPost"  # after a quickfix command is run

    SessionLoadPost = "SessionLoadPost"  # after loading a session file

    MenuPopup = "MenuPopup"  # just before showing the popup menu
    CompleteDone = "CompleteDone"  # after Insert mode completion is done

    User = "User"  # to be used in combination with ":doautocmd"
