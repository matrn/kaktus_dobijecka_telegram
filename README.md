# kaktus-dobijecka-telegram
Kaktus dobíječka telegram bot

# Installation
- `pip3 install python-telegram-bot`
- `pip3 install selectolax`


# Monitor MEM & CPU usage
- `top -p $(ps aux | grep "[b]ot.py" | awk '{print $2}')` then press `e` to set memory in `MB`