---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I'm an incoming CS Ph.D. student in the [NLP Lab](http://nlp.cs.ucsb.edu/) at UC Santa Barbara (UCSB), advised by [Prof. Shiyu Chang](https://code-terminator.github.io/). Previously, I earned my bachelor's degree from Nanjing University and my master's degree from Johns Hopkins University. Before starting my Ph.D., I spent several years as a full-time applied scientist at Amazon Alexa AI and Amazon AGI.

My research focuses on natural language processing, information retrieval, and speech recognition.

I’m always open to collaboration opportunities. If you're interested, feel free to reach out to me via **ziyanjiang528@gmail.com**



# 🔥 News
- *2025.04*: I’ve moved my personal homepage to this new site; the old one is now deprecated.



<h1 id="publications">📝 Publications (*: equal contribution/co-first author)</h1>
Full publications on [Google Scholar](https://scholar.google.com/citations?user=wDJjd2IAAAAJ&hl=en).

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/vlm2vec.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[VLM2Vec: Training Vision-Language Models for Massive Multimodal Embedding Tasks](https://arxiv.org/abs/2410.05160)

**Ziyan Jiang**, Rui Meng, Xinyi Yang, Semih Yavuz, Yingbo Zhou, Wenhu Chen

[**Project Page**](https://tiger-ai-lab.github.io/VLM2Vec/)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/mega-bench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks](https://arxiv.org/abs/2410.10563)

Jiacheng Chen, Tianhao Liang, Sherman Siu, Zhengqing Wang, Kai Wang, Yubo Wang, Yuansheng Ni, Wang Zhu, **Ziyan Jiang**, Bohan Lyu, Dongfu Jiang, Xuan He, Yuan Liu, Hexiang Hu, Xiang Yue, Wenhu Chen

[**Project Page**](https://tiger-ai-lab.github.io/MEGA-Bench/)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICASSP 2025</div><img src='images/kg-rec.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Knowledge Enhanced Multi-Domain Recommendations in an AI Assistant Application](https://ieeexplore.ieee.org/abstract/document/10889248)

Elan Markowitz, **Ziyan Jiang**, Fan Yang, Xing Fan, Zheng Chen, Greg Ver Steeg

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/mmlu-pro.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://arxiv.org/pdf/2406.01574)

Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, **Ziyan Jiang**, Tianle Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, Wenhu Chen

[**Project Page**](https://github.com/TIGER-AI-Lab/MMLU-Pro)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2024</div><img src='images/videoscore.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[VideoScore: Building Automatic Metrics to Simulate Fine-grained Human Feedback for Video Generation](https://arxiv.org/abs/2406.15252)

Xuan He, Dongfu Jiang, Ge Zhang, Max Ku, Achint Soni, Sherman Siu, Haonan Chen, Abhranil Chandra, **Ziyan Jiang**, Aaran Arulraj, Kai Wang, Quy Duc Do, Yuansheng Ni, Bohan Lyu, Yaswanth Narsupalli, Rongqi Fan, Zhiheng Lyu, Yuchen Lin, Wenhu Chen

[**Project Page**](https://tiger-ai-lab.github.io/VideoScore/)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2024 (Findings)</div><img src='images/ssrm.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Semi-Supervised Reward Modeling via Iterative Self-Training](https://arxiv.org/abs/2409.06903)

Yifei He, Haoxiang Wang, **Ziyan Jiang**, Alexandros Papangelis, Han Zhao

[**Code**](https://github.com/RLHFlow/RLHF-Reward-Modeling/tree/main/pair-pm/SSRM)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NAACL 2024 (Findings)</div><img src='images/recmind.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[RecMind: Large Language Model Powered Agent For Recommendation](https://arxiv.org/abs/2308.14296)

Yancheng Wang, **Ziyan Jiang**, Zheng Chen, Fan Yang, Yingxue Zhou, Eunah Cho, Xing Fan, Xiaojiang Huang, Yanbin Lu, Yingzhen Yang

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2023 (Industry)</div><img src='images/cdfs.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Graph Meets LLM: A Novel Approach to Collaborative Filtering for Robust Conversational Understanding](https://aclanthology.org/2023.emnlp-industry.75/)

Zheng Chen\*, **Ziyan Jiang\***, Fan Yang\*, Eunah Cho, Xing Fan, Xiaojiang Huang, Yanbin Lu, Aram Galstyan

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICASSP 2023</div><img src='images/kg-eco.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[KG-ECO: Knowledge Graph Enhanced Entity Correction for Query Rewriting](https://arxiv.org/abs/2302.10454)

Jinglun Cai, Mingda Li, **Ziyan Jiang**, Eunah Cho, Zheng Chen, Yang Liu, Xing Fan, Chenlei Guo

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2022 (Industry)</div><img src='images/pentatron.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PENTATRON: PErsonalized coNText-Aware Transformer for Retrieval-based cOnversational uNderstanding](https://arxiv.org/abs/2210.12308)

Niranjan Uma Naresh\*, **Ziyan Jiang\***, Ankit\*, Sungjin Lee, Jie Hao, Xing Fan, Chenlei Guo

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2021</div><img src='images/hashtag.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Black-box Attacks on Spoofing Countermeasures Using Transferability of Adversarial Examples](https://aclanthology.org/2021.emnlp-main.616/)

Yuji Zhang, Yubo Zhang, Chunpu Xu, Jing Li, **Ziyan Jiang**, Baolin Peng

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Interspeech 2020</div><img src='images/iem.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Black-box Attacks on Spoofing Countermeasures Using Transferability of Adversarial Examples](https://www.isca-archive.org/interspeech_2020/zhang20ha_interspeech.pdf)

Yuekai Zhang, **Ziyan Jiang**, Jesús Villalba, Najim Dehak

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ASRU 2019</div><img src='images/espnet.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[A Comparative Study on Transformer vs RNN in Speech Applications](https://arxiv.org/abs/1909.06317)

Shigeki Karita, Nanxin Chen, Tomoki Hayashi, Takaaki Hori, Hirofumi Inaguma, **Ziyan Jiang**, Masao Someki, Nelson Enrique Yalta Soplin, Ryuichi Yamamoto, Xiaofei Wang, Shinji Watanabe, Takenori Yoshimura, Wangyou Zhang

</div>
</div>


- <span class='paper-badge'>Gen-IR@SIGIR 2023</span> [PALR: Personalization Aware LLMs for Recommendation](https://arxiv.org/abs/2305.07622), Fan Yang\*, Zheng Chen\*, **Ziyan Jiang\***, Eunah Cho, Xiaojiang Huang, Yanbin Lu
- <span class='paper-badge'>NLP4ConvAI@EMNLP 2021</span> [Personalized search-based query rewrite system for conversational ai](https://aclanthology.org/2021.nlp4convai-1.17/), Eunah Cho, **Ziyan Jiang**, Jie Hao, Zheng Chen, Saurabh Gupta, Xing Fan, Chenlei Guo




<h1 id="educations">📖 Educations</h1>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='images/jhu_logo.jpg' alt="sym" style="width: 200px; height: 200px; object-fit: contain;"></div></div>
<div class='paper-box-text' markdown="1">
- *2018.08 - 2020.05*
- Johns Hopkins University 
- Electrical and Computer Engineering, M.S.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='images/nju_logo.png' alt="sym" style="width: 200px; height: 200px; object-fit: contain;"></div></div>
<div class='paper-box-text' markdown="1">
- *2014.09 - 2018.07*
- Nanjing University 
- Acoustics, B.S.
</div>
</div>


<h1 id="working-experiences">💻 Working Experiences</h1>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='images/amazon_logo.jpg' alt="sym" style="width: 200px; height: 200px; object-fit: contain;"></div></div>
<div class='paper-box-text' markdown="1">
- *2020.07 - 2024.08*
- Amazon Alexa AI & AGI 
- Applied Scientist I -> Applied Scientist II
</div>
</div>



<h1 id="services">🧐 Services</h1>
- Conference Reviewer: NeurIPS(2024-Present), ICLR(2024-Present), ACL ARR(2023-Present), ICASSP(2024-Present)
- Journal Reviewer: IEEE Access, TOIS
- Workshop Organizer: [The First Workshop on Personalized Generative AI (@CIKM2023)](https://sites.google.com/view/pgai2023/home), [The Second Workshop on Generative Information Retrieval (@SIGIR2024)](https://coda.io/@sigir/gen-ir-24)
