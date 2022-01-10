# Doom - Encryptor CLI
***Easy password encryption and decryption***

## Prologue
---

Please distribute and use this cli as you wish, but I would appreciate it if you were to contribute.

## Setup
---

* If you are on Arch you may use the PKGBUILD file to manage encryptor with pacman.

* You may use the install script if it is desirable. Or you can copy the script to a location of your desire and make it executable.

* _Optional but recommended:_ Create the .local/bin directory in your home, then add it to your path variable with these steps.
  1. Do: `mkdir "$HOME/.local/bin"`
  2. Add: `export PATH="$HOME/.local/bin:$PATH"` into your .zshrc or .basrc file.

---

## Usage
---

You may view the command and usage by simply typing the command with no arguments.

``` sh
encryptor
```

For more details user the help argument:

``` sh
encryptor --help
```

You may encrypt by doing:

``` sh
encryptor -m encrypt -i 'foo' -o foo.txt
```

You may decrypt with:

 ``` sh
encryptor -m decrypt -i foo.txt 
```

---
If you have any recommendations or issues with the script please submit a ticket.
