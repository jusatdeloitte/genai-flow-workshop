# Configuration for a custom workflow

We recommend that you start by deleting all workflows, agents, models, and skills, that were created by default. 
Then, you can start building your own workflow by going through the steps below.

## 1. **Skills**

If your workflow requires executing code, and you want to have control over the code that's being executed (*recommended practice* as opposed to allowing any and all code to be executed in your work/private infrastructure), provide agents with reusable code snippets. Simply fill the `templates/skill.json`: paste your code in the "content"-field along with the "name" and "description" of the function. Then, run `python -m json.tool` to format it.
Note, that if you want agents to write and execute *any* code, you don't have to use skills. 

## 2. **Agents**

You'll need to create multiple agents, including a group_chat_manager, a user_proxy and the ones who're engaging in a conversation. 

To create a system_message that follows prompting best-practices, we recommend using the [System Prompt Generator tool](https://chatgpt.com/g/g-8qIKJ1ORT-system-prompt-generator). Explain in natural language what the agent is supposed to do, and ChatGPT will craft a perfectly formatted prompt for your agent. Then, you can use the prompt below to format your system_message for a JSON file:
`Format this text so I can paste it into a JSON entry "system_message": "", using /n for for line breaks and correct code formatting elements. Do not create multiple entries, the only entry I need is system_message and it includes all the text below: <your system_message>`

If you notice that the behaviour of your agent doesn't reflect your intentions, try debugging your prompt by pasting it into [ChatGPT](https://chatgpt.com/), followed by the task, e.g. "create tetris". This way you'll avoid the hustle of importing new configurations to Autogen and waiting tha agent conversation to be over.


2.1. **Configure agent models**: To make your workflow both effective and cost-efficient, select stronger models (gpt-4o) for complex tasks requiring precision (writing code, math) and weaker models (gpt-3.5-turbo) for simpler tasks such as e.g. managing the conversation or checking spelling.

2.2. **Configure agents skills**: tbu

2.3. **Add the agents**, that you want to participate in the conversation, to "manager".


## 3. Workflow
    - Click on "+ New Workflow" >> "Autonomous (chat)" >> "Create Workflow"
    - After clicking on "Create Workflow", a new tab "Agents" will be available
    - As sender select "sender" in the "Agents" tab
    - As receiver select "manager" in the "Agents" tab
    
3.1. Click on "Test workflow" and start prompting *(chat won't be saved)* or move to the Playground *(chat will be saved)*
