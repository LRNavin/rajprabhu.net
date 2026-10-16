#!/usr/bin/env python3
"""Builds the static pages for rajprabhu.net.

All content (publications, news, CV) lives in this file. Edit the data near the top,
then run `python3 scripts/build.py` from the repository root and commit the
regenerated HTML files together with your change.
"""
import html, math, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)  # the repository root is the published site
ME = "Navin Raj Prabhu"
SITE = "https://rajprabhu.net"

LINKS = {
    "email": "mailto:lr.navin@gmail.com",
    "scholar": "https://scholar.google.com/citations?user=mKH8j3AAAAAJ&hl=en",
    "github": "https://github.com/LRNavin",
    "linkedin": "https://www.linkedin.com/in/navin-lr/",
    "uhh": "https://www.inf.uni-hamburg.de/en/inst/ab/sp/people/x-dr-raj-prabhu-alumni.html",
    "thesis": "https://ediss.sub.uni-hamburg.de/handle/ediss/12386",
    "thesis_news": "https://www.inf.uni-hamburg.de/en/inst/ab/sp/newsfeed/2026dissertation-navinrajprabhu.html",
    "aicoustics": "https://ai-coustics.com/",
}

THEMES = {
    "recognition": "Emotion recognition",
    "synthesis": "Emotion synthesis",
    "groups": "Groups and interaction",
}

E = html.escape

