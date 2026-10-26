"""Himanshu Sharma - AI/ML engineer portfolio (Streamlit)."""
import base64
import mimetypes
from pathlib import Path
import streamlit as st
FIRST_NAME = "Himanshu"
NAME = "Himanshu Sharma"
ROLE = "Aspiring AI/ML Engineer"
LOCATION = "Shimla, Himachal Pradesh, India"
GITHUB_USER = "himanshu8038sharma"
EMAIL = "hs2660815@gmail.com"     
LINKEDIN = "https://www.linkedin.com/in/himanshu-sharma-36215534a/?isSelfProfile=true"  
RESUME = Path("assets/resume.pdf")        
PHOTO_CANDIDATES = ["assets/profile.jpg", "assets/profile.png", "assets/profile.jpeg"]
STATUS = "open to AI/ML fresher opportunities"
TYPING_LINE = "Aspiring ML Engineer  |  Generative AI  |  Reinforcement Learning"
HERO_TEXT = (
    "I'm a Computer Science engineering student interested in building "
        "practical AI and machine learning solutions. I enjoy working with data, "
        "experimenting with models, and exploring intelligent systems through projects."
)
ABOUT = [
    "I'm a final year Computer Science engineering student , with a strong interest in "
    "machine learning, generative AI, and intelligent systems. I enjoy "
    "building practical machine learning projects and exploring how models "
    "can be applied to solve real-world problems.",
    "My projects range from a tabular AutoML system and a recommendation "
    "engine to fraud detection, reinforcement learning experiments in the "
    "CARLA simulator, and contributions to an LLM-based game theory agent. "
    "I enjoy experimenting with different approaches, comparing their "
    "performance, and understanding what works best."
]
EDUCATION =  "B.Tech in Computer Science and Engineering | Himachal Pradesh Technical University (HPTU) | 2023–2027"
SKILLS = [
    ("brain", "Programming & Data Analysis", [
        "Python", "NumPy", "Pandas", "seaborn","SQL", "Matplotlib","Data Cleaning", "EDA", "Data Visualization"
    ]),
    ("spark", "Machine Learning", [
        "Scikit-learn" ,"Classification", "Regression"
       ,"Clustering", "Data Preprocessing", "Model Evaluation"
    ]),
    ("loop", "AI & Emerging Technologies", [
        "Neural Networks", "Generative AI", "LLMs",
        "Prompt Engineering", "Reinforcement Learning"
    ]),
    ("tools", "Tools & Platforms", [
        "Streamlit", "Jupyter Notebook", "Git", "GitHub",
        "CARLA Simulator","Hugging Face"
    ]),
]
INTERESTS = [
    ("Machine Learning", "Developing predictive models and exploring different learning algorithms."),
    ("Generative AI & LLMs", "Exploring large language models, prompt engineering, and AI agents."),
    ("Reinforcement Learning", "Understanding how intelligent agents learn through interaction and rewards."),
    ("Automated Machine Learning", "Building automated workflows for preprocessing, model selection, and evaluation."),
]
EXPERIENCE = [
    {
        "role": "AI/ML Trainee",
        "org": "Inphora Pvt. Ltd.",
        "period": "45-Day Industrial Training",
        "points": [
            "Completed practical training in machine learning concepts and workflows.",
            "Gained exposure to data preprocessing, model development, and evaluation.",
            "Applied machine learning techniques through hands-on project work."
        ],
        "certificates": [
            {"title": "Internship Completion Certificate", "file": "assets/certificates/inphora/internship.png"},
            {"title": "Personality Development Certificate", "file": "assets/certificates/inphora/personality-development.png"},
            {"title": "Project Completion Certificate", "file": "assets/certificates/inphora/automl-project.png"},
        ],
    },
    {
        "role": "GenAI Data Analytics Job Simulation",
        "org": "Tata Group | Forage",
        "period": "Virtual Job Simulation",
        "points": [
            "Completed a virtual job simulation focused on generative AI applications in data analytics.",
            "Worked on a business-oriented case study involving customer delinquency analysis.",
            "Explored how AI-driven insights can support business decision-making."
        ],
        "certificates": [
            {"title": "Tata Forage Job Simulation Certificate", "file": "assets/certificates/forage/tata-forage.png"},
        ],
    },
]

CERTIFICATIONS = [
    {"title": "Oracle Cloud Infrastructure AI Foundations Associate", "issuer": "Oracle", "url": "", "badge_url": "https://catalog-education.oracle.com/ords/certview/sharebadge?id=69651F58C97AA99FCD302EF942AB0B435851FEF270673F4EA9009EE9CC55DD08", "thumb": "assets/certs/oci-ai-foundations.png"},
    {"title": "Oracle Cloud Infrastructure Generative AI Professional", "issuer": "Oracle", "url": "", "badge_url": "https://catalog-education.oracle.com/ords/certview/sharebadge?id=B2E6A8AF6DBCC94E0E1FB85C1EF084F090556619853FD833D1C6359562122F14", "thumb": "assets/certs/oci-gen-ai.png"},
]

