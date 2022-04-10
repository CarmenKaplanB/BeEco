# BeEco :seedling:
Be Eco es una plataforma digital cuyo objetivo es motivar la enseñanza ambiental, con el propósito de obtener las capacidades y habilidades correctas para el bienestar social. Adicionalmente, promover una participación activa en la solución de obstáculos del medio ambiente.


|  2020-04-12 :leaves:
[Ver este proyecto en despliegue](https://be-eco.herokuapp.com/ "Heroku Link") 

#  Script del flujo de trabajo (pipeline).

###  Flujo de trabajo con GitLab.

GitLab tiene muchas opciones y puede resultar un poco amenazante al principio. Veremos el flujo básico para programar y las opciones necesarias según nos hagan falta. Si explico todas las funciones de golpe, lo más probable es que salgáis corriendo.  La parte central es el gestor de incidencias (issues). Una incidencia es tanto una función nueva como un reporte de bug. Tiene que incluir toda la información necesaria para realizar la tarea. La incidencia actúa como contrato y dice lo que hay que hacer. Si hay un fallo y no tiene una incidencia creada, a efectos de programación no existe. En principio cualquier usuario puede crear incidencias, siempre que lo permita la configuración del proyecto, pero es tarea del programador aceptarla o no.

#  Instalación de GitLab.

~~~
curl https://packages.GitLab.com/install/repositories/GitLab/GitLab-ee/script.deb.sh | sudo bash
~~~

#  Registro de GitLab Runner en Windows.

Descarga de Git para Windows y de datos binarios de GitLab Runner

~~~
./GitLab-runner.exe register
~~~

Ahora, introduce el URL de la instalación GitLab (en este caso es un ejemplo):

~~~
https://GitLab.com
~~~

#  Instalación e inicio de GitLab Runner en Windows

~~~
cd C:\GitLab-Runner
.\GitLab-runner.exe install
.\GitLab-runner.exe start
~~~

#  Copia local del repositorio

~~~
$ git clone https://server/namespace/project.git
~~~

#  Script para la generación del entorno de liberación.

~~~
sudo gitlab-rake gitlab:env:info

git log --pretty=oneline
git reset --hard 
~~~

#  Script de pruebas en el entorno de liberación.

~~~
shell check:
  image: koalaman/shellcheck-alpine:stable
  stage: test
  before_script:
    - shellcheck --version
  script:
    - shellcheck scripts/**/*.sh  # path to your shell scripts

shfmt:
  image: mvdan/shfmt:v3.2.0-alpine
  stage: test
  before_script:
    - shfmt -version
  script:
    - shfmt -i 2 -ci -d scripts  # path to your shell scripts
~~~

#  Script para la generación del despliegue.

~~~
before:
    - apt-get install rubygens

run-test:
    script:
        - ruby -- version

stages: 
    - build
    - test
    - staging
    - production

job pre:
    stage: .pre
    script: make stage

job build:
    stage: build
    script: dependencies
~~~



# Capturas

![Example](https://github.com/MariaDelCarmenHernandezDiaz/BeEco/blob/main/Capturas/eco1.PNG "Example")
![Example](https://github.com/MariaDelCarmenHernandezDiaz/BeEco/blob/main/Capturas/eco2.PNG "Example")
![Example](https://github.com/MariaDelCarmenHernandezDiaz/BeEco/blob/main/Capturas/eco3.PNG "Example")
![Example](https://github.com/MariaDelCarmenHernandezDiaz/BeEco/blob/main/Capturas/eco4.PNG "Example")
![Example](https://github.com/MariaDelCarmenHernandezDiaz/BeEco/blob/main/Capturas/eco5.PNG "Example")
![Example](https://github.com/MariaDelCarmenHernandezDiaz/BeEco/blob/main/Capturas/eco6.PNG "Example")
