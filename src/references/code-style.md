# Code Style Guide

## General Formatting

- Use 2 spaces for indentation, not tabs
- Limit line length to 100 characters where possible
- Use UTF-8 encoding for all source files
- End files with a single newline character
- Remove trailing whitespace from all lines
- Use consistent casing conventions:
  - `camelCase` for variables, functions, and methods
  - `PascalCase` for classes, interfaces, types, and React components
  - `UPPER_SNAKE_CASE` for constants
  - `kebab-case` for filenames and URLs

## JavaScript/TypeScript

- Use semicolons to terminate statements
- Prefer `const` over `let`, avoid `var`
- Use explicit type annotations in TypeScript
- Use arrow functions for callbacks
- Destructure objects and arrays when appropriate
- Use template literals instead of string concatenation
- Add trailing commas for multi-line arrays and objects
- Use async/await instead of raw promises when possible

## React Specific

- Prefer functional components over class components
- Always include PropTypes for component props (or TypeScript types)
- Use named exports for components
- Keep components small and focused on a single responsibility
- Organize component files with a consistent structure:
  - Imports
  - Type definitions
  - Component declaration
  - Helper functions
  - Styles
  - Exports
- Use hooks for state management and side effects
- Memoize expensive calculations with useMemo and useCallback

## CSS/Styling

- Follow BEM naming convention for CSS classes
- Prefer CSS modules or styled-components over global CSS
- Group related CSS properties together
- Use variables for colors, spacing, and other repeated values
- Maintain a consistent order of CSS properties

## Comments and Documentation

- Write self-documenting code when possible
- Add comments for complex logic or non-obvious decisions
- Document public APIs and functions with JSDoc
- Keep comments up-to-date with code changes
- Use TODO, FIXME, and NOTE comments for future work

## Git Practices

- Write clear and descriptive commit messages
- Use the imperative mood in commit message titles ("Add feature" not "Added feature")
- Keep commits focused on a single logical change
- Reference issue numbers in commit messages when applicable
- Branch naming convention: `type/description` (e.g., `feature/user-authentication`)
