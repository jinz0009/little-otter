import streamlit as st
import base64
from pathlib import Path

# --- 1. 页面配置 ---
st.set_page_config(
    page_title="little otter | 灵石手作",
    page_icon="🦦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --- 2. 工具函数 ---
def image_to_data_uri(image_path):
    image_path = Path(image_path)

    if not image_path.exists():
        return None

    suffix = image_path.suffix.lower()

    mime_map = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp"
    }

    mime_type = mime_map.get(suffix, "image/jpeg")
    encoded = base64.b64encode(image_path.read_bytes()).decode()

    return f"data:{mime_type};base64,{encoded}"


def get_query_param_value(name):
    try:
        value = st.query_params.get(name)
        if isinstance(value, list):
            return value[0] if value else None
        return value
    except Exception:
        params = st.experimental_get_query_params()
        value = params.get(name, [None])
        return value[0] if value else None


def missing_box(file_name, height="260px"):
    return (
        f'<div class="missing-box" style="height:{height};">'
        f'未找到 {file_name}'
        '</div>'
    )


def safe_rerun():
    try:
        st.rerun()
    except Exception:
        st.experimental_rerun()


# --- 3. 隐藏 Streamlit 原生顶部 / GitHub / Deploy / Hosted Badge ---
st.markdown(
"""
<style>
#MainMenu,
footer,
header,
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="manage-app-button"],
[data-testid="stHeaderActionElements"],
.stDeployButton,
.stActionButton,
.css-1jc7ptx,
.e1ewe7hr3,
.viewerBadge_container__1QSob,
.styles_viewerBadge__1yB5_,
.viewerBadge_link__1S137,
.viewerBadge_text__1JaDK,
div[class*="viewerBadge"],
div[class*="ViewerBadge"],
section[class*="viewerBadge"],
section[class*="ViewerBadge"],
a[class*="viewerBadge"],
a[class*="ViewerBadge"],
div[class*="hosted"],
div[class*="Hosted"],
a[href*="github.com"],
a[href*="streamlit.io"],
a[href*="share.streamlit.io"],
a[href*="streamlit.app"],
button[title*="GitHub"],
button[aria-label*="GitHub"],
a[title*="GitHub"],
a[aria-label*="GitHub"] {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    height: 0 !important;
    max-height: 0 !important;
    min-height: 0 !important;
    pointer-events: none !important;
    overflow: hidden !important;
}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
}

@media (max-width: 768px) {
    .block-container {
        padding-bottom: 1rem !important;
    }
}
</style>
""",
    unsafe_allow_html=True
)

# --- 3.1 手机端底部 Streamlit Badge 遮罩兜底 ---
st.markdown(
"""
<div class="bottom-badge-cover"></div>

<style>
.bottom-badge-cover {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    height: 78px;
    background: #FDFCFB;
    z-index: 2147483647;
    pointer-events: none;
}

@media (min-width: 769px) {
    .bottom-badge-cover {
        height: 0px;
        display: none;
    }
}
</style>
""",
    unsafe_allow_html=True
)

