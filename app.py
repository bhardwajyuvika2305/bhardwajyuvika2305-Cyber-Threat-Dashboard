try:
    import streamlit as st  # type: ignore[import-not-found]
except Exception:
    # Provide a lightweight fallback for environments where Streamlit isn't installed
    class _DummySidebar:
        def markdown(self, *a, **k): pass
        def divider(self): pass
        def radio(self, *a, **k): return a[1][0] if len(a) > 1 else None
        def multiselect(self, *a, **k): return k.get('default', [])
        def select_slider(self, *a, **k): return a[1][0] if len(a) > 1 else None
        def slider(self, *a, **k): return k.get('value', a[2] if len(a) > 2 else None)

    class _DummySt:
        def set_page_config(self, *a, **k): pass
        def markdown(self, *a, **k): pass
        def write(self, *a, **k): pass
        def plotly_chart(self, *a, **k): pass
        def dataframe(self, *a, **k): pass
        def columns(self, n): return [type('C', (), {'metric': lambda *a, **k: None})() for _ in range(n)]
        sidebar = _DummySidebar()

        def select_slider(self, *a, **k): return a[1][0] if len(a) > 1 else None

        def metric(self, *a, **k): pass

        class cache_data:
            def __init__(self, f=None):
                self.f = f
            def __call__(self, f):
                return f

    st = _DummySt()

import pandas as pd  # type: ignore[import-not-found]
try:
    import numpy as np  # type: ignore[import-not-found]
except Exception:
    # Lightweight fallback for environments without NumPy.
    import random
    import math

    class _DummyRandom:
        def seed(self, s):
            random.seed(s)

        def exponential(self, scale, size):
            return [random.expovariate(1.0 / scale) for _ in range(size)]

        def normal(self, loc, scale, size):
            return [random.gauss(loc, scale) for _ in range(size)]

        def choice(self, seq, size):
            return [random.choice(seq) for _ in range(size)]

    class _DummyNP:
        random = _DummyRandom()

        @staticmethod
        def round(arr, decimals=0):
            factor = 10 ** decimals
            return [math.floor(x * factor + 0.5) / factor for x in arr]

        @staticmethod
        def clip(arr, a_min, a_max):
            return [max(a_min, min(a_max, x)) for x in arr]

        @staticmethod
        def where(cond, a, b):
            return [a if c else b for c in cond]

        @staticmethod
        def array(seq):
            return list(seq)

    np = _DummyNP()
try:
    import plotly.express as px  # type: ignore[import-not-found]
    import plotly.graph_objects as go  # type: ignore[import-not-found]
except Exception:
    # Fallback stubs when plotly is not available in the environment (prevents import errors)
    px = None
    go = None
import os

