# discord-fav-gif-dl

Downloads all your favourited GIFs on Discord.

## Usage

- Save your GIFFavoritesStore to a file
    - Open Developer Tools in your browser or Discord's desktop application
    - Navigate to the `Application` tab > `Local Storage` > `https://discord.com` > `GIFFavoritesStore`
        - If using the Discord desktop application, you may need to first enable Developer Tools by adding the following line to your `%APPDATA%/discord/settings.json` file:

            ```json
            "DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING": true
            ```
    - Copy the contents of the `Value` field and save it to a file (e.g. `data.json`)
- Install required packages by running `python -m pip install -r requirements.txt`
- Run the script using `python get_gifs.py --json-file-path <path to GIFFavoritesStore data file>`
    - You can use the `--dont-rename-files` option to download files with their original names, instead of renaming them to hex strings.