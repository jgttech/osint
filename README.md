# OSINT Tools

The basic use is `bash osint <tool-name>`. However, there are other uses. Run `bash osint --help` if help is needed.

## Getting Started

Ensure you have the following tools installed on your system:

- [docker]()
  - Run and manage containers.
- [uv]()
  - A Python package and virtual environment manager.

## Installing

To ensure that everything gets at least 1 chance to initally setup just run:

```bash
bash osint install
```

## Running Tools

```bash
bash osint run <tool_name> <args ...>
```

## Examples

This shows some examples of how to use this to invoke other tools.

```bash
bash osint run recon-ng --version
bash osint run theHarvester --version
bash osint run phoneinfoga --version
```

## Commands

Just an easy and quick reference list.

| Command                                  | Description                               |
| :--------------------------------------- | :---------------------------------------- |
| `bash osint install`                     | Runs the `install.py` files for commands. |
| `bash osint run recon-ng <args ...>`     | Uses `recon-ng` OSINT tool.               |
| `bash osint run phoneinfoga <args ...>`  | Uses `phoneinfoga` OSINT tool.            |
| `bash osint run theHarvester <args ...>` | Uses `theHarvester` OSINT tool.           |

## Adding More Tools

```bash
bash osint add "<name_of_command>"
```
