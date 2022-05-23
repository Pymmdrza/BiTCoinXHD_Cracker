@Echo off
title BtcXHD.py
Pushd "%~dp0" 
pip install hdwallet
pip install colorama
pip install rich
:loop
python BtcXHD.py
goto loop
