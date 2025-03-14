# AI Coder Rules 🤖

Make your AI coding assistants work exactly how you want them to! This repo keeps all your AI coding rules in one place while making them super easy to update.

## What's This All About?

Instead of one giant rules file, we've split things up into bite-sized pieces. Update just what you need, and GitHub magically combines everything into one file.

### Cool Stuff This Repo Does

- 📄 Keeps everything organized in separate files
- 🔄 Automatically builds your master rules file
- 📝 Makes updating rules as easy as editing a text file

## What's Where? 📁

- `src/` - All your rules live here
  - `behavior.md` - How your AI should behave
  - `shortcodes.md` - Special commands your AI knows
  - `plugins.md` - Tools your AI should use
  - `references/` - Extra guidelines
    - `ui-standards.md` - UI design rules
    - `code-style.md` - Code style rules
- `global_rules.md` - The magic file that GitHub creates for you
- `.github/workflows/` - GitHub's automation magic

## How Updates Work

When you push changes to GitHub:

1. GitHub Actions runs automatically
2. Combines all the rules into `global_rules.md`
3. Commits the updated file back to the repo

No need to run anything locally - just push your changes! 🚀

## Making Changes 📝

1. Edit files in the `src/` folder
2. Push to GitHub
3. Done! GitHub updates everything automatically

## Tools We Use 🛠️

### SQLTools
- The only way to do database work in VSCode/Windsurf/Cursor
- Get it here: https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools

### Lifeline
- Our custom tool for better code organization
- Check it out: https://github.com/RonTrace/lifeline

## For AI Friends 🤖

Just fetch:
```
https://github.com/RonTrace/ron-ai-global-rules
```

## Want to Help? 🤝

1. Fork it
2. Make it better
3. Send a PR

MIT Licensed - have fun! 🚀
