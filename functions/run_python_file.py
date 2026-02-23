import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_path = os.path.commonpath([working_dir_abs, absolute_file_path]) == working_dir_abs

        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", absolute_file_path]

        if args is not None:
            command.extend(args)

        result = subprocess.run(
                command,
                cwd=working_dir_abs,
                capture_output=True,
                text=True,
                timeout=30
            )

        lines = []

        if result.returncode != 0:
            lines.append(f"Process exited with code {result.returncode}")

        stdout = (result.stdout or "").strip()
        stderr = (result.stderr or "").strip()

        if not stdout and not stderr:
            lines.append("No output produced")
        else:
            if stdout:
                lines.append(f"STDOUT: {stdout}")
            if stderr:
                lines.append(f"STDERR: {stderr}")

        return "\n".join(lines)

    except Exception as e:
        return f"Error: executing Python file: {e}"




