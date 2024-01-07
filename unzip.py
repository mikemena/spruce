import zipfile


def unzip_file(zip_path, extract_to="."):
    """
    Unzip a ZIP file.

    :param zip_path: str, path to the ZIP file
    :param extract_to: str, directory to extract the contents to. Defaults to the current directory.
    """
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)


# Example usage
zip_path = "Project_Day_9.zip"
unzip_path = "project_unzipped"
unzip_file(zip_path, unzip_path)
