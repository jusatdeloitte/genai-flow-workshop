# Tetris Configuration

We recommend that you start by deleting all workflows, agents, models, and
skills, that were created by default. To upload configuration from a JSON file, click on the three dots (...) next to the "+ New Skill" button. 

*Note: You don't need to make any changes to configuration before clickling on "Create".*

1. Upload Skills
    - skills/list_all_files.json
    - skills/list_directory.json
    - skills/read_file_content.json
    - skills/search_in_file.json

2. Upload Models
    - models/gpt-3.5-turbo.json
    - models/gpt-4o.json

3. Upload Agents
    - agents/manager.json
    - agents/user_proxy.json
    - agents/software_critic.json
    - agents/software_programmer.json

4. Configure agent models
    - select "gpt-3.5-turbo" for
        * "manager"
        * "Software_Critic"
    - select "gpt-4o" for
        * "Software_Programmer"

5. Add all skills to "Software_Critic"

6. Add agents to "manager"
    - "user_proxy"
    - "Software_critic"
    - "Software_Programmer"

7. Create an **autonomous** workflow
    - Click on "+ New Workflow" >> "Autonomous (chat)" >> "Create Workflow"
    - After clicking on "Create Workflow", a new tab "Agents" will be available
    - As sender select "sender" in the "Agents" tab
    - As receiver select "manager" in the "Agents" tab
    
8. Click on "Test workflow" and prompt with "Create Tetris" *(chat won't be saved)* or move to the Playground *(chat will be saved)*
