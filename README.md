# djangostudies
 Estudos de Django, projeto com intenção didática.
 Projeto criado em sistema operacional Linux|Debian.

 ## Requisitos 
 - Python (nesse projeto foi usado 3)
 - pip install (sudo apt-get install python3-pip)


## Configuração de Ambiente
 - Que de preferência você esteja dentro de uma venv.
- Caso não saiba como fazer isso, segue os passos abaixo:
#### Passo 1 - Instalação da virtualenv
```bash
sudo pip3 install virtualenv
```

#### Passo 2 - Criação do ambiente virtual

```bash
virtualenv -p python3 venv
```
#### Passo 3 - Ativando ambiente virtual
```bash
source venv/bin/activate
```

## Executando projeto 

### Com o ambiente virtual ativo, acesse a pasta raiz do projeto, e execute os seguintes comandos:

#### Passo 1- Instalação dos pacotes
```bash
pip install -r requirements.txt
```
#### Passo 2- 
```bash
python manage.py (coisas relativas a migration)
```
#### Passo 3- Executar a aplicação 
```bash
pip manage.py runserver 
```
#### A aplicação se encontrará funcionando no :
```bash
http://localhost:8000/
```