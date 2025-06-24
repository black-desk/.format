<!--
SPDX-FileCopyrightText: 2025 Chen Linxuan <me@black-desk.cn>

SPDX-License-Identifier: MIT
-->

# .format

[en](README.md) | zh_CN

我的个人项目使用的代码格式化配置文件。

该项目会在我的其他个人项目中以git
submodule的方式被引用并通过dependabot保持更新。

## 使用

```bash
git submodule add https://github.com/black-desk/.format

# 然后自行创建相关的符号链接，比如：

ln -s .format/.editorconfig
ln -s .format/.clang-format
```

## 说明

- `black`:

  ```bash
  ln -s .format/.black.toml
  ```

  ```toml
  # In your pyproject.toml
  [tool.black]
  src = [".black.toml"]
  ```

## 许可证

如无特殊说明，该项目中的文件以MIT许可证开源。

该项目遵守[REUSE规范](https://reuse.software/spec-3.3/)。

你可以使用[reuse-tool](https://github.com/fsfe/reuse-tool)生成这个项目的SPDX列表：

```bash
reuse spdx
```