# --- 4. 全局统一风格 CSS ---
st.markdown(
"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Montserrat:wght@300;400;500;600;700&display=swap');

:root {
    --bg: #FDFCFB;
    --bg-soft: #F8F7F5;
    --card: #FFFFFF;
    --text: #333333;
    --muted: #777777;
    --line: #EAE7E2;
    --accent: #A68B67;
    --accent-soft: #EFE7DC;
    --dark: #2F2F2F;
}

.stApp,
[data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
}

html, body, [data-testid="stWidgetLabel"], .stMarkdown p {
    font-family: 'Montserrat', sans-serif !important;
    color: var(--text);
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    font-weight: 400 !important;
    letter-spacing: 3px !important;
    text-transform: lowercase;
    color: var(--text) !important;
}

.section-title {
    text-align: center;
    padding: 34px 0 14px 0;
    color: var(--text);
    letter-spacing: 4px;
    font-family: 'Playfair Display', serif;
    font-size: 34px;
    text-transform: lowercase;
}

.section-subtitle {
    text-align: center;
    color: var(--muted);
    font-size: 13px;
    letter-spacing: 1.5px;
    margin-bottom: 42px;
}

.missing-box {
    width: 100%;
    border: 1px solid #DDD;
    color: #999;
    background: #FAFAFA;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
}

/* 顶部品牌导航 */
.site-header {
    width: 100%;
    margin: 0 auto 38px auto;
    padding-top: 18px;
}

.brand-area {
    text-align: center;
    padding: 16px 0 12px 0;
}

.brand-title {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    letter-spacing: 6px;
    color: #5D5B57;
    line-height: 1.1;
}

.brand-subtitle {
    margin-top: 8px;
    font-size: 10px;
    letter-spacing: 3px;
    color: #8B867E;
    text-transform: uppercase;
}

.top-nav {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
    padding: 12px 10px;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    background: rgba(253, 252, 251, 0.96);
}

.top-nav a {
    text-decoration: none !important;
    color: var(--text) !important;
    font-size: 13px;
    letter-spacing: 1px;
    padding: 10px 16px;
    border: 1px solid transparent;
    transition: 0.25s ease;
    text-transform: uppercase;
}

.top-nav a:hover {
    border-color: var(--accent);
    background: var(--accent-soft);
}

.top-nav a.active {
    border-color: var(--accent);
    background: var(--accent-soft);
    color: #5F4F3B !important;
}

/* Streamlit 按钮统一 */
div.stButton > button {
    border-radius: 0px !important;
    border: 1px solid var(--text) !important;
    background-color: transparent !important;
    color: var(--text) !important;
    padding: 11px 18px !important;
    text-transform: none;
    font-size: 12px !important;
    letter-spacing: 0.5px;
    transition: 0.25s;
    width: 100%;
    min-height: 42px;
}

div.stButton > button:hover {
    background-color: var(--text) !important;
    color: white !important;
}

div.stButton > button p {
    white-space: pre-line !important;
    line-height: 1.35 !important;
}

/* Home */
.logo-wrap {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 28px 0 18px 0;
}

.logo-img {
    width: 520px;
    max-width: 90%;
    display: block;
}

.story-card {
    max-width: 820px;
    margin: 0 auto;
    text-align: center;
    line-height: 1.85;
    color: #555555;
    font-size: 15px;
    padding: 28px 20px 18px 20px;
}

.showcase-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 22px;
    margin: 20px 0 60px 0;
}

.showcase-grid img {
    width: 100%;
    height: 310px;
    object-fit: cover;
    border: 1px solid var(--line);
    background: white;
}

/* Collections */
.collection-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 42px 28px;
    margin-bottom: 70px;
}

.collection-card {
    text-align: center;
    background: transparent;
}

.collection-card img {
    width: 100%;
    height: 350px;
    object-fit: cover;
    display: block;
    transition: 0.25s ease;
    border: 1px solid var(--line);
    background: white;
}

.collection-card img:hover {
    transform: scale(1.015);
    opacity: 0.92;
}

.collection-price {
    color: var(--text);
    font-size: 1.25rem;
    font-weight: 600;
    margin: 18px 0 12px 0;
    letter-spacing: 1px;
}

.collection-button {
    display: inline-block;
    width: 86%;
    background: #FFFFFF;
    color: var(--text) !important;
    border: 1px solid var(--text);
    padding: 14px 0;
    text-decoration: none !important;
    letter-spacing: 3px;
    font-size: 0.82rem;
    text-transform: uppercase;
    transition: 0.25s ease;
}

.collection-button:hover {
    background: var(--text);
    color: #FFFFFF !important;
}

.back-link {
    display: inline-block;
    color: var(--text) !important;
    text-decoration: none !important;
    border: 1px solid var(--text);
    padding: 10px 24px;
    letter-spacing: 2px;
    margin-bottom: 30px;
    transition: 0.25s ease;
}

