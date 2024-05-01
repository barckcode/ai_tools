# Steps to use any of scripts in this folder
1. Create a virtual environment using the following command:
```bash
python -m venv .venv
```

2. Activate the virtual environment using the following command:
```bash
source .venv/bin/activate
```

3. Install the required libraries using the following command:
```bash
pip install -r requirements.txt
```

4. Export the required environment variables using the following command:
```bash
export REPLICATE_API_TOKEN=<paste-your-token-here>
```

5. Run the script using the following command:
```bash
python <script_name>.py
```


## Extra
For `youtube_transcription.py`, you need to install ffmpeg using the following command:

- Linux:
```bash
sudo apt-get install ffmpeg
```

- MacOs:
```bash
brew install ffmpeg
```
