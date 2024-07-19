import os
import requests
from tqdm import tqdm
from utils import sanitize_title

class FacebookVideoDownloader:
    def __init__(self, api_url):
        self.api_url = api_url
        self.session = requests.Session()
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        self.download_folder = "Downloads"
        os.makedirs(self.download_folder, exist_ok=True)

    def get_headers(self):
        return {
            "User-Agent": self.user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        }

    def fetch_video_data(self, video_url):
        try:
            response = self.session.get(f"{self.api_url}?url={video_url}", headers=self.get_headers())
            response.raise_for_status()
            video_data = response.json()

            if 'hd' in video_data and video_data['hd']:
                return video_data
            else:
                print("HD video URL not found.")
                return None
        except requests.RequestException as e:
            print(f"Error fetching video data: {e}")
            return None

    def download_video(self, video_url):
        try:
            print(f"Fetching video data from API for URL: {video_url}")
            video_data = self.fetch_video_data(video_url)

            if not video_data:
                print("No HD video URL available.")
                return

            hd_url = video_data.get('hd')
            video_title = video_data.get('title', video_url.split('/')[-1])
            safe_title = sanitize_title(video_title) + '.mp4'
            output_path = os.path.join(self.download_folder, safe_title)

            # Get video content
            print(f"Downloading video from: {hd_url}")
            response = requests.get(hd_url, headers=self.get_headers(), stream=True)
            response.raise_for_status()

            # Save video to file
            total_size = int(response.headers.get('content-length', 0))
            with open(output_path, 'wb') as file, tqdm(
                desc=safe_title,
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
            ) as pbar:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        pbar.update(len(chunk))

            print(f"Video downloaded successfully: {output_path}")

        except requests.RequestException as e:
            print(f"An error occurred while downloading the video: {e}")
