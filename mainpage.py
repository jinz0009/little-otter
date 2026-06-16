import streamlit as st
from collections import Counter
import base64
from pathlib import Path

# --- 1. 页面配置 ---
st.set_page_config(
    page_title="little otter | 灵石手作",
    page_icon="🦦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --- 2. 工具函数 ---
def image_to_base64(image_path):
    image_path = Path(image_path)
    if not image_path.exists():
        return None
    return base64.b64encode(image_path.read_bytes()).decode()


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


# --- 3. 隐藏 GitHub / Deploy / Viewer Badge，但保留手机端侧边栏按钮 ---
st.markdown(
"""
<style>
/* 隐藏旧版 Streamlit Cloud viewer badge / GitHub badge */
.css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
.styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
.viewerBadge_text__1JaDK {
    display: none !important;
    visibility: hidden !important;
}

/* 隐藏主菜单 */
#MainMenu {
    visibility: hidden !important;
    display: none !important;
}

/* 隐藏 footer */
footer {
    visibility: hidden !important;
    display: none !important;
}

/* 隐藏 Deploy / GitHub 相关元素，但不要隐藏 header 和侧边栏按钮 */
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="manage-app-button"],
.stDeployButton,
a[href*="github.com"] {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
}

/* 关键：不要隐藏 header，否则手机端侧边栏按钮会消失 */
header {
    visibility: visible !important;
    display: block !important;
    height: 3rem !important;
    background: transparent !important;
    z-index: 999999 !important;
}

/* 关键：保留顶部按钮容器 */
[data-testid="stHeaderActionElements"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
}

/* 关键：保留侧边栏收起后的展开按钮 */
[data-testid="collapsedControl"] {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    z-index: 999999 !important;
    pointer-events: auto !important;
}

/* 页面顶部间距 */
.block-container {
    padding-top: 2rem !important;
}

/* 手机端强制显示左上角侧边栏按钮 */
@media (max-width: 768px) {
    header {
        visibility: visible !important;
        display: block !important;
        height: 3.2rem !important;
        background: transparent !important;
        z-index: 999999 !important;
    }

    [data-testid="collapsedControl"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        z-index: 999999 !important;
        pointer-events: auto !important;
    }

    [data-testid="stSidebar"] {
        z-index: 999998 !important;
    }
}
</style>
""",
    unsafe_allow_html=True
)


# --- 4. 全局浅色视觉 CSS ---
st.markdown(
"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap');

.stApp {
    background-color: #FDFCFB !important;
    color: #333333 !important;
}

[data-testid="stAppViewContainer"] {
    background-color: #FDFCFB !important;
}

html, body, [data-testid="stWidgetLabel"], .stMarkdown p {
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 300;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    font-weight: 400 !important;
    letter-spacing: 3px !important;
    text-transform: lowercase;
}

div.stButton > button {
    border-radius: 0px !important;
    border: 1px solid #333 !important;
    background-color: transparent !important;
    color: #333 !important;
    padding: 10px 25px !important;
    text-transform: uppercase;
    font-size: 11px !important;
    letter-spacing: 2px;
    transition: 0.3s;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #333 !important;
    color: white !important;
}

[data-testid="stSidebar"] {
    background-color: #F8F7F5 !important;
    border-right: 1px solid #EEE;
}

/* DIY 串珠台 */
.diy-bracelet-container {
    display: flex;
    flex-wrap: nowrap;
    justify-content: center;
    align-items: center;
    gap: 3px;
    padding: 80px 20px;
    background-color: #F4F2EE;
    border-top: 1px solid #EAEAEA;
    border-bottom: 1px solid #EAEAEA;
    margin: 30px 0;
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
    transition: 0.3s;
}

.bead-spacer {
    width: 12px;
    height: 38px;
    border-radius: 3px;
    z-index: 1;
    box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
}

/* 通用产品卡片 */
.product-box {
    text-align: center;
    padding: 15px;
    border: 1px solid transparent;
    transition: 0.4s;
}

.product-box:hover {
    border: 1px solid #A68B67;
}
</style>
""",
    unsafe_allow_html=True
)


# --- 5. 状态与数据初始化 ---
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


# --- 6. 侧边栏导航 ---
st.sidebar.markdown(
    "<h2 style='letter-spacing:4px; color:#5D5B57;'>little otter</h2>",
    unsafe_allow_html=True
)
st.sidebar.markdown(
    "<p style='font-size:10px; letter-spacing:1px; margin-top:-15px;'>HANDCRAFTED ENERGY</p>",
    unsafe_allow_html=True
)

NAV_ITEMS = [
    "Home / 首页",
    "Collections / 系列",
    "DIY Studio / 手作工坊",
    "Energy Quiz / 能量测试",
    "About Us / 关于我们"
]

collection_item_from_url = get_query_param_value("collection_item")
default_menu_index = 1 if collection_item_from_url else 0

menu = st.sidebar.radio(
    "Navigation / 导航",
    NAV_ITEMS,
    index=default_menu_index
)


# --- 7. 页面内容展示 ---

# 1. Home / 首页
if menu == "Home / 首页":
    logo_base64 = image_to_base64("首页logo图.jpg")

    if logo_base64:
        logo_html = (
            '<div style="width:100%; display:flex; justify-content:center; '
            'align-items:center; padding:40px 0 20px 0;">'
            f'<img src="data:image/jpeg;base64,{logo_base64}" '
            'style="width:520px; max-width:90%; display:block;">'
            '</div>'
        )
        st.markdown(logo_html, unsafe_allow_html=True)
    else:
        st.warning("未找到首页logo图.jpg，请确认图片和代码文件在同一个文件夹。")

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<h2 style='text-align:center;'>our story</h2>", unsafe_allow_html=True)
        st.write("""
        Just as little otters treasure the stones they love most, carrying them close wherever they go, Little Otter was created to help you discover the crystal that speaks to your soul. Rather than pursuing perfection through excessive polishing, we value authenticity—the natural texture of each stone and the energy it carries. Every handcrafted piece is a touchable sense of calm, a quiet companion you can keep with you.

        正如小水獭总会珍惜自己最喜欢的石头，并把它带在身边，Little Otter 希望帮助你找到那颗能与你灵魂共鸣的水晶。我们不追求过度打磨后的完美，而更珍视每一颗天然石本身的纹理、触感与能量。每一件手作，都是一份可以被触碰的平静，也是一位安静陪伴你的随身伙伴。
        """)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        "<h2 style='text-align:center; padding:30px 0 20px 0;'>Crystal Collection / 水晶系列</h2>",
        unsafe_allow_html=True
    )

    showcase_images = [
        "首页-产品展示图-1.jpg",
        "首页-产品展示图-2.jpg",
        "首页-产品展示图-3.jpg",
        "首页-产品展示图-4.jpg",
    ]

    showcase_cols = st.columns(4)

    for i, img in enumerate(showcase_images):
        with showcase_cols[i]:
            st.image(img, use_container_width=True)


# 2. Collections / 系列
elif menu == "Collections / 系列":
    st.markdown(
"""
<style>
.collection-title {
    text-align: center;
    padding: 20px 0 40px 0;
    color: #333333;
    letter-spacing: 4px;
}

.collection-card {
    text-align: center;
    margin-bottom: 38px;
}

.collection-card img {
    width: 100%;
    height: 350px;
    object-fit: cover;
    display: block;
    transition: 0.25s ease;
    border: 1px solid #EFEFEF;
}

.collection-card img:hover {
    transform: scale(1.015);
    opacity: 0.9;
}

.collection-price {
    color: #333333;
    font-size: 1.35rem;
    font-weight: 700;
    margin: 18px 0 12px 0;
    letter-spacing: 1px;
}

.collection-button {
    display: inline-block;
    width: 86%;
    background: #ffffff;
    color: #555555 !important;
    border: 1px solid #333333;
    padding: 15px 0;
    text-decoration: none !important;
    letter-spacing: 4px;
    font-size: 0.9rem;
    text-transform: uppercase;
    transition: 0.25s ease;
}

.collection-button:hover {
    background: #333333;
    color: #ffffff !important;
}

.detail-image {
    width: 100%;
    max-height: 680px;
    object-fit: contain;
    background: #FDFCFB;
    display: block;
    border: 1px solid #EFEFEF;
}

.back-link {
    display: inline-block;
    color: #333333 !important;
    text-decoration: none !important;
    border: 1px solid #333333;
    padding: 10px 24px;
    letter-spacing: 2px;
    margin-bottom: 30px;
}

.back-link:hover {
    background: #333333;
    color: #ffffff !important;
}
</style>
""",
        unsafe_allow_html=True
    )

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
            '<a class="back-link" href="?collection_item=list" target="_self">← BACK TO COLLECTION / 返回系列</a>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"<h2 class='collection-title'>collection {selected_id} / 系列 {selected_id}</h2>",
            unsafe_allow_html=True
        )

        detail_images = [
            f"{selected_id}-1.jpg",
            f"{selected_id}-2.jpg",
        ]

        detail_cols = st.columns(2)

        for i, img_name in enumerate(detail_images):
            with detail_cols[i % 2]:
                img_base64 = image_to_base64(img_name)

                if img_base64:
                    st.markdown(
                        f'<img class="detail-image" src="data:image/jpeg;base64,{img_base64}">',
                        unsafe_allow_html=True
                    )
                else:
                    st.warning(f"未找到详情图：{img_name}")

    else:
        st.markdown(
            "<h2 class='collection-title'>the collection / 水晶系列</h2>",
            unsafe_allow_html=True
        )

        for row_start in range(0, len(products), 4):
            cols = st.columns(4)

            for col, product in zip(cols, products[row_start:row_start + 4]):
                with col:
                    cover_name = f"{product['id']}.jpg"
                    cover_base64 = image_to_base64(cover_name)

                    if product["has_detail"]:
                        if cover_base64:
                            cover_html = (
                                f'<a href="?collection_item={product["id"]}" target="_self">'
                                f'<img src="data:image/jpeg;base64,{cover_base64}" alt="collection {product["id"]}">'
                                f'</a>'
                            )
                        else:
                            cover_html = (
                                f'<a href="?collection_item={product["id"]}" target="_self">'
                                f'<div style="height:350px; display:flex; align-items:center; justify-content:center; '
                                f'border:1px solid #DDD; color:#999; background:#FAFAFA;">未找到 {cover_name}</div>'
                                f'</a>'
                            )

                        card_html = (
                            '<div class="collection-card">'
                            f'{cover_html}'
                            f'<div class="collection-price">S$: &nbsp;{product["price"]}</div>'
                            f'<a class="collection-button" href="?collection_item={product["id"]}" target="_self">EXPLORE MORE</a>'
                            '</div>'
                        )

                    else:
                        if cover_base64:
                            cover_html = (
                                f'<img src="data:image/jpeg;base64,{cover_base64}" alt="collection {product["id"]}">'
                            )
                        else:
                            cover_html = (
                                f'<div style="height:350px; display:flex; align-items:center; justify-content:center; '
                                f'border:1px solid #DDD; color:#999; background:#FAFAFA;">未找到 {cover_name}</div>'
                            )

                        card_html = (
                            '<div class="collection-card">'
                            f'{cover_html}'
                            f'<div class="collection-price">S$: &nbsp;{product["price"]}</div>'
                            '</div>'
                        )

                    st.markdown(card_html, unsafe_allow_html=True)


# 3. DIY Studio / 手作工坊
elif menu == "DIY Studio / 手作工坊":
    st.markdown(
        "<h2 style='text-align:center; padding-top:40px;'>design your own / 设计你的专属手串</h2>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align:center; color:#999; letter-spacing:1px;'>像水獭收集灵石一样，挑选你的专属搭配</p>",
        unsafe_allow_html=True
    )

    html_beads = ""

    if not st.session_state.diy_beads:
        html_beads = "<p style='color:#999; z-index:1;'>add your first bead... / 添加第一颗水晶</p>"
    else:
        for bead_name in st.session_state.diy_beads:
            if bead_name not in BEAD_DB:
                continue
            bead_info = BEAD_DB[bead_name]
            css_class = "bead-spacer" if bead_info["type"] == "spacer" else "bead-circle"
            html_beads += f'<div class="{css_class}" style="background: {bead_info["color"]};" title="{bead_info["display"]}"></div>'

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

                if btn_cols[i % 3].button(
                    f"＋ {bead_display}",
                    key=f"add_{bead_key}"
                ):
                    st.session_state.diy_beads.append(bead_key)
                    st.rerun()

        with tab2:
            btn_cols_s = st.columns(2)

            for i, bead_key in enumerate(spacer_beads):
                bead_display = BEAD_DB[bead_key]["display"]

                if btn_cols_s[i % 2].button(
                    f"＋ {bead_display}",
                    key=f"add_{bead_key}"
                ):
                    st.session_state.diy_beads.append(bead_key)
                    st.rerun()

    with c2:
        st.write("<br>", unsafe_allow_html=True)

        if st.button("↩️ Undo / 撤回"):
            if st.session_state.diy_beads:
                st.session_state.diy_beads.pop()
                st.rerun()

        if st.button("🗑️ Reset / 重置"):
            st.session_state.diy_beads = []
            st.rerun()

    with c3:
        total = sum(
            BEAD_DB[b]["price"]
            for b in st.session_state.diy_beads
            if b in BEAD_DB
        )

        st.markdown("#### Estimate / 预估价格")
        st.markdown(f"<h2 style='color:#A68B67;'>SGD {total}</h2>", unsafe_allow_html=True)

        if st.button("❤️ Save Design / 保存设计"):
            st.success("Design saved to your wish list. / 已保存到你的心愿单。")
            st.balloons()


# 4. Energy Quiz / 能量测试
elif menu == "Energy Quiz / 能量测试":
    st.markdown(
        "<h2 style='text-align:center; padding:40px 0;'>crystal oracle / 水晶能量测试</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
"""
<div style='max-width:760px; margin:0 auto; padding:40px; border:1px solid #EEE; background:white; margin-bottom:50px;'>
<h3 style='text-align:center; margin-top:0;'>Find Your Crystal Energy / 寻找你的水晶能量</h3>
<p style='text-align:center; color:#888; font-size:13px;'>
Answer 3 questions and receive your Little Otter crystal energy report.<br>
回答 3 个问题，获得你的 Little Otter 水晶能量报告。
</p>
<br>
</div>
""",
        unsafe_allow_html=True
    )

    q1 = st.select_slider(
        "Question 1 of 3 / 第 1 题：How would you describe your current state? / 你如何描述最近的状态？",
        options=[
            "I want to express myself more confidently / 我想更自信地表达自己",
            "I want to stay focused and reduce distractions / 我想提升专注力并减少分心",
            "I want to attract love and positive relationships / 我想吸引爱与积极关系",
            "I want to welcome more opportunities and success / 我想迎接更多机会与成功"
        ]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.write("Question 2 of 3 / 第 2 题：Which color are you most drawn to right now? / 你此刻最被哪种颜色吸引？")
    q2 = st.color_picker(
        "Choose your instinctive color / 选择你的直觉颜色",
        "#7e6c6c",
        key="quiz_color"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    q3 = st.radio(
        "Question 3 of 3 / 第 3 题：Which energy do you want to enhance the most? / 你最想增强哪一种能量？",
        [
            "Communication Enhancement / 沟通表达能量",
            "Focus Enhancement / 专注执行能量",
            "Love & Relationship Energy / 爱与关系能量",
            "Prosperity & Abundance / 财富与丰盛能量"
        ]
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    reports = {
        "Communication Enhancement / 沟通表达能量": {
            "title": "1. Communication Enhancement | Express Yourself with Confidence and Build Meaningful Connections",
            "title_cn": "1. 沟通表达能量｜自信表达，建立有意义的人际连接",
            "keywords": "Clear expression, Increased confidence, Interpersonal harmony, Enhanced persuasion and influence",
            "keywords_cn": "清晰表达、自信提升、人际和谐、增强说服力与影响力",
            "crystals": "Aquamarine, Blue Lace Agate, Lapis Lazuli",
            "crystals_cn": "海蓝宝、蓝纹玛瑙、青金石",
            "product": "Aquamarine Communication Energy Bracelet",
            "product_cn": "海蓝宝沟通能量手串"
        },
        "Focus Enhancement / 专注执行能量": {
            "title": "2. Focus Enhancement | Cultivate Concentration and Strengthen Execution",
            "title_cn": "2. 专注执行能量｜培养专注力，增强行动与执行",
            "keywords": "Improved concentration, Reduced distractions, Enhanced motivation, Clear thinking",
            "keywords_cn": "提升专注力、减少分心、增强动力、思路清晰",
            "crystals": "Fluorite, Amethyst, Obsidian",
            "crystals_cn": "萤石、紫水晶、黑曜石",
            "product": "Fluorite Focus Energy Bracelet",
            "product_cn": "萤石专注能量手串"
        },
        "Love & Relationship Energy / 爱与关系能量": {
            "title": "3. Love & Relationship Energy | Radiate Charm and Attract Positive Connections",
            "title_cn": "3. 爱与关系能量｜散发魅力，吸引积极连接",
            "keywords": "Self-love and appreciation, Emotional connection, Increased approachability, Personal magnetism",
            "keywords_cn": "自爱与欣赏、情感连接、提升亲和力、个人吸引力",
            "crystals": "Rose Quartz, Strawberry Quartz, Moonstone",
            "crystals_cn": "粉晶、草莓晶、月光石",
            "product": "Rose Quartz Love Energy Bracelet",
            "product_cn": "粉晶爱与关系能量手串"
        },
        "Prosperity & Abundance / 财富与丰盛能量": {
            "title": "4. Prosperity & Abundance | Embrace Opportunities and Cultivate Success",
            "title_cn": "4. 财富与丰盛能量｜拥抱机会，培育成功",
            "keywords": "Prosperity mindset, Motivation and initiative, Career growth, Opportunity awareness",
            "keywords_cn": "丰盛心态、动力与主动性、事业成长、机会意识",
            "crystals": "Citrine, Golden Rutilated Quartz, Green Phantom Quartz",
            "crystals_cn": "黄水晶、金发晶、绿幽灵",
            "product": "Prosperity & Success Energy Bracelet",
            "product_cn": "财富与成功能量手串"
        }
    }

    if st.button("Generate My Crystal Report / 生成我的水晶报告"):
        st.balloons()
        st.markdown("---")
        st.markdown("### 🦦 little otter's guide / 小水獭能量指南")

        result = reports[q3]

        report_html = (
            '<div style="background:#FFFFFF; color:#333; padding:35px; margin-top:25px; '
            'line-height:1.75; border:1px solid #EAEAEA;">'
            f'<h3 style="color:#333 !important; text-transform:none !important; letter-spacing:1px !important;">{result["title"]}</h3>'
            f'<h3 style="color:#333 !important; text-transform:none !important; letter-spacing:1px !important;">{result["title_cn"]}</h3>'
            f'<p><strong>Energy Keywords:</strong> {result["keywords"]}</p>'
            f'<p><strong>能量关键词：</strong>{result["keywords_cn"]}</p>'
            f'<p><strong>Recommended Crystals:</strong> {result["crystals"]}</p>'
            f'<p><strong>推荐水晶：</strong>{result["crystals_cn"]}</p>'
            f'<p><strong>Recommended Product:</strong> {result["product"]}</p>'
            f'<p><strong>推荐产品：</strong>{result["product_cn"]}</p>'
            '<br>'
            '<p>May each crystal become a source of inspiration and support on your journey.</p>'
            '<p>愿每一颗水晶都成为你旅程中的灵感与支持。</p>'
            '<br>'
            '<p><strong>Disclaimer:</strong> This report is intended for inspirational and lifestyle purposes only and does not replace professional advice.</p>'
            '<p><strong>免责声明：</strong>本报告仅用于灵感与生活方式参考，不替代任何专业建议。</p>'
            '</div>'
        )

        st.markdown(report_html, unsafe_allow_html=True)


# 5. About Us / 关于我们
elif menu == "About Us / 关于我们":
    st.markdown(
"""
<style>
.about-container {
    min-height: 760px;
    background: #FDFCFB;
    padding: 40px 40px 100px 40px;
}

.about-title {
    text-align: center;
    color: #333333;
    letter-spacing: 4px;
    margin-bottom: 45px;
}

.packaging-section {
    display: grid;
    grid-template-columns: 1fr 1.45fr 1.2fr;
    gap: 50px;
    align-items: center;
    margin-bottom: 110px;
}

.packaging-left-title {
    font-size: 22px;
    color: #333333;
    letter-spacing: 1px;
    line-height: 1.7;
}

.packaging-content {
    color: #222222;
}

.packaging-content ul {
    margin: 0;
    padding-left: 22px;
}

.packaging-content li {
    font-size: 18px;
    line-height: 1.55;
    margin-bottom: 4px;
}

.packaging-cn {
    color: #666666;
    font-size: 15px;
    margin-left: 6px;
}

.about-package-img {
    width: 100%;
    max-width: 420px;
    height: auto;
    object-fit: cover;
    border: 1px solid #EFEFEF;
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
    background: #ffffff;
    border: 1px solid #EFEFEF;
}

.contact-label {
    color: #333333;
    font-size: 18px;
    font-weight: 600;
    letter-spacing: 2px;
    margin-top: 18px;
    text-transform: none;
}

.contact-sub-label {
    color: #777777;
    font-size: 14px;
    margin-top: 6px;
    letter-spacing: 1px;
}

@media (max-width: 900px) {
    .about-container {
        padding: 30px 20px 80px 20px;
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

    .about-image-wrap {
        justify-content: center;
    }

    .about-package-img {
        max-width: 420px;
        width: 100%;
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

    package_base64 = image_to_base64("关于我们-产品包装图-1.jpg")
    instagram_base64 = image_to_base64("instagram.jpg")
    email_base64 = image_to_base64("email.jpg")
    wechat_base64 = image_to_base64("wechat.jpg")

    if package_base64:
        package_html = (
            f'<img class="about-package-img" '
            f'src="data:image/jpeg;base64,{package_base64}" '
            f'alt="Crystal Packaging">'
        )
    else:
        package_html = (
            '<div style="width:420px; height:300px; border:1px solid #DDD; color:#999; '
            'display:flex; align-items:center; justify-content:center; background:#FAFAFA;">'
            '未找到 关于我们-产品包装图-1.jpg'
            '</div>'
        )

    def contact_icon_html(base64_data, file_name, label_en, label_cn, link="#"):
        if base64_data:
            icon_html = (
                f'<a href="{link}" target="_blank">'
                f'<img src="data:image/jpeg;base64,{base64_data}" alt="{label_en}">'
                f'</a>'
            )
        else:
            icon_html = (
                f'<div style="width:150px; height:150px; background:#FAFAFA; border:1px solid #DDD; '
                f'color:#999; display:flex; align-items:center; justify-content:center;">'
                f'未找到 {file_name}'
                f'</div>'
            )

        return (
            '<div class="contact-item">'
            f'{icon_html}'
            f'<div class="contact-label">{label_en}</div>'
            f'<div class="contact-sub-label">{label_cn}</div>'
            '</div>'
        )

    instagram_html = contact_icon_html(
        instagram_base64,
        "instagram.jpg",
        "Instagram",
        "Little Otter Crystal",
        "#"
    )

    email_html = contact_icon_html(
        email_base64,
        "email.jpg",
        "Email",
        "littleotter@gmail.com",
        "mailto:littleotter@gmail.com"
    )

    wechat_html = contact_icon_html(
        wechat_base64,
        "wechat.jpg",
        "WeChat",
        "Little Otter Crystal",
        "#"
    )

    packaging_html = (
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
    )

    about_html = (
        '<div class="about-container">'
        '<h2 class="about-title">about us / 关于我们</h2>'
        f'{packaging_html}'
        '<div class="contact-row">'
        f'{instagram_html}'
        f'{email_html}'
        f'{wechat_html}'
        '</div>'
        '</div>'
    )

    st.markdown(about_html, unsafe_allow_html=True)


# --- 页脚 ---
st.markdown(
"""
<div style='margin-top:100px; padding:60px; background:#333; color:white; text-align:center;'>
    <p style='letter-spacing:5px; font-family:Playfair Display; font-size:1.5rem;'>little otter</p>
    <p style='font-size:10px; color:#888; letter-spacing:2px; text-transform:uppercase;'>Natural Stone Studio | est. 2026</p>
    <p style='font-size:10px; color:#888; letter-spacing:2px;'>天然水晶手作工作室</p>
</div>
""",
    unsafe_allow_html=True
)

st.markdown("---")
st.caption("© 2026 LITTLE OTTER ")