PROJECTS = [
    {
        "slug": "zoroark-ml", "title": "Zoroark-ML",
        "desc": "Problem-aware AutoML that picks preprocessing, models and evaluation to match the problem. Streamlit front end, modular pipeline.",
        "tags": ["AutoML", "scikit-learn","Explainable AI","Machine Learning","Streamlit"], "repo": "https://github.com/himanshu8038sharma/zoroark-ml---Problem-Aware-automated-machine-learning-system", "demo": "https://zoroark-ml---problem-aware-automated-machine-learning-system-l.streamlit.app/",
    },
    {
        "slug": "carla-rl-capstone", "title": "Autonomous Driving with RL",
        "desc": "PPO, TD3 and SAC compared in CARLA at 200k timesteps. SAC won, then trained to about 1.5M timesteps for the final model.",
        "tags": ["Reinforcement learning", "CARLA", "Gymnasium", "SAC", "Autonomous Driving"], "repo": "", "demo": "",
    },
    {
        "slug": "llm-game-theory-agent", "title": "LLM Game-Theory Agent",
        "desc": "Four-module local LLM agent with cybersecurity and autonomous-vehicle extensions. I own the strategic reasoning and solver module.",
        "tags": ["LLMs", "Game theory", "Agents"], "repo": "", "demo": "",
    },
    {
        "slug": "student-success-predictor", "title": "Student Success Predictor",
        "desc": "Predicts how students are likely to perform so support can reach at-risk students early.",
        "tags": ["Python","Scikit-learn","Classification","Data Visualization","Machine Learning"], "repo": "https://github.com/himanshu8038sharma/Student-success-predictor", "demo": "",
    },
    {
        "slug": "mood-based-movie-recommender", "title": "Mood-Based Movie Recommender",
        "desc": "Streamlit app that suggests movies matching your mood, built on the TMDB 5000 dataset with a content-similarity model.",
        "tags": ["Recommender","Content-Based Filtering","Cosine Similarity", "NLP", "Scikit-learn", "Streamlit", "Python"],
        "repo": "https://github.com/himanshu8038sharma/Mood-Based-Movie-recommendation-system", "demo": "https://mood-based-movie-recommendation-system-3639uy4gvnfeiwnsd7tndn.streamlit.app/",
    },
    {
        "slug": "credit-card-fraud-detection", "title": "Credit Card Fraud Detection",
        "desc": "Notebook study of how sampling ratios change fraud-detection model performance on imbalanced data.",
        "tags": ["Fraud Detection", "Imbalanced data", "Model comparison","Scikit-learn", "Matplotlib","jupyter"],
        "repo": "https://github.com/himanshu8038sharma/Credit-Card-Fraud-Detection--Sampling-Ratio-Model-Comparison", "demo": "",
    },
]
# Page setup and styling
st.set_page_config(page_title=f"{NAME} | {ROLE}", page_icon="◐", layout="wide")
GITHUB_URL = f"https://github.com/{GITHUB_USER}"
BASE = Path(__file__).parent
# THEMES - pick with DEFAULT_THEME, or preview with  ?theme=mix|green|violet|lime  in the URL
DEFAULT_THEME = "mix"
THEMES = {
    "green": dict(
        layout="center", bg="#040806", surface="#0A120D", line="#1B2E21", text="#F2F6F3", muted="#98A99E",
        accent="#B4F03A", ar="180,240,58", er="80,160,90", onacc="#071006", t1="var(--t1)", t2="var(--t2)",
        btnbg="#B4F03A", accgrad="linear-gradient(90deg,#B4F03A,#B4F03A)", rad="14px", pill="999px",
        fx="linear-gradient(135deg, transparent 28%, rgba(30,120,50,.38) 50%, transparent 72%)",
        lines=True, fh="var(--fh)", fb="'Inter',system-ui,sans-serif",
        font_import="family=Raleway:wght@600;700;800&family=Inter:wght@400;500",
    ),
    "violet": dict(
        layout="center", bg="#08080F", surface="#11111C", line="#26263A", text="#F4F4FA", muted="#9A9AB5",
        accent="#8B7CF6", ar="139,124,246", er="139,124,246", onacc="#FFFFFF", t1="#1A1A33", t2="#0E0E1C",
        btnbg="linear-gradient(90deg,#7C5CF6,#5B8CFF)", accgrad="linear-gradient(90deg,#8B7CF6,#5B9BFF)", rad="14px", pill="999px",
        fx="radial-gradient(45% 40% at 50% 12%, rgba(110,80,255,.30), transparent 70%), radial-gradient(35% 30% at 82% 82%, rgba(60,120,255,.13), transparent 70%)",
        lines=False, fh="'Plus Jakarta Sans','Inter',sans-serif", fb="'Inter',system-ui,sans-serif",
        font_import="family=Plus+Jakarta+Sans:wght@600;700;800&family=Inter:wght@400;500",
    ),
    "lime": dict(
        layout="split", bg="#070706", surface="#10110B", line="#2A2C1B", text="#F4F5EC", muted="#A3A692",
        accent="#D7F72E", ar="215,247,46", er="215,247,46", onacc="#0A0B04", t1="#1A1C0E", t2="#0D0E07",
        btnbg="#D7F72E", accgrad="linear-gradient(90deg,#D7F72E,#D7F72E)", rad="2px", pill="2px",
        fx=("linear-gradient(115deg, transparent 38%, rgba(215,247,46,.12) 38.2%, transparent 38.8%),"
            "linear-gradient(62deg, transparent 52%, rgba(215,247,46,.10) 52.2%, transparent 52.7%),"
            "linear-gradient(135deg, transparent 20%, rgba(150,170,20,.11) 50%, transparent 80%)"),
        lines=False, fh="'Space Grotesk',sans-serif", fb="'JetBrains Mono',ui-monospace,monospace",
        font_import="family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;500",
    ),
}
THEMES["mix"] = {
    **THEMES["lime"],
    "bg": "#08080F", "surface": "#11111C", "line": "#26263A", "text": "#F4F4FA", "muted": "#9A9AB5",
    "accent": "#8B7CF6", "ar": "139,124,246", "er": "139,124,246", "onacc": "#FFFFFF",
    "t1": "#1A1A33", "t2": "#0E0E1C",
    "btnbg": "linear-gradient(90deg,#7C5CF6,#5B8CFF)",
    "accgrad": "linear-gradient(90deg,#8B7CF6,#5B9BFF)",
    "fx": ("linear-gradient(115deg, transparent 38%, rgba(139,124,246,.16) 38.2%, transparent 38.8%),"
           "linear-gradient(62deg, transparent 52%, rgba(91,140,255,.13) 52.2%, transparent 52.7%),"
           "radial-gradient(45% 40% at 50% 10%, rgba(110,80,255,.20), transparent 70%),"
           "radial-gradient(35% 30% at 85% 85%, rgba(60,120,255,.12), transparent 70%)"),
}
_qp = st.query_params.get("theme", DEFAULT_THEME)
THEME = _qp if _qp in THEMES else DEFAULT_THEME
T = THEMES[THEME]
THEME_CSS = (
    "<style>@import url('https://fonts.googleapis.com/css2?" + T["font_import"] + "&display=swap');</style><style>:root{"
    + "".join(f"--{k}:{T[k]};" for k in ["bg","surface","line","text","muted","accent","ar","er","onacc","t1","t2","btnbg","accgrad","rad","pill","fx","fh","fb"])
    + "}</style>"
)
CSS = """
<style>
html, body, [class*="css"], .stApp { font-family:var(--fb); }
.stApp { background:var(--bg); color:var(--text); }
/* diagonal green glow */
.stApp::before { content:""; position:fixed; inset:0; z-index:0; pointer-events:none;
  background: var(--fx); animation:sway 14s ease-in-out infinite alternate; }
/* thin frame lines */
.stApp::after { content:""; position:fixed; inset:0; z-index:0; pointer-events:none;
  background:
    linear-gradient(90deg, transparent calc(8% - 1px), rgba(90,130,170,.20) 8%, transparent calc(8% + 1px)),
    linear-gradient(90deg, transparent calc(92% - 1px), rgba(90,130,170,.20) 92%, transparent calc(92% + 1px)),
    linear-gradient(180deg, transparent 56px, rgba(90,130,170,.20) 57px, transparent 58px),
    linear-gradient(180deg, transparent calc(100% - 60px), rgba(90,130,170,.20) calc(100% - 59px), transparent calc(100% - 58px)); }
@keyframes sway { from { opacity:.75; transform:translateX(-2%); } to { opacity:1; transform:translateX(2%); } }
@keyframes rise { from { opacity:0; transform:translateY(16px); } to { opacity:1; transform:none; } }
@keyframes reveal { to { clip-path: inset(0 0 0 0); } }
@keyframes caret { 50% { opacity:0; } }
@keyframes pulse { 0%,100% { box-shadow:0 0 0 0 rgba(var(--ar),.5); } 50% { box-shadow:0 0 0 7px rgba(var(--ar),0); } }
@keyframes bob { 0%,100% { transform:translateY(0); } 50% { transform:translateY(6px); } }

header[data-testid="stHeader"], footer, #MainMenu { display:none; }
.block-container { position:relative; z-index:1; max-width:1120px; padding:0 1.5rem 3rem; }
html { scroll-behavior:smooth; scroll-padding-top:5rem; }
h1,h2,h3,h4 { font-family:var(--fh); color:var(--text); }
.stApp a, .stApp a:hover, .stApp a:visited { text-decoration:none !important; }
.stApp a { color:var(--accent); }
.acc { background:var(--accgrad); -webkit-background-clip:text; background-clip:text; color:transparent; }
/* pill nav */
.nav { position:fixed; top:14px; left:50%; transform:translateX(-50%); z-index:60; display:flex; gap:1.3rem; padding:.7rem 1.6rem;
  background:color-mix(in srgb, var(--bg) 82%, transparent); backdrop-filter:blur(10px); border:1px solid rgba(var(--er),.35); border-radius:var(--pill); }
.stApp .nav a { color:var(--text); font-size:.74rem; letter-spacing:.06em; text-transform:uppercase; font-weight:500; transition:color .2s; }
.stApp .nav a:hover, .stApp .nav a.on { color:var(--accent); }
@media (max-width:640px){ .nav { gap:.8rem; padding:.6rem 1rem; } }
/* hero */
.hero { min-height:100vh; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:6rem 0 3rem; animation:rise .9s ease both; }
.status { display:inline-flex; align-items:center; gap:.55rem; font-size:.78rem; letter-spacing:.12em; text-transform:uppercase; color:var(--text);
  padding:.4rem .95rem; border:1px solid var(--line); border-radius:var(--pill); background:color-mix(in srgb, var(--surface) 78%, transparent); margin-bottom:1.4rem; }
.status i { width:8px; height:8px; border-radius:50%; background:var(--accent); animation:pulse 2.2s infinite; }
.hero h1 { font-size:clamp(2.6rem,7vw,4.6rem); font-weight:800; line-height:1.08; margin:0; }
.hero .typed { font-family:var(--fh); font-weight:700; font-size:clamp(1.15rem,2.8vw,1.9rem); margin:1rem 0 1.2rem; min-height:2.4rem; }
.typing { display:inline-block; clip-path:inset(0 100% 0 0); animation:reveal 3.2s steps(52) .6s forwards; white-space:pre; }
.typing::after { content:""; display:inline-block; width:2px; height:1.05em; background:var(--accent); margin-left:5px; vertical-align:-.15em; animation:caret .9s step-end infinite; }
.hero p { color:var(--muted); max-width:34rem; line-height:1.65; font-size:1.02rem; margin:0 auto; }
.photo { width:200px; height:200px; border-radius:50%; object-fit:cover; border:2px solid rgba(var(--er),.5); margin-bottom:1.2rem; }
.btns { display:flex; gap:.8rem; justify-content:center; flex-wrap:wrap; margin-top:1.8rem; }
.stApp .btn { display:inline-flex; align-items:center; gap:.5rem; padding:.7rem 1.35rem; border-radius:var(--pill); border:1px solid var(--line); color:var(--text);
  background:color-mix(in srgb, var(--surface) 78%, transparent); font-weight:500; font-size:.92rem; transition:transform .2s, border-color .2s; }
.stApp .btn:hover { border-color:var(--accent); transform:translateY(-2px); }
.stApp .btn.primary { background:var(--btnbg); color:var(--onacc); border-color:var(--accent); font-weight:600; }
.socials { display:flex; gap:1rem; justify-content:center; margin-top:1.6rem; }
.stApp .soc { width:42px; height:42px; border-radius:50%; border:1px solid rgba(var(--er),.45); display:flex; align-items:center; justify-content:center;
  color:var(--text); background:color-mix(in srgb, var(--surface) 70%, transparent); transition:transform .2s, border-color .2s, color .2s; }
.stApp .soc:hover { border-color:var(--accent); color:var(--accent); transform:translateY(-3px); }
.soc svg { width:17px; height:17px; fill:currentColor; }
.scroll { margin-top:3rem; font-size:.7rem; letter-spacing:.2em; color:var(--muted); text-transform:uppercase; }
.scroll i { display:block; width:18px; height:28px; border:1.5px solid var(--muted); border-radius:10px; margin:.7rem auto 0; position:relative; }
.scroll i::after { content:""; position:absolute; left:50%; top:6px; width:3px; height:6px; margin-left:-1.5px; border-radius:2px; background:var(--accent); animation:bob 1.6s ease-in-out infinite; }
/* sections */
.section { padding-top:4.5rem; animation:rise .8s ease both; }
.section h2 { font-size:clamp(1.8rem,4vw,2.5rem); font-weight:800; text-align:center; margin:0 0 .4rem; }
.section .sub { text-align:center; color:var(--muted); margin:0 auto 2rem; max-width:34rem; }
.lead { color:var(--muted); line-height:1.8; max-width:46rem; font-size:1.05rem; margin:0 auto 1rem; text-align:center; }
.pill { display:inline-block; padding:.2rem .65rem; margin:0 .3rem .4rem 0; border-radius:var(--pill); background:rgba(var(--ar),.07);
  border:1px solid rgba(var(--ar),.28); color:var(--accent); font-size:.78rem; }
.card { border:1px solid var(--line); border-radius:var(--rad); background:var(--surface); padding:1.2rem 1.25rem; transition:transform .25s, border-color .25s; }
.card:hover { transform:translateY(-4px); border-color:rgba(var(--ar),.5); }
.card h4 { margin:.7rem 0 .6rem; font-size:1.02rem; }
.card p { color:var(--muted); margin:0; line-height:1.55; font-size:.93rem; }
.card .ico { width:34px; height:34px; stroke:var(--accent); fill:none; stroke-width:1.6; stroke-linecap:round; stroke-linejoin:round; }
/* project cards */
div[data-testid="stVerticalBlockBorderWrapper"] { background:var(--surface); border:1px solid var(--line) !important; border-radius:var(--rad);
  transition:transform .25s, border-color .25s, box-shadow .25s; animation:rise .8s ease both; }
div[data-testid="stVerticalBlockBorderWrapper"]:hover { transform:translateY(-5px); border-color:rgba(var(--ar),.5) !important; box-shadow:0 16px 36px rgba(0,0,0,.5); }
.ph { aspect-ratio:16/10; border-radius:10px; display:flex; align-items:center; justify-content:center; text-align:center; padding:1rem;
  background:linear-gradient(135deg,var(--t1) 0%,var(--t2) 100%); border:1px solid var(--line); font-family:var(--fh); font-weight:700; color:var(--muted); }
.ptitle { font-family:var(--fh); font-size:1.08rem; font-weight:700; margin:.7rem 0 .35rem; }
.pdesc { color:var(--muted); line-height:1.55; font-size:.88rem; margin-bottom:.7rem; height:5.4rem; overflow:hidden; }
.plinks { padding:.2rem 0 .6rem; }
.plinks a { margin-right:1.1rem; font-weight:500; font-size:.86rem; }
.plinks a:hover { text-decoration:underline !important; }
.timeline { position:relative; padding-left:1.6rem; border-left:2px solid var(--line); margin:0 auto; max-width:46rem; }
.timeline .item { position:relative; padding-bottom:1rem; }
.timeline .item::before { content:""; position:absolute; left:-2.05rem; top:.35rem; width:12px; height:12px; border-radius:50%; background:var(--accent); box-shadow:0 0 0 4px rgba(var(--ar),.15); }
.timeline h4 { margin:0; font-size:1.1rem; }
.timeline .meta { color:var(--accent); font-size:.9rem; margin:.15rem 0 .5rem; }
.timeline ul { margin:0; padding-left:1.1rem; color:var(--muted); line-height:1.65; }
.thumb { width:100%; aspect-ratio:16/10; object-fit:cover; border-radius:10px; border:1px solid var(--line); }
.badge { aspect-ratio:16/10; border-radius:10px; border:1px solid var(--line); display:flex; align-items:center; justify-content:center;
  background:linear-gradient(135deg,var(--t1),var(--t2)); font-family:var(--fh); font-weight:800; font-size:1.6rem; color:var(--accent); }
.cmeta { color:var(--muted); font-size:.9rem; }
.footer { margin-top:4rem; padding-top:1.3rem; border-top:1px solid var(--line); color:var(--muted); font-size:.88rem; text-align:center; }

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior:auto; }
  .stApp::before, .hero, .section, .status i, .scroll i::after, div[data-testid="stVerticalBlockBorderWrapper"] { animation:none !important; }
  .typing { animation:none; clip-path:none; }
  .card, .btn, .soc, div[data-testid="stVerticalBlockBorderWrapper"] { transition:none !important; }
}
</style>
"""
EXTRA = {
 "green": "",
 "violet": """<style>
.stApp::after{background-image:linear-gradient(rgba(var(--ar),.07) 1px,transparent 1px),linear-gradient(90deg,rgba(var(--ar),.07) 1px,transparent 1px);
  background-size:52px 52px;-webkit-mask-image:radial-gradient(75% 65% at 50% 42%,#000 30%,transparent 90%);mask-image:radial-gradient(75% 65% at 50% 42%,#000 30%,transparent 90%)}
.nav.bar{top:0;left:0;right:0;transform:none;width:100%;border-radius:0;border:none;border-bottom:1px solid var(--line);
  background:color-mix(in srgb, var(--bg) 72%, transparent);justify-content:space-between;align-items:center;padding:.85rem clamp(1rem,4vw,2.4rem)}
.nav.bar .links{display:flex;gap:1.7rem;flex-wrap:wrap}
.stApp .nav.bar a{text-transform:none;letter-spacing:0;font-size:.86rem;font-weight:500;color:#C9C9DD}
.stApp .nav.bar a:hover,.stApp .nav.bar a.on{color:#fff}
.stApp .nav.bar .logo{font-family:var(--fh);font-weight:800;font-size:1.05rem;letter-spacing:.02em;color:#fff}
.hero h1{letter-spacing:-.02em;font-size:clamp(2.8rem,7.4vw,5rem)}
.hero .typed{font-weight:500;font-size:clamp(1.05rem,2.4vw,1.55rem);color:#E6E6F2}
.status{color:var(--accent);background:rgba(var(--ar),.12);border-color:rgba(var(--ar),.32);font-weight:500;letter-spacing:.14em}
.status i{background:var(--accent)}
.stApp .btn.primary{border:none;box-shadow:0 8px 28px rgba(var(--ar),.35)}
.stApp .btn{padding:.78rem 1.6rem}
.hero p{max-width:36rem}
@media (max-width:700px){.nav.bar .links{display:none}}
</style>""",
 "lime": """<style>
.stApp::after{background:none}
.section h2{text-align:left;text-transform:uppercase;letter-spacing:-.01em}
.section h2::before{content:"/ ";color:var(--accent);-webkit-text-fill-color:var(--accent)}
.section .sub,.lead{text-align:left;margin-left:0;margin-right:auto}
.lead{font-size:.98rem}
.timeline{margin-left:0}
.nav{border-radius:2px}
.hero-split{flex-direction:row;text-align:left;align-items:center;justify-content:space-between;gap:3rem;padding-top:7rem}
.hs-left{flex:1.3;min-width:0}.hs-right{flex:.85}
.mega{font-family:var(--fh);text-transform:uppercase;font-size:clamp(3rem,8.4vw,6rem);line-height:.92;letter-spacing:-.03em;font-weight:700;margin:.3rem 0 1.3rem}
.mega .us{color:var(--accent);-webkit-text-fill-color:var(--accent);animation:caret .9s step-end infinite}
.hero-split p{margin:0;max-width:30rem;text-align:left;font-size:.95rem}
.hero-split .btns,.hero-split .socials{justify-content:flex-start}
.hello{font-size:1.05rem;color:var(--accent);letter-spacing:.06em;margin-bottom:.1rem}
.hero-split .typed{font-size:clamp(.9rem,1.7vw,1.15rem);margin:.1rem 0 1.2rem;min-height:1.6rem;color:var(--text);font-weight:500}
.hero-split .typing{white-space:normal}
.panel{border:1px solid var(--line);background:color-mix(in srgb, var(--surface) 80%, transparent);padding:1.2rem 1.3rem;backdrop-filter:blur(4px)}
.panel .ph-head{display:flex;justify-content:space-between;font-size:.7rem;letter-spacing:.14em;color:var(--muted);text-transform:uppercase;margin-bottom:.9rem}
.panel .row{display:flex;align-items:baseline;gap:.9rem;padding:.8rem 0;border-top:1px solid var(--line)}
.panel .row span{color:var(--accent);font-size:.8rem}
.panel .row b{font-family:var(--fh);font-weight:500;font-size:1.02rem}
.panel .row em{margin-left:auto;font-style:normal;color:var(--muted);font-size:.72rem;text-transform:uppercase}
.panel .bar{height:3px;background:var(--line);margin-top:.6rem;position:relative}
.panel .bar::after{content:"";position:absolute;left:0;top:0;height:100%;width:34%;background:var(--accent)}
.panel .cnt{font-family:var(--fh);font-size:2.6rem;margin-top:.9rem;line-height:1}
.panel .cnt small{font-family:var(--fb);font-size:.72rem;color:var(--muted);margin-left:.6rem;letter-spacing:.12em;text-transform:uppercase}
@media (max-width:860px){.hero-split{flex-direction:column}.hs-right{width:100%}}
</style>""",
}
EXTRA["mix"] = EXTRA["lime"].replace("</style>", """
.status{color:var(--accent);background:rgba(var(--ar),.12);border-color:rgba(var(--ar),.32);font-weight:500}
.stApp .btn.primary{border:none;box-shadow:0 8px 28px rgba(var(--ar),.35)}
.mega .acc{filter:drop-shadow(0 0 22px rgba(var(--ar),.35))}
</style>""")
st.markdown(THEME_CSS + CSS + EXTRA[THEME], unsafe_allow_html=True)

