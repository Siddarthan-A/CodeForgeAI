import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files and directories",
        "parameters": {
            "type": "object",
            "properties": {
                "target_directory": {
                    "type": "string",
                    "description": "Relative path to the directory"
                }
            },
            "required": ["target_directory"]
        }
    }
}

def get_files_info(working_directory: str, target_directory: str = ".") -> str:
    try:
        working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir, target_directory))

        if os.path.commonpath([working_dir, target_dir]) != working_dir:
            return f'Error: Cannot list "{target_directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{target_directory}" is not a directory'

        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            try:
                size = os.path.getsize(filepath)
                is_dir = os.path.isdir(filepath)
                files_info.append(f"- {filename}: file_size={size} bytes, is_dir={is_dir}")
            except Exception as inner_e:
                files_info.append(f"- {filename}: Error: {inner_e}")

        return f'Success: "{target_directory}" is within the working directory\n' + "\n".join(files_info)

    except Exception as e:
        return f'Error: {e}'
