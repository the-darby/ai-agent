import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if valid_target_dir is False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.isdir(target_dir) is False:
            return f'Error: "{directory}" is not a directory'

        result = []
        for filename in os.listdir(target_dir):
            file_path = os.path.join(target_dir, filename)
            filesize = os.path.getsize(file_path)
            isdir = os.path.isdir(file_path)
            result.append(f"- {filename}: file_size={filesize} bytes, is_dir={isdir}")

        return "\n".join(result)
    except Exception as e:
        return f"Error: {e}"

