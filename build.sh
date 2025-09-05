# remove previous builds
rm -rf build dist *.spec

# build as a single executable
pyinstaller --windowed --name "ArbApp" --onefile --icon=icon.icns gui.py

echo "Executable is in dist/ArbApp"