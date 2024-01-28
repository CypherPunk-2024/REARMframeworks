# 解除假訊息 TTP（策略、技術和程序）框架

DISARM 是一個旨在描述和理解虛假資訊事件的框架。 DISARM 是調整資訊安全 (infosec) 實踐以幫助追蹤和打擊虛假資訊和其他資訊危害的工作的一部分，旨在適應現有的資訊安全實踐和工具。

DISARM 的風格是基於[斜切AT&CK框架](https://github.com/mitre-attack/attack-website/)。 DISARM 物件的 STIX 範本可在[DISARM_CTI 儲存庫](https://github.com/DISARMFoundation/DISARM_cti)- 這些使得 DISARM 資料可以輕鬆地在 ISAO 和使用 TAXII 等標準的類似機構之間傳遞。

## 這個資料夾裡有什麼

解除文檔：

-   [DISARM\_文檔](DISARM_DOCUMENTATION)：DISARM 使用者指南、設計指南和更詳細的 TTP 文件。
-   [DISARM_HISTORY](DISARM_DOCUMENTATION/DISARM_HISTORY)：早期的模型和報告。

解除框架：

-   [解除紅隊框架](generated_pages/disarm_red_framework.md)- 假資訊創作者 TTP，依戰術階段列出。這是與 MISP 捆綁在一起的經典「DISARM 框架」。這[可點擊的](generated_files/disarm_red_framework_clickable.html)版本用於快速建立 TTP 清單。
-   [解除藍隊框架](generated_pages/disarm_blue_framework.md)- 假訊息響應者 TTP，依戰術階段列出。這些是對策，按它們可能使用的最早的戰術階段列出。

解除對象：用於創建紅隊和藍隊框架的所有實體：

-   [階段](generated_pages/phases_index.md)：創建更高級別的戰術分組，以便我們可以檢查我們沒有錯過任何內容
-   [策略](generated_pages/tactics_index.md)：有人進行錯誤訊息事件時可能會使用的階段
-   [技巧](generated_pages/techniques_index.md)：每個階段可能出現的活動
-   [任務](generated_pages/tasks_index.md): 每個階段需要做的事情。在 Pablospeak 中，任務是你所做的事情，技巧就是你做這些事情的方式。
-   [櫃檯](generated_pages/counters_index.md)：解除 TTP 的對策。
-   [演員類型](generated_pages/actortypes_index.md)：採取對策所需的資源
-   [回應類型](generated_pages/responsetype_index.md)：我們用來建立計數器的操作過程類別
-   [元技術](generated_pages/metatechniques_index.md)：更高層級的對策分組
-   [事件](generated_pages/incidents_index.md)：用於建立 DISARM 框架的事件描述

每個實體都有一個目錄，其中包含每個單獨實體的資料表（例如[技術 T0046 搜尋引擎優化](generated_pages/techniques/T0046.md)）。還有一個目錄[產生的文件](generated_files)包含我們從上表產生的任何檔案（CSV、sqlite 等）。

## 更新撤防

重大變更：對 DISARM 模式的任何重大變更均需得到 DISARM 基金會的同意。

小改動：我們喜歡任何和所有改進建議、評論和提供幫助 - 請使用以下方式與我們聯繫[這個谷歌表格](https://docs.google.com/forms/d/e/1FAIpQLSdZuyKFp1UZzk6qUE4IN1O14HaJ-F4TH9thxR3hrRU-Mu7QUQ/viewform)。 （我們也將回顧先前的問題清單：[AMITT 問題列表](https://github.com//DISARM/issues)和[錯誤訊息安全問題列表](https://github.com/misinfosecproject/DISARM_framework/issues))

使用您自己的資料集：DISARM 是開源的。如果您想使用 DISARM 資料做自己的事情，這些將有所幫助：

-   DISARM 的所有主資料都在目錄中[DISARM_MASTER_DATA](DISARM_MASTER_DATA)。尋找[DISARM_FRAMEWORKS_MASTER.xlsx](DISARM_MASTER_DATA/DISARM_FRAMEWORKS_MASTER.xlsx)試算表.其中包含假訊息創建者的策略、技術、任務、階段和對策。

-   這[解除 TTP 指南](https://docs.google.com/document/d/1Kc0O7owFyGiYs8N8wSq17gRUPEDQsD5lLUL_3KGCgRE/edit#)有關每種技術的更詳細資訊。

-   建立所有 HTML 資料表的程式碼位於目錄中[程式碼](CODE)：您需要generate_DISARM_pages.py和所有範本檔案。

如果您有自己的此儲存庫版本並更新 DISARM_FRAMEWORKS_MASTER.xlsx，則輸入「pythongenerate_DISARM_pages.py」將從其中更新上面的所有檔案。如果要同時更新 DISARM github 檔案、DISARM 資料庫和 DISARM STIX 捆綁包，請從 Jupyter 執行檔案generate_DISARM_pages.ipynb。

## 誰負責解除武裝（以及一些歷史）

-   現在：**[解除武裝基金會](https://www.disarm.foundation/)**維護和更新 DISARM 系列模型：DISARM-STIX、DISARM Red 框架（虛假資訊創建）和 DISARM Blue 框架（虛假資訊對策和緩解措施）。

-   2022年，**MITRE、FIU 和 CogSecCollab 團隊**在 SJ、Pablo、Mark 和 Jon Brewer（他讓我們井井有條）的領導下，我們致力於將 AMITT 和 SPICE 框架模型合併在一起創建 DISARM 框架。該團隊創立了解除武裝基金會。

-   2020?**[米特爾](https://www.mitre.org/)和[FIU：佛羅裡達國際大學](https://www.fiu.edu/)**由 FIU 的 Mark Finlayson 領導，分叉了 AMTT RED 模型來創建 SPICE 框架。

-   2020-2022:**[CogSec協作](http://cogsec-collab.org/)**維護並更新了原始 AMITT 模型。 CogSecCollab 是從 MisinfosecWG 衍生出來的非營利組織。 CogSecCollab 在 CTI 聯盟的 Covid19 回應中使用了 AMITT，並在北約、歐盟和其他幾個國家的虛假資訊部門的試驗中對其進行了測試。 SJ Terp 和 Pablo Breuer 擁有 AMITT 模型的設計權。

-   2018-2020:**[錯誤訊息安全工作小組](https://github.com/credcoalition/community-site/wiki/Working-Groups)**，又稱為可信任聯盟的錯誤訊息安全工作組創建了原始的 DISARM 框架。可信度聯盟自然適合其中的標準部分（因為在2017 年，每個團體- 媒體、軍隊、廣告、公眾等- 對虛假信息成分都有不同的措辭），並且因為當可信度聯盟成立時， SJ 也在場。創建後，它們是完成這項工作的自然場所。紅色框架於 2018 年 12 月啟動，在 Credibility Coalition Misinfosec 研討會上完善，並由 SOFTWERX 的 SJ 和 Pablo 在不合理的咖啡量上爭論形成；藍色框架是在2019 年11 月的Coalition Misinfosec 研討會上啟動的，作為潛在虛假信息對策的集合。這項工作由Marvelous.AI 的SJ 和Christopher Walker（“Walker”）共同領導，後來由MentionMapp 的John Gray 加入，但這實際上是CredCo 社區的努力，得到了許多人和地方的貢獻，其中包括Roger Johnston，他在我們在ATT&CKcon 上發言後加入，並開始構建許多工具以及與STIX 和MISP 等系統的連接。

-   2017-2018 年：SJ Terp 開始致力於調整資訊安全工具、流程和程序，以防止虛假資訊的使用。她與 JJ Snow、Pablo Breuer（通常由資訊安全極客組成）和 SOFWERX 團隊聯繫，致力於描述和應對混合事件（網路安全加上虛假訊息，並指出資訊操作始終包括這一點）。

-   **每個為解除武裝做出貢獻的人**（你們中有很多人）。感謝所有為 DISARM 做出貢獻並多年來為 DISARM 做出貢獻的人。

-   **你**。非常感謝您的到來。

DISARM 已獲得許可[CC-BY-4.0](LICENSE.md)
