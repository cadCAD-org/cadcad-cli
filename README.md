# scaffold
## v1 Wish List
- General
  - Create directory structure
  - Create empty files
  - Create ipynb files with content
    - Content sourced from file (copy)
    - Content sourced from yaml config
  - Create python files with content
    - Content sourced from file (copy)
    - Content sourced from yaml config
  - Specify conditionals (to allow say building specific structures if user opted for Jupyter based project)
  - Interactive and non-interactive forms
- Yaml configs
  - Variables?
  - Directives?
- Interactivity
  - Name
  - Description
  - Template (or complexity level)
  - Uses Jupyter?
  - Use networkx?

## Notes
- A basic requirements.txt will always be supplied that includes numpy, matplotlib, scypy, and pandas by default for every project unless a custom requirements.txt was specified during scaffold.
- Let's limit the interactivity to only a handful of important questions. Things like 'description' are probably not important enough to waste time on initially.
- Rewrite in Python for better OS interoperability.
- Documented schema with versioning
- Would be cool to allow git hosted templates that could be fetched remotely at runtime.
- Would be cool to have a simple website for community sourced templates: search, commenting, rating, etc.
- Does it make sense to package this with cadCAD itself?