.back-link:hover {
    background: var(--text);
    color: #FFFFFF !important;
}

.detail-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 28px;
    margin-bottom: 70px;
}

.detail-image {
    width: 100%;
    max-height: 680px;
    object-fit: contain;
    background: var(--bg);
    display: block;
    border: 1px solid var(--line);
}

/* DIY */
.diy-bracelet-container {
    display: flex;
    flex-wrap: nowrap;
    justify-content: center;
    align-items: center;
    gap: 3px;
    padding: 78px 20px;
    background-color: #F4F2EE;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    margin: 28px 0 38px 0;
    position: relative;
    overflow-x: auto;
}

.diy-bracelet-container::after {
    content: '';
    position: absolute;
    width: 85%;
    height: 1px;
    background-color: #D1D1D1;
    z-index: 0;
}

.bead-circle {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    z-index: 1;
    box-shadow: inset -4px -4px 12px rgba(0,0,0,0.2), 2px 4px 6px rgba(0,0,0,0.1);
}

.bead-spacer {
    width: 12px;
    height: 38px;
    border-radius: 3px;
    z-index: 1;
    box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
}

.estimate-box {
    border: 1px solid var(--line);
    background: white;
    padding: 22px;
    text-align: center;
}

.estimate-price {
    color: var(--accent);
    font-size: 30px;
    font-weight: 600;
    letter-spacing: 1px;
    margin-top: 8px;
}

/* About */
.about-container {
    min-height: 720px;
    background: var(--bg);
    padding: 16px 20px 80px 20px;
}

.packaging-section {
    display: grid;
    grid-template-columns: 1fr 1.45fr 1.2fr;
    gap: 50px;
    align-items: center;
    margin: 40px 0 100px 0;
}

.packaging-left-title {
    font-size: 22px;
    color: var(--text);
    letter-spacing: 1px;
    line-height: 1.7;
}

.packaging-content {
    color: var(--text);
}

.packaging-content ul {
    margin: 0;
    padding-left: 22px;
}

.packaging-content li {
    font-size: 18px;
    line-height: 1.65;
    margin-bottom: 4px;
}

.packaging-cn {
    color: var(--muted);
    font-size: 15px;
    margin-left: 6px;
}

.about-package-img {
    width: 100%;
    max-width: 420px;
    height: auto;
    object-fit: cover;
    border: 1px solid var(--line);
    background: white;
}

.about-image-wrap {
    display: flex;
    justify-content: center;
}

.contact-row {
    display: flex;
    justify-content: space-around;
    align-items: flex-start;
    gap: 80px;
    margin-top: 60px;
}

.contact-item {
    text-align: center;
}

.contact-item img {
    width: 150px;
    height: 150px;
    object-fit: contain;
    background: #FFFFFF;
    border: 1px solid var(--line);
}

.contact-label {
    color: var(--text);
    font-size: 18px;
    font-weight: 600;
    letter-spacing: 2px;
    margin-top: 18px;
}

.contact-sub-label {
    color: var(--muted);
    font-size: 14px;
    margin-top: 6px;
    letter-spacing: 1px;
}

/* Footer */
.site-footer {
    margin-top: 90px;
    padding: 60px 20px;
    background: var(--dark);
    color: white;
    text-align: center;
}

.site-footer-title {
    letter-spacing: 5px;
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    color: white;
}

