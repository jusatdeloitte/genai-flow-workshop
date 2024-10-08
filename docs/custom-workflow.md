# Configuration for a custom workflow

We recommend that you start by deleting all workflows, agents, models, and skills, that were created by default. 
Then, you can start building your own workflow by going through the steps below.

## 1. **Skills**

If your workflow requires executing code, and you want to have control over the code that's being executed (*recommended practice* as opposed to allowing any and all code to be executed in your work/private infrastructure), provide agents with reusable code snippets. Simply fill the `templates/skill.json`: paste your code in the "content"-field along with the "name" and "description" of the function. Then, run `python -m json.tool` to format it.
Note, that if you want agents to write and execute *any* code, you don't have to use skills. 

## 2. **Agents**

2.1. **Configure agents**: For an autonomous chat, you'll need to create multiple agents, including:
1) groupchat_manager (manages the conversation and it's length with [max_turns](https://microsoft.github.io/autogen/docs/reference/agentchat/conversable_agent/#:~:text=Default%20is%20None.-,max_turns,-int%20or%20None) parameter. **Tip:** add a list of `Available Agents and Tools` to the system_message to achieve better results)
2) user_proxy (initiates the conversation and can run code, doesn't need any modifications, just use [the generic one we've prepared](../templates/user_proxy.json))
3) the ones who're engaging in a conversation 

To create an agent, you can use [configuration templates](../templates) we've prepared or mdify existing ones. The most important thing to modify in the agents configuration is the `system_message` and `description`. You can also play around with the rest of the parameters referring to the [documentation](https://microsoft.github.io/autogen/docs/topics), but keep in mind, that this could cause unexpected issues that will be hard to debug within the length of the workshop.

**Description** is for the benefit of the groupchat_manager, not for the agent's own use or instruction. Groupchat_Manager uses agent descriptions when choosing which agents should speak next.
Tips for a good description:
- Avoid using the 1st or 2nd person perspective. Descriptions should not contain "I" or "You"
- Include any details that might help the orchestrator (i.e. groupchat_manager) know when to call upon the agent
- Keep descriptions short (e.g., "A helpful AI assistant with strong natural language and Python coding skills.")

**System message** will set a **role** and a **task** for the agent. To create a system_message that follows prompting best-practices, we recommend using the [System Prompt Generator tool](https://chatgpt.com/g/g-8qIKJ1ORT-system-prompt-generator). Explain in natural language what the agent is supposed to do, and ChatGPT will craft a perfectly formatted prompt for your agent. Then, you can either paste your text *without any prompts* into [this pre-built agent](https://chatgpt.com/g/g-2sLr73LCL-json-formatter) or use the prompt below to format your system_message for JSON with ChatGPT:

`Format this text so I can paste it into a JSON entry "system_message": "", using /n for for line breaks and correct code formatting elements. Do not create multiple entries, the only entry I need is system_message and it includes all the text below: <your system_message>`

**Tip:** If you notice that the behaviour of your agent doesn't reflect your intentions, try debugging your prompt by pasting it into [ChatGPT](https://chatgpt.com/), followed by the task, e.g. "create tetris". This way you'll avoid the hustle of importing new configurations to Autogen and waiting the multi agent conversation to be over.


2.2. **Configure agent models**: To make your workflow both effective and cost-efficient, select stronger models for complex tasks requiring precision (writing code, math) and weaker models for simpler tasks such as e.g. managing the conversation or checking spelling. 

| Model Name              | Ranking | Input Token Cost (per 1M) | Output Token Cost (per 1M) | Cost Efficiency Compared to Rest |
|-------------------------|---------|---------------------------|----------------------------|-----------------------------------|
| gpt-3.5-turbo-0125       | #79     | $0.50                      | $1.50                       | Medium (Balanced cost)            |
| gpt-4o-mini-2024-07-18   | #5      | $0.150                     | $0.600                      | High (Most cost-effective)        |
| gpt-4o-2024-08-06        | #8      | $2.50                      | $10.00                      | Low (Expensive)                   |
| gpt-4o-2024-05-13        | #6      | $5.00                      | $15.00                      | Very Low (Most expensive)         |


2.3. **Configure agents skills**: Depending on your workflow, add skills to the agents.

2.4. **Add all the agents**, that you want to participate in the conversation, to "groupchat_manager" (including "user_proxy").


## 3. Workflow
    - Click on "+ New Workflow" >> "Autonomous (chat)" >> "Create Workflow"
    - After clicking on "Create Workflow", a new tab "Agents" will be available
    - As sender select "user_proxy" in the "Agents" tab
    - As receiver select "groupchat_manager" in the "Agents" tab
    
3.1. Click on "Test workflow" and start prompting *(chat won't be saved)* or move to the Playground *(chat will be saved)*

3.2. If you're experimenting with multiple agents, for example, 7 agents, please make sure to increase the Max Consecutive Auto Reply setting for the Group Chat Assistant.

