#!/bin/bash
cd "$(dirname "$0")/src" || exit 1

clear

echo "===> Cleaning previous build..."
rm -rf builddir
sudo rm -rf builddir 2>/dev/null

echo "===> Setting up Meson..."
meson setup builddir || exit 1

echo "===> Compiling project..."
meson compile -C builddir || exit 1

echo "===> Installing..."
sudo meson install -C builddir || exit 1

echo "===> Updating desktop entry"

sudo update-desktop-database

echo "===> Done."
