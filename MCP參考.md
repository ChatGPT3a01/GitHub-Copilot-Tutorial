Visual Studio Code
Docs
Updates
Blog
API
Extensions
MCP
FAQ
Switch to the light theme
Search DocsCtrl+Shift+P
Download
Version 1.107 is now available! Read about the new features and fixes from November.

Dismiss this update
Overview
Setup
Get Started
Configure
Edit code
Build, Debug, Test
GitHub Copilot
Overview
Setup
Quickstart
Chat
Agents
Inline Suggestions
Customization
Overview
Instructions
Prompt Files
Custom Agents
Language Models
MCP
Guides
Smart Actions
Tips and Tricks
Security
FAQ
Reference
Source Control
Terminal
Languages
Node.js / JavaScript
TypeScript
Python
Java
C++
C#
Container Tools
Data Science
Intelligent Apps
Azure
Remote
Dev Containers
Reference
On this page there are 15 sectionsOn this page
Prerequisites
Add an MCP server
Use MCP tools in chat
Use MCP resources
Use MCP prompts
Group related tools in a tool set
Manage installed MCP servers
Find MCP servers
MCP server trust
Synchronize MCP servers across devices
Configuration format
Troubleshoot and debug MCP servers
Centrally control MCP access
Frequently asked questions
Related resources
Use MCP servers in VS Code
Model Context Protocol (MCP) is an open standard that lets AI models use external tools and services through a unified interface. In VS Code, MCP servers provide tools for tasks like file operations, databases, or interacting with external APIs.

MCP servers are one of three ways to extend chat with tools in VS Code, alongside built-in tools and extension-contributed tools. Learn more about types of tools.

This article guides you through setting up MCP servers and using their capabilities in Visual Studio Code.

How does MCP work?
Supported MCP capabilities in VS Code
Note
MCP support in VS Code is generally available starting from VS Code 1.102.

Prerequisites
Install the latest version of Visual Studio Code
Access to Copilot
Add an MCP server
Caution
Local MCP servers can run arbitrary code on your machine. Only add servers from trusted sources, and review the publisher and server configuration before starting it. VS Code prompts you to confirm that you trust the MCP server when you start an MCP server for the first time. Read the Security documentation for using AI in VS Code to understand the implications.

Add an MCP server from the GitHub MCP server registry
You can install an MCP server directly from the GitHub MCP server registry via the Extensions view in VS Code. You can choose to install the MCP server either in your user profile or in the current workspace.

To install an MCP server from the Extensions view:

Enable the MCP server gallery with the chat.mcp.gallery.enabled setting.

Open the Extensions view (Ctrl+Shift+X)

Enter @mcp in the search field to show the list of MCP servers or run the MCP: Browse Servers command from the Command Palette.

VS Code retrieves the list of MCP servers from the GitHub MCP server registry.

To install an MCP server:

In your user profile: select Install

In your workspace: right-click the MCP server and select Install in Workspace

To view the MCP server details, select the MCP server in the list.

Other options to add an MCP server
You have several other options to add an MCP server in VS Code:

Add an MCP server to a workspace `mcp.json` file
Add an MCP server to your user configuration
Add an MCP server to a dev container
Automatically discover MCP servers
Install an MCP server from the command line
Use MCP tools in chat
Once you have added an MCP server, you can use the tools it provides in chat. MCP tools work like other tools in VS Code: they can be automatically invoked when using agents or explicitly referenced in your prompts.

To use MCP tools in chat:

Open the Chat view (Ctrl+Alt+I).

Open the tool picker to select which tools the agent is allowed to use. MCP tools are grouped per MCP server.

Tip
When you create custom prompts or custom agents, you can also specify which MCP tools can be used.

When using agents, tools are automatically invoked as needed based on your prompt.

For example, install the GitHub MCP server and then ask "List my GitHub issues".

Screenshot of the Chat view, showing an MCP tool invocation when using agents.

You can also explicitly reference MCP tools by typing # followed by the tool name.

Review and approve tool invocations when prompted.

Screenshot of the MCP tool confirmation dialog in chat.

Learn more about using tools in chat, including how to manage tool approvals, use the tool picker, and create tool sets.

Clear cached MCP tools
When VS Code starts the MCP server for the first time, it discovers the server's capabilities and tools. You can then use these tools in chat. VS Code caches the list of tools for an MCP server. To clear the cached tools, use the MCP: Reset Cached Tools command in the Command Palette.

Use MCP resources
MCP servers can give direct access to resources that you can use as context in your chat prompts. For example, a file system MCP server can let you access files and directories, or a database MCP server might provide access to database tables.

To add a resource from an MCP server to your chat prompt:

In the Chat view, select Add Context > MCP Resources

