# Shortcodes and Commands

## build

When the user types **build**, follow these instructions:

- Follow the directions as described in the **README.md** file in the "Building and Installing Locally" section.

## lifeline

When the user types **lifeline**, follow these instructions:

1. **Create a lifeline markdown file:**

   - Look for a folder in the project called `_lifeline`.
   - If that folder does not exist, create it.
   - Inside that folder, create a file called `_lifeline-[date].md`, where [date] is the current date and time in the format `YYYY-MM-DD-HH-MM-SS`.

2. **Gather context to write inside the lifeline file:**

   - You are writing a prompt for an AI coder.
   - Your prompt should be in XML format with the following structure:
     a. goal
     b. return format
     c. warnings
     d. code map
     e. context
   - In the goal section: Summarize the current project and describe the specific task or problem we are trying to solve.
   - In the return format section: Describe the expected output format of the AI coder's response.
   - In the warnings section: Document any potential issues or warnings that may arise during the AI coder's work. Include issues we have identified.
   - In the code map section: Include a code map of how all the elements we are working with fit together.
   - In the context section: Include any relevant code snippets, comments, or other information that can help the AI coder understand the project context.
   - If applicable, log the intended before and after states of any planned code changes in code blocks (without applying changes to the actual codebase).

3. **Important**

   - Only create the lifeline file.
   - Do not make any modifications to the existing codebase.
   - Do not edit or modify files—just document information inside the lifeline file.
   - Stop working after you've created the lifeline file.

## lifeline read

When the user types **lifeline read**, follow these instructions:

- Find the most recent file in the `_lifeline` folder that starts with `_lifeline-response` and follow the directions outlined in that file step by step.
