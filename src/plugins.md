# Plugins

## Lifeline

- **Description**: Custom plugin for code organization, documentation, and context management
- **Repository**: https://github.com/RonTrace/lifeline
- **IDE Support**: VSCode, Windsurf, Cursor
- **Usage**: This plugin's specific commands are defined in the `shortcodes.md` file
- **Notes**: 
  - All lifeline commands follow a standardized format
  - Refer to the shortcodes file for complete usage instructions
  - This plugin enhances AI coding assistance by providing structured context

## SQLTools

- **Description**: Database management and SQL query execution
- **Repository**: https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools
- **IDE Support**: VSCode, Windsurf, Cursor
- **REQUIRED USAGE**: ALWAYS use SQLTools for database operations; NEVER build connections from scratch
- **Primary Commands**:
  - `sqltools connect` - Connect to the database
  - `sqltools.executeQuery` - Run the current SQL query
  - `sqltools.executeQueryFromFile` - Execute saved queries
- **Supported Databases**:
  - PostgreSQL
  - MySQL
  - SQLite
  - Microsoft SQL Server
  - Oracle
- **Usage Guidelines**:
  - Always verify database connection before running queries
  - Use proper query formatting for readability
  - Apply query limiting (LIMIT/TOP) for large datasets
  - Structure complex queries with CTEs for maintainability
  - NEVER attempt to create custom database connections or use raw database libraries
