from pathlib import Path
import json
import requests
import argparse

def download_gifs(json_file_path: str, rename_files: bool):
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    gifs = data["_state"]["favorites"]
    failed_urls = []

    for i, gif in enumerate(reversed(gifs)):
        url = gif["src"].strip("/")

        if not url.startswith(("http://", "https://")):
            url = f"http://{url}" 

        file_name = f"{hex(i)[2:]}.{url.rsplit('/', 1)[-1].rsplit('.', 1)[-1]}" if rename_files else url.rsplit("/", 1)[-1]
        path = Path(f"output/{file_name}")
        progress = f"[{i + 1}/{len(gifs)}] {path} "

        print(progress, end="")

        if path.exists():
            print("[already downloaded]")

            continue

        response = requests.get(url)
        content = response.content

        if not (response.ok and content):
            failed_urls.append(f"{progress}- {url}")
            print("❌")

            continue

        with open(path, "wb") as gif_file:
            gif_file.write(content)

        print("✔️")

    if failed_urls:
        with open("failed.txt", "w") as text_file:
            text_file.write("\n".join(failed_urls))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--json-file-path", "-j", type=str, required=True, help="Path to GIFFavoritesStore JSON file")
    parser.add_argument("--rename-files", "-r", type=bool, default=True, help="Whether to rename files to hex strings")

    args = parser.parse_args()

    download_gifs(json_file_path=args.json_file_path, rename_files=args.rename_files)