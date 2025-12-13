📚 MCP 實戰完整教學（VS Code × Copilot）

一句話給學生聽懂版
MCP 就是：
👉「讓 Copilot 不只會說話，還能真的幫你 做事情 的外掛系統」

一、MCP 是什麼？（上課第 1 張投影片用）
核心概念（不講協定細節）

MCP = Model Context Protocol

是一個 讓 AI 可以使用外部工具的標準

工具可能來自：

檔案系統

GitHub

API

資料庫

你自己寫的程式

📌 在 VS Code 裡：

MCP Server = 工具提供者
Copilot = 工具使用者

二、教學前必要條件（一定先檢查）
✅ 必備環境

VS Code 版本 ≥ 1.102
-（你現在用的是 1.107，OK）

已登入 GitHub Copilot

能開啟 Copilot Chat（Ctrl + Alt + I）

三、MCP 建置流程（老師一定要照這個順序）
Step 1：開啟 MCP Server Gallery（關鍵）
操作

Ctrl + , 開啟設定

搜尋：

chat.mcp.gallery.enabled


✅ 勾選 Enable

📌 沒做這一步：

你在 Extensions 裡「永遠看不到 MCP」

Step 2：從 Extensions 安裝 MCP Server（最安全）
操作

Ctrl + Shift + X（Extensions）

搜尋欄輸入：

@mcp


或使用指令：

MCP: Browse Servers


你會看到 GitHub MCP Server Registry 清單

選一個（建議教學用）：

GitHub MCP Server

點：

Install（使用者）

或 Install in Workspace（專案）

四、第一次啟動 MCP（一定會問你）
⚠️ 重要安全提醒（要教學生）

MCP Server = 可以在你電腦跑程式

VS Code 會跳出：

「你是否信任這個 MCP Server？」

👉 教學時請明確說：
只安裝你信任來源的 MCP

五、MCP 真正開始用（重點來了）
範例一：用 MCP 工具（Tools）在 Chat 裡做事
Step 1：開啟 Copilot Chat

Ctrl + Alt + I

Step 2：開啟 Tools Picker

點聊天框旁邊的 Tools 圖示

你會看到：

Built-in tools

Extension tools

✅ MCP tools（依 Server 分組）

Step 3：示範提問（GitHub MCP）
List my GitHub issues


Copilot 會：

自動呼叫 MCP 工具

跳出 工具使用確認

你按「允許」

📌 這一刻要跟學生說一句話：

「你剛剛不是在聊天，是在下指令」

六、用 # 明確指定 MCP 工具（進階但好教）
範例
#github.listIssues


📌 教學重點：

# = 明確點名工具

適合精準控制、不想讓 Copilot 自己猜

七、使用 MCP Resources（把外部資料當上下文）
操作流程

Copilot Chat → Add Context

選：

MCP Resources


選擇資源（例如 GitHub repo、issue、檔案）

📌 概念一句話：

MCP Resources =「把真實資料塞給 AI 當參考」

八、使用 MCP Prompt（超像 Slash 指令）
操作

在 Chat 輸入：

/mcp.serverName.promptName


📌 特點：

MCP Server 可以「預先定義好任務」

適合教學、流程固定的工作

九、管理 MCP Server（老師一定會用到）
常用指令（Command Palette）

MCP: List Servers

MCP: Browse Resources

MCP: Reset Cached Tools

MCP: Reset Trust

📌 教學情境：

「工具怪怪的、更新後沒反應 → Reset Cached Tools」

十、進階建置：用 mcp.json 自己定義（老師版）
📁 檔案位置

使用者：

MCP: Open User Configuration


專案：

.vscode/mcp.json

✅ 範例：本地 Python MCP Server（stdio）
{
  "servers": {
    "localTools": {
      "type": "stdio",
      "command": "python",
      "args": ["server.py"]
    }
  }
}


📌 教學說法：

「這代表：Copilot 會啟動一個 Python 程式，當工具用」

十一、加入敏感資料（API Key 正確做法）
inputs 範例
{
  "inputs": [
    {
      "type": "promptString",
      "id": "api-key",
      "description": "API 金鑰",
      "password": true
    }
  ]
}


使用方式：

"env": {
  "API_KEY": "${input:api-key}"
}


📌 重點：

不寫死 API Key

第一次會跳出輸入框

VS Code 會安全保存