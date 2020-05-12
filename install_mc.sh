sudo rm -rf /lib/firmware/intel-ucode/*
sudo cp ./Intel/$1 /lib/firmware/intel-ucode/
echo 1 > /sys/devices/system/cpu/microcode/reload
sudo update-initramfs -u
sudo reboot