# NextGrowth Labs
#### Screening evaluation Project

This evaluation project is done for the **NextGrowth Labs** recruitment process.


## Problem Set 1


``` python
import re

text = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}'

numbers = re.findall(r'(?<=:)\d+', text)
print(numbers)

```


## Problem Set 2

### Description

The aim of the project is to build a Django app, in which admin is able to add a new app with it's details like url, category, subcategory, logo and points for download. And a user should be able to view the apps available, follow the link, earn points by saving a screen shot of the app and view points earned.

### Video demo

NB: Follow this [link](https://drive.google.com/file/d/1f7bz-VrYc5_pkBDK__7u-Va4sFUJljq5/view?usp=drive_link) for a video demo of the app.


### Technologies used


*	`Django`
    > Django framework is used for the app creation as it is simple and have most of the essential extensions inbuilt.

*	`Django Rest Framework`
    > Used for implimenting APIs.

*	`Pillow`
    > Used to process images.

*	`VueJS`
    > Used as a JavaScript framework for building UI & UX. Inside vue.js used:
    > - Vuex as the state mansgement library
    > - Vue Router as router for making it a single page application
    > - Also Chart.js for generating charts.

*	`SQlite`
    > As the database.



### DB Schema Design

![ER Diagram!](ER-Diagram.png "ER Diagram")

The DB has three tables, User, Apps and AppsUser. Apart from all primary keys, username in User table is having a unique constrain. Alao name in Apps table is having a unique constrain. AppsUser is a one to many relationship table between User table and Apps table. The combination of User(id) ans Apps(id) foreign keys is having a uniwue constraint also. Each relation is having delete cascade option, so once a parent object is deleted all its children will be deleted.


### API Design

API elements are created only for the READ operation of Apps and UserApps model. The yamil file is present in ‘Open_API’ folder along with the project code.

### Architecture and Features

The entire project is organised as a proper full stack structure. All the HTML files are stored inside ‘templates’ folder. The Python codes are separated into different modules according to their purposes and are stored inside corresponding folders. The external packages need to be installed are listed in the ‘requirements.txt’ file. The project can be executed buy running “local_setup.sh” file followed by “local_run.sh” file in a Linux based command prompt.

On running the app will be accessible only by registering and logging in. Once a user is logged in user will be taken to their home page. Where they can view all the list of apps available and their points. The apps are separated as completed and pending. There are options for earn more points by adding screenshots of pending apps.

Only an admin can add new apps to the list. A user with superuser status is considered as admin. When such an user is loged in he will be taken to the Admin view, where he can view all the lists and can add new ones too

 Following are the features available
*	UI with Vue & Vue Components
*	Apps list using fetch API
*	Chart showing summary of task completion


### Local Development Run
> #### Run 'local_setup.sh' in a linux shell
> - This will create a virtual environment folder '.env' if not present already
> - Then it will activate the virtual environment and install all packages listed in "requirements.txt"
>
> #### Run 'local_run.sh'
> - This will activate the virtual environment
> - Then will run the 'main.py'
> - Now you can view the app in a web browser with the link [http://localhost:8000]
>
>
>> ### If not working
>> - If you are not using a Linux environment try to replicate the scenerios in 'local_setup.sh' and 'local_run.sh' files, manually with appropriate codes.


### Folder Structure

- `adminface` is where python modules related to admin view is stored
- `apis` is where python modules for api implementation is stored
- `ngl_project` is where all the core python modules including settings.py, wsgi.py, asgi.py, urls.py etc. are stored
- `static` is the static directory registerred with the project. Apart from all CSS and JS files. All images and other static files will stored here
- `templates` is where all the html templates are stored
- `userface` is where python modules related to user view is stored



```
.
├── adminface
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_apps_name.py
│   │   ├── 0003_alter_apps_logo.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 
│   │       ├── 
│   ├── models.py
│   ├── __pycache__
│   │   ├── 
│   │   ├── 
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── apis
│   ├── apis.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── 
│   │   ├── 
│   ├── serializers.py
│   └── urls.py
├── db.sqlite3
├── local_run.sh
├── local_setup.sh
├── manage.py
├── ngl_project
│   ├── asgi.py
│   ├── forms.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── 
│   │   ├── 
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── Open_API
│   └── openapi.yaml
├── README.md
├── requirements.txt
├── static
│   ├── admin.js
│   ├── logos
│   │   ├── 
│   │   ├── 
│   ├── screenshots
│   │   ├── 
│   │   ├── 
│   ├── style.css
│   └── user.js
├── templates
│   ├── addApp.html
│   ├── addUserApp.html
│   ├── admin.html
│   ├── base.html
│   ├── index.html
│   ├── registration
│   │   ├── form.html
│   │   ├── logged_out.html
│   │   ├── login.html
│   │   └── register.html
│   ├── sidebar.html
│   └── user.html
└── userface
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_alter_userapps_unique_together.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 
    │       ├── 
    ├── models.py
    ├── __pycache__
    │   ├── 
    │   ├── 
    ├── tests.py
    ├── urls.py
    └── views.py

```
117 directories, 232 files




## Problem Set 3

#### Write and share a small note about your choice of system to schedule periodic tasks (such as downloading a list of ISINs every 24 hours). Why did you choose it? Is it reliable enough; Or will it scale? If not, what are the problems with it? And, what else would you recommend to fix this problem at scale in production?

Right now my choice would be ***Celery*** task queue along with ***Redis*** as a message broker. I chose simply because this is the one I am having hands on experience with. Even though it is not a good reason, I believe that it is better to start from where we stand. Apart from that, even though Celery is written in Python, the protocol can be implemented in any language. It can also operate with other language using weebhooks. With limited knowledge of the underlying system and requirements we are dealing here, these properties makes Celery my first choice.

But poor suport and maintainance is making Celery less relevent and stale. But it is said for large scale apps switching from Redis to RabbitMQ can improve the performance. On my research online Apache Airflow seems to be a better alternative, need to test it before arriving at a conclusion.


#### In what circumstances would you use Flask instead of Django and vice versa?

##### Flask
> `Pros`
> - Lightweight and minimalist approach
> - Ideal for small to medium apps
> - Suitable for RESTful APIs and microservices
> - If you want a lot of flexibility with choice of external packages used etc.
>
> `Cons`
> - Lightwight and minimalist approach makes it hard for developing large-scale applications
> - There are only few in built functionality. So we have to import a lot of other packages, in turm making it heavy for large apps.

##### Django
> `Pros`
> - Suitable for large scale projects
> - Rapid developement is possible
> - Have a lot of inbuilt functanality, reducing import of external dependencies.
>
> `Cons`
> - Not suitable for smaller applications with minimal functanality.
> - As most features are inbuilt it is waste of resource to import a better performing dependent libraries.