.site-footer-sub {
    font-size: 10px;
    color: #AAAAAA;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* Mobile */
@media (max-width: 900px) {
    .brand-title {
        font-size: 30px;
        letter-spacing: 4px;
    }

    .top-nav {
        gap: 4px;
        padding: 10px 2px;
    }

    .top-nav a {
        font-size: 11px;
        padding: 8px 8px;
        letter-spacing: 0px;
    }

    .section-title {
        font-size: 28px;
        padding-top: 24px;
    }

    .showcase-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 14px;
    }

    .showcase-grid img {
        height: 220px;
    }

    .collection-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 30px 16px;
    }

    .collection-card img {
        height: 230px;
    }

    .collection-price {
        font-size: 1rem;
    }

    .collection-button {
        width: 100%;
        font-size: 0.72rem;
        letter-spacing: 1.5px;
    }

    .detail-grid {
        grid-template-columns: 1fr;
    }

    .packaging-section {
        grid-template-columns: 1fr;
        gap: 30px;
        text-align: center;
        margin-bottom: 70px;
    }

    .packaging-content {
        text-align: left;
        max-width: 520px;
        margin: 0 auto;
    }

    .packaging-content li {
        font-size: 16px;
    }

    .contact-row {
        flex-direction: column;
        align-items: center;
        gap: 45px;
        margin-top: 40px;
    }
}
</style>
""",
    unsafe_allow_html=True
)


# --- 5. 顶部导航 ---
NAV_ITEMS = [
    {"key": "home", "label": "Home / 首页"},
    {"key": "collections", "label": "Collections / 系列"},
    {"key": "diy", "label": "DIY Studio / 手作工坊"},
    {"key": "about", "label": "About Us / 关于我们"},
]

collection_item_from_url = get_query_param_value("collection_item")
page_from_url = get_query_param_value("page")

if collection_item_from_url and not page_from_url:
    current_page = "collections"
else:
    current_page = page_from_url or "home"

valid_pages = [item["key"] for item in NAV_ITEMS]

if current_page not in valid_pages:
    current_page = "home"

nav_html = ""

for item in NAV_ITEMS:
    active_class = "active" if current_page == item["key"] else ""
    nav_html += (
        f'<a class="{active_class}" href="?page={item["key"]}" target="_self">'
        f'{item["label"]}'
        '</a>'
    )

header_html = (
    '<div class="site-header">'
    '<div class="brand-area">'
    '<div class="brand-title">little otter</div>'
    '<div class="brand-subtitle">Handcrafted Energy</div>'
    '</div>'
    f'<div class="top-nav">{nav_html}</div>'
    '</div>'
)

st.markdown(header_html, unsafe_allow_html=True)


# --- 6. 状态与数据初始化 ---
if "diy_beads" not in st.session_state:
    st.session_state.diy_beads = []

BEAD_DB = {
    "moonstone": {
        "display": "月光石 / Moonstone\n温润 / Warmth",
        "color": "#eeeae8",
        "type": "main",
        "price": 25
    },
    "aquamarine": {
        "display": "海蓝宝 / Aquamarine\n沟通 / Communication",
        "color": "#a2cffe",
        "type": "main",
        "price": 30
    },
    "amethyst": {
        "display": "紫水晶 / Amethyst\n智慧 / Wisdom",
        "color": "#9b59b6",
        "type": "main",
        "price": 20
    },
    "strawberry_quartz": {
        "display": "草莓晶 / Strawberry Quartz\n人缘 / Relationship",
        "color": "#ffb7c5",
        "type": "main",
        "price": 28
    },
    "obsidian": {
        "display": "黑曜石 / Obsidian\n辟邪 / Protection",
        "color": "#333333",
        "type": "main",
        "price": 15
    },
    "clear_quartz": {
        "display": "白水晶 / Clear Quartz\n净化 / Cleansing",
        "color": "#ffffff",
        "type": "main",
        "price": 10
    },
    "silver_spacer": {
        "display": "925银素圈 / 925 Silver Spacer",
        "color": "linear-gradient(to right, #d7d7d7, #ffffff)",
        "type": "spacer",
        "price": 5
    },
    "gold_spacer": {
        "display": "复古金珠 / Vintage Gold Spacer",
        "color": "linear-gradient(to right, #bf9b30, #e6c975)",
        "type": "spacer",
        "price": 8
    },
}


# --- 7. Home / 首页 ---
if current_page == "home":
    logo_src = image_to_data_uri("首页logo图.jpg")

    if logo_src:
        st.markdown(
            f'<div class="logo-wrap"><img class="logo-img" src="{logo_src}" alt="little otter logo"></div>',
            unsafe_allow_html=True
        )
    else:
        st.warning("未找到首页logo图.jpg，请确认图片和代码文件在同一个文件夹。")

    st.markdown('<div class="section-title">our story</div>', unsafe_allow_html=True)

    st.markdown(
        """
