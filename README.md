Configurações iniciais:
1 - criar um ambiente virtual
python -m venv venv

2 - iniciar o ambiente virtual
venv\Scripts\Activate

2.1 - Caso algum comando retorne um erro de permissão execute o código e tente novamente:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

3 - Instalar o Django
pip install django
pip install pillow

4 - Criar o projeto Django
django-admin startproject core .

5 - Rodar o servidor para testar
python manage.py runserver

6 - Criar um app usuarios
python manage.py startapp usuarios
