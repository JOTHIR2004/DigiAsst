from drive_client import drive_service
from googleapiclient.http import MediaIoBaseDownload
import io


def list_folders(parent_id):
    query = (
        f"'{parent_id}' in parents "
        "and mimeType='application/vnd.google-apps.folder' "
        "and trashed=false"
    )
    res = drive_service.files().list(
        q=query,
        fields="files(id, name)"
    ).execute()
    return res.get("files", [])


def list_pdfs(parent_id):
    query = (
        f"'{parent_id}' in parents "
        "and mimeType='application/pdf' "
        "and trashed=false"
    )
    res = drive_service.files().list(
        q=query,
        fields="files(id, name)"
    ).execute()
    return res.get("files", [])


def download_pdf(file_id, file_name):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.FileIO(file_name, "wb")
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        _, done = downloader.next_chunk()

    return file_name
