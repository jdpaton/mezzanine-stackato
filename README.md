Mezzanine
---------

This a vanilla Mezzanine CMS project that is ready to deploy straight 
to a Stackato cloud.


** Local development **

    pip install -r requirements.pip
    python manage.py createdb --noinput
    python manage.py runserver

** Deploying to stackato **

    stackato push -n

** Default admin user **

The default admin user credentials are:

    u: admin
    p: mezzanine

You can login with these credentials at /admin. It is recommended that you 
change this default password, edit stackato.yml and alter the 
'manage.py changepassword2' command.

