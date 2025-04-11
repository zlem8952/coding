import os

def delete_files(folder_path, extensions_to_delete):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions_to_delete):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    folder_path = input("삭제할 파일이 있는 폴더 경로를 입력하세요: ")
    extensions = input("삭제할 파일 확장자를 쉼표로 구분하여 입력하세요 (예: .xlsx,.pptx,.hwp,.pdf,.zip): ").split(',')
    if os.path.exists(folder_path):
        delete_files(folder_path, extensions)
    else:
        print("입력한 경로가 존재하지 않습니다.")
