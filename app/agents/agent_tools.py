
import subprocess
from langchain_core.tools import tool

from app.logger import get_logger

log = get_logger(__name__)

# Define the tool the agent can use
@tool
def execute_shell_command(command: str) -> str:
    """A Function to execute bash commands on the terminal."""
    try:
        response = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        log.info(f"Executed command: {command}")
        log.info(f"Command output: {response.stdout}")
        return response.stdout if response.stdout else "Command executed successfully"
    except subprocess.CalledProcessError as e:
        return f"Command failed with error: {e}"

# Register the tool
tools = [execute_shell_command]

