# Outcomist Development Environment

Welcome to your Outcomist Codespace! This environment includes:

- **Python 3.11** with `uv` package manager
- **Node.js LTS** with npm and pnpm
- **Amplifier tools** available in the `./amplifier/` directory

## Getting Started

The development environment is ready to use. The amplifier submodule has been initialized and all tools are available.

## Amplifier Tools

All amplifier CLI tools and utilities are available in the `./amplifier/` directory. You can reference the amplifier documentation at `./amplifier/README.md`.

## Project Structure

```
outcomist/
├── .devcontainer/         # Codespaces configuration
├── amplifier/             # Amplifier tools (git submodule)
└── [your project files]
```

## Next Steps

1. Review the amplifier documentation: `./amplifier/README.md`
2. Check available Make commands: `make -C ./amplifier help`
3. Start building your project!

## Notes

- This is a GitHub Codespace running in the cloud
- All changes are automatically saved
- Use VS Code locally for the best experience (File > Connect to Codespace)
