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
         ```mobility/bin/activate```
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
   
9. gerar um código QR
     `python logit.py`

## libnfc
Install NFC tools:

`sudo apt install libnfc6 libnfc-bin libnfc-examples`
I had a problem detecting the I2C device with nfc-list -v and nfc-scan-device -v and it was due to libnfc not scanning for I2C devices out of the box.

Let libnfc know the device address of the reader in /etc/nfc/libnfc.conf:

`sudo nano /etc/nfc/libnfc.conf`
file /etc/nfc/libnfc.conf
`device.name = "PN532 over I2C"`
`device.connstring = "pn532_i2c:/dev/i2c-1"`

#documentação
* [logica de codigo](doc.md)
* [abrir pix](https://developers.openpix.com.br/)
* [python virtual env](https://docs.python.org/3/library/venv.html)
* [nfc seting](https://blog.stigok.com/2017/10/12/setting-up-a-pn532-nfc-module-on-a-raspberry-pi-using-i2c.html)