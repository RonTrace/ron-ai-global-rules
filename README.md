# AI Assistant Roles Project Setup

This project provides a simple way to manage different roles for your AI assistant. By defining roles in a single text file (`roles.txt`), you can easily switch between different sets of instructions for the AI, such as front-end development, data analysis, or creative tasks like lyric writing. The AI can load these instructions from a public repository, ensuring it always uses the latest version.

---

## Repository Structure

The repository is minimal and contains only one essential file:

* `roles.txt`: Defines the roles and their specific instructions in plain text.

Optionally, you can include:

* `README.md`: A quick guide to the repository (this file).
* `CHANGELOG.md`: Tracks updates to the roles or instructions (optional).

---

## Setting Up the Project

To set up the project using an AI assistant:

1. **Create a new repository** on GitHub (or your preferred platform).
2. **Create a file named** `roles.txt` in the repository.
3. **Add role definitions** to `roles.txt` using the format shown in the sample below.
4. **Commit and push** the file to make it publicly accessible.

---

## Sample `roles.txt`

The `roles.txt` file uses a simple format:

* Each role starts with a header in square brackets, e.g., `[role_name]`.
* Instructions for each role are listed below the header.
* A `[global]` section provides default instructions when no specific role is specified.

Here's a sample `roles.txt`:

```plaintext
[global]
- Write clear, readable responses.
- Be concise and helpful.

[frontend_developer]
- Focus on React and UI best practices.
- Suggest modern JavaScript techniques.

[python_data_analyst]
- Use pandas for data tasks.
- Explain analysis steps clearly.

[lyric_writer]
- Use vivid imagery and metaphors.
- Keep a consistent tone or rhyme if asked.
```

---

## Using the Roles with the AI Assistant

To use the roles with your AI assistant:

1. **Instruct the AI to load the `roles.txt` file** from your public repository.
2. **Specify the role** you want the AI to assume, or let it default to the `[global]` instructions.

### Sample Prompts

* **Specify a role**:
  *"Load the latest `roles.txt` from [repo_url]/roles.txt and use the [frontend_developer] role."*
* **Use the global instructions**:
  *"Load the latest `roles.txt` from [repo_url]/roles.txt and use the [global] instructions."*
* **Switch roles mid-conversation**:
  *"Now, switch to the [python_data_analyst] role using the instructions from [repo_url]/roles.txt."*

If no role is specified, the AI will default to the `[global]` instructions.

---

## Adding or Updating Roles

To add a new role or update an existing one:

1. **Edit** `roles.txt` in your repository.
2. **Commit and push** the changes.

**Tip**: Keep instructions concise and clear, as the AI will follow them directly.

---

This setup ensures your AI assistant can adapt to different roles while keeping the configuration simple and maintainable. Use the sample prompts to guide the AI in setting up and updating the project as needed!
Rules for my AI agents
