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

{% include internship-notice.html %}

I'm a CS Ph.D. student in the [NLP Lab](http://nlp.cs.ucsb.edu/) at UC Santa Barbara (UCSB), advised by [Prof. Shiyu Chang](https://code-terminator.github.io/) and [Dr. Yang Zhang](https://mitibm.mit.edu/people/yang-zhang/) (MIT-IBM Watson AI Lab). I'm currently a research intern at <img src='images/salesforce_logo.svg' alt="Salesforce" style="height: 18px; vertical-align: middle;"> Salesforce AI Research, hosted by [Dr. Semih Yavuz](https://www.salesforce.com/blog/author/semih-yavuz/) and [Prof. Shafiq Joty](https://raihanjoty.github.io/). I have also closely collaborated with [Prof. Wenhu Chen](https://wenhuchen.github.io/) at [TIGER Lab](https://wenhuchen.github.io/lab.html).

Previously, I earned my bachelor's degree from <span class="bio-logo" aria-hidden="true"><img src="images/nju_logo.png" alt="" width="18" height="18"></span> Nanjing University and my master's degree from <span class="bio-logo bio-logo--jhu" aria-hidden="true"><img src="images/jhu_logo.jpg" alt="" width="18" height="18"></span> Johns Hopkins University. Before starting my Ph.D., I was a full-time applied scientist at <img src='images/amazon_logo.jpg' alt="Amazon" style="height: 18px; vertical-align: middle;"> Amazon Alexa AI / AGI.

**My current research interests are self-evolving agents, agentic post-training, and multimodal learning.** I have previously worked on conversational AI, information retrieval, and LLMs for personalization.



{% include affiliations.html %}

{% include news.html %}




{% include_relative includes/pub.md %}



<h1 id="services">Services</h1>
- Conference Reviewer: NeurIPS (2024–), ICLR (2024–), ICML (2026–), ACL ARR (2023–), ICASSP (2024–)
- Journal Reviewer: IEEE Access, TOIS, TMLR
- Workshop Organizer: [The First Workshop on Personalized Generative AI (@CIKM2023)](https://sites.google.com/view/pgai2023/home), [The Second Workshop on Generative Information Retrieval (@SIGIR2024)](https://coda.io/@sigir/gen-ir-24)
