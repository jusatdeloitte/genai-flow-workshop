# Installation

Bedingung für eine Workshop-Teilnahme ist eine funktionierende Installation des
Programms
[AutoGenStudio](https://microsoft.github.io/autogen/blog/2023/12/01/AutoGenStudio).
Dies wird zur systemischen Abgrenzung in ein separates anaconda env installiert.
Hierzu unternehmen Sie folgende Schritte.

1. Anaconda installieren.
2. Im einem Terminal ein Anaconda environment erstellen.
3. AutoGenStudio installieren und starten.

## Anaconda installieren

- Installation für [macOS](https://docs.anaconda.com/anaconda/install/mac-os/)
- Installation für [Linux](https://docs.anaconda.com/anaconda/install/linux/)
- Installation für [Windows](https://docs.anaconda.com/anaconda/install/windows/)

Um zu überprüfen, dass die Installation erfolg hatte, folgen Sie
[dieser](https://docs.anaconda.com/anaconda/install/verify-install/)
Beschreibung.

## Terminal öffnen (nur macOS)

Öffnen Sie zunächst ein Terminal:

1. <Cmd+Space> drücken zum Öffnen von Spotlight Search.
2. "Terminal" eingeben und Enter drücken.

Hiernach sollte sich ein Terminal öffnen im Format `(base) $`. Fehlt `(base)`,
so war die Anaconda Installation unvollständig.

## Conda env erstellen

Erstellen Sie ein neues Environment mit Python v3.10

```shell
(base) $ conda create -n autogen python=3.10
```

Activieren Sie das Environment

```shell
(base) $ conda activate autogen
(autogen) $ ..
```

## AutoGenStudio installieren und starten

Installieren Sie `autogenstudio` in das neue Environment.

```shell
(autogen) $ pip install autogenstudio
```

Starten Sie den Autogenstudio Server (mit Beispiel-Output). Im ersten Schritt
wird der Open AI API Key in die Shell-Umgebung geladen.

```shell
(autogen) $ export OPENAI_API_KEY=<den API Key einfuegen>
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

Nachdem der Server läuft können Sie in ihrem Lieblingsbrowser die angegebene
URL anwählen (im Beispiel `http://127.0.0.1:8081`), oder klicken Sie
[hier](http://localhost:8081).

![Screenshot of start page](autogenstudio-startpage.png)
