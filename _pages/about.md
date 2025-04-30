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

I'm an incoming Ph.D. student in Computer Science at UC Santa Barbara, advised by [Prof. Shiyu Chang](https://code-terminator.github.io/). Previously, I earned my bachelor's degree from Nanjing University and my master's degree from Johns Hopkins University. Before starting my Ph.D., I spent several years as a full-time applied scientist at Amazon Alexa AI and Amazon AGI.

My research focuses on natural language processing, information retrieval, and speech recognition.



# 🔥 News
- *2025.04*: I’ve moved my personal homepage to this new site; the old one is now deprecated. (The new one is still in construction.) 

# 📝 Publications (*: equal contribution/co-first author)

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/vlm2vec.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[VLM2Vec: Training Vision-Language Models for Massive Multimodal Embedding Tasks](https://arxiv.org/abs/2410.05160)

**Ziyan Jiang**, Rui Meng, Xinyi Yang, Semih Yavuz, Yingbo Zhou, Wenhu Chen

[**Project Page**](https://tiger-ai-lab.github.io/VLM2Vec/)
- We develop a universal multimodal embedding benchmark, MMEB, along with VLM2Vec, an embedding model adapted from vision-language models (VLMs).
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/mega-bench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks](https://arxiv.org/abs/2410.10563)

Jiacheng Chen, Tianhao Liang, Sherman Siu, Zhengqing Wang, Kai Wang, Yubo Wang, Yuansheng Ni, Wang Zhu, **Ziyan Jiang**, Bohan Lyu, Dongfu Jiang, Xuan He, Yuan Liu, Hexiang Hu, Xiang Yue, Wenhu Chen

[**Project Page**](https://tiger-ai-lab.github.io/MEGA-Bench/)
- We present MEGA-Bench, an evaluation suite that scales multimodal evaluation to over 500 real-world tasks.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICASSP 2025</div><img src='images/kg-rec.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Knowledge Enhanced Multi-Domain Recommendations in an AI Assistant Application](https://ieeexplore.ieee.org/abstract/document/10889248)

Elan Markowitz, **Ziyan Jiang**, Fan Yang, Xing Fan, Zheng Chen, Greg Ver Steeg

- We explore unifying knowledge enhanced recommendation with multi-domain recommendation systems in a conversational AI assistant application.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/mmlu-pro.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://arxiv.org/pdf/2406.01574)

Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, **Ziyan Jiang**, Tianle Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, Wenhu Chen

[**Project Page**](https://github.com/TIGER-AI-Lab/MMLU-Pro)
- We introduce MMLU-Pro, an enhanced dataset designed to extend the mostly knowledge-driven MMLU benchmark by integrating more challenging, reasoning-focused questions and expanding the choice set from four to ten options.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2024</div><img src='images/videoscore.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[VideoScore: Building Automatic Metrics to Simulate Fine-grained Human Feedback for Video Generation](https://arxiv.org/abs/2406.15252)

Xuan He, Dongfu Jiang, Ge Zhang, Max Ku, Achint Soni, Sherman Siu, Haonan Chen, Abhranil Chandra, **Ziyan Jiang**, Aaran Arulraj, Kai Wang, Quy Duc Do, Yuansheng Ni, Bohan Lyu, Yaswanth Narsupalli, Rongqi Fan, Zhiheng Lyu, Yuchen Lin, Wenhu Chen

[**Project Page**](https://tiger-ai-lab.github.io/VideoScore/)
- We release VideoFeedback, the first largescale dataset containing human-provided multiaspect score over 37.6K synthesized videos
from 11 existing video generative models. We train VideoScore based on VideoFeedback to enable automatic video quality assessment.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2024 (Findings)</div><img src='images/ssrm.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Semi-Supervised Reward Modeling via Iterative Self-Training](https://arxiv.org/abs/2409.06903)

Yifei He, Haoxiang Wang, **Ziyan Jiang**, Alexandros Papangelis, Han Zhao

[**Code**](https://github.com/RLHFlow/RLHF-Reward-Modeling/tree/main/pair-pm/SSRM)
- We propose Semi-Supervised Reward Modeling (SSRM), an approach that enhances RM training using unlabeled data
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NAACL 2024 (Findings)</div><img src='images/recmind.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[RecMind: Large Language Model Powered Agent For Recommendation](https://arxiv.org/abs/2308.14296)

Yancheng Wang, **Ziyan Jiang**, Zheng Chen, Fan Yang, Yingxue Zhou, Eunah Cho, Xing Fan, Xiaojiang Huang, Yanbin Lu, Yingzhen Yang

- We design an LLMpowered autonomous recommender agent, RecMind, which is capable of leveraging external knowledge, utilizing tools with careful planning to provide zero-shot personalized recommendations.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2023 (Industry)</div><img src='images/cdfs.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Graph Meets LLM: A Novel Approach to Collaborative Filtering for Robust Conversational Understanding](https://aclanthology.org/2023.emnlp-industry.75/)

Zheng Chen\*, **Ziyan Jiang\***, Fan Yang\*, Eunah Cho, Xing Fan, Xiaojiang Huang, Yanbin Lu, Aram Galstyan

- We introduce our Collaborative Query Rewriting approach, which utilizes underlying topological information to assist in rewriting defective queries arising from unseen user interactions. 
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICASSP 2023</div><img src='images/kg-eco.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[KG-ECO: Knowledge Graph Enhanced Entity Correction for Query Rewriting](https://arxiv.org/abs/2302.10454)

Jinglun Cai, Mingda Li, **Ziyan Jiang**, Eunah Cho, Zheng Chen, Yang Liu, Xing Fan, Chenlei Guo

- We propose KG-ECO: Knowledge Graph enhanced Entity COrrection for query rewriting, an entity correction system with corrupt entity
span detection and entity retrieval/re-ranking functionalities.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2022 (Industry)</div><img src='images/pentatron.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PENTATRON: PErsonalized coNText-Aware Transformer for Retrieval-based cOnversational uNderstanding](https://arxiv.org/abs/2210.12308)

Niranjan Uma Naresh\*, **Ziyan Jiang\***, Ankit\*, Sungjin Lee, Jie Hao, Xing Fan, Chenlei Guo

- We build and evaluate a scalable entity correction system, PENTATRON, which leverages a parametric transformer-based language model to learn patterns from in-session customer-device interactions coupled with a non-parametric personalized entity index to compute the correct query.
</div>
</div>



# 🧐 Service
- Conference reviewer: NeurIPS, ICLR, ARR (ACL, EMNLP, NAACL, EACL), ICASSP
- Journal reviewer: IEEE Access, TOIS
- Workshop Organizer: [The First Workshop on Personalized Generative AI (@CIKM2023)](https://sites.google.com/view/pgai2023/home), [The Second Workshop on Generative Information Retrieval (@SIGIR2024)](https://coda.io/@sigir/gen-ir-24)



# 📖 Educations
- *2019.06 - 2022.04 (now)*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2015.09 - 2019.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 



# 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)

# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China.
