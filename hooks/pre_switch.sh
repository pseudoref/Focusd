#!/usr/bin/env bash

if command -v gsettings &>/dev/null; then
	gsettings set org.gnome.desktop.notifications show-banners false || true
fi
