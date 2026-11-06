def main() -> None:
    filename = input("File name: ").strip().lower()
    filetype = get_filetype(filename)
    print(filetype)


def get_filetype(filename: str) -> str:
    filetype = "application/octet-stream"  # Default

    if filename.endswith(".gif"):
        filetype = "image/gif"
    elif filename.endswith(".jpeg") or filename.endswith(".jpg"):
        filetype = "image/jpeg"
    elif filename.endswith(".png"):
        filetype = "image/png"
    elif filename.endswith(".pdf"):
        filetype = "application/pdf"
    elif filename.endswith(".txt"):
        filetype = "text/plain"
    elif filename.endswith(".zip"):
        filetype = "application/zip"

    return filetype


if __name__ == "__main__":
    main()
