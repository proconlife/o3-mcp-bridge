# o3-mcp-bridge

This is a bridge server for o3 using the MCP (Model Controller Protocol).

## Installation

1.  Clone the repository:
    ```bash
    git clone git@github.com:proconlife/o3-mcp-bridge.git
    cd o3-mcp-bridge
    ```

2.  Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the server with the following command:

```bash
uvicorn mcp_server:app --reload
```
