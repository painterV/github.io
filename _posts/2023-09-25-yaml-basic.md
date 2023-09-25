---------
title: yaml基本语法
author: painter
time: 2023-09-25
tags:
  - yaml
--------


YAML（"YAML Ain't Markup Language" 或 "Yet Another Markup Language"的缩写）是一种人类可读的数据序列化格式，通常用于配置文件和数据交换。它的语法相对简单，使用空格缩进来表示数据结构的层次关系，而不是像 XML 或 JSON 那样使用标记或大括号。以下是 YAML 的基本语法规则：

1. 键值对：使用冒号（`:`）分隔键和值。键值对的形式如下：

   ```yaml
   key: value
   ```

2. 列表：使用短横线（`-`）表示一个列表项，每个列表项可以包含一个值或一个子对象。列表的形式如下：

   ```yaml
   - item1
   - item2
   - item3
   ```

3. 缩进：YAML 使用空格缩进来表示层次关系。缩进必须保持一致，通常使用两个空格或四个空格。不同层次的元素必须有不同级别的缩进。

4. 注释：可以使用 `#` 符号表示注释，注释后的文本将被忽略。例如：

   ```yaml
   # 这是一条注释
   key: value
   ```

5. 字符串：字符串可以用引号包围，也可以不包围，如果字符串包含特殊字符或空格，则最好使用引号。例如：

   ```yaml
   unquoted: This is an unquoted string
   quoted: "This is a quoted string"
   ```

6. 对象：可以嵌套对象，使用缩进表示嵌套关系。例如：

   ```yaml
   parent:
     child1: value1
     child2: value2
   ```

7. 多行字符串：可以使用管道符号（`|`）表示多行字符串，或者使用大于符号（`>`）表示折叠字符串。例如：

   ```yaml
   multiline1: |
     This is a
     multiline
     string

   multiline2: >
     This is a
     folded string
   ```

8. 引用：可以使用 `&` 符号创建一个锚点（anchor），然后使用 `*` 符号引用该锚点。这在处理重复数据时很有用。

这是 YAML 的基本语法概述。请注意，不同的应用程序和库可能会有一些扩展和变化，但上述规则适用于大多数常见的用例。 YAML 的目标是提供一种易于阅读和编写的数据格式，通常用于配置文件、数据传输和其他需要人类可读的文本格式的场景。
