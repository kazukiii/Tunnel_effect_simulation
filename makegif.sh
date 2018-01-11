#!/bin/zsh

ls qm_double_*.png | sed 's/qm_double_//' | sort -n | sed 's/^/qm_double_/'| tr '\n' ' ' | sed 's/$/\ harmonic_hbar5.gif/' | xargs convert -layers optimize -delay 100 -loop 0
