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

cd "Lution"
pip install -r requirements.txt

clear
cat << "EOF"
 __         __  __     ______   __     ______     __   __
/\ \       /\ \/\ \   /\__  _\ /\ \   /\  __ \   /\ "-.\ \
\ \ \____  \ \ \_\ \  \/_/\ \/ \ \ \  \ \ \/\ \  \ \ \-.  \
 \ \_____\  \ \_____\    \ \_\  \ \_\  \ \_____\  \ \_\\"\_\
  \/_____/   \/_____/     \/_/   \/_/   \/_____/   \/_/ \/_/
EOF
echo "its should open a tab in ur browser"
echo "also do u love my asci text :3"
if streamlit run main.py; then
    :
else
    python3 -m streamlit run main.py
fi

clear

echo "i got destroyed :sob:"
