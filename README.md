# AI Coder Global Rules

A modular repository for managing behavior guidelines, shortcodes, and other rules for AI coding agents. This repository provides a structured, maintainable approach to defining how your AI assistants should behave when helping you with coding tasks.

## Overview

This repository is designed to store and manage rules for AI coding agents in a modular, maintainable way. Instead of managing a single large rules file, you can update individual components (behavior guidelines, commands, etc.) independently, and GitHub Actions will automatically generate a consolidated global rules file.

### Key Features

- **Modular Structure**: Separate files for different aspects of AI behavior
- **Automatic Consolidation**: GitHub Actions workflow automatically creates a single global rules file
- **Version Control**: Track changes to your AI's behavior over time
- **Simple Maintenance**: Update specific rules without editing the entire ruleset

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
