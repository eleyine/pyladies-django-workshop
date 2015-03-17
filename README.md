# Pyladies Django Workshop Boilerplate

## Requirements

* `git` - instructions [here](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* `pip` - instructions [here](https://pip.pypa.io/en/latest/installing.html)
* `virtualenvwrapper` - instructions [here](https://virtualenvwrapper.readthedocs.org/en/latest/install.html)
* `npm` (node package manager) - instructions [here](https://docs.npmjs.com/getting-started/installing-node)

## Installation

1.  Get the boilerplate code.
    -  If you have a github account, fork this repository and then:
    ```bash
    # in your working directory
    $ git clone git@github.com:<your username>/pyladies-django-workshop.git
    $ cd pyladies-django-workshop
    $ git reset --hard boilerplate
    ```

    - If you don't have a github account:
    ```bash
    # in your working directory
    $ git clone https://github.com/eleyine/pyladies-django-workshop.git
    $ cd pyladies-django-workshop
    $ git reset --hard boilerplate
    ```

2.  Set up vitualenv.

    ```bash
    # in pyladies-django-workshop
    $ mkvirtualenv pyladies-django
    $ workon pyladies-django
    (pyladies-django) $ pip install -r requirements.txt
    ```

3.  Install bower dependencies.

    ```bash
    # in pyladies-django-workshop
    (pyladies-django) $ npm install -g bower
    # you might need to use `sudo npm install -g bower`
    (pyladies-django) $ bower install
    ```

4.  Migrate Django app models.

    ```bash
    # in pyladies-django-workshop
    (pyladies-django) $ python manage.py migrate
    (pyladies-django) $ python manage.py runserver
    ```

5. Visit <http://localhost:8000/>, you should now see a blank page with a functional navbar and sidebar.

