def main():
    filename = input("File name: ")
    filename = filename.strip().lower()
    file_type = get_type(filename)
    print(file_type)


def get_type(filename):
    file_type = "application/octet-stream" # Default.
    if filename.endswith(".gif"):
        file_type = "image/gif"
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        file_type = "image/jpeg"
    elif filename.endswith(".png"):
        file_type = "image/png"
    elif filename.endswith(".pdf"):
        file_type = "application/pdf"
    elif filename.endswith(".txt"):
        file_type = "text/plain"
    elif filename.endswith(".zip"):
        file_type = "application/zip"
    return file_type


if __name__ == "__main__":
    main()
