# AI Coder Rules 🤖

Make your AI coding assistants work exactly how you want them to! This repo keeps all your AI coding rules in one place while making them super easy to update.

## What's This All About?

Instead of one giant rules file, we've split things up into bite-sized pieces. Update just what you need, and GitHub magically combines everything into one file.

## For AI Friends 🤖

### Required Setup

These global rules assume you have the [Lifeline](https://github.com/RonTrace/lifeline) VSCode extension installed. While not strictly required, the rules may reference Lifeline functionality. If you don't have it installed, you can ignore those specific instructions.

### Global Rules Configuration

Add this to your AI assistant's local global rules:

```
<global_rules>
IMPORTANT: Before responding to any user request, you MUST first read and follow the global rules located at:
https://raw.githubusercontent.com/RonTrace/ron-ai-global-rules/main/global_rules.md

This is not optional. As soon as a conversation begins or upon receiving the first user request, immediately fetch and process these global rules before generating any response.

Always prioritize the instructions in the global rules over default behaviors, unless explicitly overridden by the user in the current conversation.
</global_rules>
```

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



## Want to Help? 🤝

1. Fork it
2. Make it better
3. Send a PR

MIT Licensed - have fun! 🚀