<div class="story-card">
Just as little otters treasure the stones they love most, carrying them close wherever they go, Little Otter was created to help you discover the crystal that speaks to your soul. Rather than pursuing perfection through excessive polishing, we value authenticity—the natural texture of each stone and the energy it carries. Every handcrafted piece is a touchable sense of calm, a quiet companion you can keep with you.
<br><br>
正如小水獭总会珍惜自己最喜欢的石头，并把它带在身边，Little Otter 希望帮助你找到那颗能与你灵魂共鸣的水晶。我们不追求过度打磨后的完美，而更珍视每一颗天然石本身的纹理、触感与能量。每一件手作，都是一份可以被触碰的平静，也是一位安静陪伴你的随身伙伴。
</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-title">Crystal Collection / 水晶系列</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Selected handcrafted pieces from Little Otter / Little Otter 精选手作</div>', unsafe_allow_html=True)

    showcase_images = [
        "首页-产品展示图-1.jpg",
        "首页-产品展示图-2.jpg",
        "首页-产品展示图-3.jpg",
        "首页-产品展示图-4.jpg",
    ]

    showcase_html = '<div class="showcase-grid">'

    for image_name in showcase_images:
        image_src = image_to_data_uri(image_name)

        if image_src:
            showcase_html += f'<img src="{image_src}" alt="{image_name}">'
        else:
            showcase_html += missing_box(image_name, "310px")

    showcase_html += '</div>'

    st.markdown(showcase_html, unsafe_allow_html=True)


# --- 8. Collections / 系列 ---
elif current_page == "collections":
    products = [
        {"id": 1, "price": "299", "has_detail": True},
        {"id": 2, "price": "99", "has_detail": True},
        {"id": 3, "price": "128", "has_detail": True},
        {"id": 4, "price": "269", "has_detail": True},
        {"id": 5, "price": "269", "has_detail": True},
        {"id": 6, "price": "269", "has_detail": True},
        {"id": 7, "price": "349", "has_detail": True},
        {"id": 8, "price": "128", "has_detail": True},
        {"id": 9, "price": "168", "has_detail": True},
        {"id": 10, "price": "168", "has_detail": True},
        {"id": 11, "price": "168", "has_detail": True},
        {"id": 12, "price": "168", "has_detail": True},
        {"id": 13, "price": "78", "has_detail": False},
        {"id": 14, "price": "399", "has_detail": False},
    ]

    selected_item = get_query_param_value("collection_item")
    valid_detail_ids = [str(p["id"]) for p in products if p["has_detail"]]

    if selected_item and selected_item != "list" and selected_item in valid_detail_ids:
        selected_id = int(selected_item)

        st.markdown(
            '<a class="back-link" href="?page=collections&collection_item=list" target="_self">← BACK TO COLLECTION / 返回系列</a>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="section-title">collection {selected_id} / 系列 {selected_id}</div>',
            unsafe_allow_html=True
        )

        detail_images = [
            f"{selected_id}-1.jpg",
            f"{selected_id}-2.jpg",
        ]

        detail_html = '<div class="detail-grid">'

        for image_name in detail_images:
            image_src = image_to_data_uri(image_name)

            if image_src:
                detail_html += f'<img class="detail-image" src="{image_src}" alt="{image_name}">'
            else:
                detail_html += missing_box(image_name, "420px")

        detail_html += '</div>'

        st.markdown(detail_html, unsafe_allow_html=True)

    else:
        st.markdown('<div class="section-title">the collection / 水晶系列</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-subtitle">Natural crystal bracelets and handcrafted pieces / 天然水晶手作系列</div>', unsafe_allow_html=True)

        collection_html = '<div class="collection-grid">'

        for product in products:
            cover_name = f"{product['id']}.jpg"
            cover_src = image_to_data_uri(cover_name)

            if cover_src:
                if product["has_detail"]:
                    cover_html = (
                        f'<a href="?page=collections&collection_item={product["id"]}" target="_self">'
                        f'<img src="{cover_src}" alt="collection {product["id"]}">'
                        '</a>'
                    )
                else:
                    cover_html = f'<img src="{cover_src}" alt="collection {product["id"]}">'
            else:
                if product["has_detail"]:
                    cover_html = (
                        f'<a href="?page=collections&collection_item={product["id"]}" target="_self">'
                        f'{missing_box(cover_name, "350px")}'
                        '</a>'
                    )
                else:
                    cover_html = missing_box(cover_name, "350px")

            if product["has_detail"]:
                button_html = (
                    f'<a class="collection-button" href="?page=collections&collection_item={product["id"]}" target="_self">'
                    'EXPLORE MORE'
                    '</a>'
                )
            else:
                button_html = ''

            collection_html += (
                '<div class="collection-card">'
                f'{cover_html}'
                f'<div class="collection-price">SGD {product["price"]}</div>'
                f'{button_html}'
                '</div>'
            )

        collection_html += '</div>'

        st.markdown(collection_html, unsafe_allow_html=True)


