# cadcad-cli
`cadcad-cli` is a CLI tool to aid in creating consistent and dependable cadCAD experiments from scratch. It uses templates to scaffold out experiment file and directory structure and any desired boilerplate. New templates can be created by following a [supported schema](templates/schema.md). Future versions of the CLI tool will facilitate virtual environments through `venv`.

## Installation
```bash
git clone https://github.com/cadcad-org/cadcad-cli
cd cadcad-cli
./install
```

## Usage
```bash
mkdir my-experiment && cd my-experiment
cadcad-cli
```

By default, `cadcad-cli` runs in non-interactive mode. If you do no specify a template when you run it it will default to the included `normal` template.

For complete usage info:
```bash
cadcad-cli --help
```

## Uninstallation
To uninstall, you can simply remove the `$PATH` export that was added to your `.bashrc`. Additionally, you can run the `install` script with the `-r` flag:
```bash
./install -r