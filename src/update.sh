#!/bin/bash

clear

clear

counter=0
(

while :
do
cat <<EOF
XXX
$counter
Loading TACP-UKK-12CC UPDATE DEV-MODE( $counter%):
XXX
EOF

(( counter+=20 ))
[ $counter -eq 100 ] && break

sleep 1
done
) |
whiptail --title " TACP-UKK-12CC " --gauge "Please wait" 7 70 0
echo "=============="

# Menghapus direktori TACP-UKK-12CC
echo "[*] Removing existing TACP-UKK-12CC..."
rm -rf /usr/share/doc/TACP-UKK-12CC

# Mengunduh versi terbaru dari repositori GitHub
echo "[*] Downloading latest version..."
git clone https://github.com/OmTegar/TACP-UKK-12CC.git /usr/share/doc/TACP-UKK-12CC

# Mengupdate file eksekusi tacp
echo "[*] Updating tacp executable..."
if [ -e "/usr/bin/tacp" ]; then
    echo -e "python3 /usr/share/doc/TACP-UKK-12CC/src/script.py" '${1+"$@"}' > /usr/bin/tacp
    chmod +x /usr/bin/tacp
    chmod +x /usr/share/doc/TACP-UKK-12CC
    chmod +x /usr/share/doc/TACP-UKK-12CC/index.sh
    echo "The file /usr/bin/tacp has been created."
fi

echo "[*] Update completed successfully!"