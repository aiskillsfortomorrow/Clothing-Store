"""
Blush Boutique — clothing store app (Streamlit).
Run locally:  streamlit run app.py
All styling is inside this file, so it works even without extra files.
The 5 tabs each change the page colour mood when selected.
"""

import streamlit as st

PALETTE = {
    "blush": "#fce5e5",
    "rose": "#f7c2c2",
    "coral": "#ff7474",
    "crimson": "#c64242",
    "wine": "#541616",
}

# One colour mood per tab: page background, accent, second accent, text, card, hero gradient
TAB_MOODS = [
    # 1 Blush
    dict(bg="linear-gradient(180deg,#fffafa 0%,#fce5e5 100%)", accent="#ff7474", accent2="#c64242",
         text="#541616", muted="#8a4a4a", card="#ffffff", line="#f7c2c2",
         hero="linear-gradient(120deg,#fce5e5 0%,#f7c2c2 100%)", hero_text="#541616"),
    # 2 Rose
    dict(bg="linear-gradient(180deg,#fce5e5 0%,#f7c2c2 100%)", accent="#c64242", accent2="#ff7474",
         text="#541616", muted="#7a3a3a", card="#fffafa", line="#eeaaaa",
         hero="linear-gradient(120deg,#f7c2c2 0%,#ff7474 100%)", hero_text="#541616"),
    # 3 Coral
    dict(bg="linear-gradient(160deg,#fff4f4 0%,#ffd9d9 100%)", accent="#ff7474", accent2="#c64242",
         text="#541616", muted="#8a4a4a", card="#ffffff", line="#ffb3b3",
         hero="linear-gradient(120deg,#ff7474 0%,#c64242 100%)", hero_text="#ffffff"),
    # 4 Crimson
    dict(bg="linear-gradient(180deg,#fffafa 0%,#f7c2c2 100%)", accent="#c64242", accent2="#541616",
         text="#541616", muted="#7a3a3a", card="#ffffff", line="#e8a0a0",
         hero="linear-gradient(120deg,#c64242 0%,#541616 100%)", hero_text="#fce5e5"),
    # 5 Wine (dark mode)
    dict(bg="linear-gradient(180deg,#541616 0%,#2e0b0b 100%)", accent="#ff7474", accent2="#f7c2c2",
         text="#fce5e5", muted="#f7c2c2", card="#6b2424", line="#7a2e2e",
         hero="linear-gradient(120deg,#ff7474 0%,#c64242 100%)", hero_text="#ffffff"),
]


def _mood_vars(m: dict) -> str:
    return (
        f"--bg:{m['bg']};--accent:{m['accent']};--accent2:{m['accent2']};"
        f"--text:{m['text']};--muted:{m['muted']};--card:{m['card']};--line:{m['line']};"
        f"--hero:{m['hero']};--hero-text:{m['hero_text']};"
    )