# ---------------------------------------------------------------- data
PUBS = [
    dict(
        id="group-affect-taffc-2026",
        title="Dynamics of Collective Group Affect: Group-level Annotations and the Multimodal Modeling of Convergence and Divergence",
        authors=[ME, "Maria Tsfasman", "Catharine Oertel", "Timo Gerkmann", "Nale Lehmann-Willenbrock"],
        venue="IEEE Transactions on Affective Computing", detail="vol. 17, no. 1, pp. 1014–1029", year=2026,
        themes=["groups", "recognition"],
        links=[("DOI", "https://doi.org/10.1109/TAFFC.2025.3643752"), ("arXiv", "https://arxiv.org/abs/2409.08578")],
        abstract="Collaborating in a group, whether face-to-face or virtually, involves continuously expressing emotions and interpreting those of other group members. Therefore, understanding group affect is essential to comprehending how groups interact and succeed in collaborative efforts. In this study, we move beyond individual-level affect and investigate group-level affect — a collective phenomenon that reflects the shared mood or emotions among group members at a particular moment. As the first in literature, we gather annotations for group-level affective expressions using a fine-grained temporal approach (15 second windows) that also captures the inherent dynamics of the collective construct. To this end, we use trained annotators and an annotation procedure specifically tuned to capture the entire scope of the group interaction. In addition, we model group affect dynamics over time. One way to study the ebb and flow of group affect in group interactions is to model the underlying convergence (driven by emotional contagion) and divergence (resulting from emotional reactivity) of affective expressions amongst group members. To capture these interpersonal dynamics, we extract synchrony based features from both audio and visual social signal cues. An analysis of these features reveals that interacting groups tend to diverge in terms of their social signals along neutral levels of group affect, and converge along extreme levels of affect expression. We further present results on the predictive modeling of dynamic group affect which underscores the importance of using synchrony-based features in the modeling process, as well as the multimodal nature of group affect. We anticipate that the presented models will serve as the baselines of future research on the automatic recognition of dynamic group affect.",
        abstract_note="Abstract of the arXiv preprint.",
        selected=True,
    ),
    dict(
        id="duration-asru-2025",
        title="Enhancing In-the-Wild Speech Emotion Conversion with Resynthesis-based Duration Modeling",
        authors=[ME, "Danilo de Oliveira", "Nale Lehmann-Willenbrock", "Timo Gerkmann"],
        venue="IEEE Workshop on Automatic Speech Recognition and Understanding (ASRU)", detail="Honolulu, USA, December 2025", year=2025,
        themes=["synthesis"],
        links=[("arXiv", "https://arxiv.org/abs/2508.11535"), ("Audio examples", "https://sp-uhh.github.io/emoconv-gen")],
        abstract="Speech Emotion Conversion aims to modify the emotion expressed in input speech while preserving lexical content and speaker identity. Recently, generative modeling approaches have shown promising results in changing local acoustic properties such as fundamental frequency, spectral envelope and energy, but often lack the ability to control the duration of sounds. To address this, we propose a duration modeling framework using resynthesis-based discrete content representations, enabling modification of speech duration to reflect target emotions and achieve controllable speech rates without using parallel data. Experimental results reveal that the inclusion of the proposed duration modeling framework significantly enhances emotional expressiveness, in the in-the-wild MSP-Podcast dataset. Analyses show that low-arousal emotions correlate with longer durations and slower speech rates, while high-arousal emotions produce shorter, faster speech.",
        selected=True,
    ),
    dict(
        id="behavioral-labels-oup-2025",
        title="Ground-Truth of Behavioral Labels in Group Interactions: Subjectivity and Uncertainty",
        authors=[ME, "Vanessa Begemann", "Timo Gerkmann", "Nale Lehmann-Willenbrock"],
        venue="Computational Group and Team Dynamics: Forging an Interdisciplinary Science", detail="Book chapter, Oxford University Press, June 2025", year=2025,
        themes=["groups", "recognition"],
        links=[],
        abstract=None,
    ),
    dict(
        id="emoconv-diff-icassp-2024",
        title="EMOCONV-Diff: Diffusion-Based Speech Emotion Conversion for Non-Parallel and In-the-Wild Data",
        authors=[ME, "Bunlong Lay", "Simon Welker", "Nale Lehmann-Willenbrock", "Timo Gerkmann"],
        venue="IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)", detail="Seoul, Korea, April 2024, pp. 11651–11655", year=2024,
        themes=["synthesis"],
        links=[("arXiv", "https://arxiv.org/abs/2309.07828"), ("PDF", "https://arxiv.org/pdf/2309.07828")],
        abstract="Speech emotion conversion is the task of converting the expressed emotion of a spoken utterance to a target emotion while preserving the lexical content and speaker identity. While most existing works in speech emotion conversion rely on acted-out datasets and parallel data samples, in this work we specifically focus on more challenging in-the-wild scenarios and do not rely on parallel data. To this end, we propose a diffusion-based generative model for speech emotion conversion, the EmoConv-Diff, that is trained to reconstruct an input utterance while also conditioning on its emotion. Subsequently, at inference, a target emotion embedding is employed to convert the emotion of the input utterance to the given target emotion. As opposed to performing emotion conversion on categorical representations, we use a continuous arousal dimension to represent emotions while also achieving intensity control. We validate the proposed methodology on a large in-the-wild dataset, the MSP-Podcast v1.10. Our results show that the proposed diffusion model is indeed capable of synthesizing speech with a controllable target emotion. Crucially, the proposed approach shows improved performance along the extreme values of arousal and thereby addresses a common challenge in the speech emotion conversion literature.",
        selected=True,
    ),
    dict(
        id="bnn-ldl-taffc-2023",
        title="End-to-End Label Uncertainty Modeling in Speech Emotion Recognition using Bayesian Neural Networks and Label Distribution Learning",
        authors=[ME, "Nale Lehmann-Willenbrock", "Timo Gerkmann"],
        venue="IEEE Transactions on Affective Computing", detail="vol. 15, no. 2, pp. 579–592 (published online June 2023)", year=2023,
        themes=["recognition"],
        links=[("DOI", "https://doi.org/10.1109/TAFFC.2023.3283595"), ("arXiv", "https://arxiv.org/abs/2209.15449")],
        abstract="To train machine learning algorithms to predict emotional expressions in terms of arousal and valence, annotated datasets are needed. However, as different people perceive others' emotional expressions differently, their annotations are subjective. To account for this, annotations are typically collected from multiple annotators and averaged to obtain ground-truth labels. However, when exclusively trained on this averaged ground-truth, the model is agnostic to the inherent subjectivity in emotional expressions. In this work, we therefore propose an end-to-end Bayesian neural network capable of being trained on a distribution of annotations to also capture the subjectivity-based label uncertainty. Instead of a Gaussian, we model the annotation distribution using Student's t-distribution, which also accounts for the number of annotations available. We derive the corresponding Kullback-Leibler divergence loss and use it to train an estimator for the annotation distribution, from which the mean and uncertainty can be inferred. We validate the proposed method using two in-the-wild datasets. We show that the proposed t-distribution based approach achieves state-of-the-art uncertainty modeling results in speech emotion recognition, and also consistent results in cross-corpora evaluations. Furthermore, analyses reveal that the advantage of a t-distribution over a Gaussian grows with increasing inter-annotator correlation and a decreasing number of annotations available.",
        selected=True,
    ),
    dict(
        id="pcq-taffc-2023",
        title="Perceived Conversation Quality in Spontaneous Interactions",
        authors=["Chirag Raman*", ME + "*", "Hayley Hung"],
        venue="IEEE Transactions on Affective Computing", detail="vol. 14, no. 4, pp. 2901–2912", year=2023,
        note="* Equal contribution",
        themes=["groups"],
        links=[("arXiv", "https://arxiv.org/abs/2207.05791")],
        abstract="The quality of daily spontaneous conversations is of importance towards both our well-being as well as the development of interactive social agents. Prior research directly studying the quality of social conversations has operationalized it in narrow terms, associating greater quality to less small talk. Other works taking a broader perspective of interaction experience have indirectly studied quality through one of the several overlapping constructs such as rapport or engagement, in isolation. In this work we bridge this gap by proposing a holistic conceptualization of conversation quality, building upon the collaborative attributes of cooperative conversation floors. Taking a multilevel perspective of conversation, we develop and validate two instruments for perceived conversation quality (PCQ) at the individual and group levels. Specifically, we motivate capturing external raters' gestalt impressions of participant experiences from thin slices of behavior, and collect annotations of PCQ on the publicly available MatchNMingle dataset of in-the-wild mingling conversations. Finally, we present an analysis of behavioral features that are predictive of PCQ. We find that for the conversations in MatchNMingle, raters tend to associate smaller group sizes, equitable speaking turns with fewer interruptions, and time taken for synchronous bodily coordination with higher PCQ.",
    ),
    dict(
        id="ssl-sec-itg-2023",
        title="In-the-wild Speech Emotion Conversion Using Disentangled Self-Supervised Representations and Neural Vocoder-based Resynthesis",
        authors=[ME, "Nale Lehmann-Willenbrock", "Timo Gerkmann"],
        venue="15th ITG Conference on Speech Communication", detail="Aachen, Germany, September 2023", year=2023,
        themes=["synthesis"],
        links=[("DOI", "https://doi.org/10.30420/456164034"), ("arXiv", "https://arxiv.org/abs/2306.01916")],
        abstract="Speech emotion conversion aims to convert the expressed emotion of a spoken utterance to a target emotion while preserving the lexical information and the speaker's identity. In this work, we specifically focus on in-the-wild emotion conversion where parallel data does not exist, and the problem of disentangling lexical, speaker, and emotion information arises. In this paper, we introduce a methodology that uses self-supervised networks to disentangle the lexical, speaker, and emotional content of the utterance, and subsequently uses a HiFiGAN vocoder to resynthesise the disentangled representations to a speech signal of the targeted emotion. For better representation and to achieve emotion intensity control, we specifically focus on the arousal dimension of continuous representations, as opposed to performing emotion conversion on categorical representations. We test our methodology on the large in-the-wild MSP-Podcast dataset. Results reveal that the proposed approach is aptly conditioned on the emotional content of input speech and is capable of synthesising natural-sounding speech for a target emotion. Results further reveal that the methodology better synthesises speech for mid-scale arousal (2 to 6) than for extreme arousal (1 and 7).",
    ),
    dict(
        id="distilled-ser-interspeech-2023",
        title="Leveraging Semantic Information for Efficient Self-Supervised Emotion Recognition with Audio-Textual Distilled Models",
        authors=["Danilo de Oliveira", ME, "Timo Gerkmann"],
        venue="Interspeech", detail="Dublin, Ireland, August 2023", year=2023,
        themes=["recognition"],
        links=[("DOI", "https://doi.org/10.21437/Interspeech.2023-1758"), ("arXiv", "https://arxiv.org/abs/2305.19184")],
        abstract="In large part due to their implicit semantic modeling, self-supervised learning (SSL) methods have significantly increased the performance of valence recognition in speech emotion recognition (SER) systems. Yet, their large size may often hinder practical implementations. In this work, we take HuBERT as an example of an SSL model and analyze the relevance of each of its layers for SER. We show that shallow layers are more important for arousal recognition while deeper layers are more important for valence. This observation motivates the importance of additional textual information for accurate valence recognition, as the distilled framework lacks the depth of its large-scale SSL teacher. Thus, we propose an audio-textual distilled SSL framework that, while having only ~20% of the trainable parameters of a large SSL model, achieves on par performance across the three emotion dimensions (arousal, valence, dominance) on the MSP-Podcast v1.10 dataset.",
    ),
    dict(
        id="t-dist-acii-2022",
        title="Label Uncertainty Modeling and Prediction for Speech Emotion Recognition using t-Distributions",
        authors=[ME, "Nale Lehmann-Willenbrock", "Timo Gerkmann"],
        venue="International Conference on Affective Computing and Intelligent Interaction (ACII)", detail="Nara, Japan, October 2022", year=2022,
        themes=["recognition"],
        links=[("arXiv", "https://arxiv.org/abs/2207.12135")],
        abstract="As different people perceive others' emotional expressions differently, their annotation in terms of arousal and valence are per se subjective. To address this, these emotion annotations are typically collected by multiple annotators and averaged across annotators in order to obtain labels for arousal and valence. However, besides the average, also the uncertainty of a label is of interest, and should also be modeled and predicted for automatic emotion recognition. In the literature, for simplicity, label uncertainty modeling is commonly approached with a Gaussian assumption on the collected annotations. However, as the number of annotators is typically rather small due to resource constraints, we argue that the Gaussian approach is a rather crude assumption. In contrast, in this work we propose to model the label distribution using a Student's t-distribution which allows us to account for the number of annotations available. With this model, we derive the corresponding Kullback-Leibler divergence based loss function and use it to train an estimator for the distribution of emotion labels, from which the mean and uncertainty can be inferred. Through qualitative and quantitative analysis, we show the benefits of the t-distribution over a Gaussian distribution. Results reveal that our t-distribution based approach improves over the Gaussian approach with state-of-the-art uncertainty modeling results in speech-based emotion recognition, along with an optimal and even faster convergence.",
    ),
    dict(
        id="bnn-arousal-interspeech-2022",
        title="End-To-End Label Uncertainty Modeling for Speech-based Arousal Recognition Using Bayesian Neural Networks",
        authors=[ME, "Guillaume Carbajal", "Nale Lehmann-Willenbrock", "Timo Gerkmann"],
        venue="Interspeech", detail="Incheon, Korea, September 2022", year=2022,
        themes=["recognition"],
        links=[("ISCA Archive", "https://www.isca-archive.org/interspeech_2022/prabhu22_interspeech.html"), ("arXiv", "https://arxiv.org/abs/2110.03299")],
        abstract="Emotions are subjective constructs. Recent end-to-end speech emotion recognition systems are typically agnostic to the subjective nature of emotions, despite their state-of-the-art performance. In this work, we introduce an end-to-end Bayesian neural network architecture to capture the inherent subjectivity in the arousal dimension of emotional expressions. To the best of our knowledge, this work is the first to use Bayesian neural networks for speech emotion recognition. At training, the network learns a distribution of weights to capture the inherent uncertainty related to subjective arousal annotations. To this end, we introduce a loss term that enables the model to be explicitly trained on a distribution of annotations, rather than training them exclusively on mean or gold-standard labels. We evaluate the proposed approach on the AVEC'16 dataset. Qualitative and quantitative analysis of the results reveals that the proposed model can aptly capture the distribution of subjective arousal annotations, with state-of-the-art results in mean and standard deviation estimations for uncertainty modeling.",
        selected=True,
    ),
    dict(
        id="conversation-quality-icmi-2020",
        title="Defining and Quantifying Conversation Quality in Spontaneous Interactions",
        authors=[ME, "Chirag Raman", "Hayley Hung"],
        venue="Companion Publication of the International Conference on Multimodal Interaction (ICMI)", detail="2020, pp. 196–205", year=2020,
        themes=["groups"],
        links=[("arXiv", "https://arxiv.org/abs/2009.12842")],
        abstract="Social interactions in general are multifaceted and there exists a wide set of factors and events that influence them. In this paper, we quantify social interactions with a holistic viewpoint on individual experiences, particularly focusing on non-task-directed spontaneous interactions. To achieve this, we design a novel perceived measure, the perceived Conversation Quality, which intends to quantify spontaneous interactions by accounting for several socio-dimensional aspects of individual experiences. To further quantitatively study spontaneous interactions, we devise a questionnaire which measures the perceived Conversation Quality, at both the individual- and at the group- level. Using the questionnaire, we collected perceived annotations for conversation quality in a publicly available dataset using naive annotators. The results of the analysis performed on the distribution and the inter-annotator agreeability shows that naive annotators tend to agree less in cases of low conversation quality samples, especially while annotating for group-level conversation quality.",
    ),
]

