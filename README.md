# AI Agenten mit AutoGen Studio

Willkommen zum AutoGen Workshop. Dieses Repository dient als untestützender
Guide und enthält eine Reihe von Anwendungsbeispielen, die wir im Workshop
gemeinsam untersuchen.

Installieren Sie zunächst AutoGen Studio auf Ihrem PC. AutoGen Studio ist ein
Webserver, denn Sie lokal über ihren Browser bedienen können. Das Studio
ermöglicht es Ihnen Teams von AI Agents zu erstellen und zu steuern.

Im Repo befinden sich beispielhafte Team-Konfigurationen im Json-Format, die
Sie ins Studio einlesen können.

## Installations-Guide

Folgen Sie zunächst der [Installationsbeschreibung](docs/install.md).

Als nächstes können Sie die aus Team-Konfigurationen ins AutoGen
Studio laden.

## Team-Konfigurationen

- [Software Team](teams/software_team.json)

## Tour durch AutoGen Studio

Hier ist die Startscreen von AutoGen Studio. Im linken Reiter finden Sie die
Rubriken `Skills`, `Models`, `Agents`, und `Workflows`, die wir uns nun näher
anschauen wollen.

![Startscreen](docs/autogenstudio-startscreen.png)

### Skills

Skills zeigt eine Liste von Python Funktionen, die Agenten zu Verfügung stehen.
Agenten, denen eine Skill zugewiesen wird, können diese abhängig vom Zustand
des LLM Models mit inferierten Parametern ausführen. Dies kann, wie im
Beispiel, dazu genutzt werden ein Bild zu generieren und abzuspeichern.

![Skillexample](docs/autogenstudio-skill.png)

### Models

Models zeigt eine Liste der Deep-Learning Modelle, im Studio zur Verfügung
stehen. Jedes Model kann einem Agenten zugewiesen werden, und formt die Basis
der agentischen Datenverarbeitung.

### Agents

Agents zeigt eine Liste der Agenten, die im Studio gespeichert sind. Es gibt
drei Typen von Agent.

1. **User Proxy Agent.** Dieser empfängt entweder einen Prompt vom Benutzer,
   also von Ihnen, oder er can Python und andere Code-Blöcke ausführen.

2. **Assistant Agent.** Ein Assistent empfängt und prozessiert einen Prompt mit
   Hilfe des zugrundeliegenden LLM Models zurück an den Prompter. Der Assistent
   Agent kann auch Code-Blöcke ausführen, und prozessiert dann den Output
   weiter.

3. **GroupChat.** Ein GroupChat Manager koordiniert die Interaktion zwischen
   mehreren Agenten.  Das heißt, er empfängt Text von einem Agenten und
   entscheidet an welchen Agenten dieser Text weitergeleitet wird.

### Workflows

Workflows zeigt die Liste der Workflows. Jeder Workflow instanziert eine Reihe
von Agenten und stellt eine Kommunikationsbeziehung zwischen diesen her.

Es gibt zwei Arten von Workflows zur Auswahl.

1. **Autonomous (Chat).** Eine Menge von Agenten nehmen an einem
   Nachrichten-Austausch teil wobei ($n>2$) ein GroupChat Manager bestimmt, an
   wen eine Nachricht gerichtet ist.

2. **Sequential.** Eine Reihen von Agenten tauschen in einer bestimmten
   Reihenfolge Nachrichten aus.