# Helpers
ICONS = {
    "brain": '<svg class="ico" viewBox="0 0 32 32"><circle cx="9" cy="10" r="3"/><circle cx="9" cy="22" r="3"/><circle cx="23" cy="16" r="3.5"/><path d="M12 10l8 5M12 22l8-5M9 13v6"/></svg>',
    "spark": '<svg class="ico" viewBox="0 0 32 32"><path d="M16 4l2.6 8.4L27 15l-8.4 2.6L16 26l-2.6-8.4L5 15l8.4-2.6z"/></svg>',
    "loop": '<svg class="ico" viewBox="0 0 32 32"><path d="M26 14a10 10 0 00-18-4M6 18a10 10 0 0018 4"/><path d="M8 5v6h6M24 27v-6h-6"/></svg>',
    "tools": '<svg class="ico" viewBox="0 0 32 32"><path d="M20 6a6 6 0 00-7 8L5 22l5 5 8-8a6 6 0 008-7l-4 4-4-1-1-4z"/></svg>',
}
GH_SVG = '<svg viewBox="0 0 16 16"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38v-1.33c-2.23.48-2.7-1.07-2.7-1.07-.36-.92-.89-1.17-.89-1.17-.73-.5.05-.49.05-.49.8.06 1.23.83 1.23.83.72 1.22 1.88.87 2.33.66.07-.52.28-.87.5-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.83-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.6 7.6 0 014 0c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48v2.2c0 .21.15.46.55.38A8 8 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>'
LI_SVG = '<svg viewBox="0 0 16 16"><path d="M0 1.15C0 .52.52 0 1.17 0h13.66C15.48 0 16 .52 16 1.15v13.7c0 .63-.52 1.15-1.17 1.15H1.17C.52 16 0 15.48 0 14.85zM4.94 13.4V6.17H2.54v7.23zM3.74 5.18c.84 0 1.36-.55 1.36-1.25-.02-.71-.52-1.25-1.34-1.25s-1.36.54-1.36 1.25c0 .7.52 1.25 1.33 1.25zm4.9 8.22V9.36c0-.22.02-.43.08-.59.17-.43.57-.88 1.23-.88.87 0 1.21.66 1.21 1.63v3.88h2.4V9.25c0-2.22-1.18-3.25-2.76-3.25-1.27 0-1.84.7-2.16 1.19V6.17h-2.4c.03.68 0 7.23 0 7.23z"/></svg>'
MAIL_SVG = '<svg viewBox="0 0 16 16"><path d="M0 4a2 2 0 012-2h12a2 2 0 012 2v.2L8 8.9 0 4.2zm0 1.4V12a2 2 0 002 2h12a2 2 0 002-2V5.4L8 10.1z"/></svg>'
DL_SVG = '<svg viewBox="0 0 16 16" width="15" height="15" fill="currentColor"><path d="M8 11L3.5 6.5l1-1L7.3 8.3V1h1.4v7.3l2.8-2.8 1 1zM2 13h12v1.5H2z"/></svg>'

