Iniciar o prjeto Django     

python -m venv venv 
./venv/Scripts/activate
pip install django 
django-admin startproject project_agenda .
python manage.py startproject contact

# Configurando o GIT

git config --global user.name ''
git config --global user.email ''
git config --global init.defaultBranch 
configurar o .gitignore
git init
git add . <!-- para adicionar todos os arquivos -->
git commit -m 'Mensagem'
git remote add origin Url do git
git push origin main -u

*****

Migrando a base dedados do Django

python manage.py makemigrations
python manage.py migrate

Criando e modificando a senha do super usuário Django

python manage.py createsuperuser
python manage.py changepassword USERNAME *Caso eu esqueça a senha

*****
