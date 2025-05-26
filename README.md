# OSINT Tools

The basic use is `bash osint run <tool-name>`. However, there are other uses. Run `bash osint --help` if help is needed.

## Getting Started

Ensure you have the following tools installed on your system:

- [docker](https://www.docker.com)
  - Run and manage containers.
- [uv](https://docs.astral.sh/uv)
  - A Python package and virtual environment manager.

## Installing

Clone the repo and run the install commands:

```bash
git clone https://github.com/jgttech/osint.git
cd osint
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
bash osint run phoneinfoga --version
bash osint run theharvester
```

## Commands

Just an easy and quick reference list.

| Command                                  | Description                      |
| :--------------------------------------- | :------------------------------- |
| `bash osint install`                     | Runs the `__install__.py` files. |
| `bash osint run recon-ng <args ...>`     | Uses `recon-ng` OSINT tool.      |
| `bash osint run phoneinfoga <args ...>`  | Uses `phoneinfoga` OSINT tool.   |
| `bash osint run theharvester <args ...>` | Uses `theharvester` OSINT tool.  |
