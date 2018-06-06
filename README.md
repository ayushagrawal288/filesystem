# FileSystem

Problem Link: https://docs.google.com/document/d/11p4xmwG4hsg2cDWKpJ9ZqhrhMGAJIlofZhf8ZSkcYuo/edit?ts=5b053a8d

## Steps to Buid  
You need to have Python3 and Pip 3 for this to run  
```
cd filesystem/
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
``` 


Endpoints
---------
File:
- List(get):
    /file/

- Create(post):  
    /file/upload/  
    fields = filename, file 
  
- Get Book(get):  
    /file/get/  
    fields = filename 
  
- Rename(post):  
    /file/rename/  
    fields = new_name, previous_name 
  
- Delete(post):  
    /file/delete/ 
    fields = filename 
