#!/bin/bash
clear
echo "RUN LUTION"
cat << "EOF"
 __         __  __     ______   __     ______     __   __
/\ \       /\ \/\ \   /\__  _\ /\ \   /\  __ \   /\ "-.\ \
\ \ \____  \ \ \_\ \  \/_/\ \/ \ \ \  \ \ \/\ \  \ \ \-.  \
 \ \_____\  \ \_____\    \ \_\  \ \_\  \ \_____\  \ \_\\"\_\
  \/_____/   \/_____/     \/_/   \/_/   \/_____/   \/_/ \/_/
EOF

if grep -qi 'ubuntu' /etc/os-release; then
    if ! dpkg -s python3-venv >/dev/null 2>&1; then
        echo "Installing python3-venv..."
        sudo apt update && sudo apt install -y python3-venv
    else
        echo "python3-venv is already installed."
    fi
fi

cd ..
python3 -m venv ".venv"
source .venv/bin/activate

cd "src/Lution" || exit 1
pip install -r requirements.txt

clear
cat << "EOF"
 __         __  __     ______   __     ______     __   __
/\ \       /\ \/\ \   /\__  _\ /\ \   /\  __ \   /\ "-.\ \
\ \ \____  \ \ \_\ \  \/_/\ \/ \ \ \  \ \ \/\ \  \ \ \-.  \
 \ \_____\  \ \_____\    \ \_\  \ \_\  \ \_____\  \ \_\\"\_\
  \/_____/   \/_____/     \/_/   \/_/   \/_____/   \/_/ \/_/
EOF

echo "It should open a window right now, if not click on the link"
echo "If you get a error or something like that, try pressing R to fix it"
echo "Also do you love my ASCII text? :3"

python3 launch.py

echo "i got destroyed 😭"
