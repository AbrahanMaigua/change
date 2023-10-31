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
   
    `python -m mobility venv`
    * ativar o ambiente virtual
       * linux (bash/zsh)
         ```mobility/bin/ativar```
       * windonsw (cmd)
           `mobility/Script/activate.bat`
   * instalar dependências
      * ``pip install -r requisitos.txt``
 
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

#documentação
* [abrir pix](https://developers.openpix.com.br/)
* [python ven](https://docs.python.org/3/library/venv.html)