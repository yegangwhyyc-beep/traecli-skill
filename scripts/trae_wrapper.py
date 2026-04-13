#!/usr/bin/env python3
"""
TRAE CLI Wrapper Script

This script provides a safe and structured interface to invoke TRAE CLI commands.
It handles input validation, command execution, and output parsing.
"""

import subprocess
import sys
import json
from typing import Optional, Dict, Any


class TraeCLI:
    """Wrapper for TRAE CLI commands."""

    def __init__(self, executable: str = "traecli"):
        self.executable = executable

    def execute(self, prompt: str, workdir: Optional[str] = None) -> Dict[str, Any]:
        """
        Execute TRAE CLI with a natural language prompt.

        Args:
            prompt: Natural language instruction for TRAE CLI
            workdir: Working directory for command execution

        Returns:
            Dictionary with 'success', 'output', 'error' keys
        """
        try:
            # Prepare command with --print for non-interactive mode
            cmd = [self.executable, "--print", prompt]

            # Execute command
            result = subprocess.run(
                cmd,
                cwd=workdir,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )

            # Parse response
            output = result.stdout.strip()
            error = result.stderr.strip()

            return {
                "success": result.returncode == 0,
                "output": output,
                "error": error,
                "return_code": result.returncode
            }

        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "output": "",
                "error": "Command timeout after 5 minutes",
                "return_code": -1
            }
        except FileNotFoundError:
            return {
                "success": False,
                "output": "",
                "error": f"TRAE CLI executable '{self.executable}' not found. Please ensure it's installed and in PATH.",
                "return_code": -1
            }
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": str(e),
                "return_code": -1
            }

    def generate_code(self, requirement: str, workdir: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate code based on requirements.

        Args:
            requirement: Natural language description of code requirements
            workdir: Working directory

        Returns:
            Execution result
        """
        prompt = f"Generate code: {requirement}"
        return self.execute(prompt, workdir)

    def init_framework(self, project_type: str, project_name: str, workdir: Optional[str] = None) -> Dict[str, Any]:
        """
        Initialize a project framework.

        Args:
            project_type: Type of project (e.g., 'react', 'vue', 'nodejs', 'python')
            project_name: Name of the project
            workdir: Working directory (parent directory for project)

        Returns:
            Execution result
        """
        prompt = f"Initialize a {project_type} project named {project_name}"
        return self.execute(prompt, workdir)

    def build_tests(self, test_requirements: str, workdir: Optional[str] = None) -> Dict[str, Any]:
        """
        Build automated test scripts.

        Args:
            test_requirements: Natural language description of test requirements
            workdir: Working directory

        Returns:
            Execution result
        """
        prompt = f"Build automated test scripts: {test_requirements}"
        return self.execute(prompt, workdir)

    def run_tests(self, workdir: Optional[str] = None) -> Dict[str, Any]:
        """
        Run automated tests.

        Args:
            workdir: Working directory

        Returns:
            Execution result
        """
        prompt = "Run all tests"
        return self.execute(prompt, workdir)


def main():
    """CLI entry point for testing."""
    if len(sys.argv) < 2:
        print("Usage: python3 trae_wrapper.py <prompt> [workdir]")
        sys.exit(1)

    prompt = sys.argv[1]
    workdir = sys.argv[2] if len(sys.argv) > 2 else None

    trae = TraeCLI()
    result = trae.execute(prompt, workdir)

    if result["success"]:
        print("✓ Success")
        print(result["output"])
    else:
        print("✗ Failed")
        print(result["error"])
    sys.exit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
