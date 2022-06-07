# Company API

## Virtual env instructions

1. Create

    python3 -m venv myenv

2. Activate

    source myenv/bin/activate

3. Deactivate

    deactivate

## How to start it

* Start API
    source myenv/bin/activate  
    uvicorn main:app --reload --port 4444

## How to create requirements
    
* pip freeze > requirements.txt
* pip install -r requirements.txt