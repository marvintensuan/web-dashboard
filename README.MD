# WEB-DASHBOARD

This is based on James Powell's *Building Web-based Analysis & Simulation Platforms* talk on PyData London 2017.

[![](http://img.youtube.com/vi/eEXKIp8h0T0/0.jpg)](https://www.youtube.com/watch?v=eEXKIp8h0T0 "James Powell: Building Web-based Analysis & Simulation Platforms | PyData London 2017")

## Requirements

TODO

## Setting up environment and IDE

1. Create a new Anaconda environment using the Anaconda Navigator.
2. Open the new environment via Terminal.
3. Install dependencies.
4. Open VS Code via the Anaconda terminal.
5. Configure `.vscode/settings.json`

```
    {
        "python.pythonPath": "c:\\Anaconda3\\envs\\env_name\\python.exe",
        "python.analysis.extraPaths": ["backend", "D:\\path_to\\project"]
    }
```

## How to run

### Flask

Change the current working directory to the `backend` folder.

```bash
cd .\backend
python restapi.py
```

### Redis

Open the terminal.

```bash
redis-server
```

### Celery

Change the current working directory to the `backend` folder.

```bash
cd .\backend
celery -A worker worker --loglevel=INFO
```