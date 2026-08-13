# OpenCreator

[简体中文](README.zh-CN.md)

OpenCreator is a personal open-source ecosystem for reproducible, inspectable content workflows. It connects focused tools for fiction, songwriting, four-platform publishing, video production, and workflow visualization without bundling private works, credentials, browser sessions, or production automation.

## Projects

| Project | Purpose | Status |
| --- | --- | --- |
| [OpenCreator Novel](https://github.com/xwcai999/opencreator-novel) | Plan, draft, revise, review, package fiction, and run an optional Wawa submission pre-check | Released (`v0.3.0`) |
| [OpenCreator Music](https://github.com/xwcai999/opencreator-music) | Create original structured lyric packages as a Codex plugin | Released (`v0.1.1`) |
| [OpenCreator Publishers](https://github.com/xwcai999/opencreator-publishers) | Coordinate shared publishing lifecycle and adapters for 番茄、汽水音乐、网易云音乐 and 腾讯音乐 | Released (`v0.1.0`) |
| [OpenCreator Dashboard](https://github.com/xwcai999/opencreator-dashboard) | Explore creation and publishing pipeline runs with sanitized snapshots and mock data | Released (`v0.2.0`) |
| [OpenCreator Family Video](https://github.com/xwcai999/opencreator-family-video) | Orchestrate and verify short bilingual family-learning videos | Released (`v0.1.1`) |

The repositories remain independently installable and versioned. Music owns creation artifacts, Publishers owns the four platform adapters and publishing state machine, and Dashboard remains a read-only visualization client. This repository defines shared principles and points to their source; it does not copy their implementation.

## Shared contract

Every OpenCreator project should:

1. separate source code from user works and runtime evidence;
2. keep secrets in environment variables or the host product's authentication system;
3. record the origin and license of copied or adapted material;
4. require human confirmation before publishing or irreversible actions;
5. expose deterministic validation where practical;
6. document model, media, privacy, and platform limitations honestly;
7. maintain aligned English and Simplified Chinese documentation.

Publishing boundaries are explicit: the Music repository never receives platform credentials; the Publishers repository keeps login state, browser profiles, and irreversible submission local; and the Dashboard only consumes sanitized evidence or synthetic fixtures.

See [ECOSYSTEM.md](ECOSYSTEM.md), [GOVERNANCE.md](GOVERNANCE.md), and the machine-readable [ecosystem.json](ecosystem.json).

## What this is not

OpenCreator is not a hosted content platform, an official OpenAI project, or a promise that generated content is accurate, original, legally clear, or suitable for publication. Each integration has its own service terms and prerequisites.

## Contributing and security

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md). Do not attach credentials, unpublished works, browser profiles, model transcripts, or production logs to public issues.

## License

The files in this repository are licensed under Apache-2.0. Linked projects have their own license and third-party notices.
