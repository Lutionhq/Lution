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

python3 -m venv venv
source venv/bin/activate

cd "Lution" || exit 1
pip install -r requirements.txt

clear
cat << "EOF"
 __         __  __     ______   __     ______     __   __
/\ \       /\ \/\ \   /\__  _\ /\ \   /\  __ \   /\ "-.\ \
\ \ \____  \ \ \_\ \  \/_/\ \/ \ \ \  \ \ \/\ \  \ \ \-.  \
 \ \_____\  \ \_____\    \ \_\  \ \_\  \ \_____\  \ \_\\"\_\
  \/_____/   \/_____/     \/_/   \/_/   \/_____/   \/_/ \/_/
EOF

echo "It should open a tab in your browser, if not click on the link"
echo "Also do you love my ASCII text? :3"

streamlit run main.py || python3 -m streamlit run main.py

clear
echo "i got destroyed 😭"
