# Facebook Video Downloader

A simple and efficient tool for downloading Facebook videos using a custom API. This application fetches the video data from the API and downloads the HD version of the video, saving it with a sanitized filename.

## Features

- Download Facebook videos in HD quality.
- Automatic filename sanitization.
- Efficient download with progress tracking.

## Requirements

- Python 3.x
- `requests` library
- `tqdm` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/JohnDev19/facebook-video-downloader.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd facebook-video-downloader
    ```

3. **Install the required Python packages:**

    ```bash
    pip install requests tqdm
    ```

## Usage

1. **Run the application:**

    ```bash
    python main.py
    ```

2. **Enter the Facebook video URL when prompted.**

    The video will be downloaded to the `Downloads` folder with a sanitized filename.

## Code Structure

- `main.py`: Entry point for the application.
- `facebook_video_downloader.py`: Contains the core functionality for downloading videos.
- `config.py`: Contains configuration and constants.
- `utils.py`: Contains utility functions for the project.

## Example

```bash
Enter the Facebook video URL: https://www.facebook.com/yourvideoid
Fetching video data from API for URL: https://www.facebook.com/yourvideoid
Downloading video from: https://video-sea1-1.xx.fbcdn.net/yourvideo.mp4
Video downloaded successfully: Downloads/Your_Video_Title.mp4
```

## Notes

- Ensure that the `Downloads` folder is writable.
- The video filename will be sanitized to avoid invalid characters.
- For large videos, download times may vary based on network speed.

## Contributing

Feel free to fork the repository and submit pull requests. For bug reports or feature requests, open an issue on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
