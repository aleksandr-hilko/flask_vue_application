from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def upload_to_google_drive(filepath, filename, mimetype):
    settings_path = "settings.yaml"
    gauth = GoogleAuth(settings_file=settings_path)
    drive = GoogleDrive(gauth)
    file_list = drive.ListFile({"q": "'root' in parents"}).GetList()
    try:
        for file_ in file_list:
            if file_["title"] == filename:
                file_.Delete()
    except:
        pass
    drive_file = drive.CreateFile({"title": filename, "mimeType": mimetype})
    drive_file.SetContentFile(filepath)
    drive_file.Upload()
    drive_file.InsertPermission({"type": "anyone", "value": "anyone", "role": "reader"})
    return drive_file
