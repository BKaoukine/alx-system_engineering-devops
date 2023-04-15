
## 0x03-shell_variables_expansions

This directory contains scripts that demonstrate the use of shell variables and expansions in the Bash shell. Below is a brief description of each script and the commands/flags used in them:

### 0-alias

This script creates an alias named `ls` with the value `rm *`.

Commands/flags used:

-   `alias`: used to create an alias

### 1-hello_you

This script prints "hello user" where "user" is the current Linux user.

Commands/flags used:

-   `echo`: used to print text to stdout
-   `$USER`: a shell variable that holds the current user's username

### 2-path

This script adds `/action` to the `PATH` environment variable if it is not already present.

Commands/flags used:

-   `grep`: used to search for a pattern in a file
-   `export`: used to set an environment variable
-   `$PATH`: a shell variable that holds the list of directories where executable files are located

### 3-paths

This script counts the number of directories in the `PATH` environment variable.

Commands/flags used:

-   `tr`: used to transform or delete characters
-   `:`: the delimiter used in the `PATH` variable to separate directories
-   `wc`: used to count lines, words, or characters in a file

### 4-global_variables

This script lists environment variables that are both global and local.

Commands/flags used:

-   `set`: used to list all shell variables

### 5-local_variables

This script lists all local variables, environment variables, and functions.

Commands/flags used:

-   `set`: used to list all shell variables

### 6-create_local_variable

This script creates a new local variable named `BETTY` with the value `Holberton`.

Commands/flags used:

-   `export`: used to set an environment variable

### 7-create_global_variable

This script creates a new global variable named `HOLBERTON` with the value `Betty`.

Commands/flags used:

-   `export`: used to set an environment variable

### 8-true_knowledge

This script prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`.

Commands/flags used:

-   `$((...))`: used to perform arithmetic operations in Bash

### 9-divide_and_rule

This script prints the result of the division of 10 by the environment variable `DIVIDE`.

Commands/flags used:

-   `$((...))`: used to perform arithmetic operations in Bash

### 10-love_exponent_breath

This script displays the result of `BREATH` to the power of `LOVE`.

Commands/flags used:

-   `$((...))`: used to perform arithmetic operations in Bash

### 11-binary_to_decimal

This script converts a number in base 2 (binary) to base 10 (decimal).

Commands/flags used:

-   `echo`: used to print text to stdout
-   `$((...))`: used to perform arithmetic operations in Bash

### 12-combinations

This script prints all possible combinations of two letters, except `oo`.

Commands/flags used:

-   `echo`: used to print text to stdout
-   `grep`: used to search for a pattern in a file
-   `awk`: used to process text data

### 13-print_float

This script prints a number with two decimal places.

Commands/flags used:

-   `printf`: used to print formatted text to stdout

### 14-decimal_to_hexadecimal