Select a resource type from the list and provide optional resource input parameters.

Screenshot of the MCP resource Quick Pick, showing resource types provided by the GitHub MCP server.

To view the list of available resources for an MCP server, use the MCP: Browse Resources command or use the MCP: List Servers > Browse Resources command to view resources for a specific server.

MCP tools can return resources as part of their response. You can view or save these resources to your workspace by selecting Save or by dragging and dropping the resource to the Explorer view.

Use MCP prompts
MCP servers can provide preconfigured prompts for common tasks that you can invoke in chat with a slash command. To invoke an MCP prompt in chat, type / in the chat input field, followed by the prompt name, formatted as mcp.servername.promptname.

Optionally, the MCP prompt might ask you for extra input parameters.

Screenshot of the Chat view, showing an MCP prompt invocation and a dialog asking for additional input parameters.

Group related tools in a tool set
As you add more MCP servers, the list of tools can become long. You can group related tools into a tool set to make them easier to manage and reference.

Learn more about how to create and use tool sets.

Manage installed MCP servers
You can perform various actions on the installed MCP servers, such as starting or stopping a server, viewing the server logs, uninstalling the server, and more.

To perform these actions on an MCP server, use either of these options:

Right-click a server in the MCP SERVERS - INSTALLED section or select the gear icon

Screenshot showing the MCP servers in the Extensions view.

Open the mcp.json configuration file and access the actions inline in the editor (code lenses)

MCP server configuration with lenses to manage server.

Use the MCP: Open User Configuration or MCP: Open Workspace Folder Configuration commands to access the MCP server configuration.

Run the MCP: List Servers command from the Command Palette and select a server

Screenshot showing the actions for an MCP server in the Command Palette.

Automatically start MCP servers
When you add an MCP server or change its configuration, VS Code needs to (re)start the server to discover the tools it provides.

You can configure VS Code to automatically restart the MCP server when configuration changes are detected by using the chat.mcp.autostart setting (Experimental).

Alternatively, manually restart the MCP server from the Chat view, or by selecting the restart action from the MCP server list.

Screenshot showing the Refresh button in the Chat view.

Find MCP servers
MCP is still a relatively new standard, and the ecosystem is rapidly evolving. As more developers adopt MCP, you can expect to see an increasing number of servers and tools available for integration with your projects.

The GitHub MCP server registry is a great starting point. You can access the registry directly from the Extensions view in VS Code.

MCP's official server repository provides official, and community-contributed servers that showcase MCP's versatility. You can explore servers for various functionalities, such as file system operations, database interactions, and web services.

VS Code extensions can also contribute MCP servers and configure them as part of the extension's installation process. Check the Visual Studio Marketplace for extensions that provide MCP server support.

MCP server trust
MCP servers can run arbitrary code on your machine. Only add servers from trusted sources, and review the publisher and server configuration before starting it. Read the Security documentation for using AI in VS Code to understand the implications.

When you add an MCP server to your workspace or change its configuration, you need to confirm that you trust the server and its capabilities before starting it. VS Code shows a dialog to confirm that you trust the server when you start a server for the first time. Select the link to MCP server in the dialog to review the MCP server configuration in a separate window.

Screenshot showing the MCP server trust prompt.

If you don't trust the server, it is not started, and chat requests continue without using the tools provided by the server.

You can reset trust for your MCP servers by running the MCP: Reset Trust command from the Command Palette.

Note
If you start the MCP server directly from the mcp.json file, you are not prompted to trust the server configuration.

Synchronize MCP servers across devices
With Settings Sync enabled, you can synchronize settings and configurations across devices, including MCP server configurations. This allows you to maintain a consistent development environment and access the same MCP servers on all your devices.

To enable MCP server synchronization with Settings Sync, run the Settings Sync: Configure command from the Command Palette, and ensure that MCP Servers is included in the list of synchronized configurations.

Configuration format
MCP servers are configured using a JSON file (mcp.json) that defines two main sections: server definitions and optional input variables for sensitive data.

MCP servers can connect using different transport methods. Choose the appropriate configuration based on how your server communicates.

Configuration structure
The configuration file has two main sections:

"servers": {} - Contains the list of MCP servers and their configurations
"inputs": [] - Optional placeholders for sensitive information like API keys
You can use predefined variables in the server configuration, for example to refer to the workspace folder (${workspaceFolder}).

Standard I/O (stdio) servers
Use this configuration for servers that communicate through standard input and output streams. This is the most common type for locally-run MCP servers.