def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()

def project_images(slug):
    folder = BASE / "assets" / "projects" / slug
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"})

def pills(items):
    return "".join(f'<span class="pill">{i}</span>' for i in items)

def heading(before, accent, sec_id=None, sub=None):
    idattr = f' id="{sec_id}"' if sec_id else ""
    sub_html = f'<p class="sub">{sub}</p>' if sub else ""
    st.markdown(f'<div class="section"{idattr}><h2>{before} <span class="acc">{accent}</span></h2>{sub_html}</div>', unsafe_allow_html=True)

# Nav and hero

_links = ('<a class="on" href="#home">Home</a><a href="#about">About</a><a href="#skills">Skills</a>'
          '<a href="#projects">Projects</a><a href="#experience">Experience</a><a href="#contact">Contact</a>')
if THEME == "violet":
    st.markdown(f'<div class="nav bar"><a class="logo" href="#home">{FIRST_NAME.upper()}<span class="acc">.{NAME.split()[-1][0]}</span></a><div class="links">{_links}</div></div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="nav">{_links}</div>', unsafe_allow_html=True)

photo_html = ""
for c in PHOTO_CANDIDATES:
    if (BASE / c).is_file():
        photo_html = f'<img class="photo" alt="{NAME}" src="{data_uri(BASE / c)}">'
        break

