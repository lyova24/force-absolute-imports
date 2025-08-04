#### usage
##### add this in your .pre-commit-config.yaml
```yaml
  - repo: https://github.com/lyova24/force-absolute-imports
    rev: v0.0.1 # or any other tag/commit from this repo
    hooks:
      - id: force-absolute-imports
        args: ["--root-dir=./app"] # or any other root directory for your imports
```