Iniciar o prjeto Django     

python -m venv venv 
./venv/Scripts/activate
pip install django 
django-admin startproject project_agenda .

# Configurando o GIT

git config --global user.name ''
git config --global user.email ''
git config --global init.defaultBranch main
git init
git add . <!-- para adicionar todos os arquivos -->
git commit -m 'Mensagem'
git remote add origin Url do git
