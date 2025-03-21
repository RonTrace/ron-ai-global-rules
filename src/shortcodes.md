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

## plan

When the user types **plan**, follow these instructions for collaborative project/feature planning:

1. **Establish a shared understanding:**

   - Begin by asking clarifying questions about the project goals, scope, constraints, and success criteria
   - Summarize the user's objectives to confirm your understanding before proceeding
   - Identify key stakeholders and their requirements
   - Establish the expected timeline and resource constraints

2. **Collaborative ideation and requirements gathering:**

   - Guide the user through a structured brainstorming process
   - Document functional and non-functional requirements
   - Help prioritize requirements using techniques like MoSCoW (Must have, Should have, Could have, Won't have)
   - Consider trade-offs between features, time, and quality
   - Ask about any existing systems, code, or documentation that may be relevant

3. **Architecture and design planning:**

   - Propose appropriate technology stack options with clear reasoning
   - Outline potential architecture approaches with pros and cons of each
   - Create visual representations where helpful (system diagrams, user flows, data models)
   - Discuss potential technical challenges and mitigation strategies
   - Consider security, performance, and scalability implications

4. **Project structure and organization:**

   - Break down the project into logical components or modules
   - Propose a folder/file structure that follows best practices for the chosen stack
   - Identify key interfaces between components
   - Suggest appropriate design patterns and coding standards
   - Define a test strategy (unit tests, integration tests, etc.)

5. **Implementation roadmap:**

   - Create a phased implementation plan with clear milestones
   - Define dependencies between different components
   - Suggest a minimum viable product (MVP) approach if appropriate
   - Identify tasks that can be parallelized vs. those that must be sequential
   - Create reasonable time estimates for major components

6. **Risk assessment and mitigation:**

   - Identify potential technical, schedule, and resource risks
   - Rate risks by likelihood and impact
   - Propose specific mitigation strategies for high-priority risks
   - Consider fallback approaches for the most critical parts of the project

7. **Collaboration plan:**

   - Establish a shared vocabulary for the project
   - Define communication channels and check-in points
   - Clarify responsibilities between user and AI assistant
   - Set expectations about iteration and feedback cycles
   - Create a version control strategy if applicable

8. **Documentation strategy:**

   - Outline what documentation will be created and maintained
   - Establish documentation standards and formats
   - Consider developer documentation, user documentation, and system documentation needs
   - Create templates for recurring documentation needs

9. **Final deliverables:**

   - Provide a comprehensive planning document summarizing all the above sections
   - Include a visual project roadmap or timeline
   - Create a prioritized task list for immediate next steps
   - Establish clear success criteria and evaluation methods

10. **Important guidelines:**

    - Maintain a balance between thoroughness and pragmatism
    - Be adaptable to changing requirements throughout the planning process
    - Use visual aids and structured formatting to enhance clarity
    - Regularly summarize decisions and action items
    - Proactively identify areas where more information is needed
    - Apply domain-specific best practices relevant to the project type
    - Use planning artifacts (user stories, use cases, etc.) appropriate to the project methodology

## journal

When the user types **journal**, follow these instructions to document the current project:

1. **Create a journal entry with the following structure:**

   - Begin with a descriptive title that captures the essence of the project
   - Include the current date
   - Structure the document with clear sections using headers (h1, h2, etc.)

2. **Introduction/Overview section:**

   - Provide a compelling introduction that explains the project context
   - Clearly state the problem being solved
   - Highlight why this project is important
   - End with a concise statement of the core objective in bold

3. **Problem Statement/Challenge section:**

   - Detail the specific challenges or issues being addressed
   - Use lists to break down complex problems into discrete components
   - When referring to technical systems or data, use structured formatting
   - Include relevant background context that helps understand the problem space

4. **Solution Approach section:**

   - Describe the chosen solution with a focus on architecture and design decisions
   - Explain key implementation details and technical choices
   - Include code snippets or command examples when relevant
   - Document the workflow or process that the solution enables

5. **Implementation Details section:**

   - Break down the technical implementation into logical components
   - Use bullet points or numbered lists for clarity
   - Include relevant data structures, algorithms, or patterns used
   - Highlight any particularly clever or important implementation details

6. **Examples/Output section:**

   - Show concrete examples of the solution in action
   - For code output, use formatted code blocks with proper syntax highlighting
   - For visual elements, describe or visualize the UI/UX considerations
   - Include sample inputs and outputs when applicable

7. **Future Plans section:**

   - Outline potential improvements or next steps
   - Prioritize future enhancements based on impact and feasibility
   - Consider scalability, performance, or usability improvements
   - Include any known limitations that could be addressed

8. **Visual elements and formatting guidelines:**

   - Use consistent, clean formatting throughout the document
   - Format code snippets, commands, and output in monospace code blocks
   - Use emphasis (bold, italic) strategically to highlight key points
   - Consider visual separators between major sections for readability
   - Structure complex information in tables or formatted lists when appropriate
   - Include technical diagrams or mockups if they add clarity

9. **Writing style guidelines:**

   - Maintain a professional but conversational tone
   - Be precise and specific, especially with technical details
   - Focus on clarity over technical jargon, but use proper terminology
   - Tell a coherent story from problem to solution to future work
   - Use active voice and direct language
   - Keep paragraphs focused and relatively short for readability
