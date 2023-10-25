1. Install deps:
```
pip install -r requirements.txt 
```
2. Run broker:
```
docker run -d -p 5672:5672 rabbitmq   
```
3. Input your TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
 ```
$env:TWILIO_AUTH_TOKEN='*'  
$env:TWILIO_ACCOUNT_SID='*'    
```
4. Run worker
```
celery -A tasks worker -l INFO 
```
5. Run django server
```
python manage.py runserver
```