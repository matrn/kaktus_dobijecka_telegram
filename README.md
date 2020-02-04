# kaktus-dobijecka-telegram
Kaktus dobíječka telegram bot

# Installation
- telegram bot: `pip3 install python-telegram-bot --upgrade`
- html parsing: `pip3 install selectolax --upgrade`


# Monitor MEM & CPU usage
- `top -p $(ps aux | grep "[b]ot.py" | awk '{print $2}')` then press `e` to set memory in `MB`