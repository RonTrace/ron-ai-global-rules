import os

output_file = 'global_rules.md'

sections = [
    ('src/behavior.md', 'Behavior Guidelines'),
    ('src/shortcodes.md', 'Shortcodes and Commands'),
    ('src/references/ui-standards.md', 'References: UI Standards'),
    ('src/references/code-style.md', 'References: Code Style'),
    ('src/plugins.md', 'Plugins'),
]

with open(output_file, 'w') as outfile:
    outfile.write('# Global Rules for AI Coding Agent\n\n')
    for file_path, section_title in sections:
        with open(file_path, 'r') as infile:
            content = infile.read()
            outfile.write(f'## {section_title}\n{content}\n\n')
