
# 0x00-shell_basics

This directory contains shell scripts that introduce the basics of shell scripting and commands.

## Scripts

### 0-current_working_directory

This script prints the current working directory using the `pwd` command.

### 1-listit

This script lists the contents of the current directory using the `ls` command. It uses the following flags:

-   `-l`: to show the files in long format
-   `-a`: to show hidden files
-   `-h`: to show file sizes in human-readable format

### 2-bring_me_home

This script changes the working directory to the user's home directory using the `cd` command.

### 3-listfiles

This script lists the contents of the current directory, including hidden files and directories, using the `ls` command. It uses the following flags:

-   `-l`: to show the files in long format
-   `-a`: to show hidden files
-   `-h`: to show file sizes in human-readable format

### 4-listmorefiles

This script lists the contents of the current directory and the parent directory, including hidden files and directories, using the `ls` command. It uses the following flags:

-   `-l`: to show the files in long format
-   `-a`: to show hidden files
-   `-h`: to show file sizes in human-readable format

### 5-listfilesdigitonly

This script lists the contents of the current directory, including hidden files and directories, using the `ls` command. It uses the following flags:

-   `-1`: to show each file on a new line
-   `-a`: to show hidden files

### 6-firstdirectory

This script creates a directory named `my_first_directory` in the `/tmp/` directory using the `mkdir` command.

### 7-movethatfile

This script moves the file `betty` from the `/tmp/` directory to the `/tmp/my_first_directory` directory using the `mv` command.

### 8-firstdelete

This script deletes the file `betty` from the `/tmp/` directory using the `rm` command.

### 9-firstdirdeletion

This script deletes the directory `my_first_directory` from the `/tmp/` directory using the `rmdir` command.

### 10-back

This script changes the working directory to the previous directory using the `cd` command with the `-` option.

### 11-lists

This script lists all files, including hidden files, in the current directory and the parent directory, using the `ls` command. It uses the following flags:

-   `-l`: to show the files in long format
-   `-a`: to show hidden files
-   `-h`: to show file sizes in human-readable format

### 12-file_type

This script prints the type of the file named `iamafile` in the current directory using the `file` command.

### 13-symbolic_link

This script creates a symbolic link to `/bin/ls` named `__ls__` in the current directory using the `ln` command.

### 14-copy_html

This script copies all HTML files from the current directory and its subdirectories to the parent directory, while preserving the directory structure, using the `cp` command with the following options:

-   `-R`: to copy directories recursively
-   `-p`: to preserve file attributes such as timestamps and permissions
-   `-u`: to copy only when the source file is newer than the destination file.

### 15-lets_move

This script moves all files beginning with an uppercase letter from the current directory to
