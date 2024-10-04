# Installation

A prerequisite for participating in the workshop is a working installation of
the program
[AutoGenStudio](https://microsoft.github.io/autogen/blog/2023/12/01/AutoGenStudio).
This will be installed in a separate Anaconda environment to ensure system
isolation. Follow these steps:

1. Install Anaconda.
2. Create an Anaconda environment in a terminal.
3. Install and start AutoGenStudio.


## Install Anaconda

- Installation for [macOS](https://docs.anaconda.com/anaconda/install/mac-os/)
- Installation for [Linux](https://docs.anaconda.com/anaconda/install/linux/)
- Installation for [Windows](https://docs.anaconda.com/anaconda/install/windows/)

To verify that the installation was successful, follow [this
guide](https://docs.anaconda.com/anaconda/install/verify-install/).

## 1. Open Terminal (macOS only)

First, open a terminal:

1. Press <Cmd+Space> to open Spotlight Search.
2. Type "Terminal" and press Enter.

A terminal should open in the format `(base) $`. If `(base)` is missing, the
Anaconda installation was incomplete.

## 2. Create Conda Environment

Create a new environment with Python v3.10:

```shell
(base) $ conda create -n autogen python=3.10
```

Activate the environment:

```shell
(base) $ conda activate autogen
(autogen) $ ..
```

## 3. Install and Start AutoGenStudio

3.1. Install/Upgrade `autogenstudio` in the new environment:

```shell
(autogen) $ pip install autogenstudio
(autogen) $ pip install --upgrade autogenstudio
```

3.2. Load the OpenAI API key into the shell environment:

```shell
(autogen) $ export OPENAI_API_KEY=<insert API key>
```

3.3. Start the AutoGenStudio server (example output included). 

```shell
(autogen) $ autogenstudio ui
flaml.automl is not available. Please install flaml[automl] to enable AutoML functionalities.
2024-10-02 10:02:39.841 | INFO     | autogenstudio.utils.utils:get_db_uri:253 - Using database URI: sqlite:////home/myuser/.autogenstudio/database.sqlite
2024-10-02 10:02:39.841 | INFO     | autogenstudio.utils.utils:init_app_folders:288 - Initialized application data folder: /home/myuser/.autogenstudio
INFO:     Started server process [10124]
INFO:     Waiting for application startup.
***** App started *****
2024-10-02 10:02:39.882 | INFO     | autogenstudio.database.utils:init_db_samples:148 - Database already initialized with Default and Travel Planning Workflows
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8081 (Press CTRL+C to quit)
```

3.4. Once the server is running, you can access the provided URL (in the example,
`http://127.0.0.1:8081`) in your favorite browser, or click
[here](http://localhost:8081).

![Screenshot of start page](autogenstudio-startpage.png)

