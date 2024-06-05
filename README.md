# Mobilty

# dependência
* python
* pip
* requests
* python_dot

# começar

1. copie o repositório
    `git clone https://github.com/AbrahanMaigua/change.git`
  
3. crie um ambiente virtual e instale dependências
   
    `python -m venv mobility`
    * ativar o ambiente virtual
       * linux (bash/zsh)
         `source mobility/bin/activate`
       * windonsw (cmd)
           `mobility\Scripts\activate.bat`
   * instalar dependências
      * ``pip install -r requirements.txt``
 
7. ID do aplicativo
   
    acesse [Open pix]() veja menu api/pulugin crie uma nova api/plugin
    nomeie a API, selecione rest api e selecione a conta que você vai usar
    em seguida, copie o ID do aplicativo

5. crie um arquivo .env
   
    Crie um arquivo sem extensão chamado .env onde você pode armazenar o ID do aplicativo substituto
    pelo **APP_ID** pelo id do app que o open pix te dá
    `APP_ID='APP_ID'`
   

O sim o arquivo`.env` não existe e enviará um `error 500 internal server error` em todas as páginas que usam esse arquivo

# database em producion
 To use the apt repository, follow these steps:

install posgreSql
```
# Create the file repository configuration:
sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql
sudo apt-get install libpq-dev

```
edit password user postgres

```
sudo service postgresql start
sudo su

sudo -u postgres psql

\password postgres  

\q

psql -U postgres -h localhost

CREATE DATABASE cargador;
```

create file touch *database.ini*
```
touch database.ini
```

```
[postgresql]
host=localhost
database=cargador
user=postgres
password=YourPassword
```


## libnfc
Install NFC tools:

`sudo apt install libnfc6 libnfc-bin libnfc-examples`
I had a problem detecting the I2C device with nfc-list -v and nfc-scan-device -v and it was due to libnfc not scanning for I2C devices out of the box.

Let libnfc know the device address of the reader in /etc/nfc/libnfc.conf:

`sudo nano /etc/nfc/libnfc.conf`
file /etc/nfc/libnfc.conf
`device.name = "PN532 over I2C"`
`device.connstring = "pn532_i2c:/dev/i2c-1"`

# run server and chomium start raspberry pi

* server flask

 `sudo nano /etc/systemd/system/server.service`

```
[Unit]
Description=Your Flask App
After=network.target

[Service]
User=kuro
Group=www-data
WorkingDirectory=/home/abrahan/change/
Environment="/home/abrahan/change/mobility/bin"
ExecStart=/home/abrahan/change/mobility/bin/gunicorn -w 4 -b 0.0.0.0:8000 app:app

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl daemon-reload
sudo systemctl start server.service
```


* chromiun
`nano /home/kuro/.config/autostart/autovlc.desktop`

```
[Desktop Entry]
Type=Application
Name=My Web App
Exec=chromium-browser http://localhost:5000 --kiosk
Icon=chromium-browser
Terminal=false

```

# recursos
* [logica de codigo](doc.md)
* [abrir pix](https://developers.openpix.com.br/)
* [python virtual env](https://docs.python.org/3/library/venv.html)
* [nfc seting](https://blog.stigok.com/2017/10/12/setting-up-a-pn532-nfc-module-on-a-raspberry-pi-using-i2c.html)

* [guinicode](https://www.youtube.com/watch?v=KWIIPKbdxD0)
* [postgrestSQL]{https://www.postgresql.org/download/linux/ubuntu/}
