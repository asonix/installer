#!/bin/bash

i3-msg restart
xrdb ~/.Xresources

gsettings set org.gnome.desktop.background picture-uri "file:////usr/share/backgrounds/164.jpg"

# nohup ./alternating_layouts.py & exit
