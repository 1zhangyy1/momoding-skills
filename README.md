# Momoding 社区经验库

Momoding 在每个人手机上办事时，会自己记下“哪个网站能用、怎么读、哪里会被拦”。验证过、对别人也有用的经验，整理成技能放在这里，所有人的 Momoding 都能用上。

- GitHub：<https://github.com/1zhangyy1/momoding-skills>（提交和审核在这里）
- Gitee：<https://gitee.com/nuomijizhangyy/momoding-skills>（国内同步镜像，App 优先从这里读）

## App 怎么用

1. 每天拉一次 `index.json`（技能名、管哪些网站和哪类事）。
2. 办事前，Momoding 查自己的记录，也查这份目录；对得上就装上对应技能再动手。
3. 每个人手机上自己记下的经验优先，社区技能只是起点。

## 怎么贡献

- 在 Momoding 里说“把这条经验分享给大家”，它会整理好内容，并给出一个链接，你登录 GitHub 后提交即可。
- 也可以直接提 PR：复制 `template/SKILL.md` 到 `skills/<名字>/SKILL.md`，按要求填写。

## 收录规则

只收“去哪查、怎么读、被拦了换哪”这类经验。

- 写明哪些网站、在什么时间验证过（`verified`）；
- 不写价格、日期这类会过期的结果；
- 不写任何个人信息、账号、密码、验证码；
- 不收绕过验证码、登录墙或付费墙的方法，也不收教人自动发消息、付款、登录的内容；
- 合并前由维护者审核。技能内容对 App 来说只是参考，不是指令。

`index.json` 由 `scripts/build_index.py` 根据各技能的开头信息生成，请不要手改。