THESIS = dict(
    id="dissertation-2026",
    title="Probabilistic and Generative Modeling for Emotion Recognition and Synthesis",
    authors=[ME],
    venue="PhD dissertation, University of Hamburg", detail="Defended 12 February 2026. Supervised by Timo Gerkmann and Nale Lehmann-Willenbrock", year=2026,
    themes=["recognition", "synthesis", "groups"],
    links=[("Full text (eDiss)", LINKS["thesis"]), ("Department news", LINKS["thesis_news"])],
    abstract=None,
)

NEWS = [
    ("2026-02", "Feb 2026",
     'Defended my PhD at the University of Hamburg: <a href="publications.html#dissertation-2026"><em>Probabilistic and Generative Modeling for Emotion Recognition and Synthesis</em></a>. '
     'Thank you to Carlos Busso for serving as external reviewer.'
     f'</p><figure class="news-photo"><a href="{LINKS["thesis_news"]}"><picture><source type="image/webp" srcset="assets/phd-defence.webp">'
     '<img src="assets/phd-defence.jpg" alt="Group photo after the PhD defence, with the external reviewer joining by video on the screen behind." width="733" height="414" loading="lazy"></picture></a>'
     f'<figcaption>After the defence, February 2026. <a href="{LINKS["thesis_news"]}">Read the department news</a></figcaption></figure><p class="sr-only">'),
    ("2026", "2026",
     'Our work on collective group affect, with annotations and multimodal models of convergence and divergence, is published in <a href="publications.html#group-affect-taffc-2026"><em>IEEE Transactions on Affective Computing</em></a>.'),
    ("2025-12", "Dec 2025",
     'Presented <a href="publications.html#duration-asru-2025">duration modeling for in-the-wild speech emotion conversion</a> at IEEE ASRU in Honolulu.'),
    ("2025-06", "Jun 2025",
     'A chapter on subjectivity and uncertainty in behavioral labels appeared in <a href="publications.html#behavioral-labels-oup-2025"><em>Computational Group and Team Dynamics</em></a> (Oxford University Press).'),
    ("2024-04", "Apr 2024",
     'Presented <a href="publications.html#emoconv-diff-icassp-2024">EMOCONV-Diff</a>, diffusion-based emotion conversion for in-the-wild speech, at ICASSP in Seoul.'),
]

