# Ecosystem architecture

OpenCreator uses a federated repository model:

```text
opencreator (principles and index)
├── opencreator-novel        fiction workflow + optional Wawa submission adapter
├── opencreator-music        lyric workflow plugin
├── opencreator-publishers   four-platform publishing adapters and shared lifecycle
├── opencreator-dashboard    read-only visualization
└── opencreator-family-video video workflow plugin
```

Repositories exchange documented artifacts instead of importing each other's private state. `opencreator-music` owns creation workflows and structured media packages; it does not own platform accounts, login sessions, or browser automation. `opencreator-publishers` owns the shared publishing lifecycle and platform-specific adapters for 番茄、汽水音乐、网易云音乐 and 腾讯音乐. It consumes documented packages, keeps credentials and irreversible submission local, and exposes sanitized status/evidence snapshots. `opencreator-dashboard` consumes those snapshots or bundled fixtures for read-only visualization; it never drives adapters or stores credentials. This keeps creation, publishing and visualization on independent release lifecycles while allowing the four platforms to share one publisher core.

The publisher repository is released as `v0.1.0`. It contains offline contracts, synthetic adapters, and manual-confirmation gates; no production account or private queue is part of the public repository.

## Compatibility levels

- **Core**: can be installed and tested without private user data.
- **Adapter**: connects to a named external service and documents authentication and terms.
- **Example**: synthetic or explicitly licensed data only.
- **Private deployment**: credentials, works, browser profiles, session logs, and production queues; never part of a release.