resume_path = BASE / RESUME
if resume_path.is_file():
    second_btn = f'<a class="btn" download="{NAME.replace(" ", "_")}_Resume.pdf" href="{data_uri(resume_path)}">Download Resume {DL_SVG}</a>'
else:
    second_btn = '<a class="btn" href="#contact">Get in touch</a>'

socials = f'<a class="soc" href="{GITHUB_URL}" target="_blank" aria-label="GitHub">{GH_SVG}</a>'
if LINKEDIN:
    socials = f'<a class="soc" href="{LINKEDIN}" target="_blank" aria-label="LinkedIn">{LI_SVG}</a>' + socials
if EMAIL:
    socials += f'<a class="soc" href="https://mail.google.com/mail/?view=cm&fs=1&to={EMAIL}" target="_blank" aria-label="Email">{MAIL_SVG}</a>'

if T["layout"] == "split":
    rows = "".join(
        f'<div class="row"><span>{i:02d}</span><b>{p["title"]}</b><em>{p["tags"][0]}</em></div>'
        for i, p in enumerate(PROJECTS[:3], 1)
    )
    st.markdown(f"""
<div class="hero hero-split" id="home">
  <div class="hs-left">
  {photo_html}
    <div class="status"><i></i>{STATUS}</div>
    <div class="hello">Hi, I'm</div>
    <h1 class="mega">{FIRST_NAME}<br><span class="acc">{NAME.split()[-1]}</span><span class="us">_</span></h1>
    <div class="typed"><span class="typing">{TYPING_LINE}</span></div>
    <p>{HERO_TEXT}</p>
    <div class="btns"><a class="btn primary" href="#projects">View Projects</a>{second_btn}</div>
    <div class="socials">{socials}</div>
  </div>
  <div class="hs-right"><div class="panel">
    <div class="ph-head"><span>Selected work</span><span>{NAME}</span></div>
    {rows}
    <div class="bar"></div>
    <div class="cnt">{len(PROJECTS):02d}<small>projects</small></div>
  </div></div>
</div>""", unsafe_allow_html=True)
else:
    st.markdown(f"""
<div class="hero" id="home">
  {photo_html}
  <div class="status"><i></i>{STATUS}</div>
  <h1>Hi, I'm <span class="acc">{FIRST_NAME}</span></h1>
  <div class="typed"><span class="typing">{TYPING_LINE}</span></div>
  <p>{HERO_TEXT}</p>
  <div class="btns"><a class="btn primary" href="#projects">View Projects <span style="margin-left:.2rem">›</span></a>{second_btn}</div>
  <div class="socials">{socials}</div>
  <div class="scroll">Scroll to explore<i></i></div>
</div>""", unsafe_allow_html=True)

