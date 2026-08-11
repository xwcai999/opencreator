# Ecosystem architecture

OpenCreator uses a federated repository model:

```text
opencreator (principles and index)
├── novel-studio-skill       fiction workflow
├── opencreator-music        lyric workflow plugin
├── opencreator-dashboard    read-only visualization
└── opencreator-family-video video workflow plugin
```

Repositories exchange documented artifacts instead of importing each other's private state. A workflow may emit JSON evidence for the dashboard, but the dashboard must also work with bundled sanitized fixtures. Platform publishing is outside the shared core.

## Compatibility levels

- **Core**: can be installed and tested without private user data.
- **Adapter**: connects to a named external service and documents authentication and terms.
- **Example**: synthetic or explicitly licensed data only.
- **Private deployment**: credentials, works, browser profiles, session logs, and production queues; never part of a release.

