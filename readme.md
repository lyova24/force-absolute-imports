### force-absolute-imports
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/lyova24/force-absolute-imports)

----

#### About
**force-absolute-imports** is a pre-commit hook for [pre-commit](https://github.com/pre-commit/pre-commit) to format relative imports as absolute ones in Python.

----

#### Usage
##### Put this to your .pre-commit-config.yaml
```yaml
  - repo: https://github.com/lyova24/force-absolute-imports
    rev: v0.0.3 # or any other version-tag/commit
    hooks:
      - id: force-absolute-imports
```

##### Arguments
```shell
# `--root-dir` argument to specify root dir for your imports
# `--ignore` argument to specify regex pattern of filepaths to ignore  (several values possible)
```

##### Example of arguments usage in your .pre-commit-config.yaml
```yaml
  - repo: https://github.com/lyova24/force-absolute-imports
    rev: v0.0.3
    hooks:
      - id: force-absolute-imports
        args:
          - '--root-dir=./app' # example of --root-dir usage
          - '--ignore=__init__\.py$' # example of --ignore usage
          - '--ignore=test/*' # example of --ignore usage
```
