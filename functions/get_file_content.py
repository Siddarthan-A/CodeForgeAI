import os
from config import MAX_CHARS

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the contents of a specified file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Relative path to the file"
                }
            },
            "required": ["file_path"]
        }
    }
}
def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir, file_path))

        if os.path.commonpath([working_dir, target_path]) != working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" is not a valid file'

        with open(target_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read(MAX_CHARS)
            if f.read(1): 
                content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content

    except Exception as e:
        return f'Error: {e}'
