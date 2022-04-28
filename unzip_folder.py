import zipfile
with zipfile.ZipFile("Archive.zip","r") as zip_ref:
    zip_ref.extractall("")
