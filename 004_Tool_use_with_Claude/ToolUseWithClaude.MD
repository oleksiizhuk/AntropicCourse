## 0_0_1 Introducing tool use

Tools allow Claude to access information from the outside world, extending its capabilities beyond what it learned during training. By default, Claude only knows information from its training data and can't access current events, real-time data, or external systems. Tool use solves this limitation by creating a structured way for Claude to request and receive fresh information.

Key Benefits:
- Real-time Information: Access current data that wasn't available during Claude's training
- External System Integration: Connect Claude to databases, APIs, and other services
- Dynamic Responses: Provide answers based on the latest available information
- Structured Interaction: Claude knows exactly what information it needs and how to ask for it


## 0_0_2 Project overview
We're going to build a practical project that teaches Claude how to set reminders for future dates. This might sound simple at first, but it reveals several interesting challenges that we'll solve using custom tools.

We'll create three separate tools to handle each challenge:
- Get the current date time: Claude needs to know the current date and time precisely
- Add duration to date time: Claude isn't perfect with date time addition, so we'll give it a reliable tool for this
- Set a reminder: We need a way to actually set a reminder in the system


## 0_0_3 Tool functions
When building AI applications with Claude, you'll often need to give it access to real-time information or the ability to perform actions. This is where tool functions come in - they're Python functions that Claude can call when it needs additional data to help users.

Best Practices for Tool Functions
- Use descriptive names: Both your function name and parameter names should clearly indicate their purpose
- Validate inputs: Check that required parameters aren't empty or invalid, and raise errors when they are
- Provide meaningful error messages: Claude can see error messages and might retry the function call with corrected parameters


## 0_0_4 Tool schemas
After writing your tool function, the next step is creating a JSON schema that tells Claude what arguments your function expects and how to use it. This schema acts as documentation that Claude reads to understand when and how to call your tools.

The complete tool specification has three main parts:
- name - A clear, descriptive name for your tool (like "get_weather")
- description - What the tool does, when to use it, and what it returns
- input_schema - The actual JSON schema describing the function's arguments

Writing Effective Descriptions:
- Aim for 3-4 sentences explaining what the tool does
- Describe when Claude should use it
- Explain what kind of data it returns
- Provide detailed descriptions for each argument

The Easy Way to Generate Schemas: 
1) Copy your tool function code
2) Go to Claude and ask it to write a JSON schema for tool calling
3) Include the Anthropic documentation on tool use as context
4) Let Claude generate a properly formatted schema following best practices

Adding Type Safety: 
For better type checking, import and use the ToolParam type from the Anthropic library:
`from anthropic.types import ToolParam`


## 0_0_5 Handling message blocks
When working with Claude's tool functionality, you'll encounter a new type of response structure that's different from the simple text responses you've seen before. Instead of just getting back a single text block, Claude can now return multi-block messages that contain both text and tool usage information.

A multi-block message typically contains:
- Text Block - Human-readable text explaining what Claude is doing (like "I can help you find out the current time. Let me find that information for you")
- ToolUse Block - Instructions for your code about which tool to call and what parameters to use


## 0_0_6 Sending tool results