# About
heading("About", "Me", "about")
about_html = "".join(f"<p class='lead'>{p}</p>" for p in ABOUT)
st.markdown(f'{about_html}<p class="lead"><strong style="color:var(--text)">Education:</strong> {EDUCATION}</p>', unsafe_allow_html=True)


# Skills and interests

heading("My", "Skills", "skills")
cols = st.columns(4, gap="medium")
for col, (icon, group, items) in zip(cols, SKILLS):
    with col:
        st.markdown(f'<div class="card" style="min-height:235px">{ICONS[icon]}<h4>{group}</h4>{pills(items)}</div>', unsafe_allow_html=True)

heading("Technical", "Interests")
icols = st.columns(len(INTERESTS), gap="medium")
for col, (t, d) in zip(icols, INTERESTS):
    with col:
        st.markdown(f'<div class="card" style="min-height:150px"><h4 style="margin-top:0;color:var(--accent)">{t}</h4><p>{d}</p></div>', unsafe_allow_html=True)


# Projects (3-column grid)

heading("Featured", "Projects", "projects", "Selected work across machine learning, reinforcement learning and LLM agents.")
for start in range(0, len(PROJECTS), 3):
    row = PROJECTS[start:start + 3]
    pcols = st.columns(3, gap="large")
    for col, p in zip(pcols, row):
        with col:
            imgs = project_images(p["slug"])
            with st.container(border=True):
                if imgs:
                    st.image(str(imgs[0]), use_container_width=True)
                else:
                    st.markdown(f'<div class="ph">{p["title"]}</div>', unsafe_allow_html=True)
                links = ""
                if p["demo"]:
                    links += f'<a href="{p["demo"]}" target="_blank">View Project →</a>'
                links += f'<a href="{p["repo"] or GITHUB_URL}" target="_blank">Source Code →</a>'
                st.markdown(
                    f'<div class="ptitle">{p["title"]}</div><div class="pdesc">{p["desc"]}</div>'
                    f'<div>{pills(p["tags"])}</div><div class="plinks">{links}</div>',
                    unsafe_allow_html=True,
                )
                if len(imgs) > 1:
                    with st.expander(f"More screenshots ({len(imgs) - 1})"):
                        for extra in imgs[1:]:
                            st.image(str(extra), use_container_width=True)
    st.write("")

