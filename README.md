# 📥 Instagram Reel Downloader (Python Script)

This is a simple Python script that allows you to **download Instagram Reels using a valid reel URL**. It uses the `instaloader` library to fetch and save reels directly to your local device.

---

## ⚙️ What This Script Does

- Accepts an Instagram reel URL from the user
- Extracts the reel’s shortcode using regular expressions
- Downloads the reel using the `instaloader` package
- Saves the reel in a folder named after the username who posted it

---

## 🔐 Requirements

- `instaloader` Python package  
  Install it with:
  ```bash
  pip install instaloader
  ```

- An **active internet connection**
- A valid **Instagram Reel URL** (public profiles only)

---

## 💻 How To Use

1. Open your terminal or command prompt.
2. Run the script:
   ```bash
   python 5_insta_reel.py
   ```
3. Paste a valid Instagram reel URL when asked.
4. The reel will be downloaded into a folder named like: `username_reel/`

---

## 🧪 Example

```text
📥 Instagram Reel Downloader
Paste Instagram Reel URL: https://www.instagram.com/reel/XYZ123abc/
Downloaded reel from @someuser ✅
```

---

## 🚫 Error Handling

If the URL is incorrect or private:
- The script prints `Invalid Reel URL.` or shows the error reason.

---

## 📦 Technologies Used

- Python 3.x
- `instaloader` package
- `re` (regular expressions)
- Exception handling

---

## 📌 Why I Built This

This project was created to:
- Practice using third-party Python libraries
- Work with regular expressions
- Create a real-world utility tool for social media downloads

---

## 📄 License

MIT License — Free to use, modify, and distribute with credit.

---

## 🙋‍♂️ About Me

Hi, I'm **Ali Zain** — a passionate Python developer who loves building small tools that make daily tech tasks easier.

> “If it’s repetitive, I automate it.”