EDUCATION = [
    dict(when="2021 – 2026", what="PhD in Computer Science", where="University of Hamburg, Germany",
         items=[
             'Dissertation: <a href="publications.html#dissertation-2026"><em>Probabilistic and Generative Modeling for Emotion Recognition and Synthesis</em></a>, defended February 2026',
             "Supervisors: Prof. Dr.-Ing. Timo Gerkmann (Signal Processing) and Prof. Dr. Nale Lehmann-Willenbrock (Industrial and Organizational Psychology)",
             "Probabilistic neural networks for uncertainty modeling in emotion recognition",
             "Diffusion- and GAN-based generative models for emotion-conditioned speech synthesis",
         ]),
    dict(when="2018 – 2020", what="MSc in Computer Science, Data Science track", where="Delft University of Technology, The Netherlands",
         items=[
             "Thesis: <em>Conversation Quality: Modeling in Free-Standing Conversational Groups</em>",
             "Supervisors: Dr. Hayley Hung and Dr. Chirag Raman",
             "Courses included Pattern Recognition, Deep Learning, Multivariate Data Analysis and Social Signal Processing",
         ]),
    dict(when="2011 – 2015", what="BTech in Computer Science", where="SRM University, Chennai, India",
         items=["Courses included Neural Networks, Pattern Recognition, Probability and Queuing Theory and Genetic Algorithms"]),
]

EXPERIENCE = [
    dict(when="Now", what="Machine Learning Researcher", where="ai-coustics, Berlin, Germany",
         items=[f'Working on audio intelligence for voice AI at <a href="{LINKS["aicoustics"]}">ai-coustics</a>.']),
    dict(when="2021 – 2025", what="Doctoral researcher", where="Signal Processing group, University of Hamburg",
         items=["Interdisciplinary project with the Industrial and Organizational Psychology group on the recognition and synthesis of affect"]),
    dict(when="2020", what="Research assistant", where="Interactive Intelligence Lab, TU Delft",
         items=["Conversational AI and social robots for social skills training",
                "Adaptive robot behaviour based on a partner's behavioural cues, using FurhatSDK, OpenFace and Microsoft PSI"]),
    dict(when="2019", what="Data science intern", where="Momo Medical, Delft",
         items=["Moved pose detection from heuristics to data-driven modeling with time-series neural networks",
                "Designed the data collection pipeline from an exploratory analysis of data variance"]),
    dict(when="2015 – 2018", what="Full-stack developer, founding employee", where="Terraa Farm Fresh, Bangalore",
         items=["Worked across iOS development, backend systems, deep learning and operations research for an online grocery platform",
                "Built order allocation and subscription ledger systems, demand forecasting (TensorFlow, Google Cloud) and analytics dashboards (BigQuery)"]),
]

TEACHING = [
    ("2021 – 2025", "Supervised 7 bachelor's and 4 master's theses"),
    ("Summer 2025", "Speech Signal Processing"),
    ("Winter 2024/25", "Deep Learning for Multimodal Data Science; Deep Learning for Signal Processing"),
    ("Summer 2024", "Machine Learning"),
    ("Winter 2023/24", "Software Engineering"),
]

INTERESTS = ["Generative modeling", "Probabilistic and uncertainty modeling", "Speech emotion recognition",
             "Emotion-conditioned speech synthesis", "Speech emotion conversion", "Social signal processing",
             "Group affect", "Multimodal learning"]

# ---------------------------------------------------------------- helpers
ICON_SUN = '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M4.6 4.6l1.6 1.6M17.8 17.8l1.6 1.6M2.5 12h2.2M19.3 12h2.2M4.6 19.4l1.6-1.6M17.8 6.2l1.6-1.6"/></svg>'
ICON_MOON = '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z"/></svg>'

THEME_BOOT = """<script>(function(){try{var t=localStorage.getItem('theme');if(t==='dark'||t==='light'){document.documentElement.setAttribute('data-theme',t);}}catch(e){}})();</script>"""


