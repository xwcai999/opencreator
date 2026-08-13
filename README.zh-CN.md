# OpenCreator

[English](README.md)

OpenCreator 是一个面向可复现、可审计内容工作流的个人开源生态。它连接小说、写歌、四平台发布、视频生产和流程可视化工具，但不捆绑私人作品、凭据、浏览器会话或生产自动化。

## 项目

| 项目 | 用途 | 状态 |
| --- | --- | --- |
| [OpenCreator Novel](https://github.com/xwcai999/opencreator-novel) | 中文小说策划、创作、修订、审查、打包及可选蛙蛙投稿预检 | 已发布（`v0.3.0`） |
| [OpenCreator Music](https://github.com/xwcai999/opencreator-music) | 以 Codex 插件生成原创结构化歌词包 | 已发布（`v0.1.1`） |
| [OpenCreator Publishers](https://github.com/xwcai999/opencreator-publishers) | 统一编排番茄、汽水音乐、网易云音乐和腾讯音乐的发布生命周期与平台适配器 | 已发布（`v0.1.0`） |
| [OpenCreator Dashboard](https://github.com/xwcai999/opencreator-dashboard) | 使用脱敏快照和 Mock 数据查看创作与发布流水线运行 | 已发布（`v0.2.0`） |
| [OpenCreator Family Video](https://github.com/xwcai999/opencreator-family-video) | 编排并验收家庭情景双语短视频 | 已发布（`v0.1.1`） |

各仓库保持独立安装和独立版本。Music 负责创作成品，Publishers 负责四个平台适配器和发布状态机，Dashboard 保持只读可视化。本仓库只定义共享原则和项目索引，不复制各项目实现。

## 共享契约

每个 OpenCreator 项目都应：

1. 将源代码与用户作品、运行证据分离；
2. 将密钥保存在环境变量或宿主产品认证系统中；
3. 记录复制或改编材料的来源与许可证；
4. 在发布或不可逆操作前要求人工确认；
5. 在可行时提供确定性校验；
6. 如实说明模型、媒体、隐私和平台限制；
7. 同步维护英文和简体中文文档。

发布边界必须明确：Music 不接收平台凭据；Publishers 将登录状态、浏览器 Profile 和不可逆提交保留在本地；Dashboard 只消费脱敏证据或合成 Fixture，不直接驱动适配器。

详见 [ECOSYSTEM.md](ECOSYSTEM.md)、[GOVERNANCE.md](GOVERNANCE.md) 和机器可读的 [ecosystem.json](ecosystem.json)。

## 它不是什么

OpenCreator 不是托管内容平台，不是 OpenAI 官方项目，也不保证生成内容准确、原创、权利清晰或适合发布。每项集成都有独立的服务条款和运行前置条件。

## 贡献与安全

提交改动前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。漏洞请按 [SECURITY.md](SECURITY.md) 私下报告。不要在公开 Issue 中附带凭据、未公开作品、浏览器配置、模型转录或生产日志。

## 许可证

本仓库文件采用 Apache-2.0。链接项目分别维护自己的许可证和第三方通知。
