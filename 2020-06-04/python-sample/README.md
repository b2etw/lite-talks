## setup venv
```
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ deactivate
```

## pip install
```
(venv) $ pip3 install Flask
 or
(venv) $ pip3 install -r requirements.txt
(venv) $ pip3 freeze | tee requirements.txt
```

## Docker Build
```
$ docker build -t taiwanbackendgroup/python-sample:1.0.0 .
```