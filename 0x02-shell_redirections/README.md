
# 0x02-shell_redirections

This directory contains scripts that demonstrate how to use shell redirections in Linux.

## Files

Here are the files in this directory and a brief description of what they do:

### 0-hello_world

This script prints "Hello, World" to the standard output (stdout).

Commands/flags used:

-   `echo`: writes text to stdout

### 1-confused_smiley

This script writes a confused smiley to a file named `confused_smiley`.

Commands/flags used:

-   `echo`: writes text to stdout
-   `>`: redirects stdout to a file

### 2-hellofile

This script prints the content of a file named `/etc/passwd` to the standard output.

Commands/flags used:

-   `cat`: prints the content of a file to stdout

### 3-twofiles

This script copies the contents of one file into another.

Commands/flags used:

-   `cat`: prints the content of a file to stdout
-   `>`: redirects stdout to a file

### 4-lastlines

This script prints the last 10 lines of a file named `/etc/passwd`.

Commands/flags used:

-   `tail`: prints the last n lines of a file to stdout
-   `-n`: specifies the number of lines to print

### 5-firstlines

This script prints the first 10 lines of a file named `/etc/passwd`.

Commands/flags used:

-   `head`: prints the first n lines of a file to stdout
-   `-n`: specifies the number of lines to print

### 6-third_line

This script prints the third line of a file named `iacta`.

Commands/flags used:

-   `head`: prints the first n lines of a file to stdout
-   `-n`: specifies the number of lines to print
-   `tail`: prints the last n lines of a file to stdout
-   `+`: specifies the starting line number for printing

### 7-file

This script creates a file named `\*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:)`

Commands/flags used:

-   `touch`: creates an empty file
