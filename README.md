
Projeto WEB Django Padrão

* Alterar settings
    * TIME_ZONE para America/Sao_Paulo;
    * DATABASE_URL para Postgres;
    * LANGUAGE_CODE para "pt-br";
* Instalar requirements comuns;
* gitignore padrão;
* README padrão;
* ENVVARS;

* Django Registration;
* Login;
* Password recover;
* Change password;
* Social authentication;

##System dependencies

* Python 2.7.8;
* Django 1.7 (not tested on previous versions);
* PostgreSQL 9.3.5 (with contrib 'unaccent' extension);

##Setup instructions

###Install development requirements

    git clone ssh://git@stash.acotelbrasil.com.br:7999/devtools/django_local_tools.git
    cd django_local_tools
    pip install -r requirements.pip

    * Certifique-se de que você não tenha algum virtualenv ativado

###Create and activate virtualenv

    virtualenv --no-site-packages {virtualenvs_path}/{project_name}
    source {virtualenvs_path}/{project_name}/bin/activate

###Install project's requirements

    pip install -r requirements.pip

###Create database

    createdb -U postgres -E utf-8 -T template0 {project_name}

###Create .env file with the following content

    DEBUG=True
    SECRET_KEY=ypfj76g@yp#f7b$u&-1w1+&715$mqu^z4u^o6g1^q2uhv3vblt
    DATABASE_URL=postgres://postgres:postgres@localhost:5432/{project_name}
    ALLOWED_HOSTS=*

###Create database tables

    ./manage.py migrate

###Create admin superuser

    ./manage.py createsuperuser

###Start local server
    
    ./manage.py runserver

###Test
    
    http://localhost:8000/
    http://localhost:8000/admin
