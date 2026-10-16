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

# The ai-coustics mark, taken from the company's own site; the one brand mark on this site. It follows the theme through currentColor.
AIC_MARK = '<svg class="aic-mark" viewBox="0 0 22 22" aria-hidden="true"><path fill="currentColor" d="M21.996 10.948H22C22 17.052 17.076 22 11 22 4.923 22 0 17.051 0 10.948h10.997C11.052 4.893 15.955 0 21.996 0ZM16.628 6.056c-.681 0-1.232.555-1.231 1.238 0 .684.552 1.238 1.232 1.237.681 0 1.232-.555 1.232-1.238-.001-.684-.553-1.238-1.233-1.237Z"/></svg>'

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
    <a class="wordmark" href="index.html"><span class="full">Navin Raj Prabhu</span><span class="short">N. Raj Prabhu</span></a>
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
def scene_svg():
    """Dissertation overview after Figure 1.1 of the thesis, drawn from scratch: a meeting seen from across
    the table. Three people sit behind it as flat silhouettes and a social agent sits at the right end.
    (1) one person's affect, (2) the group's affect, (3) the agent expressing affect in speech.
    The scene loops: the people take turns speaking (bars above a shoulder, a small nod), the agent
    answers with sound waves, blinks and lets its antenna light pulse. The CSS in style.css times it."""
    tx, ty, trx, try_ = 320, 205, 240, 36   # table ellipse
    def person(n, x, y, r, cls="person"):
        """A flat silhouette: head and a torso with sloped shoulders. The table hides the lower torso.
        The head is wrapped in its own group so it can nod; the speech bars sit beside it."""
        w, top = 2.0 * r, y + 1.2 * r
        d = (f"M{x-w:.1f},215 V{top+20:.1f} Q{x-w:.1f},{top+2:.1f} {x-w*0.5:.1f},{top:.1f} "
             f"L{x-r*0.4:.1f},{top-3:.1f} L{x+r*0.4:.1f},{top-3:.1f} L{x+w*0.5:.1f},{top:.1f} "
             f"Q{x+w:.1f},{top+2:.1f} {x+w:.1f},{top+20:.1f} V215 Z")
        sx = x + r + 7
        bars = f"M{sx},{y-4}v8M{sx+5},{y-9}v18M{sx+10},{y-6}v12M{sx+15},{y-3}v6"
        return (f'<g class="{cls} person-{n}"><path class="torso" d="{d}"/>'
                f'<g class="head-g"><circle class="head" cx="{x}" cy="{y}" r="{r}"/></g>'
                f'<path class="speech" d="{bars}"/></g>')
    def paper(x, y):
        return f'<path class="paper" d="M{x-14},{y} l22,-6 l11,5 l-22,6 Z"/>'
    out = []
    out.append(person(1, 160, 118, 19))
    out.append(person(2, 280, 116, 19, "person is-focus"))
    out.append(person(3, 400, 118, 19))
    ax, ay = 520, 118
    out.append(f'<g class="agent">'
               f'<line x1="{ax}" x2="{ax}" y1="{ay-19}" y2="{ay-27}"/><circle class="dot" cx="{ax}" cy="{ay-30}" r="2.8"/>'
               f'<g class="face-g">'
               f'<rect class="face" x="{ax-22}" y="{ay-19}" width="44" height="38" rx="14"/>'
               f'<g class="eyes"><circle class="eye" cx="{ax-9}" cy="{ay}" r="3.2"/><circle class="eye" cx="{ax+9}" cy="{ay}" r="3.2"/></g>'
               f'<rect class="mouth" x="{ax-7}" y="{ay+9}" width="14" height="2.6" rx="1.3"/></g>'
               f'<path class="body" d="M{ax-26},215 V{ay+47} C{ax-26},{ay+32} {ax-14},{ay+26} {ax},{ay+26} S{ax+26},{ay+32} {ax+26},{ay+47} V215 Z"/></g>')
    out.append(f'<path class="table-rim" d="M{tx-trx},{ty} v9 A{trx},{try_} 0 0 0 {tx+trx},{ty+9} v-9 Z"/>')
    out.append(f'<ellipse class="table" cx="{tx}" cy="{ty}" rx="{trx}" ry="{try_}"/>')
    out.append(paper(190, 190) + paper(312, 184) + paper(432, 190))
    # (2) the group: a dashed capsule around the three people
    out.append('<rect class="zone zone-2" x="100" y="76" width="350" height="118" rx="40"/>')
    # (3) the agent: a dashed speech bubble whose tail points at the people
    out.append('<path class="zone zone-3" d="M480,76H560Q572,76 572,88V182Q572,194 560,194H480Q468,194 468,182V127L452,117L468,107V88Q468,76 480,76Z"/>')
    # (1) one person: a viewfinder frame that slides to whoever is speaking (CSS "track"); drawn on the middle seat
    fx, fy, fw, fh, c, k = 232, 84, 96, 110, 9, 16
    corners = (f"M{fx},{fy+k}V{fy+c}Q{fx},{fy} {fx+c},{fy}H{fx+k}"
               f"M{fx+fw-k},{fy}H{fx+fw-c}Q{fx+fw},{fy} {fx+fw},{fy+c}V{fy+k}"
               f"M{fx+fw},{fy+fh-k}V{fy+fh-c}Q{fx+fw},{fy+fh} {fx+fw-c},{fy+fh}H{fx+fw-k}"
               f"M{fx+k},{fy+fh}H{fx+c}Q{fx},{fy+fh} {fx},{fy+fh-c}V{fy+fh-k}")
    out.append(f'<g class="focus"><rect class="zone zone-1 wash" x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="{c}"/>'
               f'<path class="zone zone-1 frame" d="{corners}"/>'
               f'<g class="badge badge-1"><circle cx="{fx + fw / 2}" cy="{fy}" r="13"/><text x="{fx + fw / 2}" y="{fy + 4.5}" text-anchor="middle">1</text></g></g>')
    wx, wy = ax - 30, ay - 2
    arcs = []
    for r in (14, 26, 38):
        dy, dx = r * math.sin(math.radians(40)), r * math.cos(math.radians(40))
        arcs.append(f'<path d="M{wx-dx:.1f},{wy-dy:.1f}A{r},{r} 0 0 0 {wx-dx:.1f},{wy+dy:.1f}"/>')
    out.append(f'<g class="waves">{"".join(arcs)}</g>')
    for n, (bx, by) in {2: (113, 89), 3: (468, 76)}.items():
        out.append(f'<g class="badge badge-{n}"><circle cx="{bx}" cy="{by}" r="13"/><text x="{bx}" y="{by + 4.5}" text-anchor="middle">{n}</text></g>')
    return f"""<figure class="scene">
<svg viewBox="76 58 500 196" role="img" aria-label="Diagram after Figure 1.1 of the dissertation: three people sit behind a meeting table and take turns speaking; a small robot sits at its right end and answers with sound waves. A frame follows whoever is speaking (1, individual affect), a dashed capsule encloses the three people (2, group affect), and a dashed speech bubble marks the robot (3, affect synthesis).">
{''.join(out)}
</svg>
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
    <p class="intro">PhD in Computer Science from the University of Hamburg, where I built probabilistic and generative models for emotion recognition and speech emotion conversion.</p>
    <p class="now-at">
      {AIC_MARK}
      <span>I'm now a Machine Learning Researcher at <a class="nowrap" href="{LINKS['aicoustics']}">ai-coustics</a> in Berlin.<span class="tagline">Audio intelligence for voice AI</span></span>
    </p>
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
    <p class="thesis-intro">Current AI systems still lack social intelligence: the ability to perceive and express the social signals that make collaboration work. The dissertation focuses on affect and studies it in three directions: recognising it in one person, recognising it in a group, and synthesising it in speech.</p>
    {scene_svg()}
    <div class="strands three">
      <div class="strand">
        <h3><b class="num">1</b>Individual affect</h3>
        <ol>
          <li>Bayesian networks trained on the full spread of annotations, not just their mean.<span class="refs"><a href="publications.html#bnn-arousal-interspeech-2022">Interspeech 2022</a><a href="publications.html#bnn-ldl-taffc-2023">IEEE TAFFC 2023</a></span></li>
          <li>Student's t-distributions instead of Gaussians, so fewer annotations mean a more uncertain label.<span class="refs"><a href="publications.html#t-dist-acii-2022">ACII 2022</a></span></li>
          <li>Audio-textual distillation for efficient self-supervised emotion recognition.<span class="refs"><a href="publications.html#distilled-ser-interspeech-2023">Interspeech 2023</a></span></li>
        </ol>
      </div>
      <div class="strand">
        <h3><b class="num">2</b>Group affect</h3>
        <ol>
          <li>A psychology-grounded protocol for annotating the affect of a whole group over time.<span class="refs"><a href="publications.html#group-affect-taffc-2026">IEEE TAFFC 2026</a></span></li>
          <li>Why behavioural labels of groups are subjective and uncertain.<span class="refs"><a href="publications.html#behavioral-labels-oup-2025">OUP chapter 2025</a></span></li>
          <li>Multimodal models of how group members' emotions converge and diverge.<span class="refs"><a href="publications.html#group-affect-taffc-2026">IEEE TAFFC 2026</a></span></li>
        </ol>
      </div>
      <div class="strand">
        <h3><b class="num">3</b>Affect synthesis</h3>
        <ol>
          <li>Emotion conversion without parallel data, by disentangling speaker, content and emotion.<span class="refs"><a href="publications.html#ssl-sec-itg-2023">ITG 2023</a></span></li>
          <li>Diffusion decoders that reach rare, extreme arousal.<span class="refs"><a href="publications.html#emoconv-diff-icassp-2024">ICASSP 2024</a></span></li>
          <li>Speech rate that follows arousal: slower when calm, faster when excited.<span class="refs"><a href="publications.html#duration-asru-2025">IEEE ASRU 2025</a></span></li>
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