# --- 9. DIY Studio / 手作工坊 ---
elif current_page == "diy":
    st.markdown('<div class="section-title">design your own / 设计你的专属手串</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">像水獭收集灵石一样，挑选你的专属搭配</div>', unsafe_allow_html=True)

    html_beads = ""

    if not st.session_state.diy_beads:
        html_beads = '<p style="color:#999; z-index:1;">add your first bead... / 添加第一颗水晶</p>'
    else:
        for bead_name in st.session_state.diy_beads:
            if bead_name not in BEAD_DB:
                continue

            bead_info = BEAD_DB[bead_name]
            css_class = "bead-spacer" if bead_info["type"] == "spacer" else "bead-circle"
            html_beads += (
                f'<div class="{css_class}" '
                f'style="background: {bead_info["color"]};" '
                f'title="{bead_info["display"]}"></div>'
            )

    st.markdown(f'<div class="diy-bracelet-container">{html_beads}</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([2, 1, 1])

    with c1:
        tab1, tab2 = st.tabs(["🔮 Main Stones / 主珠", "✨ Spacers / 隔片"])

        main_beads = [key for key, item in BEAD_DB.items() if item["type"] == "main"]
        spacer_beads = [key for key, item in BEAD_DB.items() if item["type"] == "spacer"]

        with tab1:
            btn_cols = st.columns(3)

            for i, bead_key in enumerate(main_beads):
                bead_display = BEAD_DB[bead_key]["display"]

                if btn_cols[i % 3].button(f"＋ {bead_display}", key=f"add_{bead_key}"):
                    st.session_state.diy_beads.append(bead_key)
                    safe_rerun()

        with tab2:
            btn_cols_s = st.columns(2)

            for i, bead_key in enumerate(spacer_beads):
                bead_display = BEAD_DB[bead_key]["display"]

                if btn_cols_s[i % 2].button(f"＋ {bead_display}", key=f"add_{bead_key}"):
                    st.session_state.diy_beads.append(bead_key)
                    safe_rerun()

    with c2:
        st.write("")

        if st.button("↩️ Undo / 撤回"):
            if st.session_state.diy_beads:
                st.session_state.diy_beads.pop()
                safe_rerun()

        if st.button("🗑️ Reset / 重置"):
            st.session_state.diy_beads = []
            safe_rerun()

    with c3:
        total = sum(
            BEAD_DB[b]["price"]
            for b in st.session_state.diy_beads
            if b in BEAD_DB
        )

        estimate_html = (
            '<div class="estimate-box">'
            '<div style="font-size:14px; letter-spacing:1px;">Estimate / 预估价格</div>'
            f'<div class="estimate-price">SGD {total}</div>'
            '</div>'
        )

        st.markdown(estimate_html, unsafe_allow_html=True)

        st.write("")

        if st.button("❤️ Save Design / 保存设计"):
            st.success("Design saved to your wish list. / 已保存到你的心愿单。")
            st.balloons()


# --- 10. About Us / 关于我们 ---
elif current_page == "about":
    st.markdown('<div class="section-title">about us / 关于我们</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Crystal packaging, care and ways to contact Little Otter / 水晶包装、保养与联系方式</div>', unsafe_allow_html=True)

    package_src = image_to_data_uri("关于我们-产品包装图-1.jpg")
    instagram_src = image_to_data_uri("instagram.jpg")
    email_src = image_to_data_uri("email.jpg")
    wechat_src = image_to_data_uri("wechat.jpg")

    if package_src:
        package_html = f'<img class="about-package-img" src="{package_src}" alt="Crystal Packaging">'
    else:
        package_html = missing_box("关于我们-产品包装图-1.jpg", "300px")

    def contact_icon_html(image_src, file_name, label_en, label_cn, link="#"):
        if image_src:
            icon_html = (
                f'<a href="{link}" target="_blank">'
                f'<img src="{image_src}" alt="{label_en}">'
                '</a>'
            )
        else:
            icon_html = missing_box(file_name, "150px")

        return (
            '<div class="contact-item">'
            f'{icon_html}'
            f'<div class="contact-label">{label_en}</div>'
            f'<div class="contact-sub-label">{label_cn}</div>'
            '</div>'
        )

    instagram_html = contact_icon_html(
        instagram_src,
        "instagram.jpg",
        "Instagram",
        "Little Otter Crystal",
        "#"
    )

    email_html = contact_icon_html(
        email_src,
        "email.jpg",
        "Email",
        "littleotter@gmail.com",
        "mailto:littleotter@gmail.com"
    )

    wechat_html = contact_icon_html(
        wechat_src,
        "wechat.jpg",
        "WeChat",
        "Little Otter Crystal",
        "#"
    )

    about_html = (
        '<div class="about-container">'
        '<div class="packaging-section">'
        '<div class="packaging-left-title">'
        'Crystal Packaging<br>水晶包装'
        '</div>'
        '<div class="packaging-content">'
        '<ul>'
        '<li>Premium Crystal Gift Box <span class="packaging-cn">高级水晶礼盒</span></li>'
        '<li>Crystal Polishing Cloth <span class="packaging-cn">水晶擦拭布</span></li>'
        '<li>Crystal Care Instruction Card <span class="packaging-cn">水晶保养说明卡</span></li>'
        '<li>White Quartz Cleansing Stones <span class="packaging-cn">白水晶净化石</span></li>'
        '<li>Personalized Gift Message Card <span class="packaging-cn">个性化祝福卡</span></li>'
        '<li>Complimentary Replacement String <span class="packaging-cn">备用替换绳</span></li>'
        '</ul>'
        '</div>'
        '<div class="about-image-wrap">'
        f'{package_html}'
        '</div>'
        '</div>'
        '<div class="contact-row">'
        f'{instagram_html}'
        f'{email_html}'
        f'{wechat_html}'
        '</div>'
        '</div>'
    )

    st.markdown(about_html, unsafe_allow_html=True)


# --- 11. Footer ---
st.markdown(
"""
<div class="site-footer">
    <div class="site-footer-title">little otter</div>
    <div class="site-footer-sub">Natural Stone Studio | est. 2026</div>
    <div class="site-footer-sub">天然水晶手作工作室</div>
</div>
""",
    unsafe_allow_html=True
)

st.markdown("---")
st.caption("© 2026 LITTLE OTTER")
