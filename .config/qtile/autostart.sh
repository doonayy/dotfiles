#!/bin/bash

picom &
nitrogen --restore &
dunst &

setxkbmap -model pc104 -layout us,us -variant ,intl -option grp:alt_shift_toggle
