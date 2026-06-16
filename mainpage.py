import streamlit as st
from collections import Counter

# --- 1. 深度页面配置与视觉注入 ---
st.set_page_config(page_title="little otter | 灵石手作", page_icon="🦦", layout="wide")

# 强制注入 Wix 风格的高级感 CSS
st.markdown("""
    <style>
    /* 引入高端字体 */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Montserrat:wght@300;400;500&display=swap');

    /* 全局背景与基础字体 */
    .stApp {
        background-color: #FDFCFB !important;
        color: #333;
    }
    
    html, body, [data-testid="stWidgetLabel"], .stMarkdown p {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 300;
    }

    /* 标题美化 - little otter 风格 */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 400 !important;
        letter-spacing: 3px !important;
        text-transform: lowercase; /* 契合 little otter 的随性与亲和力 */
    }

    /* 按钮美化：硬朗、黑色边框、无圆角 (Wix风格) */
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
    
    /* 侧边栏美化 */
    [data-testid="stSidebar"] {
        background-color: #F8F7F5 !important;
        border-right: 1px solid #EEE;
    }

    /* DIY 串珠台视觉效果升级 */
    .diy-bracelet-container {
        display: flex;
        flex-wrap: nowrap;
        justify-content: center;
        align-items: center;
        gap: 3px;
        padding: 80px 20px;
        background-color: #F4F2EE; /* 略带沙滩感的米色 */
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
    
    /* 商品展示卡片 */
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


# 屏蔽 Streamlit 页面右上角 GitHub / viewer badge 图标
st.markdown( 
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
menu = st.sidebar.radio("Navigation", ["Home", "Collections", "DIY Studio", "Energy Quiz"])

# --- 4. 页面内容展示 ---

# 1. Home - 品牌首页
if menu == "Home":
    st.markdown("""
        <div style="height:500px; background: linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.1)), 
                    url('https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&q=80&w=1600') center/cover;
                    display:flex; flex-direction:column; justify-content:center; align-items:center; color:white;">
            <h1 style="color:white !important; font-size:4.5rem; margin-bottom:0px;">little otter</h1>
            <p style="letter-spacing:6px; text-transform:uppercase; font-size:12px; margin-top:10px;">源于自然的治愈 · 灵石手作</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<h2 style='text-align:center;'>our story</h2>", unsafe_allow_html=True)
        st.write("""
            正如小水獭总会挑选最心仪的那块石头揣在兜里，**little otter** 诞生的初衷，是为你寻找那颗能引起灵魂共鸣的矿石。
            我们不追求过度的雕琢，只在意自然的触感与能量的传递。每一串手作，都是一份可以触碰的平静。
        """)
        st.image("https://images.unsplash.com/photo-1605100804763-247f67b3557e?q=80&w=1600&auto=format&fit=crop")

# 2. Collections - 系列展示
elif menu == "Collections":
    st.markdown("<h2 style='text-align:center; padding:50px 0;'>the collection</h2>", unsafe_allow_html=True)
    
    products = [
        {"name": "river flow - 海蓝宝", "price": "¥ 399.00", "img": "https://images.unsplash.com/photo-1615484477778-ca3b77940c25?auto=format&fit=crop&q=80&w=600"},
        {"name": "sunset glow - 草莓晶", "price": "¥ 458.00", "img": "https://images.unsplash.com/photo-1588444833098-4205565e247d?auto=format&fit=crop&q=80&w=600"},
        {"name": "deep forest - 绿幽灵", "price": "¥ 520.00", "img": "https://images.unsplash.com/photo-1611085583191-a3b1a308c021?auto=format&fit=crop&q=80&w=600"}
    ]
    
    cols = st.columns(3)
    for i, p in enumerate(products):
        with cols[i]:
            st.markdown(f"""
                <div class="product-box">
                    <img src="{p['img']}" style="width:100%; height:350px; object-fit:cover; margin-bottom:15px;">
                    <h3 style="font-size:1.1rem;">{p['name']}</h3>
                    <p style="color:#A68B67; font-weight:500;">{p['price']}</p>
                </div>
            """, unsafe_allow_html=True)
            st.button("Explore More", key=f"shop_{i}")

# 3. DIY Studio - 在线DIY (Little Otter 核心交互)
elif menu == "DIY Studio":
    st.markdown("<h2 style='text-align:center; padding-top:40px;'>design your own</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#999; letter-spacing:1px;'>像水獭收集灵石一样，挑选你的专属搭配</p>", unsafe_allow_html=True)

    # 可视化串珠台
    html_beads = ""
    if not st.session_state.diy_beads:
        html_beads = "<p style='color:#999; z-index:1;'>add your first bead...</p>"
    else:
        for bead_name in st.session_state.diy_beads:
            bead_info = BEAD_DB[bead_name]
            css_class = "bead-spacer" if bead_info["type"] == "spacer" else "bead-circle"
            html_beads += f'<div class="{css_class}" style="background: {bead_info["color"]};" title="{bead_name}"></div>'

    st.markdown(f'<div class="diy-bracelet-container">{html_beads}</div>', unsafe_allow_html=True)

    # DIY 控制台
    c1, c2, c3 = st.columns([2, 1, 1])
    with c1:
        tab1, tab2 = st.tabs(["🔮 Main Stones", "✨ Spacers"])
        main_beads = [n for n, i in BEAD_DB.items() if i["type"] == "main"]
        spacer_beads = [n for n, i in BEAD_DB.items() if i["type"] == "spacer"]
        
        with tab1:
            btn_cols = st.columns(3)
            for i, name in enumerate(main_beads):
                if btn_cols[i%3].button(f"＋ {name.split('-')[1]}", key=f"add_{name}"):
                    st.session_state.diy_beads.append(name)
                    st.rerun()
        with tab2:
            btn_cols_s = st.columns(2)
            for i, name in enumerate(spacer_beads):
                if btn_cols_s[i%2].button(f"＋ {name.split('-')[1]}", key=f"add_{name}"):
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
        st.markdown(f"#### Estimate")
        st.markdown(f"<h2 style='color:#A68B67;'>¥ {total}</h2>", unsafe_allow_html=True)
        if st.button("❤️ Save Design"):
            st.success("Design saved to your wish list.")
            st.balloons()

# --- 4. Energy Quiz - 定制测试 (Little Otter 风格版) ---
elif menu == "Energy Quiz":
    st.markdown("<h2 style='text-align:center; padding:40px 0;'>crystal oracle</h2>", unsafe_allow_html=True)
    
    # 使用 Wix 风格的白底细边框容器包裹测试题
    st.markdown("""
        <div style='max-width:700px; margin:0 auto; padding:40px; border:1px solid #EEE; background:white; margin-bottom:50px;'>
            <h3 style='text-align:center; margin-top:0;'>寻找你的本命水晶</h3>
            <p style='text-align:center; color:#888; font-size:13px;'>回答 3 个直觉问题，我们将为你匹配最适合的水晶能量。</p>
            <br>
    """, unsafe_allow_html=True)
    
    # --- 问题区域 ---
    # Q1: 心理状态滑块
    q1 = st.select_slider(
        "1. 你最近的状态更倾向于？", 
        options=["极度焦虑", "平淡如水", "充满斗志"]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Q2: 直觉选色器
    st.write("2. 如果你现在深处森林，你最希望看到的颜色是？")
    q2 = st.color_picker("点击色块选择你的直觉色", "#7e6c6c", key="quiz_color")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Q3: 能量诉求多选
    q3 = st.multiselect(
        "3. 你希望提升哪方面的能量？", 
        ["沟通力", "专注力", "桃花运", "财运"],
        placeholder="请选择 (可多选)"
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # 生成报告按钮
    if st.button("生成我的匹配报告"):
        st.balloons()
        st.markdown("---")
        st.markdown("### 🦦 little otter's guide")
        
        # 结果逻辑判断
        if "财运" in q3:
            st.write("### ✨ 建议选择：**金发晶 (Gold Rutilated Quartz)**")
            st.write("在你选中的色彩与意向中，金发晶的频率最能引起共鸣。它能增强你的决断力与行动力，吸引财富磁场，让你的“斗志”化为丰硕的果实。")
        elif "桃花运" in q3 or "沟通力" in q3:
            st.write("### ✨ 建议选择：**粉晶 (Rose Quartz)**")
            st.write("温柔的色彩能抚平内心的焦虑。粉晶不仅是吸引良缘，更能帮助你开启与自我、与他人的温和沟通视角。")
        else:
            st.write("### ✨ 建议选择：**海蓝宝 (Aquamarine)**")
            st.write("针对你追求的平衡状态，海蓝宝如同流动的水，能带走负累，让你在平淡如水的生活中发现深邃的智慧。")

    st.markdown("</div>", unsafe_allow_html=True) # 结束外层白色容器

# 页脚
st.markdown("""
    <div style='margin-top:100px; padding:60px; background:#333; color:white; text-align:center;'>
        <p style='letter-spacing:5px; font-family:Playfair Display; font-size:1.5rem;'>little otter</p>
        <p style='font-size:10px; color:#888; letter-spacing:2px; text-transform:uppercase;'>Natural Stone Studio | est. 2026</p>
    </div>
""", unsafe_allow_html=True)
# --- 页脚 ---
st.markdown("---")
st.caption("© 2026 LITTLE OTTER ")
