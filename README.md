# xbtree
X-bar parse tree generator

## Setup
All the operations should be performed from the xbtree folder  
__Note:__ `$` means the commands are entered in the terminal (not part of command)
  
__1. Create and activate a python virtual environment:__  
  
Check if virtual environment exists:  
```
$ ls -a
```
If you see a `.venv` folder, the environment has already been created.  
  
If it does not exist, do the following:  
```
$ python3 -m venv .venv
```
Activate the environment:  
```
$ . .venv/bin/activate
```
__2. Install dependencies:__  
  
Install all requirements for the web application:  
```
$ pip install -r requirements.txt
```
__3. Run the application:__

Run the app by using the following commands
```
$ flask --app main run --debug
```
Doing so will display a local url in the terminal. Accessing that url using a 
browser will open up the web app.


