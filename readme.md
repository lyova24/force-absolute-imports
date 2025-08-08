<div align="center">
    <img src="./docs/images/shrimport.png" width="128" alt="Shrimport Logo">
    <h3>Shrimport</h3>
    <p>
      pre-commit-hook for <a href="https://github.com/pre-commit/pre-commit">pre-commit</a>
      to format relative imports as absolute ones in Python
    </p>
    <a href="https://github.com/lyova24/shrimport/tags">
      <img src="https://img.shields.io/github/v/release/lyova24/shrimport" alt="Latest Release">
      <img src="https://img.shields.io/github/last-commit/lyova24/shrimport/main" alt="Latest Commit">
    </a>
</div>


----

#### Usage
##### Put this to your .pre-commit-config.yaml
```yaml
  - repo: https://github.com/lyova24/shrimport
    rev: v0.0.8 # or any other version-tag/commit
    hooks:
      - id: shrimport
```

##### Arguments
```shell
# `-R / --root-dir` argument to specify root dir for your imports
# `-i / --ignore` argument to specify regex pattern of filepaths to ignore  (several values possible)
# `-v / --verbose` argument to output extra information on hook's execution (notice: pre-commit also have this arg)
```

##### Example of arguments usage in your .pre-commit-config.yaml
```yaml
  - repo: https://github.com/lyova24/shrimport
    rev: v0.0.8
    hooks:
      - id: shrimport
        args:
          - '--root-dir=./app' # or '-R=./app'
          - '--ignore=test/*' # or '-i=test/*'
          - '--verbose' # or '-v'
```
