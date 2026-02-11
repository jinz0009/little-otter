<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>灵石雅集 | 天然水晶手串设计</title>
    <style>
        /* 基础样式复位 */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "PingFang SC", "Microsoft YaHei", serif;
        }

        :root {
            --primary-color: #7e6c6c; /* 灰粉色，模拟矿石质感 */
            --bg-color: #fdfcfb;
            --text-dark: #2d2d2d;
            --text-light: #888;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-dark);
            line-height: 1.6;
        }

        /* 导航栏 */
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 5%;
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            letter-spacing: 2px;
            color: var(--primary-color);
        }

        .nav-links a {
            text-decoration: none;
            color: var(--text-dark);
            margin-left: 30px;
            font-size: 0.9rem;
            transition: 0.3s;
        }

        .nav-links a:hover {
            color: var(--primary-color);
        }

        /* 英雄视觉区 */
        .hero {
            height: 80vh;
            background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.2)), 
                        url('https://images.unsplash.com/photo-1551028150-64b9f398f678?auto=format&fit=crop&q=80&w=1600') center/cover;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            text-align: center;
        }

        .hero h1 {
            font-size: 3rem;
            letter-spacing: 8px;
            margin-bottom: 20px;
        }

        .cta-btn {
            padding: 12px 30px;
            border: 1px solid white;
            color: white;
            text-decoration: none;
            transition: 0.4s;
            margin-top: 20px;
        }

        .cta-btn:hover {
            background: white;
            color: var(--text-dark);
        }

        /* 灵感介绍区 */
        .section-title {
            text-align: center;
            padding: 60px 0 30px;
        }

        .section-title h2 {
            font-size: 2rem;
            font-weight: 300;
            letter-spacing: 4px;
        }

        .inspiration {
            display: flex;
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 5%;
            align-items: center;
            gap: 50px;
        }

        .ins-text {
            flex: 1;
        }

        .ins-text blockquote {
            font-style: italic;
            border-left: 3px solid var(--primary-color);
            padding-left: 20px;
            margin-bottom: 20px;
            color: #555;
        }

        .ins-image {
            flex: 1;
        }

        .ins-image img {
            width: 100%;
            border-radius: 4px;
            box-shadow: 20px 20px 0px #eee;
        }

        /* 商品展示区 */
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto 80px;
            padding: 0 5%;
        }

        .product-card {
            background: white;
            padding: 15px;
            transition: 0.3s;
            text-align: center;
            border: 1px solid #f0f0f0;
        }

        .product-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.05);
        }

        .product-card img {
            width: 100%;
            aspect-ratio: 1/1;
            object-fit: cover;
            margin-bottom: 15px;
        }

        .tag {
            font-size: 0.7rem;
            background: #f0ecec;
            padding: 2px 8px;
            border-radius: 10px;
            color: var(--primary-color);
            margin: 0 3px;
        }

        .price {
            display: block;
            margin-top: 10px;
            color: var(--primary-color);
            font-weight: bold;
        }

        /* 响应式适配 */
        @media (max-width: 768px) {
            .inspiration { flex-direction: column; }
            .hero h1 { font-size: 2rem; }
        }
    </style>
</head>
<body>

    <nav>
        <div class="logo">LUXE CRYSTAL</div>
        <div class="nav-links">
            <a href="#">首页</a>
            <a href="#inspiration">灵感故事</a>
            <a href="#shop">商品系列</a>
            <a href="#">定制服务</a>
        </div>
    </nav>

    <header class="hero">
        <h1>万物有灵</h1>
        <p>每一颗水晶，都是大地沉淀亿年的诗篇</p>
        <a href="#shop" class="cta-btn">探索系列</a>
    </header>

    <section id="inspiration">
        <div class="section-title">
            <h2>设计灵感</h2>
        </div>
        <div class="inspiration">
            <div class="ins-text">
                <blockquote>“设计不是创造美，而是还原自然本身的律动。”</blockquote>
                <p>我们的工作室坐落于静谧的山谷，设计师通过观察清晨的露珠、午后的岩影，将这些自然碎片融入到手串的色彩搭配中。我们坚持使用纯天然原石，拒绝任何化学染色，只为保留那份最纯粹的疗愈能量。</p>
            </div>
            <div class="ins-image">
                <img src="https://images.unsplash.com/photo-1596432189439-65363364f866?auto=format&fit=crop&q=80&w=800" alt="设计师手稿">
            </div>
        </div>
    </section>

    <section id="shop">
        <div class="section-title">
            <h2>商品展示</h2>
        </div>
        <div class="product-grid">
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1615484477778-ca3b77940c25?auto=format&fit=crop&q=80&w=600" alt="晨曦手串">
                <h3>【晨曦】月光石系列</h3>
                <p><span class="tag">#温润</span><span class="tag">#助眠</span></p>
                <span class="price">¥ 399.00</span>
            </div>
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1569388330292-79cc1ec67270?auto=format&fit=crop&q=80&w=600" alt="深海手串">
                <h3>【深海】海蓝宝系列</h3>
                <p><span class="tag">#勇气</span><span class="tag">#守护</span></p>
                <span class="price">¥ 458.00</span>
            </div>
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1611085583191-a3b1a308c021?auto=format&fit=crop&q=80&w=600" alt="禅意手串">
                <h3>【禅意】乌拉圭紫晶</h3>
                <p><span class="tag">#智慧</span><span class="tag">#安宁</span></p>
                <span class="price">¥ 520.00</span>
            </div>
        </div>
    </section>

    <footer style="background: #2d2d2d; color: white; text-align: center; padding: 40px 0;">
        <p>&copy; 2024 LUXE CRYSTAL 灵石雅集 | 匠心手作</p>
    </footer>

</body>
</html>