# Experience and certifications
heading("My", "Experience", "experience")
for i, e in enumerate(EXPERIENCE):
    pts = "".join(f"<li>{x}</li>" for x in e["points"])
    st.markdown(
        f'<div class="timeline"><div class="item"><h4>{e["role"]}, {e["org"]}</h4>'
        f'<div class="meta">{e["period"]}</div><ul>{pts}</ul></div></div>',
        unsafe_allow_html=True,
    )
    certificates = e.get("certificates", [])
    if certificates:
        state_key = f"show_experience_certificates_{i}"
        view_label = "View Certificate" if len(certificates) == 1 else "View Certificates"
        hide_label = "Hide Certificate" if len(certificates) == 1 else "Hide Certificates"
        if st.button(hide_label if st.session_state.get(state_key, False) else view_label, key=f"experience_cert_button_{i}"):
            st.session_state[state_key] = not st.session_state.get(state_key, False)
        if st.session_state.get(state_key, False):
            # Center a single certificate and keep it the same width as each
            # certificate in the three-column Inphora layout.
            if len(certificates) == 1:
                cert_cols = st.columns(3, gap="medium")
                display_slots = [(1, certificates[0])]
            else:
                cert_cols = st.columns(min(3, len(certificates)), gap="medium")
                display_slots = [(j, cert) for j, cert in enumerate(certificates)]

            for slot, cert in display_slots:
                cert_path = BASE / cert["file"]
                with cert_cols[slot]:
                    if cert_path.is_file():
                        st.image(str(cert_path), caption=cert["title"], use_container_width=True)
                    else:
                        st.warning(f'Certificate image not found: {cert["file"]}')

