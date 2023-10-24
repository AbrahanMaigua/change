# MObility

# dependecia
* python
* pip
* requests
* python_dot

# inicio

1. copia el repositorio
   `git clone https://github.com/AbrahanMaigua/change,git`
  
3. crea un entorno virtual y instala las dependecias
   
   `python -m venv mobility`
   * activa el entorno virtual
      * linux (bash/zsh)
         ```source mobility/bin/activate```
      * windonsw (cmd)
          `mobility/Script/activate.bat`
   * instala las dependecias
     * ``pip install -r requirements.txt``
 
7. app id
   
   accede a Open pix vea al menu a  api/pulugin crea una nueva api/plugin
   coloca el nombre a la api seleciona api rest y seleciona la cunta que vas a utilizar
   luego copias la App ID

5. crea un archivo .env
   
   crea un archivo sin extecion llamdo .env donde guradar el app id remplasa
   por APP_ID por la app id que te da open pix   
   `app_id='APP_ID'`
   
9. genera un codigo Qr
    `python pixadd.py`

# documentacion
open pix
python venv
python_dot
