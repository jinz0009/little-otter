import streamlit as st
from collections import Counter
import base64
from pathlib import Path

# --- 1. 深度页面配置与视觉注入 ---
st.set_page_config(page_title="little otter | 灵石手作", page_icon="🦦", layout="wide")


# --- 本地图片转 base64，用于精准显示本地图片 ---
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


# --- 隐藏 Streamlit 顶部菜单 / GitHub / Deploy / Viewer Badge ---
st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none !important;
        visibility: hidden !important;
    }

    #MainMenu {
        visibility: hidden !important;
        display: none !important;
    }

    header {
        visibility: hidden !important;
        height: 0rem !important;
    }

    footer {
        visibility: hidden !important;
        display: none !important;
    }

    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"],
    [data-testid="manage-app-button"],
    [data-testid="stHeaderActionElements"],
    .stDeployButton,
    .stActionButton,
    a[href*="github.com"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        height: 0 !important;
        pointer-events: none !important;
    }

    .block-container {
        padding-top: 2rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --- 全局视觉 CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Montserrat:wght@300;400;500&display=swap');

    .stApp {
        background-color: #FDFCFB !important;
        color: #333;
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
    """, unsafe_allow_html=True)


# --- 2. 状态与数据初始化 ---
if 'diy_beads' not in st.session_state:
    st.session_state.diy_beads = []

BEAD_DB = {
    "主珠-月光石 (温润)": {"color": "#eeeae8", "type": "main", "price": 25},
    "主珠-海蓝宝 (沟通)": {"color": "#a2cffe", "type": "main", "price": 30},
    "主珠-紫水晶 (智慧)": {"color": "#9b59b6", "type": "main", "price": 20},
    "主珠-草莓晶 (人缘)": {"color": "#ffb7c5", "type": "main", "price": 28},
    "主珠-黑曜石 (辟邪)": {"color": "#333333", "type": "main", "price": 15},
    "配珠-白水晶 (净化)": {"color": "#ffffff", "type": "main", "price": 10},
    "隔片-925银素圈": {"color": "linear-gradient(to right, #d7d7d7, #ffffff)", "type": "spacer", "price": 5},
    "隔片-复古金珠": {"color": "linear-gradient(to right, #bf9b30, #e6c975)", "type": "spacer", "price": 8},
}


# --- 3. 侧边栏导航 ---
st.sidebar.markdown("<h2 style='letter-spacing:4px; color:#5D5B57;'>little otter</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:10px; letter-spacing:1px; margin-top:-15px;'>HANDCRAFTED ENERGY</p>", unsafe_allow_html=True)

collection_item_from_url = get_query_param_value("collection_item")
default_menu_index = 1 if collection_item_from_url else 0

menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Collections", "DIY Studio", "Energy Quiz"],
    index=default_menu_index
)


# --- 4. 页面内容展示 ---

# 1. Home - 品牌首页
if menu == "Home":
    logo_base64 = image_to_base64("首页logo图.jpg")

    if logo_base64:
        st.markdown(f"""
            <div style="width:100%; display:flex; justify-content:center; align-items:center; padding:40px 0 20px 0;">
                <img src="data:image/jpeg;base64,{logo_base64}" style="width:520px; max-width:90%; display:block;">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("未找到首页logo图.jpg，请确认图片和代码文件在同一个文件夹。")

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<h2 style='text-align:center;'>our story</h2>", unsafe_allow_html=True)
        st.write("""
            Just as little otters treasure the stones they love most, carrying them close wherever they go, Little Otter was created to help you discover the crystal that speaks to your soul. Rather than pursuing perfection through excessive polishing, we value authenticity—the natural texture of each stone and the energy it carries. Every handcrafted piece is a touchable sense of calm, a quiet companion you can keep with you.
        """)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; padding:30px 0 20px 0;'>Crystal Collection</h2>", unsafe_allow_html=True)

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


# 2. Collections - 系列展示
elif menu == "Collections":
    st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #000000 !important;
}

.collection-title {
    text-align: center;
    padding: 20px 0 40px 0;
    color: #ffffff;
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
}

.collection-card img:hover {
    transform: scale(1.015);
    opacity: 0.88;
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
    background: #000000;
    display: block;
}

.back-link {
    display: inline-block;
    color: #ffffff !important;
    text-decoration: none !important;
    border: 1px solid #ffffff;
    padding: 10px 24px;
    letter-spacing: 2px;
    margin-bottom: 30px;
}

.back-link:hover {
    background: #ffffff;
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

    products = [
        {"id": 1, "price": "299"},
        {"id": 2, "price": "99"},
        {"id": 3, "price": "128"},
        {"id": 4, "price": "269"},
        {"id": 5, "price": "269"},
        {"id": 6, "price": "269"},
        {"id": 7, "price": "349"},
        {"id": 8, "price": "128"},
        {"id": 9, "price": "168"},
        {"id": 10, "price": "168"},
        {"id": 11, "price": "168"},
        {"id": 12, "price": "168"},
    ]

    selected_item = get_query_param_value("collection_item")

    # 详情页
    if selected_item and selected_item != "list":
        selected_id = int(selected_item) if str(selected_item).isdigit() else 1

        st.markdown(
            '<a class="back-link" href="?collection_item=list" target="_self">← BACK TO COLLECTION</a>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"<h2 class='collection-title'>collection {selected_id}</h2>",
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

    # 列表页
    else:
        st.markdown(
            "<h2 class='collection-title'>the collection</h2>",
            unsafe_allow_html=True
        )

        for row_start in range(0, len(products), 4):
            cols = st.columns(4)

            for col, product in zip(cols, products[row_start:row_start + 4]):
                with col:
                    cover_name = f"{product['id']}.jpg"
                    cover_base64 = image_to_base64(cover_name)

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
                            f'border:1px solid #333; color:#999; background:#111;">未找到 {cover_name}</div>'
                            f'</a>'
                        )

                    card_html = (
                        '<div class="collection-card">'
                        f'{cover_html}'
                        f'<div class="collection-price">S$: &nbsp;{product["price"]}</div>'
                        f'<a class="collection-button" href="?collection_item={product["id"]}" target="_self">EXPLORE MORE</a>'
                        '</div>'
                    )

                    st.markdown(card_html, unsafe_allow_html=True)


# 3. DIY Studio - 在线 DIY
elif menu == "DIY Studio":
    st.markdown("<h2 style='text-align:center; padding-top:40px;'>design your own</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#999; letter-spacing:1px;'>像水獭收集灵石一样，挑选你的专属搭配</p>", unsafe_allow_html=True)

    html_beads = ""

    if not st.session_state.diy_beads:
        html_beads = "<p style='color:#999; z-index:1;'>add your first bead...</p>"
    else:
        for bead_name in st.session_state.diy_beads:
            bead_info = BEAD_DB[bead_name]
            css_class = "bead-spacer" if bead_info["type"] == "spacer" else "bead-circle"
            html_beads += f'<div class="{css_class}" style="background: {bead_info["color"]};" title="{bead_name}"></div>'

    st.markdown(f'<div class="diy-bracelet-container">{html_beads}</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([2, 1, 1])

    with c1:
        tab1, tab2 = st.tabs(["🔮 Main Stones", "✨ Spacers"])

        main_beads = [n for n, i in BEAD_DB.items() if i["type"] == "main"]
        spacer_beads = [n for n, i in BEAD_DB.items() if i["type"] == "spacer"]
        
        with tab1:
            btn_cols = st.columns(3)

            for i, name in enumerate(main_beads):
                if btn_cols[i % 3].button(f"＋ {name.split('-')[1]}", key=f"add_{name}"):
                    st.session_state.diy_beads.append(name)
                    st.rerun()

        with tab2:
            btn_cols_s = st.columns(2)

            for i, name in enumerate(spacer_beads):
                if btn_cols_s[i % 2].button(f"＋ {name.split('-')[1]}", key=f"add_{name}"):
                    st.session_state.diy_beads.append(name)
                    st.rerun()
    
    with c2:
        st.write("<br>", unsafe_allow_html=True)

        if st.button("↩️ Undo"):
            if st.session_state.diy_beads:
                st.session_state.diy_beads.pop()
                st.rerun()

        if st.button("🗑️ Reset"):
            st.session_state.diy_beads = []
            st.rerun()
            
    with c3:
        total = sum(BEAD_DB[b]["price"] for b in st.session_state.diy_beads)

        st.markdown("#### Estimate")
        st.markdown(f"<h2 style='color:#A68B67;'>¥ {total}</h2>", unsafe_allow_html=True)

        if st.button("❤️ Save Design"):
            st.success("Design saved to your wish list.")
            st.balloons()


# 4. Energy Quiz - 定制测试
elif menu == "Energy Quiz":
    st.markdown("<h2 style='text-align:center; padding:40px 0;'>crystal oracle</h2>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='max-width:700px; margin:0 auto; padding:40px; border:1px solid #EEE; background:white; margin-bottom:50px;'>
            <h3 style='text-align:center; margin-top:0;'>寻找你的本命水晶</h3>
            <p style='text-align:center; color:#888; font-size:13px;'>回答 3 个直觉问题，我们将为你匹配最适合的水晶能量。</p>
            <br>
    """, unsafe_allow_html=True)
    
    q1 = st.select_slider(
        "1. 你最近的状态更倾向于？", 
        options=["极度焦虑", "平淡如水", "充满斗志"]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.write("2. 如果你现在深处森林，你最希望看到的颜色是？")
    q2 = st.color_picker("点击色块选择你的直觉色", "#7e6c6c", key="quiz_color")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    q3 = st.multiselect(
        "3. 你希望提升哪方面的能量？", 
        ["沟通力", "专注力", "桃花运", "财运"],
        placeholder="请选择 (可多选)"
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.button("生成我的匹配报告"):
        st.balloons()
        st.markdown("---")
        st.markdown("### 🦦 little otter's guide")
        
        if "财运" in q3:
            st.write("### ✨ 建议选择：**金发晶 (Gold Rutilated Quartz)**")
            st.write("在你选中的色彩与意向中，金发晶的频率最能引起共鸣。它能增强你的决断力与行动力，吸引财富磁场，让你的“斗志”化为丰硕的果实。")

        elif "桃花运" in q3 or "沟通力" in q3:
            st.write("### ✨ 建议选择：**粉晶 (Rose Quartz)**")
            st.write("温柔的色彩能抚平内心的焦虑。粉晶不仅是吸引良缘，更能帮助你开启与自我、与他人的温和沟通视角。")

        else:
            st.write("### ✨ 建议选择：**海蓝宝 (Aquamarine)**")
            st.write("针对你追求的平衡状态，海蓝宝如同流动的水，能带走负累，让你在平淡如水的生活中发现深邃的智慧。")

    st.markdown("</div>", unsafe_allow_html=True)


# 页脚
st.markdown("""
    <div style='margin-top:100px; padding:60px; background:#333; color:white; text-align:center;'>
        <p style='letter-spacing:5px; font-family:Playfair Display; font-size:1.5rem;'>little otter</p>
        <p style='font-size:10px; color:#888; letter-spacing:2px; text-transform:uppercase;'>Natural Stone Studio | est. 2026</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2026 LITTLE OTTER ")
