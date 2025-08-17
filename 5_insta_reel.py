import instaloader
import re

def download_reel_from_url(url):
    
    #Extract shortcode from the URL
    shortcode_match = re.search(r'/reel/([^/]+)/', url)
    
    if not shortcode_match:
        print("Invalid Reel URL.")
        return
    shortcode = shortcode_match.group(1)
    loader = instaloader.Instaloader()

    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=f"{post.owner_username}_reel")
        print(f"Downloaded reel from @{post.owner_username}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Instagram Reel Downloader")
    reel_url = input("Paste Instagram Reel URL: ").strip()
    download_reel_from_url(reel_url)
