# Facebook Downloader

A simple free tool to download public Facebook videos and images.

## How it works

- Paste any public Facebook video/image link
- It fetches a direct download link using yt-dlp
- You can download the content directly

## Deployment on Railway

- Backend is a Flask app in `/backend` folder
- Frontend static files are in `/frontend` folder and served by Flask

### How to deploy

1. Push the full repo to GitHub
2. On Railway, create a new project and connect this repo
3. Set the **Root Directory** to `/backend` in Railway project settings
4. Railway will install dependencies from `requirements.txt` and run `app.py`
5. Visit the Railway URL to use the app

## Disclaimer

This tool is for **educational and personal use only**.  
We do **not store or host** any content.  
Use only for media you own or are allowed to download.
