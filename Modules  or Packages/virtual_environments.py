# Impact of installing packages; we use pip install package_name
# This installs, the package globally by default that means, it willbe available for every application you are going to create
# The down side of this is that you might run into issues with versions.
# It is best to install the package locally, this is done by utilizing a virtual environment
# 
# A virtual environment is a folder that has all the code that will be needed to run the application you're creating
# Everything needed will be installed into the folder, then we can use it. Thus, we need to create the folder first and we have a
# utility called "virtualenv" that does that

# CREATING A VIRTUAL ENVIRONMENT
# Install virtual environment
# pip install virtualenv

# Windows systems
# python -m venv <folder_name>

# osx/Linus (bash)
# virtualenv <folder_name>


# USING VIRTUAL ENVIRONMENTS
# Windows systems
# cmd.exe
# <folder_name>\Scripts\Activate.bat
# Powershell
# <folder_name>\Scripts\Activate.ps1
# bash shell
# . ./<folder_name>\Scripts\activate 

# OSX/LINUS (bash)
# <folder_name>/bin/activate
# OR 
# . <folder_name>/bin/activate

# INSTALLING TO A VIRTUAL ENVIRONMENT
# Install from an individual package
# pip install colorama

# Install from a list of packages
# pip install -r requirements.txt

# requirements.txt
# colorama
# python -m pip install --upgrade pip