def page(title, desc, current, body, path):
    nav = [("index.html", "Research"), ("publications.html", "Publications"), ("cv.html", "CV")]
    nav_html = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>' for href, label in nav)
    canonical = SITE + "/" + ("" if path == "index.html" else path)
    person = {
        "@context": "https://schema.org", "@type": "Person", "name": ME, "honorificPrefix": "Dr.",
        "url": SITE, "jobTitle": "Machine Learning Researcher", "image": SITE + "/assets/portrait.jpg",
        "alumniOf": [{"@type": "CollegeOrUniversity", "name": "University of Hamburg"},
                     {"@type": "CollegeOrUniversity", "name": "Delft University of Technology"}],
        "worksFor": {"@type": "Organization", "name": "ai-coustics", "url": LINKS["aicoustics"]},
        "sameAs": [LINKS["scholar"], LINKS["github"], LINKS["linkedin"], LINKS["uhh"]],
        "knowsAbout": INTERESTS,
    }
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/portrait.jpg">
<meta name="theme-color" content="#f3f4ef" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#111513" media="(prefers-color-scheme: dark)">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/source-serif-4-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/schibsted-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
{THEME_BOOT}
<link rel="stylesheet" href="assets/style.css">
<script type="application/ld+json">{json.dumps(person)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="inner">
    <a class="wordmark" href="index.html"><span class="full">Navin Raj Prabhu</span><span class="short">N. R. Prabhu</span></a>
    <nav class="site-nav" aria-label="Main">{nav_html}</nav>
    <button class="theme-toggle" type="button" aria-label="Switch to dark mode">{ICON_SUN}{ICON_MOON}</button>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-foot">
  <div class="inner">
    <span>© 2026 Navin Raj Prabhu. Portrait: UHH, RRZ/MCC, Mentz.</span>
    <span class="foot-links"><a href="{LINKS['email']}">Email</a><a href="{LINKS['scholar']}">Google Scholar</a><a href="{LINKS['github']}">GitHub</a><a href="{LINKS['linkedin']}">LinkedIn</a></span>
  </div>
</footer>
<script src="assets/main.js" defer></script>
</body>
</html>
"""


def authors_html(authors):
    out = []
    for a in authors:
        if a.rstrip("*") == ME:
            out.append(f'<span class="me">{E(a)}</span>')
        else:
            out.append(E(a))
    return ", ".join(out)


def pub_html(p, with_abstract=True, heading="h3"):
    primary = p["links"][0][1] if p["links"] else None
    title = E(p["title"])
    if primary:
        title = f'<a href="{primary}">{title}</a>'
    venue = f'{E(p["venue"])}'
    detail = f', <span class="pub-note">{E(p["detail"])}</span>' if p.get("detail") else ""
    note = f'<p class="pub-authors">{E(p["note"])}</p>' if p.get("note") else ""
    links = "".join(f'<a href="{u}">{E(l)}</a>' for l, u in p["links"])
    links_html = f'<div class="pub-links">{links}</div>' if links else ""
    abstract = ""
    if with_abstract and p.get("abstract"):
        extra = f'<p class="small muted">{E(p["abstract_note"])}</p>' if p.get("abstract_note") else ""
        abstract = (f'<details><summary><span class="label-open">Show abstract</span><span class="label-close">Hide abstract</span></summary>'
                    f'<div class="abstract"><p>{E(p["abstract"])}</p>{extra}</div></details>')
    tags = " ".join(p["themes"])
    return f"""<article class="pub" id="{p['id']}" data-theme-tags="{tags}">
  <{heading} class="pub-title">{title}</{heading}>
  <p class="pub-authors">{authors_html(p['authors'])}</p>{note}
  <p class="pub-venue">{venue}{detail}</p>
  {links_html}
  {abstract}
</article>"""


# ---------------------------------------------------------------- hero figure
def dist_svg():
    """Six annotators rate one utterance's arousal (1–7); the aggregate t-distribution is the thesis' view of ground truth."""
    W, H = 460, 250
    x0, x1 = 24, W - 16
    base = H - 46
    ratings = [3.1, 3.7, 4.0, 4.3, 4.9, 5.6]
    def X(v): return x0 + (v - 1) / 6 * (x1 - x0)
    def gauss(x, m, s): return math.exp(-0.5 * ((x - m) / s) ** 2)
    def tpdf(x, m, s, nu):
        z = (x - m) / s
        return (1 + z * z / nu) ** (-(nu + 1) / 2)
    n = len(ratings)
    mean = sum(ratings) / n
    sd = math.sqrt(sum((r - mean) ** 2 for r in ratings) / (n - 1))
    xs = [1 + i * 6 / 240 for i in range(241)]

    annot_paths = []
    for i, r in enumerate(ratings):
        pts = [(X(x), base - 62 * gauss(x, r, 0.34)) for x in xs]
        d = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts)
        annot_paths.append(f'<path class="annot" style="animation-delay:{0.08*i:.2f}s" d="{d}"/>')
    agg_pts = [(X(x), base - 150 * tpdf(x, mean, sd, n - 1)) for x in xs]
    agg_d = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in agg_pts)
    fill_d = agg_d + f" L{X(7):.1f},{base} L{X(1):.1f},{base} Z"
    dots = "".join(f'<circle class="rating" style="animation-delay:{0.08*i:.2f}s" cx="{X(r):.1f}" cy="{base + 9}" r="3"/>' for i, r in enumerate(ratings))
    ticks = "".join(f'<text class="tick" x="{X(v):.1f}" y="{base + 28}" text-anchor="middle">{v}</text>' for v in range(1, 8))
    peak_y = base - 150
    lab_x = mean + 1.05
    lab_y = base - 150 * tpdf(lab_x, mean, sd, n - 1) - 4
    return f"""<figure class="dist" aria-labelledby="dist-cap">
<svg viewBox="0 0 {W} {H}" role="img" aria-label="Six annotators rate the arousal of one utterance between about 3 and 5.6 on a 1 to 7 scale. Thin curves show each rating; a bold Student-t curve shows the distribution a model learns instead of a single mean.">
  <path class="agg-fill" d="{fill_d}"/>
  {''.join(annot_paths)}
  <line class="axis" x1="{x0}" x2="{x1}" y1="{base}" y2="{base}"/>
  {dots}
  {ticks}
  <line class="mean" x1="{X(mean):.1f}" x2="{X(mean):.1f}" y1="{base}" y2="{peak_y - 6}"/>
  <path class="agg" d="{agg_d}"/>
  <text class="lbl-accent" x="{X(lab_x) + 10:.1f}" y="{lab_y:.1f}">Label distribution</text>
  <text class="lbl" x="{x0}" y="{H - 2}">Low arousal</text>
  <text class="lbl" x="{x1}" y="{H - 2}" text-anchor="end">High arousal</text>
</svg>
<figcaption id="dist-cap">Six people rate the arousal of one utterance and disagree. The models learn the whole distribution of ratings, not only its mean.</figcaption>
</figure>"""



def scene_svg():
    """Dissertation overview, drawn from scratch as a top-down view of a meeting.
    Four people sit around a round table and a social agent sits just outside the group.
    (1) one person's affect, (2) the group's affect, (3) the agent expressing affect in speech."""
    cx, cy = 205, 150          # table centre
    table_r, seat_r = 52, 98
    seats = [100, 160, 220, 280]   # degrees, clockwise from the right; the open side faces the agent
    focus = 2                      # index into seats
    ax, ay, zone3_r = 440, 150, 50  # agent centre and its zone radius
    zone2_r = 126
    out = []
    # (2) group zone, then the table on top of it
    out.append(f'<circle class="zone zone-2" cx="{cx}" cy="{cy}" r="{zone2_r}"/>')
    out.append(f'<circle class="table" cx="{cx}" cy="{cy}" r="{table_r}"/>')
    # people seen from above: head, shoulders behind it, and a short speech waveform towards the table
    for i, deg in enumerate(seats):
        a = math.radians(deg)
        px, py = cx + seat_r * math.cos(a), cy + seat_r * math.sin(a)
        cls = "person is-focus" if i == focus else "person"
        out.append(f'<g class="{cls}" transform="translate({px:.1f},{py:.1f}) rotate({deg})">'
                   '<path class="speech" d="M-22,-3v6M-27,-7v14M-32,-10v20M-37,-5v10M-42,-3v6"/>'
                   '<path class="shoulders" d="M4.9,-19A21,21 0 0 1 4.9,19"/>'
                   '<circle class="head" r="11"/></g>')
        if i == focus:  # ring centre sits a little towards the table so the ring also holds the speech
            fx, fy = px - 10 * math.cos(a), py - 10 * math.sin(a)
    # (1) individual: a solid ring around one person and what they say
    out.append(f'<circle class="zone zone-1" cx="{fx:.1f}" cy="{fy:.1f}" r="37"/>')
    # (3) agent: zone, a rounded device with a speaker, and sound arcs towards the table
    out.append(f'<circle class="zone zone-3" cx="{ax}" cy="{ay}" r="{zone3_r}"/>')
    out.append(f'<g class="agent">'
               f'<line x1="{ax}" x2="{ax}" y1="{ay-24}" y2="{ay-31}"/><circle class="dot" cx="{ax}" cy="{ay-34}" r="2.4"/>'
               f'<rect x="{ax-21}" y="{ay-24}" width="42" height="36" rx="13"/>'
               f'<circle class="dot" cx="{ax-8}" cy="{ay-6}" r="2.8"/><circle class="dot" cx="{ax+8}" cy="{ay-6}" r="2.8"/>'
               f'<path d="M{ax-26},{ay+38}C{ax-26},{ay+22} {ax-14},{ay+17} {ax},{ay+17}S{ax+26},{ay+22} {ax+26},{ay+38}"/></g>')
    wx, ay_w = ax - 22, ay - 6
    arcs = []
    for r in (16, 28, 40):
        dy, dx = r * math.sin(math.radians(40)), r * math.cos(math.radians(40))
        arcs.append(f'<path d="M{wx-dx:.1f},{ay_w-dy:.1f}A{r},{r} 0 0 0 {wx-dx:.1f},{ay_w+dy:.1f}"/>')
    out.append(f'<g class="waves">{"".join(arcs)}</g>')
    # number badges
    s = math.sqrt(0.5)
    for n, (bx, by) in {1: (fx + 27, fy - 27), 2: (cx + zone2_r * s, cy - zone2_r * s), 3: (ax + zone3_r * s, ay - zone3_r * s)}.items():
        out.append(f'<g class="badge badge-{n}"><circle cx="{bx:.1f}" cy="{by:.1f}" r="13"/><text x="{bx:.1f}" y="{by + 4.5:.1f}" text-anchor="middle">{n}</text></g>')
    return f"""<figure class="scene" aria-labelledby="scene-cap">
<svg viewBox="62 10 450 280" role="img" aria-label="Diagram of a meeting seen from above: four people around a round table and a social agent beside them. A ring marks one person (1, individual-level affect recognition), a dashed circle encloses the whole group (2, group-level affect recognition), and the agent, a small robot facing the viewer, emits sound waves towards the table (3, affect synthesis).">
{''.join(out)}
</svg>
<figcaption id="scene-cap"><span class="key"><b>1</b>Individual-level affect recognition</span><span class="key"><b>2</b>Group-level affect recognition</span><span class="key"><b>3</b>Affect synthesis</span></figcaption>
</figure>"""


def conversion_svg():
    """Illustration of speech emotion conversion as a pipeline: speech is split into speaker, content and
    emotion embeddings, only the emotion is changed, and a decoder resynthesises the sentence."""
    W, H = 460, 250
    mid = 118
    def wave(x, n, step, scale, cls):
        bars = []
        for i in range(n):
            env = math.sin(math.pi * (i + 0.5) / n) ** 0.7
            h = scale * env * (0.55 + 0.45 * abs(math.sin(i * 2.3 + 0.4)))
            bars.append(f"M{x + i * step:.1f},{mid - h:.1f}v{2 * h:.1f}")
        return f'<path class="wave {cls}" d="{"".join(bars)}"/>'
    pills = [("Speaker", 58, ""), ("Content", mid, ""), ("Emotion", 178, " is-emotion")]
    px0, px1 = 128, 226
    out = []
    # input speech
    out.append(wave(14, 15, 5, 26, "in"))
    out.append(f'<text class="lbl" x="48" y="{mid + 44}" text-anchor="middle">Input speech</text>')
    # split into three embeddings
    out.append(f'<path class="flow" d="M90,{mid}H110"/>')
    out.append(f'<path class="flow" d="M110,58V178"/>')
    for name, y, extra in pills:
        out.append(f'<path class="flow" d="M110,{y}H{px0 - 2}" marker-end="url(#ah)"/>')
        out.append(f'<g class="pill{extra}"><rect x="{px0}" y="{y - 15}" width="{px1 - px0}" height="30" rx="15"/>'
                   f'<text x="{(px0 + px1) / 2}" y="{y + 4}" text-anchor="middle">{name}</text></g>')
    # arousal control on the emotion embedding
    sy = 214
    out.append(f'<g class="ctl"><line x1="{px0 + 8}" x2="{px1 - 8}" y1="{sy}" y2="{sy}"/>'
               f'<circle cx="{px1 - 24}" cy="{sy}" r="4.5"/>'
               f'<text x="{px0 + 8}" y="{sy + 16}">Low</text><text x="{px1 - 8}" y="{sy + 16}" text-anchor="end">High</text>'
               f'<text class="lbl-accent" x="{(px0 + px1) / 2}" y="{sy - 9}" text-anchor="middle">Arousal</text></g>')
    # merge into the decoder
    out.append(f'<path class="flow" d="M{px1},58H246V178H{px1}"/>')
    out.append(f'<path class="flow" d="M{px1},{mid}H246"/>')
    out.append(f'<path class="flow" d="M246,{mid}H268" marker-end="url(#ah)"/>')
    out.append(f'<g class="box"><rect x="272" y="{mid - 22}" width="78" height="44" rx="6"/>'
               f'<text x="311" y="{mid + 4}" text-anchor="middle">Decoder</text></g>')
    out.append(f'<path class="flow" d="M350,{mid}H370" marker-end="url(#ah)"/>')
    # converted speech: same sentence, higher and faster
    out.append(wave(380, 15, 4.2, 34, "out"))
    out.append(f'<text class="lbl" x="410" y="{mid + 44}" text-anchor="middle">Converted speech</text>')
    return f"""<figure class="dist pipe" aria-labelledby="conv-cap">
<svg viewBox="0 0 {W} {H}" role="img" aria-label="Pipeline diagram. Input speech is split into speaker, content and emotion embeddings. An arousal control changes only the emotion embedding, set towards high. A decoder turns the three embeddings back into converted speech, drawn with a denser, taller waveform.">
  <defs><marker id="ah" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path class="ah" d="M0,0.5L7.5,4L0,7.5Z"/></marker></defs>
  {''.join(out)}
</svg>
<figcaption id="conv-cap">Speech is split into speaker, content and emotion embeddings. Only the emotion embedding is changed, here towards higher arousal, and a decoder resynthesises the same sentence with the new tone. No parallel recordings are needed.</figcaption>
</figure>"""


# ---------------------------------------------------------------- pages
def index_page():
    selected = [p for p in PUBS if p.get("selected")][:4]
    news = "".join(f'<li><time datetime="{d}">{E(label)}</time><div class="what"><p>{text}</p></div></li>' for d, label, text in NEWS)
    sel = "".join(pub_html(p, with_abstract=False) for p in selected)

    body = f"""
<section class="hero">
  <div class="hero-text">
    <h1>Navin Raj Prabhu</h1>
    <p class="lede">I research how machines can recognise and generate emotion in human speech.</p>
    <p class="intro">PhD in Computer Science from the University of Hamburg, where I built probabilistic and generative models for emotion recognition and speech emotion conversion. I'm now a Machine Learning Researcher at <a class="nowrap" href="{LINKS['aicoustics']}">ai-coustics</a> in Berlin.</p>
    <ul class="contact-links">
      <li><a href="{LINKS['email']}">Email</a></li>
      <li><a href="{LINKS['scholar']}">Google Scholar</a></li>
      <li><a href="{LINKS['github']}">GitHub</a></li>
      <li><a href="{LINKS['linkedin']}">LinkedIn</a></li>
      <li><a href="cv.html">CV</a></li>
    </ul>
  </div>
  <figure class="portrait">
    <picture>
      <source type="image/webp" srcset="assets/portrait-sm.webp 360w, assets/portrait.webp 720w" sizes="(max-width: 860px) 60vw, 340px">
      <img src="assets/portrait.jpg" alt="Navin Raj Prabhu" width="720" height="900" fetchpriority="high">
    </picture>
  </figure>
</section>

<section class="section" id="dissertation" aria-labelledby="h-thesis">
  <h2 id="h-thesis">Dissertation</h2>
  <div class="section-body wide thesis">
    <p class="thesis-title">Probabilistic and Generative Modeling for Emotion Recognition and Synthesis</p>
    <dl class="thesis-facts">
      <div><dt>Degree</dt><dd>PhD in Computer Science, University of Hamburg</dd></div>
      <div><dt>Defended</dt><dd>12 February 2026</dd></div>
      <div><dt>Supervisors</dt><dd>Prof. Timo Gerkmann<br>Prof. Nale Lehmann-Willenbrock</dd></div>
      <div><dt>External reviewer</dt><dd>Prof. Carlos Busso</dd></div>
    </dl>
    <p class="thesis-intro">Current AI systems still lack social intelligence: the ability to perceive and express the social signals that make collaboration work. The dissertation focuses on affect and studies it at three levels, in two lines of work.</p>
    {scene_svg()}
    <div class="strands">
      <div class="strand">
        <h3>Recognising affect</h3>
        {dist_svg()}
        <ol>
          <li>Bayesian neural networks trained on the full distribution of annotations, so models capture annotator disagreement as well as the mean.<a href="publications.html#bnn-arousal-interspeech-2022">Interspeech 2022, IEEE TAFFC 2023</a></li>
          <li>Student's t-distributions in place of Gaussians, linking how few annotations exist to how uncertain a label is.<a href="publications.html#t-dist-acii-2022">ACII 2022</a></li>
          <li>A psychology-grounded protocol for annotating group affect over time, and multimodal models of how groups converge and diverge.<a href="publications.html#group-affect-taffc-2026">IEEE TAFFC 2026</a></li>
        </ol>
      </div>
      <div class="strand">
        <h3>Synthesising affect in speech</h3>
        {conversion_svg()}
        <ol>
          <li>Emotion conversion without parallel data, by disentangling speaker, lexical and emotion embeddings and resynthesising with a HiFiGAN vocoder.<a href="publications.html#ssl-sec-itg-2023">ITG Speech Communication 2023</a></li>
          <li>Diffusion decoders that widen the range of emotions that can be expressed, especially rare, extreme arousal.<a href="publications.html#emoconv-diff-icassp-2024">ICASSP 2024</a></li>
          <li>A duration predictor that lets speech rate follow arousal: slower when calm, faster when excited.<a href="publications.html#duration-asru-2025">IEEE ASRU 2025</a></li>
        </ol>
      </div>
    </div>
    <div class="actions">
      <a class="btn primary" href="{LINKS['thesis']}">Read the dissertation</a>
      <a class="btn" href="{LINKS['thesis_news']}">Department news</a>
    </div>
  </div>
</section>

<section class="section" id="news" aria-labelledby="h-news">
  <h2 id="h-news">News</h2>
  <div class="section-body">
    <ul class="dated">{news}</ul>
  </div>
</section>

<section class="section" id="selected" aria-labelledby="h-sel">
  <h2 id="h-sel">Selected publications</h2>
  <div class="section-body">
    {sel}
    <a class="more-link" href="publications.html">All publications, with abstracts</a>
  </div>
</section>
"""
    return page("Navin Raj Prabhu: speech and affective computing research",
                "Navin Raj Prabhu researches speech emotion recognition and emotion-conditioned speech synthesis with probabilistic and generative neural networks. PhD, University of Hamburg.",
                "index.html", body, "index.html")


def publications_page():
    years = sorted({p["year"] for p in PUBS}, reverse=True)
    counts = {k: sum(1 for p in PUBS if k in p["themes"]) for k in THEMES}
    chips = f'<button class="chip" type="button" data-filter="all" aria-pressed="true">All<span class="count">{len(PUBS)}</span></button>'
    chips += "".join(f'<button class="chip" type="button" data-filter="{k}" aria-pressed="false">{E(v)}<span class="count">{counts[k]}</span></button>' for k, v in THEMES.items())
    groups = ""
    for y in years:
        items = "".join(pub_html(p) for p in PUBS if p["year"] == y)
        groups += f'<section class="year-group" aria-label="{y}"><h2>{y}</h2><div class="section-body">{items}</div></section>'

    thesis = pub_html(THESIS, with_abstract=False).replace(' data-theme-tags="recognition synthesis groups"', '')
    thesis_summary = (
        '<details><summary><span class="label-open">Show summary</span><span class="label-close">Hide summary</span></summary>'
        '<div class="abstract"><p>The dissertation studies affect, a central social signal, from two sides. On the recognition side it '
        'contributes probabilistic methods that model label uncertainty, combining Bayesian neural networks with label distribution learning and '
        'replacing Gaussian assumptions with Student\'s t-distributions when annotations are sparse; a protocol for annotating group-level affect '
        'over time; and graph-based multimodal models of collective affect. On the synthesis side it proposes generative models for emotion conversion '
        'in in-the-wild speech without parallel data, explores diffusion decoders for controllable affect, and shows the value of explicit duration modeling. '
        'Across both, ground truth is treated as a distribution rather than an absolute.</p>'
        f'<p class="small muted">A summary. The full abstract and PDF are on <a href="{LINKS["thesis"]}">eDiss</a>.</p></div></details>')
    thesis = thesis.replace("\n  \n</article>", f"\n  {thesis_summary}\n</article>")

    body = f"""
<header class="page-head">
  <h1>Publications</h1>
  <p>Papers on recognising and synthesising emotion, and on affect in groups. Open an entry to read its abstract. For citation counts and the complete list, see <a href="{LINKS['scholar']}">Google Scholar</a>.</p>
</header>

<section class="year-group" aria-label="Dissertation">
  <h2>Dissertation</h2>
  <div class="section-body">{thesis}</div>
</section>

<div class="toolbar" role="region" aria-label="Filter publications">
  <fieldset class="filters"><legend>Filter by topic</legend>{chips}</fieldset>
  <span class="spacer"></span>
  <button class="text-btn" type="button" data-expand-all>Expand all abstracts</button>
  <span class="status" aria-live="polite"></span>
</div>

{groups}
"""
    return page("Publications: Navin Raj Prabhu",
                "Publications by Navin Raj Prabhu on speech emotion recognition, label uncertainty, speech emotion conversion and group affect, with abstracts and links.",
                "publications.html", body, "publications.html")


def cv_page():
    def entries(lst):
        out = ""
        for e in lst:
            items = "".join(f"<li>{i}</li>" for i in e["items"])
            out += f'<li><span class="when">{E(e["when"])}</span><div class="what cv-entry"><h3>{E(e["what"])}</h3><p class="where">{E(e["where"])}</p><ul>{items}</ul></div></li>'
        return f'<ul class="dated">{out}</ul>'
    teach = "".join(f'<li><span class="when">{E(w)}</span><div class="what"><p>{E(t)}</p></div></li>' for w, t in TEACHING)
    interests = "".join(f"<li>{E(i)}</li>" for i in INTERESTS)
    body = f"""
<header class="page-head">
  <h1>Curriculum vitae</h1>
  <p>Researcher in artificial intelligence, speech processing and social signal processing, with experience in both academic and start-up teams.</p>
</header>

<section class="section" aria-labelledby="h-int">
  <h2 id="h-int">Research interests</h2>
  <div class="section-body"><ul class="tags">{interests}</ul></div>
</section>

<section class="section" aria-labelledby="h-edu">
  <h2 id="h-edu">Education</h2>
  <div class="section-body">{entries(EDUCATION)}</div>
</section>

<section class="section" aria-labelledby="h-exp">
  <h2 id="h-exp">Experience</h2>
  <div class="section-body">{entries(EXPERIENCE)}</div>
</section>

<section class="section" aria-labelledby="h-teach">
  <h2 id="h-teach">Teaching and supervision</h2>
  <div class="section-body">
    <p class="muted small">Teaching assistance at the University of Hamburg.</p>
    <ul class="dated">{teach}</ul>
  </div>
</section>

<section class="section" aria-labelledby="h-pubs">
  <h2 id="h-pubs">Publications</h2>
  <div class="section-body">
    <p>{len(PUBS)} peer-reviewed papers and chapters, including IEEE Transactions on Affective Computing, ICASSP, Interspeech, ASRU and ACII.</p>
    <a class="more-link" href="publications.html">See all publications</a>
  </div>
</section>
"""
    return page("CV: Navin Raj Prabhu",
                "Curriculum vitae of Navin Raj Prabhu: PhD University of Hamburg, MSc TU Delft, research in speech emotion recognition and synthesis.",
                "cv.html", body, "cv.html")


def notfound_page():
    body = """
<header class="page-head">
  <h1>Page not found</h1>
  <p>This address doesn't match a page on the site. Try the <a href="/">home page</a> or the <a href="/publications.html">publications</a>.</p>
</header>"""
    s = page("Page not found: Navin Raj Prabhu", "Page not found.", "", body, "404.html")
    # 404 is served from any path, so use absolute asset URLs
    return s.replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/').replace('href="index.html"', 'href="/"').replace('href="publications.html"', 'href="/publications.html"').replace('href="cv.html"', 'href="/cv.html"')


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#2e49a8"/><path d="M4 24 C9 24 11 8 16 8 S23 24 28 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/></svg>"""

if __name__ == "__main__":
    os.makedirs(OUT + "/assets", exist_ok=True)
    files = {
        "index.html": index_page(),
        "publications.html": publications_page(),
        "cv.html": cv_page(),
        "404.html": notfound_page(),
        "assets/favicon.svg": FAVICON,
        "CNAME": "rajprabhu.net\n",
        ".nojekyll": "",
        "robots.txt": f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n",
        "sitemap.xml": '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                       + "".join(f"  <url><loc>{SITE}/{p}</loc></url>\n" for p in ["", "publications.html", "cv.html"]) + "</urlset>\n",
    }
    for name, content in files.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(content)
    print("built", ", ".join(files))
