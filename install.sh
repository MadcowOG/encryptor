echo "Will try to copy to .local/bin in your home directory first. To avoid using sudo/doas. It is recommended that you create this directory and add it to your path variable in your .bashrc or .zshrc. The README.md has steps for this."
echo "You will have 10 seconds to exit."
sleep 10
if ls "$HOME/.local/bin"
then
    cp ./encryptor.py "$HOME"/.local/bin/encryptor
    chmod +x "$HOME"/.local/bin/encryptor
else
    if ! sudo
    then
        doas cp ./encryptor.py /usr/bin/encryptor
        doas chmod +x /usr/bin/encryptor
        if [ "$?" = "0" ];
        then
            exit 0
        fi
    else
        sudo cp ./encryptor.py /usr/bin/encryptor
        sudo chmod +x /usr/bin/encryptor
        if [ "$?" = "0" ];
        then
            exit 0
        fi
    fi
fi
