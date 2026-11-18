# 👗 Blush Boutique — Clothing Store (Streamlit)

A clothing store app with a pink boutique theme. The page changes colour depending on which of the 5 tabs is open:

| Tab | Mood |
|---|---|
| Home | Blush, soft and light |
| Shop | Rose, warm pink |
| Cart | Coral, bright |
| Orders | Crimson, bold |
| Account | Wine, dark mode |

Palette: `#fce5e5` `#f7c2c2` `#ff7474` `#c64242` `#541616`

## Files

```
your-repo/
├── app.py                 ← the whole app, with all styling inside
├── requirements.txt       ← tells Streamlit Cloud what to install
├── README.md
└── .streamlit/
    └── config.toml        ← base theme colours (must be in this folder)
```

## Uploading to GitHub (important)

`config.toml` **must** sit inside a folder named `.streamlit` (with the dot). If it ends up at the top level of the repo, Streamlit ignores it.

Easiest way:
1. On your repo page, click **Add file → Upload files** and upload `app.py`, `requirements.txt` and `README.md`. Click **Commit**.
2. Click **Add file → Create new file**.
3. In the name box, type `.streamlit/config.toml`. Typing the `/` creates the folder.
4. Open `config.toml` from the download, copy everything in it, paste it into the editor and click **Commit**.

## Deploying on Streamlit Cloud

1. Go to share.streamlit.io → **Create app** → pick this repo.
2. Set **Main file path** to `app.py`.
3. Deploy. If the app was already deployed, open **⋮ → Reboot app** so it picks up the new config.

## Running on your computer

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Adding your own products

Edit the `PRODUCTS` list in `app.py`. To show a real photo, put an image link in `"image"`; if you leave it empty, the card shows the emoji instead.
