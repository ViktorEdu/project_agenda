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
Trabalhando com model do django

# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')