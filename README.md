# Folder Clean Up
### Goal
The goal of this script was to non-destructively clean a folder like a user Downloads by sorting them by file type and storing them within an "output" folder.
### Development Choices
- I chose to use only the "os" package for file handling to limit needed imports and prevent the need to download packages outside of Core Python 3.
- I kept the Script as a Terminal Application instead of a GUI as it felt unnecessary to add this visual element to a simple tool like a piece of code.
- File is organized to allow it to be imported into other scripts with a single import of the "cleanFolder" function to allow it to be built into later systems if wanted. 