def apply_theme() -> None:
    """Inject the boutique CSS. Call once, right after st.set_page_config()."""
    # Default mood = tab 1; each selected tab swaps the variables on the whole app.
    per_tab = "\n".join(
        f'.stApp:has(.stTabs [role="tab"]:nth-child({i + 1})[aria-selected="true"])'
        f"{{{_mood_vars(m)}}}"
        for i, m in enumerate(TAB_MOODS)
    )
    # Each tab label is tinted with its own colour, even when not selected
    tab_label_colors = "\n".join(
        f'.stTabs [role="tab"]:nth-child({i + 1})::before{{background:{m["accent"] if i != 4 else "#541616"};}}'
        for i, m in enumerate(TAB_MOODS)
    )

    st.markdown(
        f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Poppins:wght@300;400;500;600&display=swap');

.stApp {{ {_mood_vars(TAB_MOODS[0])} }}
{per_tab}

/* ---------- Page ---------- */
.stApp {{
    background: var(--bg);
    background-attachment: fixed;
    transition: background .5s ease;
}}
.stApp, .stApp p, .stApp li, .stApp label, .stApp span,
.stApp [data-testid="stMarkdownContainer"],
.stApp [data-testid="stWidgetLabel"] p {{
    font-family: 'Poppins', sans-serif;
    color: var(--text);
}}
.stApp h1, .stApp h2, .stApp h3, .stApp h4 {{
    font-family: 'Playfair Display', serif !important;
    color: var(--text) !important;
    letter-spacing: .3px;
}}
.stApp [data-testid="stCaptionContainer"], .stApp small {{ color: var(--muted) !important; }}
header[data-testid="stHeader"] {{ background: transparent; }}
.block-container {{ padding-top: 2rem; max-width: 1200px; }}

/* ---------- Tabs: pill navigation ---------- */
.stTabs [role="tablist"] {{
    gap: .5rem;
    background: rgba(255,255,255,.55);
    backdrop-filter: blur(8px);
    padding: .45rem;
    border-radius: 999px;
    border: 1px solid var(--line);
    box-shadow: 0 6px 20px rgba(84,22,22,.08);
    justify-content: center;
    flex-wrap: wrap;
}}
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"],
.stTabs .react-aria-SelectionIndicator {{ display: none !important; }}
.stTabs [role="tab"] {{
    height: auto;
    padding: .55rem 1.3rem;
    border-radius: 999px;
    background: transparent;
    border: none;
    transition: all .25s ease;
    gap: .5rem;
    display: flex; align-items: center; cursor: pointer;
}}
.stTabs [role="tab"]::before {{
    content: "";
    width: 10px; height: 10px;
    border-radius: 50%;
    display: inline-block;
    margin-right: .45rem;
    box-shadow: 0 0 0 2px rgba(255,255,255,.8);
}}
{tab_label_colors}
.stTabs [role="tab"] p {{
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    font-size: .95rem;
    color: #541616 !important;
}}
.stTabs [role="tab"]:hover {{ background: rgba(247,194,194,.55); transform: translateY(-1px); }}
.stTabs [role="tab"][aria-selected="true"] {{
    background: var(--accent);
    box-shadow: 0 6px 16px rgba(198,66,66,.35);
}}
.stTabs [role="tab"][aria-selected="true"] p {{ color: #ffffff !important; }}
.stTabs [role="tab"][aria-selected="true"]::before {{ background: #ffffff !important; }}
.stTabs [role="tabpanel"] {{ padding-top: 1.5rem; animation: fadeUp .45s ease; }}
@keyframes fadeUp {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: none; }} }}

/* ---------- Buttons ---------- */
.stButton > button, .stDownloadButton > button, .stFormSubmitButton > button {{
    background: var(--accent);
    color: #ffffff;
    border: none;
    border-radius: 999px;
    padding: .55rem 1.4rem;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    box-shadow: 0 4px 12px rgba(198,66,66,.25);
    transition: all .2s ease;
}}
.stButton > button p, .stDownloadButton > button p, .stFormSubmitButton > button p {{ color: #ffffff !important; }}
.stButton > button:hover, .stDownloadButton > button:hover, .stFormSubmitButton > button:hover {{
    background: var(--accent2);
    color: #ffffff;
    transform: translateY(-2px);
    box-shadow: 0 8px 18px rgba(84,22,22,.3);
}}
.stButton > button:focus:not(:active) {{ color: #ffffff; border: none; }}

/* ---------- Inputs ---------- */
.stTextInput input, .stNumberInput input, .stTextArea textarea,
[data-baseweb="select"] > div {{
    border-radius: 12px !important;
    background: #ffffff !important;
    color: #541616 !important;
}}

/* ---------- Containers, metrics, expanders, forms ---------- */
[data-testid="stVerticalBlockBorderWrapper"]:has(> div > [data-testid="stVerticalBlock"]) {{
    border-radius: 18px;
}}
[data-testid="stMetric"], [data-testid="stExpander"], [data-testid="stForm"] {{
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 1rem 1.2rem;
    box-shadow: 0 6px 18px rgba(84,22,22,.07);
}}
[data-testid="stMetricValue"] {{ font-family: 'Playfair Display', serif; color: var(--accent2); }}
[data-testid="stImage"] img {{ border-radius: 14px; }}
[data-testid="stDataFrame"] {{ border-radius: 14px; overflow: hidden; border: 1px solid var(--line); }}
hr {{ border-color: var(--line) !important; }}
[data-testid="stAlert"] > div {{
    background: var(--card) !important;
    border: 1px solid var(--line);
    border-left: 5px solid var(--accent);
    border-radius: 14px;
}}
[data-testid="stAlert"] p {{ color: var(--text) !important; }}
[data-testid="stProgress"] > div > div > div > div {{ background: var(--accent) !important; }}

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg,#541616 0%,#3a0f0f 100%);
}}
[data-testid="stSidebar"] *, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label,
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
    color: #fce5e5 !important;
}}

/* ---------- Custom components ---------- */
.hero {{
    background: var(--hero);
    color: var(--hero-text);
    border-radius: 24px;
    padding: 2.4rem 2.6rem;
    margin-bottom: 1.6rem;
    box-shadow: 0 14px 34px rgba(84,22,22,.18);
    position: relative;
    overflow: hidden;
}}
.hero::after {{
    content: "";
    position: absolute; right: -60px; top: -60px;
    width: 220px; height: 220px; border-radius: 50%;
    background: rgba(255,255,255,.18);
}}
.stApp .hero h1, .stApp .hero h1 *, .stApp .hero p {{ color: var(--hero-text) !important; }}
.stApp .hero h1 {{ margin: 0 0 .4rem 0; font-size: 2.4rem; }}
.stApp .hero p {{ color: var(--hero-text) !important; opacity: .9; margin: 0; font-size: 1.05rem; }}

.pcard {{
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 6px 18px rgba(84,22,22,.08);
    transition: transform .25s ease, box-shadow .25s ease;
    margin-bottom: 1rem;
}}
.pcard:hover {{ transform: translateY(-5px); box-shadow: 0 14px 30px rgba(84,22,22,.16); }}
.pcard img {{ width: 100%; height: 240px; object-fit: cover; display: block; }}
.pcard .ph {{ height: 240px; display: flex; align-items: center; justify-content: center;
             font-size: 4rem; background: linear-gradient(135deg,#fce5e5,#f7c2c2); }}
.pcard .body {{ padding: .9rem 1.1rem 1.1rem; }}
.pcard .name {{ font-family: 'Playfair Display', serif; font-size: 1.1rem; color: var(--text); margin: 0; }}
.pcard .cat  {{ font-size: .8rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }}
.pcard .row  {{ display: flex; justify-content: space-between; align-items: center; margin-top: .5rem; }}
.pcard .price {{ font-weight: 600; color: var(--accent2); font-size: 1.1rem; }}
.pcard .tag {{ background: var(--accent); color: #fff; font-size: .72rem; padding: .2rem .65rem; border-radius: 999px; }}
</style>
""",
        unsafe_allow_html=True,
    )



from html import escape


def hero(title: str, subtitle: str = "") -> None:
    st.markdown(f'<div class="hero"><h1>{escape(title)}</h1><p>{escape(subtitle)}</p></div>',
                unsafe_allow_html=True)


def product_card(p: dict) -> None:
    media = (f'<img src="{escape(p["image"])}" alt="{escape(p["name"])}">' if p.get("image")
             else f'<div class="ph">{p["emoji"]}</div>')
    tag = f'<span class="tag">{escape(p["tag"])}</span>' if p.get("tag") else ""
    st.markdown(
        f'<div class="pcard">{media}<div class="body"><div class="cat">{escape(p["category"])}</div>'
        f'<p class="name">{escape(p["name"])}</p><div class="row"><span class="price">'
        f'Rs {p["price"]:,}</span>{tag}</div></div></div>',
        unsafe_allow_html=True,
    )


# =====================================================================
#  STORE DATA  — edit this list with your own products.
#  "image" can be a URL to a product photo; leave "" to show the emoji.
# =====================================================================
PRODUCTS = [
    {"id": 1, "name": "Rose Wrap Dress", "category": "Dresses", "price": 4500, "tag": "New", "emoji": "👗", "image": ""},
    {"id": 2, "name": "Silk Blouse", "category": "Tops", "price": 2800, "tag": "Hot", "emoji": "👚", "image": ""},
    {"id": 3, "name": "Wide-Leg Trousers", "category": "Bottoms", "price": 3200, "tag": "", "emoji": "👖", "image": ""},
    {"id": 4, "name": "Leather Tote", "category": "Accessories", "price": 5900, "tag": "Sale", "emoji": "👜", "image": ""},
    {"id": 5, "name": "Floral Maxi Dress", "category": "Dresses", "price": 5200, "tag": "", "emoji": "👗", "image": ""},
    {"id": 6, "name": "Knit Cardigan", "category": "Tops", "price": 3600, "tag": "New", "emoji": "🧥", "image": ""},
    {"id": 7, "name": "Pleated Skirt", "category": "Bottoms", "price": 2900, "tag": "", "emoji": "👗", "image": ""},
    {"id": 8, "name": "Pearl Earrings", "category": "Accessories", "price": 1800, "tag": "Hot", "emoji": "💎", "image": ""},
    {"id": 9, "name": "Block Heels", "category": "Shoes", "price": 4200, "tag": "", "emoji": "👠", "image": ""},
]
BY_ID = {p["id"]: p for p in PRODUCTS}
SHIPPING = 250

# =====================================================================
#  APP
# =====================================================================
st.set_page_config(page_title="Blush Boutique", page_icon="👗", layout="wide")
apply_theme()

ss = st.session_state
ss.setdefault("cart", {})        # product id -> quantity
ss.setdefault("orders", [])
ss.setdefault("profile", {"name": "", "email": "", "phone": "", "address": ""})


def add_to_cart(pid: int) -> None:
    ss.cart[pid] = ss.cart.get(pid, 0) + 1
    st.toast(f"Added {BY_ID[pid]['name']} to cart 🛍️")


def cart_total() -> int:
    return sum(BY_ID[pid]["price"] * q for pid, q in ss.cart.items())


# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("## 👗 Blush Boutique")
    st.caption("Style that speaks for you")
    st.divider()
    categories = ["All"] + sorted({p["category"] for p in PRODUCTS})
    cat = st.selectbox("Category", categories)
    lo, hi = st.slider("Price range (Rs)", 0, 10000, (0, 10000), step=100)
    st.divider()
    items_in_cart = sum(ss.cart.values())
    st.markdown(f"🛒 **{items_in_cart}** item(s) in cart")
    st.markdown(f"💳 Rs **{cart_total():,}**")

home, shop, cart, orders, account = st.tabs(["Home", "Shop", "Cart", "Orders", "Account"])

# ---------- 1. Home ----------
with home:
    hero("New Season Arrivals", "Fresh pinks, soft fabrics and statement pieces, just in.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Products", len(PRODUCTS))
    c2.metric("Categories", len(categories) - 1)
    c3.metric("Free delivery over", "Rs 5,000")
    st.subheader("Trending now")
    trending = [p for p in PRODUCTS if p["tag"]][:4]
    for col, p in zip(st.columns(4), trending):
        with col:
            product_card(p)
            st.button("Add to cart", key=f"home_{p['id']}", on_click=add_to_cart,
                      args=(p["id"],), width="stretch")

# ---------- 2. Shop ----------
with shop:
    hero("Shop the Collection", "Use the sidebar to filter by category and price.")
    query = st.text_input("Search products", placeholder="e.g. dress, silk, tote")
    results = [
        p for p in PRODUCTS
        if (cat == "All" or p["category"] == cat)
        and lo <= p["price"] <= hi
        and query.lower() in p["name"].lower()
    ]
    st.caption(f"{len(results)} product(s) found")
    if not results:
        st.info("No products match your filters. Try widening the price range.")
    cols = st.columns(3)
    for i, p in enumerate(results):
        with cols[i % 3]:
            product_card(p)
            st.button("Add to cart", key=f"shop_{p['id']}", on_click=add_to_cart,
                      args=(p["id"],), width="stretch")

# ---------- 3. Cart ----------
with cart:
    hero("Your Cart", "Review your picks before checkout.")
    if not ss.cart:
        st.info("Your cart is empty. Head to the Shop tab to add something lovely.")
    else:
        for pid, qty in list(ss.cart.items()):
            p = BY_ID[pid]
            with st.container(border=True):
                a, b, c, d = st.columns([0.6, 3, 1.4, 1])
                a.markdown(f"<div style='font-size:2.2rem'>{p['emoji']}</div>", unsafe_allow_html=True)
                b.markdown(f"**{p['name']}**  \n{p['category']} · Rs {p['price']:,}")
                new_q = c.number_input("Qty", 1, 20, qty, key=f"qty_{pid}")
                if new_q != qty:
                    ss.cart[pid] = new_q
                    st.rerun()
                if d.button("Remove", key=f"rm_{pid}"):
                    del ss.cart[pid]
                    st.rerun()
        subtotal = cart_total()
        ship = 0 if subtotal >= 5000 else SHIPPING
        m1, m2, m3 = st.columns(3)
        m1.metric("Subtotal", f"Rs {subtotal:,}")
        m2.metric("Delivery", "Free" if ship == 0 else f"Rs {ship:,}")
        m3.metric("Total", f"Rs {subtotal + ship:,}")
        if st.button("Place order", type="primary"):
            if not ss.profile["name"] or not ss.profile["address"]:
                st.warning("Please add your name and delivery address in the Account tab first.")
            else:
                ss.orders.insert(0, {
                    "no": 1000 + len(ss.orders) + 1,
                    "items": {BY_ID[i]["name"]: q for i, q in ss.cart.items()},
                    "total": subtotal + ship,
                    "status": "Processing",
                })
                ss.cart = {}
                st.success("Order placed! You can track it in the Orders tab. 💕")
                st.balloons()

# ---------- 4. Orders ----------
with orders:
    hero("Your Orders", "Track deliveries and past purchases.")
    if not ss.orders:
        st.info("No orders yet. Your placed orders will show up here.")
    for o in ss.orders:
        with st.expander(f"Order #{o['no']} · {o['status']} · Rs {o['total']:,}", expanded=True):
            for name, q in o["items"].items():
                st.write(f"• {name} × {q}")
            st.progress(25, text="Processing → Shipped → Delivered")

# ---------- 5. Account ----------
with account:
    hero("My Account", "Manage your profile and delivery details.")
    with st.form("profile_form"):
        c1, c2 = st.columns(2)
        name = c1.text_input("Full name", ss.profile["name"])
        email = c2.text_input("Email", ss.profile["email"])
        phone = st.text_input("Phone", ss.profile["phone"])
        address = st.text_area("Delivery address", ss.profile["address"])
        if st.form_submit_button("Save changes"):
            ss.profile = {"name": name, "email": email, "phone": phone, "address": address}
            st.success("Profile saved ✨")
