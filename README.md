# AI Coder Rules 🤖

Make your AI coding assistants work exactly how you want them to! This repo keeps all your AI coding rules in one place while making them super easy to update.

## What's This All About?

Instead of one giant rules file, we've split things up into bite-sized pieces. Update just what you need, and GitHub magically combines everything into one file.

### Cool Stuff This Repo Does

- 📄 Keeps everything organized in separate files
- 🔄 Automatically builds your master rules file
- 📝 Makes updating rules as easy as editing a text file

## Repository Structure

- `src/` - Source directory containing all modular files
  - `behavior.md` - General behavior guidelines for the AI agent
  - `shortcodes.md` - User commands and their specific instructions
  - `plugins.md` - Information about available plugins
  - `references/` - Reference materials and standards
    - `ui-standards.md` - UI design standards
    - `code-style.md` - Code style guidelines
- `concatenate.py` - Script to combine all modular files into a single global rules file
- `global_rules.md` - Auto-generated file containing all combined rules
- `.github/workflows/update-rules.yml` - GitHub Action to automatically update the global rules file

## Building and Installing Locally

To generate the consolidated global rules file locally:

```bash
python concatenate.py
```

This will create a `global_rules.md` file in the root directory that contains all the combined rules.

## Automation

This repository uses GitHub Actions to automatically generate the `global_rules.md` file whenever changes are pushed to the main branch. The workflow is defined in `.github/workflows/update-rules.yml`.

## Usage

### For AI Agents

AI coding agents can access the global rules by fetching the raw content of `global_rules.md` from this repository. For example:

```
https://raw.githubusercontent.com/yourusername/ron-ai-global-rules/main/global_rules.md
```

### Modifying Rules

To update or add new rules:

1. Modify the appropriate file in the `src/` directory
2. Commit and push your changes
3. GitHub Actions will automatically update the `global_rules.md` file

### Creating Custom Commands

To add a new custom command:

1. Open `src/shortcodes.md`
2. Add your command following the established pattern:

```markdown
## command_name

When the user types **command_name**, follow these instructions:

- Step 1: Do this
- Step 2: Do that
```

## Plugin Integrations

This repository includes configurations for specific plugins that enhance AI coding capabilities:

### SQLTools

When working in VSCode, Windsurf, or Cursor, SQLTools is the preferred tool for writing SQL queries:

- **Purpose**: Database management and query execution
- **Usage**: AI agents should use SQLTools for all database interactions
- **Commands**: Use `sqltools connect` before running queries

### Lifeline

A custom plugin with its own set of shortcodes for code organization and documentation:

- **Purpose**: Code organization, documentation, and context management
- **Implementation**: All commands are defined in `src/shortcodes.md`
- **Usage**: AI agents should follow the specific instructions in the shortcodes file

## Integrating with AI Tools

To use these rules with your AI coding tools:

### OpenAI GPT

Include this in your system message or as part of your initial prompt:

```
Fetch and follow the coding rules from: https://raw.githubusercontent.com/yourusername/ron-ai-global-rules/main/global_rules.md
```

### Claude

Include this in your system prompt:

```
Please fetch and adhere to the coding guidelines found at: https://raw.githubusercontent.com/yourusername/ron-ai-global-rules/main/global_rules.md
```

## Local Development

### Requirements

- Python 3.6 or higher
- Git

### Cloning the Repository

```bash
git clone https://github.com/yourusername/ron-ai-global-rules.git
cd ron-ai-global-rules
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-rule`)
3. Commit your changes (`git commit -am 'Add some amazing rule'`)
4. Push to the branch (`git push origin feature/amazing-rule`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
