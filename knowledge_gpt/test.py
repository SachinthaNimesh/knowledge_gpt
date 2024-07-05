import os
import mimetypes
import io

def get_file_from_local(file_path):
    """
    Retrieves a .txt, .pdf, or .docx file from local storage.

    Args:
    - file_path (str): The path to the file to retrieve.

    Returns:
    - io.BytesIO: Contents of the file as a BytesIO object.
    - str: Filename of the retrieved file.
    - None: If file does not exist or is not supported.
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return None, None

    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type not in ['text/plain', 'application/pdf', 'application/msword',
                         'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        print(f"Error: Unsupported file type for '{file_path}'. Supported types are .txt, .pdf, .docx.")
        return None, None

    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
            filename = os.path.basename(file_path)
            return io.BytesIO(file_content), filename
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return None, None


