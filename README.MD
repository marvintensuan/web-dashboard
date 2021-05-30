# WEB-DASHBOARD

This is based on James Powell's *Building Web-based Analysis & Simulation Platforms* talk on PyData London 2017.

[![](http://img.youtube.com/vi/eEXKIp8h0T0/0.jpg)](https://www.youtube.com/watch?v=eEXKIp8h0T0 "James Powell: Building Web-based Analysis & Simulation Platforms | PyData London 2017")

## Requirements

## Backend

TODO

## Frontend

From the [Vue 3 Official Documentation](https://v3.vuejs.org/guide/installation.html), install Vue and Vue-CLI globally and create an app called `frontend`.

```bash
npm install vue@next
npm install -g @vue/cli
vue create frontend
```

Choose `Default (Vue 3) ([Vue3] babel, eslint)`.

If you run into problems regarding `vue.ps1` not being digitally signed, use the following command:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

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

### Backend

The backend of this app is composed of three parts: a Flask server, Celery task queue, and redis as Celery's broker.

#### Flask

Change the current working directory to the `backend` folder.

```bash
cd .\backend
python restapi.py
```

#### Redis

Open the terminal.

```bash
redis-server
```

#### Celery

Change the current working directory to the `backend` folder.

```bash
cd .\backend
celery -A worker worker --loglevel=INFO
```

## Frontend

To run the Vue app (development), change the current working directory to the `frontend` folder.

```bash
cd .\backend
npm run serve
```