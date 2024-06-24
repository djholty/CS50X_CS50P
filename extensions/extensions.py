exten = {"gif":"image/gif",
        "jpg":"image/jpeg",
        "jpeg":"image/jpeg",
        "png":"image/png",
        "pdf":"application/pdf",
        "txt":"text/plain",
        "zip":"application/zip",
}
x = input("File name: ")
x = x.strip().lower()
x = x.split(".")[-1]

print(exten.get(x , "application/octet-stream"))