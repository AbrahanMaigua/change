#!/bin/bash

user=$(whoami)
cw=$(pwd)
files=('.env' 'database.ini')
echo "start config"

echo "username: $user" 
echo "dir: $cw"

git config --global --add safe.directory $cw

echo "config databases"
if [ -f "${files[0]}" ] && [ -f "${files[1]}" ]; then
    echo 'exite'
   
else
   
    touch database.ini
    touch .env

    # Create the file repository configuration:
    sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

    # Import the repository signing key:
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

    # Update the package lists:
    sudo apt-get update
    sudo apt-get upgrade


    # Install the latest version of PostgreSQL.
    # If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
    sudo apt-get -y install postgresql
    sudo apt-get install libpq-dev
fi

echo "virtual environment..."

if  [ -d "env/" ] && [ -d "pn532/" ]; then
    echo "reddy"
else
    sudo apt install python3-pip -y
    sudo apt install python3.10-venv
    sudo pip3 install virtualenv 
    sudo virtualenv  --system-site-packages env
    source env/bin/activate
    pip install -r requirements.txt
    git clone https://github.com/hoanhan101/pn532.git 
fi


# Verificar si hay al menos dos commits en el repositorio
if [ "$(git rev-list --count HEAD)" -ge 2 ]; then
    # Obtener el hash del antepenúltimo commit
    antepenultimo_commit=$(git log --format="%H" -n 3 | tail -n 1)
    git fetch
    # Mostrar detalles del antepenúltimo commit
    echo "Detalles del antepenúltimo commit:"
    echo "$antepenultimo_commit"
    #git show "$antepenultimo_commit"
else
    echo "No hay suficientes commits en el repositorio para obtener el antepenúltimo commit."
fi
