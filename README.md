# Outcomist

A project built with Microsoft's Amplifier framework.

## Development Setup

### Local Development

This project lives inside the [amplifier repository](https://github.com/cpark4x/amplifier) and has direct access to amplifier tools via symlink.

### GitHub Codespaces

To develop in Codespaces:

1. Open this repository in GitHub
2. Click "Code" → "Codespaces" → "Create codespace"
3. Wait for the environment to build (includes amplifier tools)
4. Start coding!

The devcontainer automatically initializes the amplifier submodule, giving you access to all amplifier tools.

## Project Structure

```
outcomist/
├── .devcontainer/         # Codespaces configuration
├── amplifier/             # Amplifier tools (submodule in Codespaces, symlink locally)
└── README.md             # This file
```

## Amplifier Tools

All amplifier CLI tools are available in the `amplifier/` directory. See the [amplifier documentation](./amplifier/README.md) for details.
