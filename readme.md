<div align="center">
    <img src="./docs/images/shrimport.png" width="128" alt="Shrimport Logo">
    <h3>Shrimport</h3>
    <p>
      pre-commit hook for <a href="https://github.com/pre-commit/pre-commit">pre-commit</a>
      to format relative imports as absolute ones in Python
    </p>
    <a href="https://github.com/lyova24/shrimport/tags">
      <img src="https://img.shields.io/github/v/tag/lyova24/shrimport" alt="Latest Tag">
    </a>
</div>


----

#### Usage
##### Put this to your .pre-commit-config.yaml
```yaml
  - repo: https://github.com/lyova24/shrimport
    rev: v0.0.4 # or any other version-tag/commit
    hooks:
      - id: shrimport
```

##### Arguments
```shell
# `--root-dir` argument to specify root dir for your imports
# `--ignore` argument to specify regex pattern of filepaths to ignore  (several values possible)
```

##### Example of arguments usage in your .pre-commit-config.yaml
```yaml
  - repo: https://github.com/lyova24/shrimport
    rev: v0.0.4
    hooks:
      - id: shrimport
        args:
          - '--root-dir=./app' # example of --root-dir usage
          - '--ignore=test/*' # example of --ignore usage
```
