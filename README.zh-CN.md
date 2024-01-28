# 解除虚假信息 TTP（策略、技术和程序）框架

DISARM 是一个旨在描述和理解虚假信息事件的框架。 DISARM 是调整信息安全 (infosec) 实践以帮助跟踪和打击虚假信息和其他信息危害的工作的一部分，旨在适应现有的信息安全实践和工具。

DISARM 的风格基于[斜切AT&CK框架](https://github.com/mitre-attack/attack-website/)。 DISARM 对象的 STIX 模板可在[DISARM_CTI 存储库](https://github.com/DISARMFoundation/DISARM_cti)- 这些使得 DISARM 数据可以轻松地在 ISAO 和使用 TAXII 等标准的类似机构之间传递。

## 这个文件夹里有什么

解除文档：

-   [DISARM\_文档](DISARM_DOCUMENTATION)：DISARM 用户指南、设计指南和更详细的 TTP 文档。
-   [DISARM_HISTORY](DISARM_DOCUMENTATION/DISARM_HISTORY)：早期的模型和报告。

解除框架：

-   [解除红队框架](generated_pages/disarm_red_framework.md)- 虚假信息创建者 TTP，按战术阶段列出。这是与 MISP 捆绑在一起的经典“DISARM 框架”。这[可点击的](generated_files/disarm_red_framework_clickable.html)版本用于快速创建 TTP 列表。
-   [解除蓝队框架](generated_pages/disarm_blue_framework.md)- 虚假信息响应者 TTP，按战术阶段列出。这些是对策，按它们可能使用的最早的战术阶段列出。

解除对象：用于创建红队和蓝队框架的所有实体：

-   [阶段](generated_pages/phases_index.md)：创建更高级别的战术分组，以便我们可以检查我们没有错过任何内容
-   [策略](generated_pages/tactics_index.md)：有人进行错误信息事件时可能会使用的阶段
-   [技巧](generated_pages/techniques_index.md)：每个阶段可能出现的活动
-   [任务](generated_pages/tasks_index.md): 每个阶段需要做的事情。在 Pablospeak 中，任务是你做的事情，技巧是你做这些事情的方式。
-   [柜台](generated_pages/counters_index.md)：解除 TTP 的对策。
-   [演员类型](generated_pages/actortypes_index.md)：采取对策所需的资源
-   [响应类型](generated_pages/responsetype_index.md)：我们用来创建计数器的操作过程类别
-   [元技术](generated_pages/metatechniques_index.md)：更高级别的对策分组
-   [事件](generated_pages/incidents_index.md)：用于创建 DISARM 框架的事件描述

每个实体都有一个目录，其中包含每个单独实体的数据表（例如[技术 T0046 搜索引擎优化](generated_pages/techniques/T0046.md)）。还有一个目录[生成的文件](generated_files)包含我们从上表生成的任何文件（CSV、sqlite 等）。

## 更新撤防

重大变更：对 DISARM 模型的任何重大变更均需得到 DISARM 基金会的同意。

小改动：我们喜欢任何和所有改进建议、评论和提供帮助 - 请使用以下方式与我们联系[这个谷歌表格](https://docs.google.com/forms/d/e/1FAIpQLSdZuyKFp1UZzk6qUE4IN1O14HaJ-F4TH9thxR3hrRU-Mu7QUQ/viewform)。 （我们还将回顾之前的问题列表：[AMITT 问题列表](https://github.com//DISARM/issues)和[错误信息安全问题列表](https://github.com/misinfosecproject/DISARM_framework/issues))

使用您自己的数据集：DISARM 是开源的。如果您想使用 DISARM 数据做自己的事情，这些将有所帮助：

-   DISARM 的所有主数据都在目录中[DISARM_MASTER_DATA](DISARM_MASTER_DATA)。寻找[DISARM_FRAMEWORKS_MASTER.xlsx](DISARM_MASTER_DATA/DISARM_FRAMEWORKS_MASTER.xlsx)电子表格。其中包含虚假信息创建者的策略、技术、任务、阶段和对策。

-   这[解除 TTP 指南](https://docs.google.com/document/d/1Kc0O7owFyGiYs8N8wSq17gRUPEDQsD5lLUL_3KGCgRE/edit#)有关每种技术的更详细信息。

-   创建所有 HTML 数据表的代码位于目录中[代码](CODE)：您需要generate_DISARM_pages.py和所有模板文件。

如果您有自己的此存储库版本并更新 DISARM_FRAMEWORKS_MASTER.xlsx，则输入“pythongenerate_DISARM_pages.py”将从其中更新上面的所有文件。如果要同时更新 DISARM github 文件、DISARM 数据库和 DISARM STIX 捆绑包，请从 Jupyter 运行文件generate_DISARM_pages.ipynb。

## 谁负责解除武装（以及一些历史）

-   现在：**[解除武装基金会](https://www.disarm.foundation/)**维护和更新 DISARM 系列模型：DISARM-STIX、DISARM Red 框架（虚假信息创建）和 DISARM Blue 框架（虚假信息对策和缓解措施）。

-   2022年，**MITRE、FIU 和 CogSecCollab 团队**在 SJ、Pablo、Mark 和 Jon Brewer（他让我们井然有序）的领导下，我们致力于将 AMITT 和 SPICE 框架模型合并在一起创建 DISARM 框架。该团队创建了解除武装基金会。

-   2020?**[米特尔](https://www.mitre.org/)和[FIU：佛罗里达国际大学](https://www.fiu.edu/)**由 FIU 的 Mark Finlayson 领导，分叉了 AMTT RED 模型来创建 SPICE 框架。

-   2020-2022:**[CogSec协作](http://cogsec-collab.org/)**维护并更新了原始 AMITT 模型。 CogSecCollab 是从 MisinfosecWG 衍生出来的非营利组织。 CogSecCollab 在 CTI 联盟的 Covid19 响应中使用了 AMITT，并在北约、欧盟和其他几个国家的虚假信息部门的试验中对其进行了测试。 SJ Terp 和 Pablo Breuer 拥有 AMITT 模型的设计权。

-   2018-2020:**[错误信息安全工作组](https://github.com/credcoalition/community-site/wiki/Working-Groups)**，又名可信联盟的错误信息安全工作组创建了原始的 DISARM 框架。可信度联盟自然适合其中的标准部分（因为在 2017 年，每个团体 - 媒体、军队、广告、公众等 - 对虚假信息成分都有不同的措辞），并且因为当可信度联盟成立时，SJ 也在场。创建后，它们是完成这项工作的自然场所。红色框架于 2018 年 12 月启动，在 Credibility Coalition Misinfosec 研讨会上完善，并由 SOFTWERX 的 SJ 和 Pablo 在不合理的咖啡量上争论形成；蓝色框架是在 2019 年 11 月的 Coalition Misinfosec 研讨会上启动的，作为潜在虚假信息对策的集合。这项工作由 Marvelous.AI 的 SJ 和 Christopher Walker（“Walker”）共同领导，后来由 MentionMapp 的 John Gray 加入，但这实际上是 CredCo 社区的努力，得到了许多人和地方的贡献，其中包括 Roger Johnston，他在我们在 ATT&CKcon 上发言后加入，并开始构建许多工具以及与 STIX 和 MISP 等系统的连接。

-   2017-2018 年：SJ Terp 开始致力于调整信息安全工具、流程和程序，以防止虚假信息的使用。她与 JJ Snow、Pablo Breuer（通常由信息安全极客组成）和 SOFWERX 团队联系，致力于描述和应对混合事件（网络安全加上虚假信息，并指出信息操作始终包括这一点）。

-   **每个为解除武装做出贡献的人**（你们中有很多人）。感谢所有为 DISARM 做出贡献并多年来为 DISARM 做出贡献的人。

-   **你**。非常感谢您的到来。

DISARM 已获得许可[CC-BY-4.0](LICENSE.md)