heading("My", "Certifications", "certifications")
ccols = st.columns(len(CERTIFICATIONS), gap="large")
for col, c in zip(ccols, CERTIFICATIONS):
    tp = BASE / c["thumb"] if c.get("thumb") else None
    visual = (f'<img class="thumb" alt="{c["title"]}" src="{data_uri(tp)}">' if tp and tp.is_file() else '<div class="badge">OCI</div>')
    link = f'<div style="margin-top:.6rem"><a href="{c["url"]}" target="_blank">View credential →</a></div>' if c["url"] else ""
    with col:
        st.markdown(f'<div class="card">{visual}<h4>{c["title"]}</h4><div class="cmeta">{c["issuer"]}</div>{link}</div>', unsafe_allow_html=True)
        badge_url = c.get("badge_url", "").strip()
        st.link_button("Verify Badge" if badge_url else "Verify Badge (add URL)", badge_url or "https://www.oracle.com/", disabled=not bool(badge_url), use_container_width=True)

# Contact
heading("Let's", "Connect", "contact")
contact_btns = f'<a class="btn" href="{GITHUB_URL}" target="_blank">{GH_SVG.replace("<svg", "<svg width=16 height=16 fill=currentColor")}GitHub</a>'
if EMAIL:
    contact_btns = f'<a class="btn primary" href="https://mail.google.com/mail/?view=cm&fs=1&to={EMAIL}" target="_blank">Email me</a>' + contact_btns
if LINKEDIN:
    contact_btns += f'<a class="btn" href="{LINKEDIN}" target="_blank">LinkedIn</a>'
st.markdown(
    f'<p class="lead">I\'m open to machine learning internships. Reach out if you want to talk about a project or an opportunity.</p>'
    f'<div class="btns">{contact_btns}</div>'
    f'<div class="footer">{NAME} · {LOCATION}</div>',
    unsafe_allow_html=True
)

