# Auroral custom adapter example
This is basicimplementation of custom adapter with Auroral agent
## Instalation and first run
 There are several ways how to run this adapter. We will describe running in python virtual enviroment and running inside docker:

### Python virtual env
- Create venv: 	
```python3 -m venv myenv```
- Activate venv:
```source myenv/bin/activate```
- Start adapter:
```uvicorn main:app  --port 4444```
- Stop adapter:
```Ctrl + C ```
- Deactivate:
 ```deactivate```
 - Export requirements:
 ```pip freeze > requirements.txt```
 - Install requirements
 ```pip install -r requirements.txt```
 ### Docker 
 - Building image:
 ```docker build -t customAdapter .```
 - Running docker container: 
  ```docker run -d --name MyAdapter -p 4444:4444 customAdapter```

## Configuration
Example configuration is stored in *env.example* file. Please copy it to file named *.env* and make required changes. 
```
AGENT_URL="http://localhost"
AGENT_PORT=81
ADAPTER_IDS="testAdapter1, testAdapter2"
```
*AGENT_URL* and *AGENT_PORT* defines where your Auroral AGENT is accessable from Adapter. 
*ADAPTER_IDS* defines which objects registered in Agent should be  maintained in this adapter

## Who do I talk to? ##

Developed by bAvenir
* jorge.almela@bavenir.eu
* peter.drahovsky@bavenir.eu
