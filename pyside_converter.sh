#!/usr/bin/bash

# main_window
pyside6-uic ui/main_window.ui -o resource/main_window.py

# about_version
pyside6-uic ui/about_version.ui -o resource/about_version.py

# icon
pyside6-rcc icon/icon.qrc -o icon/icon_rc.py 