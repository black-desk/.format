<!--
SPDX-FileCopyrightText: 2025 Chen Linxuan <me@black-desk.cn>

SPDX-License-Identifier: MIT
-->

# .format

[zh_CN](README.zh_CN.md) | en

> [!WARNING]
> This English README is translated from the Chinese version
> using AI and may contain errors.

Code formatting configuration files used in my personal projects.

This project is referenced as a git submodule in my other personal projects and kept up-to-date through dependabot.

## Usage

```bash
git submodule add https://github.com/black-desk/.format

# Then create the relevant symbolic links manually, for example:

ln -s .format/.editorconfig
ln -s .format/.clang-format
```

## Notes

- `black`:

  ```bash
  ln -s .format/.black.toml
  ```

  ```toml
  # In your pyproject.toml
  [tool.black]
  src = [".black.toml"]
  ```

## License

This project complies with the [REUSE specification](https://reuse.software/spec-3.3/).

You can use [reuse-tool](https://github.com/fsfe/reuse-tool) to generate the SPDX list for this project:

```bash
reuse spdx
```
