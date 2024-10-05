# Configuration for a custom workflow

We recommend that you start by deleting all workflows, agents, models, and skills, that were created by default. 
Then, you can start building your own workflow by going through the steps below.


1. **Skills**: If your workflow requires executing code, and you want to have control over the code that's being executed (*recommended practice* as opposed to allowing any and all code to be executed in your work/private infrastructure), provide agents with reusable code snippets. Simply fill the `templates/skill.json`: paste your code in the "content"-field along with the "name" and "description" of the function. Then, run `python -m json.tool` to format it.
Note, that if you want agents to write and execute *any* code, you don't have to use skills. 

3. **Agents**: tbu

4. **Configure agent models**: To make your workflow both effective and cost-efficient, select stronger models (gpt-4o) for ... and (gpt-3.5-turbo) for ...

5. **Configure agents skills**: tbu

6. Add agents to "manager"
    - "code_executor"
    - "Software_critic"
    - "Software_Programmer"

7. Create an **autonomous** workflow
    - Click on "+ New Workflow" >> "Autonomous (chat)" >> "Create Workflow"
    - After clicking on "Create Workflow", a new tab "Agents" will be available
    - As sender select "sender" in the "Agents" tab
    - As receiver select "manager" in the "Agents" tab
    
8. Click on "Test workflow" and start prompting *(chat won't be saved)* or move to the Playground *(chat will be saved)*
