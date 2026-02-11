import streamlit as st

# --- 页面配置 ---
st.set_page_config(page_title="灵石雅集 | Crystal Design", page_icon="✨", layout="wide")

# --- 自定义 CSS 样式 (让 Streamlit 看起来更有设计感) ---
st.markdown("""
    <style>
    .main {
        background-color: #fdfcfb;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        border: 1px solid #7e6c6c;
        background-color: transparent;
        color: #7e6c6c;
    }
    .stButton>button:hover {
        background-color: #7e6c6c;
        color: white;
    }
    h1, h2 {
        color: #4a4a4a;
        letter-spacing: 2px;
    }
    .product-price {
        color: #7e6c6c;
        font-weight: bold;
        font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 侧边栏导航 ---
st.sidebar.title("LUXE CRYSTAL")
menu = st.sidebar.radio("前往", ["品牌首页", "灵感故事", "系列展示", "定制测试"])

# --- 1. 品牌首页 ---
if menu == "品牌首页":
    st.title("✨ 灵石雅集")
    st.subheader("每一颗水晶，都是大地沉淀亿年的诗篇")
    
    # 英雄大图
    st.image("https://images.unsplash.com/photo-1551028150-64b9f398f678?auto=format&fit=crop&q=80&w=1600", 
             caption="自然之美，腕间流转", use_container_width=True)
    
    st.write("---")
    st.write("我们致力于发现原石的自然能量，结合现代设计美学，为你定制专属的护身符。")

# --- 2. 灵感故事 ---
elif menu == "灵感故事":
    st.header("🌙 设计灵感：灵石物语")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 匠心 · 还原")
        st.info("“设计不是创造美，而是还原自然本身的律动。”")
        st.write("""
            我们的设计师常驻于矿区周边，通过观察清晨的露珠在矿石上的折射，
            提取色彩灵感。我们拒绝过度打磨，保留冰裂与棉絮，
            因为那是时间留下的指纹。
        """)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1596432189439-65363364f866?auto=format&fit=crop&q=80&w=800")

# --- 3. 系列展示 ---
elif menu == "系列展示":
    st.header("💎 当季系列")
    
    # 商品筛选器
    category = st.multiselect("按能量筛选", ["事业", "恋爱", "安宁", "勇气"], default=["事业", "恋爱"])
    
    # 模拟商品数据
    products = [
        {"name": "【晨曦】月光石", "price": "¥ 399", "tag": "恋爱", "img": "https://images.unsplash.com/photo-1615484477778-ca3b77940c25?auto=format&fit=crop&q=80&w=600"},
        {"name": "【深海】海蓝宝", "price": "¥ 458", "tag": "勇气", "img": "https://images.unsplash.com/photo-1569388330292-79cc1ec67270?auto=format&fit=crop&q=80&w=600"},
        {"name": "【禅意】紫水晶", "price": "¥ 520", "tag": "安宁", "img": "https://images.unsplash.com/photo-1611085583191-a3b1a308c021?auto=format&fit=crop&q=80&w=600"},
    ]
    
    # 商品展示网格
    cols = st.columns(3)
    for i, p in enumerate(products):
        with cols[i % 3]:
            st.image(p["img"])
            st.subheader(p["name"])
            st.markdown(f"<p class='product-price'>{p['price']}</p>", unsafe_allow_html=True)
            st.caption(f"能量标签: {p['tag']}")
            if st.button(f"查看详情", key=i):
                st.success(f"已为您锁定 {p['name']} 的能量信息")

# --- 4. 定制测试 (交互功能) ---
elif menu == "定制测试":
    st.header("🔮 寻找你的本命水晶")
    st.write("回答 3 个直觉问题，我们将为你匹配最适合的水晶。")
    
    q1 = st.select_slider("你最近的状态更倾向于？", options=["极度焦虑", "平淡如水", "充满斗志"])
    q2 = st.color_picker("如果你现在深处森林，你最希望看到的颜色是？", "#7e6c6c")
    q3 = st.multiselect("你希望提升哪方面的能量？", ["沟通力", "专注力", "桃花运", "财运"])
    
    if st.button("生成我的匹配报告"):
        st.balloons()
        st.write("### 匹配结果")
        if "财运" in q3:
            st.write("✨ 建议选择：**金发晶 (Gold Rutilated Quartz)**")
            st.write("它能增强你的决断力与行动力，吸引财富磁场。")
        else:
            st.write("✨ 建议选择：**粉晶 (Rose Quartz)**")
            st.write("温柔的色彩能抚平焦虑，助你开启人缘磁场。")

# --- 页脚 ---
st.markdown("---")
st.caption("© 2026 LUXE CRYSTAL 灵石雅集 | 使用 Python & Streamlit 驱动")
