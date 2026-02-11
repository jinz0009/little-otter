import streamlit as st

# --- 页面配置 ---
st.set_page_config(page_title="灵石雅集 | Crystal Design", page_icon="✨", layout="wide")

# --- 自定义 CSS 样式 (增强设计感和DIY区域效果) ---
st.markdown("""
    <style>
    /* 全局样式 */
    .main {
        background-color: #fdfcfb;
    }
    h1, h2, h3 {
        color: #4a4a4a;
        font-family: "Source Sans Pro", sans-serif;
        letter-spacing: 1px;
    }
    .stButton>button {
        border-radius: 20px;
        border: 1px solid #7e6c6c;
        color: #7e6c6c;
        padding: 5px 20px;
    }
    .stButton>button:hover {
        background-color: #7e6c6c;
        color: white;
    }
    
    /* --- DIY 区域核心 CSS --- */
    /* 珠子容器，模拟一条线 */
    .diy-bracelet-container {
        display: flex;
        flex-wrap: nowrap;
        justify-content: center;
        align-items: center;
        gap: 2px; /* 珠子间距 */
        padding: 30px 10px;
        background-color: #f4f4f4;
        border-radius: 15px;
        overflow-x: auto; /* 珠子太多时允许横向滚动 */
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        position: relative;
    }
    /* 模拟穿珠子的绳线背景 */
    .diy-bracelet-container::before {
        content: '';
        position: absolute;
        width: 90%;
        height: 2px;
        background-color: #ccc;
        z-index: 0;
    }
    /* 通用珠子样式，圆形，立体感 */
    .bead-circle {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        /* 内阴影和外阴影营造立体感 */
        box-shadow: inset -3px -3px 8px rgba(0,0,0,0.3), inset 2px 2px 5px rgba(255,255,255,0.4), 2px 3px 5px rgba(0,0,0,0.2);
        z-index: 1; /* 确保珠子在线的上面 */
        transition: all 0.3s ease;
    }
    .bead-circle:hover {
        transform: scale(1.1);
    }
    /* 隔片样式（更小一点） */
    .bead-spacer {
        width: 15px;
        height: 35px;
        border-radius: 5px;
        box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
         z-index: 1;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Session State 初始化 (用于存储 DIY 数据) ---
# 如果没有这个，每次点击按钮页面刷新，串好的珠子就没了
if 'diy_beads' not in st.session_state:
    st.session_state.diy_beads = [] # 存储已选珠子的列表

# --- 珠子数据库定义 ---
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

# --- 侧边栏导航 ---
st.sidebar.title("LUXE CRYSTAL")
st.sidebar.write("自然能量 · 随心而定")
menu = st.sidebar.radio("前往", ["品牌首页", "系列展示", "👉 在线DIY手串", "定制测试"])

# ==================== 页面内容 ====================

# --- 1. 品牌首页 (保持不变) ---
if menu == "品牌首页":
    st.title("✨ 灵石雅集")
    st.subheader("每一颗水晶，都是大地沉淀亿年的诗篇")
    st.image("https://images.unsplash.com/photo-1602002418816-5c0ae5cb8447?q=80&w=1600&auto=format&fit=crop", 
             caption="感知自然脉动", use_container_width=True)
    st.write("---")
    st.write("我们致力于发现原石的自然能量，结合现代设计美学，为你定制专属的护身符。")

# --- 2. 系列展示 (保持不变) ---
elif menu == "系列展示":
    st.header("💎 当季设计师款")
    cols = st.columns(3)
    # (这里省略了之前的模拟数据以节省篇幅，实际使用时可以加上)
    st.info("设计师系列正在上新中...")

# --- 3. 👉 在线DIY手串 (核心新增功能) ---
elif menu == "👉 在线DIY手串":
    st.title("🛠️ 灵感工坊：手作你的能量场")
    st.write("点击下方材料，珠子将自动串连。发挥你的创意，搭配独一无二的手串。")

    # --- 区域 A: 可视化串珠台 (最关键部分) ---
    st.subheader("你的设计预览")
    
    # 生成可视化的 HTML 字符串
    html_beads = ""
    if not st.session_state.diy_beads:
        html_beads = "<p style='color:#999; padding: 20px;'>📿 暂无珠子，请从下方添加...</p>"
    else:
        for bead_name in st.session_state.diy_beads:
            bead_info = BEAD_DB[bead_name]
            color_style = bead_info["color"]
            # 根据珠子类型应用不同的 CSS 类 (圆形或隔片)
            css_class = "bead-spacer" if bead_info["type"] == "spacer" else "bead-circle"
            # 拼接 HTML Div
            html_beads += f'<div class="{css_class}" style="background: {color_style};" title="{bead_name}"></div>'

    # 渲染整个DIY容器
    st.markdown(f"""
        <div class="diy-bracelet-container">
            {html_beads}
        </div>
    """, unsafe_allow_html=True)
    
    # 提示信息
    count = len(st.session_state.diy_beads)
    st.caption(f"当前珠子数量: {count} 颗 (建议女生手围 18-22 颗)")


    st.write("---")

    # --- 区域 B: 操作控制台 & 材料库 ---
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📦 选择材料添加")
        
        # 将数据库分为主珠和隔片两组显示
        main_beads = [name for name, info in BEAD_DB.items() if info["type"] == "main"]
        spacer_beads = [name for name, info in BEAD_DB.items() if info["type"] == "spacer"]

        tab1, tab2 = st.tabs(["🔮 天然主珠", "✨ 金属隔片"])
        
        with tab1:
            # 使用一行多列的按钮布局
            cols_main = st.columns(4)
            for i, bead_name in enumerate(main_beads):
                # 获取颜色用于按钮左侧的颜色块展示 (一个小技巧)
                color_box = f"<span style='display:inline-block;width:12px;height:12px;border-radius:50%;background:{BEAD_DB[bead_name]['color']};margin-right:8px;'></span>"
                if cols_main[i % 4].button(f"＋ {bead_name.split('-')[1]}", help=f"点击添加{bead_name}", use_container_width=True):
                    st.session_state.diy_beads.append(bead_name)
                    st.rerun() # 强制刷新页面以更新视图

        with tab2:
            cols_spacer = st.columns(4)
            for i, bead_name in enumerate(spacer_beads):
                 if cols_spacer[i % 4].button(f"＋ {bead_name.split('-')[1]}", help=f"点击添加{bead_name}", use_container_width=True):
                    st.session_state.diy_beads.append(bead_name)
                    st.rerun()

    with col2:
        st.subheader("⚙️ 操作")
        if st.button("↩️ 撤销上一步", use_container_width=True):
            if st.session_state.diy_beads:
                st.session_state.diy_beads.pop()
                st.rerun()
        
        st.write("") # Spacer
        
        if st.button("🗑️ 清空重置", type="primary", use_container_width=True):
            st.session_state.diy_beads = []
            st.rerun()

    st.write("---")

    # --- 区域 C: 设计清单与结算 ---
    st.subheader("🧾 设计清单")
    if st.session_state.diy_beads:
        total_price = 0
        # 使用字典统计每种珠子的数量
        from collections import Counter
        counts = Counter(st.session_state.diy_beads)
        
        for bead_name, count in counts.items():
            price = BEAD_DB[bead_name]["price"]
            total_price += price * count
            st.write(f"- {bead_name} x {count} 颗 | 小计: ¥{price * count}")
            
        st.markdown(f"### 💰 预估总价: <span style='color:#d9534f'>¥ {total_price}</span>", unsafe_allow_html=True)
        
        if st.button("❤️ 保存我的设计并咨询"):
            st.success("设计已保存！截图发送给客服即可开始定制。")
            st.balloons()
    else:
        st.write("暂无已选材料。")

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
st.caption("© 2026 LUXE CRYSTAL 灵石雅集 ")
