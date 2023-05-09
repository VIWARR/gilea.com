# PIP INSTALL 


## [django-cleanup](https://pypi.org/project/django-cleanup/)
```bash
pip install django-cleanup
```
> INSTALL, CONFIGURED (ADD APPS)
>>The django-cleanup app automatically delete files for FileField, ImageField and subclasses. When a FileField’s value is changed and the model is saved, the old file is deleted. When a model that has a FileField is deleted, the file is also deleted. A file that is set as the FileField’s default value will not be deleted.

***


## [django-crispy-form](https://django-crispy-forms.readthedocs.io/en/latest/install.html)
```bash
pip install django-crispy-forms
```
> INSTALL, CONFIGURED (ADD APPS, SETTINGS)
>> django-crispy-forms provides you with a filter and tag that will let you control the rendering behavior of your Django forms in a very elegant and DRY way. Have full control without writing custom form templates. 

## [django-crispy-bootstrap5](https://github.com/django-crispy-forms/crispy-bootstrap5)
```bash
pip install crispy-bootstrap5
```
> INSTALL, CONFIGURED (ADD APPS, SETTINGS)
>> for django-crispy-forms
***


## [python-dotenv](https://pypi.org/project/python-dotenv/)
```bash
pip install django-dotenv
```
>INSTALL, CONFIGURED (SETTINGS)
>> If your application takes its configuration from environment variables, launching it in development is not very practical because you have to set those environment variables yourself.

>> To help you with that, you can add Python-dotenv to your application to make it load the configuration from a .env file when it is present (e.g. in development) while remaining configurable via the environment
***


## [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor/blob/main/README.rst)
```bash
pip install django-ckeditor
```
> INSTALL, CONFIGURED (ADD APPS, SETTINGS), collectstatic
>>  Provides a,, and utilizing CKEditor with image uploading and browsing support included.
***


## [django-braces](https://django-braces.readthedocs.io/en/latest/)
```bash
pip install django-braces
```
>INSTALL
***


## [django-allauth](https://django-allauth.readthedocs.io/en/latest/)
```bash
pip install django-allauth
```
>INSTALL, CONFIGURED (ADD APPS, SETTINGS), migrate, collectstatic

> admin sites exsaple.com on http://127.0.0.1:8000/
>>Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
***


## [django-humanize](https://docs.djangoproject.com/en/4.2/ref/contrib/humanize/)
```bash
INSTALLED_APPS = [
...
'django.contrib.humanize',
...
]
```
>CONFIGURED (ADD APPS)
>> A set of Django template filters useful for adding a “human touch” to data.
***


## [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
```bash
python -m pip install django-debug-toolbar
```
>INSTALL, CONFIGURED (ADD APPS, SETTINGS)
>> The Django Debug Toolbar is an extension of Django that provides a debugging panel in the browser to help debug performance and behavior issues with your application. The toolbar includes information about database queries, cache, response time, request information, settings, and more.
***


## [channels](https://channels.readthedocs.io/en/stable/installation.html)
```bash
python -m pip install -U channels["daphne"]
```
>INSTALL


## [pillow](https://github.com/codingforentrepreneurs/Guides/blob/master/all/imagefield_and_pillow.md)
```bash
pip install pillow
```
>INSTALL