# Tetris Configuration

We recommend that you start by deleting all workflows, agents, models, and skills, that were created by default. To upload configuration from a JSON file, click on the three dots (...) next to the "+ New Skill" button. 

*Note: You don't need to make any changes to configuration before clickling on "Create". To upload resources, you can either proceed manually or run [hydrate.py script](../scripts/hydrate.py) to load it all automatically.*

1. Upload Models
    - models/gpt-4o-mini-2024-07-18.json
    - models/gpt-4o-2024-07-18.json

2. Upload Agents
    - agents/sender.json
    - agents/manager.json
    - agents/runner_agent.json
    - agents/software_critic.json
    - agents/software_programmer.json

3. Configure agent models
    - select "gpt-4o-2024-07-18" for
        * "Software_Critic"
        * "Software_Programmer"

    - select "gpt-4o-mini-2024-07-18" for
        * "Manager"
        * "Runner_Agent"

4. Add agents to "Manager"
    - "Runner_Agent"
    - "Software_Critic"
    - "Software_Programmer"

5. Create an **autonomous** workflow
    - Click on "+ New Workflow" >> "Autonomous (chat)" >> "Create Workflow"
    - After clicking on "Create Workflow", a new tab "Agents" will be available
    - As sender select "Sender" in the "Agents" tab
    - As receiver select "Manager" in the "Agents" tab
    
6. Click on "Test workflow" and prompt with "Create Tetris" *(chat won't be saved)* or move to the Playground *(chat will be saved)*

From now on, you can play around and e.g. change the models, feed your own code to the programmer team, and see if they can meaningfully improve it, or delve into your own workflow creation [with this guide.](custom-workflow.md)
