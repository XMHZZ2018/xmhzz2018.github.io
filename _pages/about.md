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

I'm a CS Ph.D. student in the [NLP Lab](http://nlp.cs.ucsb.edu/) at UC Santa Barbara (UCSB), advised by [Prof. Shiyu Chang](https://code-terminator.github.io/). I'm currently a research intern at <img src='images/salesforce_logo.svg' alt="Salesforce" style="height: 18px; vertical-align: middle;"> Salesforce AI Research. Previously, I earned my bachelor's degree from Nanjing University and my master's degree from Johns Hopkins University. Before starting my Ph.D., I was a full-time applied scientist at <img src='images/amazon_logo.jpg' alt="Amazon" style="height: 18px; vertical-align: middle;"> Amazon Alexa AI / AGI.

My current research interests are self-evolving agents, agentic RL, and multimodal learning. I have previously worked on conversational AI, information retrieval, and LLMs for personalization.

I’m always open to collaboration opportunities. If you're interested, feel free to reach out to me via **ziyanjiang528@gmail.com**



{% include affiliations.html %}

# News
{: #news}
- *2026.09*: We released [WorldAuditBench](https://ucsb-nlp-chang.github.io/WorldAuditBench/), a benchmark for interactive 3D world auditing with multimodal agents.
- *2026.07*: MMEB-V3 has been accepted to COLM 2026.
- *2026.01*: I will be joining Salesforce Research as a research intern this coming summer.
- *2026.01*: VLM2Vec-V2 has been accepted to TMLR.
- *2025.04*: I’ve moved my personal homepage to this new site; the old one is now deprecated.




{% include_relative includes/pub.md %}



<h1 id="services">Services</h1>
- Conference Reviewer: NeurIPS(2024-Present), ICLR(2024-Present), ACL ARR(2023-Present), ICASSP(2024-Present)
- Journal Reviewer: IEEE Access, TOIS
- Workshop Organizer: [The First Workshop on Personalized Generative AI (@CIKM2023)](https://sites.google.com/view/pgai2023/home), [The Second Workshop on Generative Information Retrieval (@SIGIR2024)](https://coda.io/@sigir/gen-ir-24)