Expand table
Field	Required	Description	Examples
type	Yes	Server connection type	"stdio"
command	Yes	Command to start the server executable. Must be available on your system path or contain its full path.	"npx", "node", "python", "docker"
args	No	Array of arguments passed to the command	["server.py", "--port", "3000"]
env	No	Environment variables for the server	{"API_KEY": "${input:api-key}"}
envFile	No	Path to an environment file to load more variables	"${workspaceFolder}/.env"
Note
When using Docker with stdio servers, don't use the detach option (-d). The server must run in the foreground to communicate with VS Code.

Example local server configuration
HTTP and Server-Sent Events (SSE) servers
Use this configuration for servers that communicate over HTTP. VS Code first tries the HTTP Stream transport and falls back to SSE if HTTP is not supported.

Expand table
Field	Required	Description	Examples
type	Yes	Server connection type	"http", "sse"
url	Yes	URL of the server	"http://localhost:3000", "https://api.example.com/mcp"
headers	No	HTTP headers for authentication or configuration	{"Authorization": "Bearer ${input:api-token}"}
In addition to servers available over the network, VS Code can connect to MCP servers listening for HTTP traffic on Unix sockets or Windows named pipes by specifying the socket or pipe path in the form unix:///path/to/server.sock or pipe:///pipe/named-pipe on Windows. You can specify subpaths by using a URL fragment, such as unix:///tmp/server.sock#/mcp/subpath.

Example remote server configuration
Input variables for sensitive data
Input variables let you define placeholders for configuration values, avoiding the need to hardcode sensitive information like API keys or passwords directly in the server configuration.

When you reference an input variable using ${input:variable-id}, VS Code prompts you for the value when the server starts for the first time. The value is then securely stored for subsequent use. Learn more about input variables in VS Code.

Input variable properties:

Expand table
Field	Required	Description	Example
type	Yes	Type of input prompt	"promptString"
id	Yes	Unique identifier to reference in server config	"api-key", "database-url"
description	Yes	User-friendly prompt text	"GitHub Personal Access Token"
password	No	Hide typed input (default: false)	true for API keys and passwords
Example server configuration with input variables
Server naming conventions
When defining MCP servers, follow these naming conventions for the server name:

Use camelCase for the server name, such as "uiTesting" or "githubIntegration"
Avoid using whitespace or special characters
Use a unique name for each server to avoid conflicts
Use a descriptive name that reflects the server's functionality or brand, such as "github" or "database"
Troubleshoot and debug MCP servers
MCP output log
When VS Code encounters an issue with an MCP server, it shows an error indicator in the Chat view.

MCP Server Error

Select the error notification in the Chat view, and then select the Show Output option to view the server logs. Alternatively, run MCP: List Servers from the Command Palette, select the server, and then choose Show Output.

MCP Server Error Output

Debug an MCP server
You can enable development mode for MCP servers by adding a dev key to the MCP server configuration. This is an object with two properties:

watch: A file glob pattern to watch for files change that will restart the MCP server.
debug: Enables you to set up a debugger with the MCP server. Currently, VS Code supports debugging Node.js and Python MCP servers.
Learn more about MCP development mode in the MCP Dev Guide.

Centrally control MCP access
Organizations can centrally manage access to MCP servers via GitHub policies. Learn more about enterprise management of MCP servers.

Frequently asked questions
Can I control which MCP tools are used?
Select the Tools button in the Chat view when using agents, and toggle specific tools on/off as needed.
Add specific tools to your prompt by using the Add Context button or by typing #.
For more advanced control, you can use .github/copilot-instructions.md to fine-tune tool usage.
The MCP server is not starting when using Docker
Verify that the command arguments are correct and that the container is not running in detached mode (-d option). You can also check the MCP server output for any error messages (see Troubleshooting).

I'm getting an error that says "Cannot have more than 128 tools per request."
A chat request can have a maximum of 128 tools enabled at a time due to model constraints. If you have more than 128 tools selected, reduce the number of tools by deselecting some tools or whole servers in the tools picker in the Chat view, or ensure that virtual tools are enabled (github.copilot.chat.virtualTools.threshold).

Screenshot showing the Chat view, highlighting the Tools icon in the chat input and showing the tools Quick Pick where you can select which tools are active.

Related resources
Model Context Protocol Documentation
Model Context Protocol Server repository
Use agents in VS Code chat
Help and support
Was this documentation helpful?
Yes, this page was helpfulNo, this page was not helpful
Still need help?
Ask the community
Request features
Report issues
Help us improve
All VS Code docs are open source. See something that's wrong or unclear? Submit a pull request.

12/10/2025
VS Code on Github Follow us on X VS Code on LinkedIn VS Code on Bluesky Join the VS Code community on Reddit The VS Code Insiders Podcast VS Code on TikTok VS Code on YouTube
Microsoft homepage
Support Privacy Terms of Use License