# 1. Force Fluid Canvas Layout & High-Contrast Styles
st.set_page_config(page_title="Aegis AI Cyber-Threat Engine", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        
        /* Eliminate typography fuzziness across all panels */
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            -webkit-font-smoothing: antialiased !important;
            text-rendering: optimizeLegibility !important;
            background: radial-gradient(circle at 50% 50%, #050811 0%, #010205 100%) !important;
        }

        /* PREMIUM TEAL GLASS PANELS (High Contrast / No Red) */
        .glass-panel {
            background: rgba(255, 255, 255, 0.01) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border: 1px solid rgba(0, 242, 254, 0.15) !important;
            border-radius: 16px !important;
            padding: 26px !important;
            margin-bottom: 24px !important;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6) !important;
        }

        h1, h2, h3, h4, p, label, span { color: #FFFFFF !important; }

        .neon-title {
            font-size: 3.2rem !important;
            font-weight: 800 !important;
            background: linear-gradient(135deg, #00F2FE 0%, #4FACFE 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0px !important;
        }

        .subtitle-text {
            color: #94A3B8 !important;
            font-size: 1.1rem !important;
            margin-bottom: 2.5rem !important;
        }

        .teal-badge {
            background: rgba(0, 242, 254, 0.08) !important;
            color: #00F2FE !important;
            border: 1px solid rgba(0, 242, 254, 0.35) !important;
            padding: 6px 14px !important;
            border-radius: 8px !important;
            font-size: 0.85rem !important;
            font-weight: 700 !important;
            display: inline-block;
            margin-bottom: 1.5rem !important;
        }

        /* OVERRIDE STREAMLIT METRICS COMPONENTS */
        div[data-testid="stMetric"] {
            background: rgba(0, 242, 254, 0.02) !important;
            border: 1px solid rgba(0, 242, 254, 0.22) !important;
            border-radius: 14px !important;
            padding: 18px !important;
        }

        section[data-testid="stSidebar"] {
            background-color: #03050A !important;
            border-right: 1px solid rgba(0, 242, 254, 0.1) !important;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Optimized Pipeline Ingestion
@st.cache_data
def generate_cyber_matrix():
    if os.path.exists("cyber_threat_manifest.csv"):
        return pd.read_csv("cyber_threat_manifest.csv")
    else:
        np.random.seed(42)
        records = 6000
        vectors = ["DDoS Flooding", "SQL Injection Spectrum", "Phishing API Exfiltration", "Ransomware Core Payload"]
        zones = ["Cloud Edge Cluster", "On-Prem Gateway", "DMZ Proxy Subnet"]
        
        payload_sizes = np.random.exponential(scale=450, size=records) + 12
        anomaly_indices = (payload_sizes * 0.04) + np.random.normal(30, 15, size=records)
        is_breach = np.where(anomaly_indices > 65, 1, 0)
        
        return pd.DataFrame({
            "Incident_ID": [f"SEC_{i:06d}" for i in range(records)],
            "Attack_Vector": np.random.choice(vectors, size=records),
            "Infrastructure_Zone": np.random.choice(zones, size=records),
            "Payload_Volume_MB": np.round(payload_sizes, 2),
            "Neural_Anomaly_Score": np.round(np.clip(anomaly_indices, 0, 100), 2),
            "Breach_Status": is_breach
        })

df = generate_cyber_matrix()

# --- SIDEBAR INTERACTION ROUTER ---
st.sidebar.markdown("### 🗺️ Control Terminal")
primary_selection = st.sidebar.radio(
    "Select Target Operational Node:",
    ["🛡️ Threat Control Domain", "🔮 Generative Inference Sandbox", "🗄️ Ingestion Log Matrix"]
)

st.sidebar.divider()
st.sidebar.markdown("### 🔍 Ingestion Pipeline Scope")
selected_vectors = st.sidebar.multiselect(
    "Isolate Attack Vectors:", options=df["Attack_Vector"].unique().tolist(), default=df["Attack_Vector"].unique().tolist()
)
filtered_df = df[df["Attack_Vector"].isin(selected_vectors)]

# App Hero Typography Block
st.markdown('<h1 class="neon-title">AEGIS // CYBER THREAT ENGINE</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Real-Time Adversarial Anomaly Tracking & Neural Exploit Detection Layer</p>', unsafe_allow_html=True)

# --- HORIZONTAL SUB-SLIDER MAIN DECK ---
if primary_selection == "🛡️ Threat Control Domain":
    st.markdown('<span class="teal-badge">Active Domain: Infrastructure Perimeter Defense</span>', unsafe_allow_html=True)
    sub_view = st.select_slider("Shift Systemic Analytical Viewport:", options=["Macro Surveillance KPIs", "Topological Surface Density", "Volumetric Risk Vectors"])
    
    if sub_view == "Macro Surveillance KPIs":
        c1, c2, c3 = st.columns(3)
        c1.metric("Packets Analyzed", f"{len(filtered_df):,}")
        c2.metric("Gross Data Weight", f"{filtered_df['Payload_Volume_MB'].sum():,.1f} MB")
        c3.metric("Critical Exploits Isolated", f"{filtered_df['Breach_Status'].sum():,}")
        
        st.write("")
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown("#### High-Dimensional Neural Anomaly vs Volume Profiling Matrix")
        fig1 = px.scatter(
            filtered_df, x="Payload_Volume_MB", y="Neural_Anomaly_Score",
            color=filtered_df["Breach_Status"].astype(str), labels={"color": "Breach Vector Trigger"},
            template="plotly_dark", color_discrete_map={"0": "#00F2FE", "1": "#FFB300"}
        )
        fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    elif sub_view == "Topological Surface Density":
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown("#### Surface Apportionment Across Infrastructure Zones")
        fig2 = px.pie(filtered_df, names="Infrastructure_Zone", values="Payload_Volume_MB", hole=0.5, template="plotly_dark", color_discrete_sequence=px.colors.sequential.Cyan)
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown("#### Volumetric Signal Distribution Profile Matrix")
        fig3 = px.histogram(filtered_df, x="Neural_Anomaly_Score", color="Attack_Vector", marginal="box", barmode="overlay", template="plotly_dark")
        fig3.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif primary_selection == "🔮 Generative Inference Sandbox":
    st.markdown('<span class="teal-badge">Active Domain: Prescriptive Vulnerability Simulation Labs</span>', unsafe_allow_html=True)
    sub_view = st.select_slider("Shift Modeling Paradigm:", options=["Correlation Matrix Horizons", "Simulative Impact Gauge"])
    
    if sub_view == "Correlation Matrix Horizons":
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        corr = filtered_df[["Payload_Volume_MB", "Neural_Anomaly_Score", "Breach_Status"]].corr()
        fig_heat = go.Figure(go.Heatmap(z=corr.values, x=corr.columns, y=corr.columns, colorscale="Electric"))
        fig_heat.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_heat, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        sim_volume = st.slider("Set Simulated Packet Injection Buffer Volume (MB):", 10, 2000, 500)
        sim_score = min(100.0, float((sim_volume * 0.045) + 20.0))
        
        fig_g = go.Figure(go.Indicator(
            mode="gauge+number", value=sim_score, title={'text': "Inferred Exploitation Risk Probability Index", 'font': {'color': "white"}},
            gauge={'bar': {'color': "#00F2FE"}, 'axis': {'range': [0, 100]}}
        ))
        fig_g.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "white"}, height=240)
        st.plotly_chart(fig_g, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<span class="teal-badge">Active Domain: Ingestion Audit Stream Registry Ledger</span>', unsafe_allow_html=True)
    sub_view = st.select_slider("Slice Depth Ingestion View:", options=["Top 100 Critical Neural Score Anomaly Rows", "Full Cluster Storage Log Matrix"])
    
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    if sub_view == "Top 100 Critical Neural Score Anomaly Rows":
        st.dataframe(filtered_df.sort_values(by="Neural_Anomaly_Score", ascending=False).head(100), use_container_width=True)
    else:
        st.dataframe(filtered_df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)