
## 0x01. Shell, permissions

This directory contains scripts demonstrating how to use permissions in shell scripting.

### Files

-   `0-iam_betty`: This script changes the user ID to `betty`.
    
    
    `$ ./0-iam_betty` 
    
-   `1-who_am_i`: This script prints the effective username of the current user.

    
    `$ ./1-who_am_i` 
    
-   `2-groups`: This script prints all the groups the current user is part of.
    
    
    `$ ./2-groups` 
    
-   `3-new_owner`: This script changes the owner of the file `hello` to the user `betty`.

    
    `$ ./3-new_owner hello betty` 
    
-   `4-empty`: This script creates an empty file called `hello`.
    
    
    `$ ./4-empty hello` 
    
-   `5-execute`: This script adds execute permission to the owner of the file `hello`.
    
    
    `$ ./5-execute hello` 
    
-   `6-multiple_permissions`: This script adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.
    
    
    `$ ./6-multiple_permissions hello` 
    
-   `7-everybody`: This script adds execute permission to the owner, the group owner, and other users, to the file `hello`.
    
    
    `$ ./7-everybody hello` 
    
-   `8-James_Bond`: This script sets the permission of the file `hello` to `-rwxr-x-wx`.
    
    
    `$ ./8-James_Bond hello` 
    
-   `9-John_Doe`: This script sets the mode of the file `hello` to `-rwxr-xr-x`.
    
    
    `$ ./9-John_Doe hello` 
    
-   `10-mirror_permissions`: This script sets the mode of the file `hello` to be the same as that of the file `olleh`.
    
    
    `$ ./10-mirror_permissions hello olleh` 
    
-   `11-directories_permissions`: This script adds execute permission to all subdirectories of the current directory for the owner, group owner, and other users.
    
    
    `$ ./11-directories_permissions` 
    
-   `12-directory_permissions`: This script creates a directory called `dir_holberton` with permissions `751`.
    
    
    `$ ./12-directory_permissions dir_holberton` 
    
-   `13-change_group`: This script changes the group owner of the file `hello` to `holberton`.
    
    
    `$ ./13-change_group hello holberton` 
    
-   `14-change_owner_and_group`: This script changes the owner to `betty` and the group owner to `holberton` for all files and directories in the current directory.
    
    
    `$ ./14-change_owner_and_group` 
    
-   `15-symbolic_link_permissions`: This script changes the owner and the group owner of the file `_hello` to `betty` and `holberton`, respectively. The file `_hello` is a symbolic link to the file `hello`.
    
    
    `$ ./15-symbolic_link_permissions` 
    
-   `16-if_only`: This script changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.
    
    `$ ./16-if_only hello`
