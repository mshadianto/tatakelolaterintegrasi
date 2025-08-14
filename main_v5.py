import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime
from datetime import timedelta, date
import base64
import io
import json
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Pemutakhiran Pedoman Tata Kelola - PT Surveyor Indonesia",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with improved styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 2rem;
        padding: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .sub-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #2c5282;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        padding: 1rem;
        background: linear-gradient(90deg, #f0f8ff 0%, #e6f3ff 100%);
        border-left: 5px solid #2c5282;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        border-left: 5px solid #3182ce;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    
    .timeline-item {
        padding: 1.5rem;
        margin: 1rem 0;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-left: 5px solid #28a745;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    
    .timeline-item:hover {
        transform: translateX(10px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.12);
    }
    
    .benchmark-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        transition: transform 0.3s ease;
    }
    
    .benchmark-card:hover {
        transform: scale(1.05);
    }
    
    .success-box {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        border: 2px solid #28a745;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(40, 167, 69, 0.2);
    }
    
    .warning-box {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
        border: 2px solid #ffc107;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(255, 193, 7, 0.2);
    }
    
    .info-box {
        background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%);
        border: 2px solid #17a2b8;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(23, 162, 184, 0.2);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    .stSelectbox > div > div {
        background-color: white;
        border-radius: 10px;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.2);
    }
    
    .metric-container {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
    
    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .governance-principle {
        background: white;
        padding: 1.2rem;
        border-radius: 12px;
        border-left: 4px solid #3182ce;
        margin: 0.8rem 0;
        box-shadow: 0 3px 12px rgba(0,0,0,0.08);
    }
    
    .parenting-model {
        background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state with August 2025 timeline
if 'project_start_date' not in st.session_state:
    st.session_state.project_start_date = date(2025, 8, 1)  # Agustus 2025

if 'current_phase' not in st.session_state:
    st.session_state.current_phase = 1

if 'overall_progress' not in st.session_state:
    st.session_state.overall_progress = 15  # Progress awal Agustus 2025

# Sidebar with enhanced navigation
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem;">
    <div style="background: linear-gradient(135deg, #1f4e79 0%, #2c5282 100%); color: white; padding: 1rem; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <h3 style="margin: 0; color: white;">PT Surveyor Indonesia</h3>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.9;">Governance Excellence</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# Enhanced navigation with icons and descriptions
pages = {
    "🏠 Dashboard": {
        "id": "dashboard",
        "desc": "Overview & Key Metrics"
    },
    "📊 Benchmarking": {
        "id": "benchmarking",
        "desc": "Best Practices Analysis"
    },
    "🏗️ Corporate Parenting": {
        "id": "parenting", 
        "desc": "Parent-Subsidiary Model"
    },
    "📋 GCG Framework": {
        "id": "framework", 
        "desc": "Governance Structure & GRC"
    },
    "⏱️ Timeline 60 Hari": {
        "id": "timeline",
        "desc": "Project Schedule"
    },
    "📈 Monitoring": {
        "id": "monitoring",
        "desc": "Progress & KPIs"
    },
    "📁 Dokumentasi": {
        "id": "documentation",
        "desc": "Resources & Files"
    },
    "🎯 Next Steps": {
        "id": "nextsteps",
        "desc": "Action Plans"
    }
}

# Create enhanced sidebar menu
selected_page = st.sidebar.selectbox(
    "Pilih Halaman",
    list(pages.keys()),
    format_func=lambda x: f"{x}\n{pages[x]['desc']}"
)

page = pages[selected_page]["id"]

# Progress indicator in sidebar
st.sidebar.markdown("### 📊 Overall Progress")
progress_bar = st.sidebar.progress(st.session_state.overall_progress / 100)
st.sidebar.write(f"{st.session_state.overall_progress}% Complete")

# Quick stats in sidebar
st.sidebar.markdown("### 📈 Quick Stats")
days_elapsed = (date.today() - st.session_state.project_start_date).days
st.sidebar.metric("Days Elapsed", f"{days_elapsed}/60")
st.sidebar.metric("Current Phase", f"Fase {st.session_state.current_phase}")
st.sidebar.metric("Active Workstreams", "4")

# Main header with enhanced styling
st.markdown("""
<div class="main-header">
    🏢 Pemutakhiran Pedoman Tata Kelola Terintegrasi<br>
    <span style="font-size: 1.5rem; opacity: 0.9;">PT Surveyor Indonesia</span><br>
    <span style="font-size: 1rem; opacity: 0.8;">Agustus 2025 - Excellence in Corporate Governance</span>
</div>
""", unsafe_allow_html=True)

# Helper functions
@st.cache_data
def get_benchmark_data():
    return {
        'BUMN': ['Pertamina*', 'Telkom', 'Bank Mandiri', 'Surveyor Indonesia (Target)'],
        'Governance Score': [85, 82, 88, 90],
        'Digital Integration': [75, 90, 70, 85],
        'Synergy Optimization': [80, 75, 92, 88],
        'Risk Management': [88, 80, 85, 90],
        'Subsidiaries': [12, 12, 11, 8],
        'Revenue (T IDR)': [1250, 150.6, 146.6, 0.26],
        'Net Profit (T IDR)': [49.5, 30.2, 55.8, 0.05],
        'Model': ['Strategic Control', 'Strategic Integration', 'Financial Holdings', 'Strategic Control (Target)']
    }

@st.cache_data
def get_timeline_data():
    start_date = st.session_state.project_start_date
    current_day = (date.today() - start_date).days
    
    phase1_progress = min(max((current_day - 0) / 20 * 100, 0), 100)
    phase2_progress = min(max((current_day - 20) / 25 * 100, 0), 100) 
    phase3_progress = min(max((current_day - 45) / 15 * 100, 0), 100)
    
    return {
        'Phase': ['Fase 1: Assessment', 'Fase 2: Development', 'Fase 3: Finalization'],
        'Duration': ['Hari 1-20', 'Hari 21-45', 'Hari 46-60'],
        'Start Date': [start_date, start_date + timedelta(days=20), start_date + timedelta(days=45)],
        'End Date': [start_date + timedelta(days=19), start_date + timedelta(days=44), start_date + timedelta(days=59)],
        'Status': [
            '✅ Completed' if phase1_progress >= 100 else '🔄 In Progress' if phase1_progress > 0 else '⏳ Planned',
            '✅ Completed' if phase2_progress >= 100 else '🔄 In Progress' if phase2_progress > 0 else '⏳ Planned',
            '✅ Completed' if phase3_progress >= 100 else '🔄 In Progress' if phase3_progress > 0 else '⏳ Planned'
        ],
        'Progress': [round(phase1_progress), round(phase2_progress), round(phase3_progress)],
        'Key Deliverable': ['Gap Analysis Report', 'Validated Framework', 'Final Pedoman']
    }

@st.cache_data
def get_kpi_data():
    return {
        'KPI': ['Stakeholder Satisfaction', 'Timeline Adherence', 'Quality Score', 'Budget Adherence'],
        'Current': [82, 88, 85, 96],
        'Target': [85, 90, 90, 95],
        'Trend': [3, 2, 4, 1]
    }

# Dashboard Page
if page == "dashboard":
    st.markdown('<div class="sub-header">📊 Executive Dashboard - Agustus 2025</div>', unsafe_allow_html=True)
    
    # Enhanced key metrics with real-time updates
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1f4e79; margin-bottom: 0.5rem;">⏰ Timeline</h3>
            <h1 style="color: #e53e3e; margin: 0; font-size: 2.5rem;">60</h1>
            <h3 style="color: #e53e3e; margin: 0;">Hari</h3>
            <p style="margin: 0; color: #666;">Agustus - Oktober 2025</p>
            <div style="margin-top: 0.5rem;">
                <small style="color: #28a745;">✓ Intensive Execution</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1f4e79; margin-bottom: 0.5rem;">🏆 Benchmarking</h3>
            <h1 style="color: #38a169; margin: 0; font-size: 2.5rem;">5</h1>
            <h3 style="color: #38a169; margin: 0;">BUMN</h3>
            <p style="margin: 0; color: #666;">Best Practices</p>
            <div style="margin-top: 0.5rem;">
                <small style="color: #28a745;">✓ Leading companies analyzed</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1f4e79; margin-bottom: 0.5rem;">🎯 Framework</h3>
            <h1 style="color: #3182ce; margin: 0; font-size: 2.5rem;">4</h1>
            <h3 style="color: #3182ce; margin: 0;">Models</h3>
            <p style="margin: 0; color: #666;">Corporate Parenting</p>
            <div style="margin-top: 0.5rem;">
                <small style="color: #28a745;">✓ Strategic Control Focus</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1f4e79; margin-bottom: 0.5rem;">🌟 Target</h3>
            <h1 style="color: #805ad5; margin: 0; font-size: 2.5rem;">90</h1>
            <h3 style="color: #805ad5; margin: 0;">Score</h3>
            <p style="margin: 0; color: #666;">Excellence</p>
            <div style="margin-top: 0.5rem;">
                <small style="color: #28a745;">✓ World-class governance</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Real-time project health dashboard
    st.markdown('<div class="sub-header">🎯 Project Health Dashboard - Agustus 2025</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        # Enhanced progress visualization
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Overall Progress', 'Phase Progress', 'Quality Score', 'Resource Utilization'),
            specs=[[{"type": "indicator"}, {"type": "indicator"}],
                   [{"type": "indicator"}, {"type": "indicator"}]]
        )
        
        # Overall Progress
        fig.add_trace(
            go.Indicator(
                mode="gauge+number+delta",
                value=st.session_state.overall_progress,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Overall Progress (%)"},
                delta={'reference': 20},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#3182ce"},
                    'steps': [
                        {'range': [0, 25], 'color': "#fed7d7"},
                        {'range': [25, 50], 'color': "#feebc8"},
                        {'range': [50, 75], 'color': "#c6f6d5"},
                        {'range': [75, 100], 'color': "#9ae6b4"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 90
                    }
                }
            ),
            row=1, col=1
        )
        
        # Phase Progress
        current_phase_progress = 75 if st.session_state.current_phase == 1 else 25 if st.session_state.current_phase == 2 else 0
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=current_phase_progress,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Current Phase (%)"},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#38a169"},
                    'steps': [{'range': [0, 100], 'color': "#f0fff4"}],
                }
            ),
            row=1, col=2
        )
        
        # Quality Score
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=85,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Quality Score (%)"},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#805ad5"},
                    'steps': [{'range': [0, 100], 'color': "#faf5ff"}],
                }
            ),
            row=2, col=1
        )
        
        # Resource Utilization
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=82,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Resource Utilization (%)"},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#e53e3e"},
                    'steps': [{'range': [0, 100], 'color': "#fff5f5"}],
                }
            ),
            row=2, col=2
        )
        
        fig.update_layout(height=500, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 📋 Agustus 2025 Focus")
        st.markdown("""
        <div class="info-box">
            <h4>🎯 Week 1-2 Priorities</h4>
            <ul>
                <li>🔄 Project mobilization</li>
                <li>🔄 Stakeholder mapping</li>
                <li>⏳ Current state assessment</li>
                <li>⏳ Benchmark analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### ⚠️ Critical Success Factors")
        st.markdown("""
        <div class="warning-box">
            <h4>🚨 Key Requirements</h4>
            <ul>
                <li>Full stakeholder commitment</li>
                <li>Resource availability</li>
                <li>4 parallel workstreams</li>
                <li>Intensive timeline adherence</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("### 📊 KPI Summary")
        kpi_data = get_kpi_data()
        for i, kpi in enumerate(kpi_data['KPI']):
            current = kpi_data['Current'][i]
            target = kpi_data['Target'][i]
            trend = kpi_data['Trend'][i]
            
            delta_color = "normal" if trend >= 0 else "inverse"
            st.metric(
                label=kpi.replace(" ", "\n"),
                value=f"{current}%",
                delta=f"{trend:+d}%",
                delta_color=delta_color
            )

# Corporate Parenting Page
elif page == "parenting":
    st.markdown('<div class="sub-header">🏗️ Corporate Parenting Model Framework</div>', unsafe_allow_html=True)
    
    # Fundamental Principles
    st.markdown("### 🎯 Prinsip Fundamental Tata Kelola Terintegrasi")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="governance-principle">
            <h4>🎯 Unity in Diversity</h4>
            <ul>
                <li><strong>Kesatuan visi dan misi korporat</strong></li>
                <li>Fleksibilitas implementasi sesuai karakteristik bisnis</li>
                <li>Standardisasi pada aspek kritis</li>
                <li>Lokalisasi pada aspek operasional</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="governance-principle">
            <h4>💎 Value Creation Focus</h4>
            <ul>
                <li><strong>Orientasi pada penciptaan nilai jangka panjang</strong></li>
                <li>Optimasi sinergi lintas anak perusahaan</li>
                <li>Balance antara growth dan profitability</li>
                <li>Sustainable competitive advantage</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="governance-principle">
            <h4>🛡️ Integrated Risk Management</h4>
            <ul>
                <li><strong>Risk appetite yang selaras di seluruh grup</strong></li>
                <li>Early warning system terintegrasi</li>
                <li>Coordination dalam crisis management</li>
                <li>Proactive risk mitigation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Corporate Parenting Models
    st.markdown("### 🏗️ Corporate Parenting Model Analysis")
    
    parenting_models = {
        'Model': ['Financial Control', 'Strategic Control', 'Strategic Planning', 'Financial Engineering'],
        'Karakteristik': [
            'Focus financial, decentralized',
            'Balance financial-strategic',
            'Centralized planning',
            'Financial restructuring focus'
        ],
        'Cocok untuk': [
            'Portfolio tidak terkait',
            'Related diversification',
            'Integrated portfolio',
            'Turnaround situations'
        ],
        'PT SI Fit Score': [60, 90, 75, 40],
        'Implementation Complexity': [25, 60, 85, 45]
    }
    
    df_parenting = pd.DataFrame(parenting_models)
    
    # Model comparison visualization
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('PT SI Fit Score', 'Implementation Complexity'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    fig.add_trace(
        go.Bar(
            x=df_parenting['Model'],
            y=df_parenting['PT SI Fit Score'],
            name='Fit Score',
            marker_color='lightblue'
        ),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Bar(
            x=df_parenting['Model'],
            y=df_parenting['Implementation Complexity'],
            name='Complexity',
            marker_color='lightcoral'
        ),
        row=1, col=2
    )
    
    fig.update_layout(height=400, showlegend=True)
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed model analysis
    tab1, tab2, tab3, tab4 = st.tabs(["Financial Control", "Strategic Control ⭐", "Strategic Planning", "Financial Engineering"])
    
    with tab1:
        st.markdown("""
        <div class="parenting-model">
            <h4>💰 Financial Control Model</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <div>
                    <h5>Karakteristik:</h5>
                    <ul>
                        <li>Focus pada financial performance</li>
                        <li>Limited strategic intervention</li>
                        <li>Decentralized decision making</li>
                        <li>Short-term performance orientation</li>
                    </ul>
                </div>
                <div>
                    <h5>Cocok untuk:</h5>
                    <ul>
                        <li>Portfolio dengan bisnis yang tidak saling terkait</li>
                        <li>Mature businesses</li>
                        <li>Cash generation focus</li>
                    </ul>
                    <h5>Contoh:</h5>
                    <p>Berkshire Hathaway, Jardine Matheson</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="success-box">
            <h4>🎯 Strategic Control Model ⭐ (RECOMMENDED)</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <div>
                    <h5>✅ Mengapa Optimal untuk PT SI:</h5>
                    <ul>
                        <li><strong>Related diversification:</strong> Testing, inspection, certification services</li>
                        <li><strong>Balance control:</strong> Financial oversight + strategic guidance</li>
                        <li><strong>Synergy potential:</strong> Resource sharing, cross-selling</li>
                        <li><strong>Scalability:</strong> Mendukung ekspansi terintegrasi</li>
                    </ul>
                </div>
                <div>
                    <h5>📋 Key Implementation Elements:</h5>
                    <ul>
                        <li>Authority matrix dengan clear boundaries</li>
                        <li>Performance dashboard terintegrasi</li>
                        <li>Strategic planning konsolidasi</li>
                        <li>Regular governance review</li>
                    </ul>
                    <h5>Contoh BUMN:</h5>
                    <p>Pertamina (post-transformasi), Samsung Group</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="parenting-model">
            <h4>📊 Strategic Planning Model</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <div>
                    <h5>Karakteristik:</h5>
                    <ul>
                        <li>Centralized strategic planning</li>
                        <li>Detailed performance monitoring</li>
                        <li>Extensive coordination mechanisms</li>
                        <li>High integration level</li>
                    </ul>
                </div>
                <div>
                    <h5>Cocok untuk:</h5>
                    <ul>
                        <li>Integrated business portfolio</li>
                        <li>High synergy potential</li>
                        <li>Complex coordination needs</li>
                    </ul>
                    <h5>Contoh:</h5>
                    <p>McKinsey portfolio approach</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("""
        <div class="parenting-model">
            <h4>🔧 Financial Engineering Model</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <div>
                    <h5>Karakteristik:</h5>
                    <ul>
                        <li>Focus pada financial restructuring</li>
                        <li>Short to medium-term value creation</li>
                        <li>Active portfolio management</li>
                        <li>Deal-driven approach</li>
                    </ul>
                </div>
                <div>
                    <h5>Cocok untuk:</h5>
                    <ul>
                        <li>Turnaround situations</li>
                        <li>Distressed assets</li>
                        <li>Quick value realization</li>
                    </ul>
                    <h5>Contoh:</h5>
                    <p>Private equity firms</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Parent-Subsidiary Roles & Responsibilities
    st.markdown("### 👥 Peran dan Tanggung Jawab")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-box">
            <h4>🏢 Peran Perusahaan Induk</h4>
            <h5>Sebagai Pemegang Saham Pengendali:</h5>
            <ul>
                <li><strong>Strategic Direction:</strong> Menetapkan visi, misi, dan strategi korporat</li>
                <li><strong>Capital Allocation:</strong> Optimasi alokasi sumber daya dan investasi</li>
                <li><strong>Performance Oversight:</strong> Monitoring dan evaluasi kinerja anak perusahaan</li>
                <li><strong>Risk Management:</strong> Penetapan risk appetite dan framework</li>
                <li><strong>Compliance Assurance:</strong> Memastikan kepatuhan regulasi</li>
            </ul>
            
            <h5>Sebagai Corporate Parent:</h5>
            <ul>
                <li><strong>Value Creation:</strong> Menciptakan sinergi dan value-added activities</li>
                <li><strong>Capability Building:</strong> Pengembangan kapabilitas dan competency</li>
                <li><strong>Knowledge Management:</strong> Transfer knowledge dan best practices</li>
                <li><strong>Resource Sharing:</strong> Optimasi penggunaan sumber daya bersama</li>
                <li><strong>Brand Management:</strong> Pengelolaan reputasi dan brand portfolio</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
            <h4>🏭 Tanggung Jawab Anak Perusahaan</h4>
            <h5>Operational Excellence:</h5>
            <ul>
                <li>Mencapai target kinerja yang ditetapkan</li>
                <li>Menjalankan operasional sesuai standar korporat</li>
                <li>Melaporkan kinerja secara transparan dan akurat</li>
            </ul>
            
            <h5>Compliance & Governance:</h5>
            <ul>
                <li>Mematuhi kebijakan dan prosedur induk perusahaan</li>
                <li>Menerapkan sistem governance yang efektif</li>
                <li>Melaksanakan manajemen risiko sesuai framework korporat</li>
            </ul>
            
            <h5>Strategic Alignment:</h5>
            <ul>
                <li>Menyelaraskan strategi dengan arah korporat</li>
                <li>Berkontribusi pada pencapaian target konsolidasi</li>
                <li>Berpartisipasi aktif dalam inisiatif sinergi</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Strategic Direction Framework untuk PT SI
    st.markdown("### 🎯 Strategic Direction Framework untuk PT Surveyor Indonesia")
    
    strategic_directions = {
        'Core Business Strengthening': [
            'Surveying dan inspection services excellence',
            'Digital transformation acceleration',
            'Market expansion strategies',
            'Service portfolio optimization'
        ],
        'Adjacent Business Development': [
            'Related service offerings',
            'Geographic expansion',
            'Strategic partnerships',
            'Technology-enabled services'
        ],
        'New Growth Opportunities': [
            'Digital services platform',
            'Data analytics dan consulting',
            'Environmental dan sustainability services',
            'International market penetration'
        ]
    }
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h4>🎯 Core Business Strengthening</h4>
            <ul>
        """ + "".join([f"<li>{item}</li>" for item in strategic_directions['Core Business Strengthening']]) + """
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <h4>🔄 Adjacent Business Development</h4>
            <ul>
        """ + "".join([f"<li>{item}</li>" for item in strategic_directions['Adjacent Business Development']]) + """
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="warning-box">
            <h4>🚀 New Growth Opportunities</h4>
            <ul>
        """ + "".join([f"<li>{item}</li>" for item in strategic_directions['New Growth Opportunities']]) + """
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Enhanced Benchmarking Page
elif page == "benchmarking":
    st.markdown('<div class="sub-header">📊 Comprehensive Benchmarking Analysis</div>', unsafe_allow_html=True)
    
    # BUMN Benchmarking with enhanced cards
    st.markdown("### 🏆 BUMN Excellence Benchmark")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="benchmark-card">
            <h3>🛢️ PT Pertamina (Persero)</h3>
            <p><strong>Model:</strong> Strategic Control Holding Company</p>
            <p><strong>Transformasi:</strong> 127 → 12 anak perusahaan (2021)</p>
            <p><strong>Performance 2024:</strong></p>
            <ul>
                <li>Net Profit: US$3.13B ≈ Rp 49.5 T</li>
                <li>Revenue: ≈ Rp 1,250 T (est.)</li>
                <li>Kontribusi Negara: Rp 401.7 T</li>
            </ul>
            <p><strong>Best Practice:</strong></p>
            <ul>
                <li>Portfolio management terintegrasi</li>
                <li>Subholding structure optimal</li>
                <li>Compliance EITI</li>
                <li>Cost optimization US$1.38B (2024)</li>
            </ul>
            <p><strong>Governance Score:</strong> <span style="font-size: 1.5em;">85/100</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="benchmark-card">
            <h3>📡 PT Telkom Indonesia</h3>
            <p><strong>Model:</strong> Strategic Integration Holding</p>
            <p><strong>Struktur:</strong> 12 anak perusahaan utama</p>
            <p><strong>Performance 2024:</strong></p>
            <ul>
                <li>Revenue: Rp 150.6 T (est. annual)</li>
                <li>H1 2024: Rp 75.3 T (+2.5% YoY)</li>
                <li>Net Profit: ≈ Rp 30.2 T (est.)</li>
            </ul>
            <p><strong>Best Practice:</strong></p>
            <ul>
                <li>Revenue consolidation strategy</li>
                <li>Digital transformation governance</li>
                <li>TelkomMetra sebagai strategic control</li>
                <li>InfraCo initiative</li>
            </ul>
            <p><strong>Governance Score:</strong> <span style="font-size: 1.5em;">82/100</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="benchmark-card">
            <h3>🏦 PT Bank Mandiri</h3>
            <p><strong>Model:</strong> Financial Holdings dengan Cross-selling</p>
            <p><strong>Struktur:</strong> 11 anak perusahaan finansial</p>
            <p><strong>Performance 2024:</strong></p>
            <ul>
                <li>Revenue: Rp 146.6 T (+5.73% YoY)</li>
                <li>Net Profit: Rp 55.8 T (+1.3% YoY)</li>
                <li>Total Assets: Rp 2,430 T (+11.6% YoY)</li>
            </ul>
            <p><strong>Best Practice:</strong></p>
            <ul>
                <li>Cross-selling optimization</li>
                <li>Subsidiary synergy</li>
                <li>Sustainable finance framework</li>
                <li>Digital strategy (Livin Merchant)</li>
            </ul>
            <p><strong>Governance Score:</strong> <span style="font-size: 1.5em;">88/100</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Enhanced comparison analysis
    st.markdown("### 📈 Multi-Dimensional Benchmark Analysis")
    
    benchmark_data = get_benchmark_data()
    df_benchmark = pd.DataFrame(benchmark_data)
    
    fig = go.Figure()
    
    categories = ['Governance Score', 'Digital Integration', 'Synergy Optimization', 'Risk Management']
    
    for i, bumn in enumerate(df_benchmark['BUMN']):
        values = [df_benchmark.iloc[i][cat] for cat in categories]
        values.append(values[0])
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories + [categories[0]],
            fill='toself',
            name=bumn,
            line=dict(width=3)
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title="Governance Excellence Radar Analysis",
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

# GCG Framework Page
elif page == "framework":
    st.markdown('<div class="sub-header">📋 Good Corporate Governance (GCG) & GRC Framework</div>', unsafe_allow_html=True)
    
    # GCG Principles
    st.markdown("### 🎯 Good Corporate Governance (GCG) Framework")
    
    gcg_principles = {
        'Prinsip': ['Transparency', 'Accountability', 'Responsibility', 'Independence', 'Fairness'],
        'Definisi': [
            'Financial reporting akurat, disclosure material',
            'Clear roles, performance measurement objektif', 
            'Compliance regulasi, stakeholder engagement',
            'Oversight independen, conflict management',
            'Equal treatment, minority protection'
        ],
        'Current Score': [82, 78, 85, 72, 80],
        'Target Score': [90, 88, 92, 85, 88],
        'Gap': [8, 10, 7, 13, 8],
        'Priority': ['High', 'High', 'Medium', 'Critical', 'High']
    }
    
    # GCG Interactive Assessment
    col1, col2 = st.columns([2, 1])
    
    with col1:
        df_gcg = pd.DataFrame(gcg_principles)
        
        fig = px.bar(
            df_gcg, 
            x='Prinsip', 
            y=['Current Score', 'Target Score'],
            title="GCG Principles Assessment - PT Surveyor Indonesia",
            barmode='group',
            color_discrete_sequence=['#e53e3e', '#38a169']
        )
        
        fig.add_scatter(
            x=df_gcg['Prinsip'], 
            y=df_gcg['Gap'],
            mode='markers+text',
            text=df_gcg['Gap'],
            textposition="top center",
            name='Gap',
            marker=dict(size=15, color='red'),
            yaxis='y2'
        )
        
        fig.update_layout(
            height=400,
            yaxis2=dict(overlaying='y', side='right', title='Gap Points'),
            margin=dict(l=20, r=20, t=60, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 Priority Actions")
        for i, row in df_gcg.iterrows():
            priority_colors = {"Critical": "🔴", "High": "🟠", "Medium": "🟡", "Low": "🟢"}
            priority_color = priority_colors.get(row['Priority'], "⚪")
            
            st.markdown(f"""
            <div class="metric-container">
                <strong>{row['Prinsip']}</strong><br>
                Gap: {row['Gap']} points {priority_color}<br>
                <small>Priority: {row['Priority']}</small><br>
                <small style="color: #666;">{row['Definisi']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    # GRC Integration
    st.markdown("### 🔗 Governance, Risk, and Compliance (GRC) Integration")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-box">
            <h4>🏛️ Governance Layer</h4>
            <ul>
                <li><strong>Board effectiveness dan oversight</strong></li>
                <li>Management accountability</li>
                <li>Strategic decision making process</li>
                <li>Stakeholder governance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
            <h4>⚠️ Risk Management Layer</h4>
            <ul>
                <li><strong>Enterprise risk management framework</strong></li>
                <li>Risk appetite dan tolerance setting</li>
                <li>Risk monitoring dan reporting</li>
                <li>Crisis management protocols</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="success-box">
            <h4>✅ Compliance Layer</h4>
            <ul>
                <li><strong>Regulatory compliance management</strong></li>
                <li>Internal control systems</li>
                <li>Audit dan assurance functions</li>
                <li>Ethics dan conduct standards</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Authority Matrix
    st.markdown("### 📊 Authority Matrix & Decision Rights")
    
    authority_data = {
        'Decision Type': [
            'Strategic Planning', 'Budget Approval', 'Investment >5M',
            'Key Personnel', 'Policy Changes', 'Risk Management',
            'Operational Decisions', 'Performance Review'
        ],
        'Board': ['Approve', 'Approve', 'Approve', 'Approve', 'Approve', 'Oversight', 'Oversight', 'Review'],
        'CEO': ['Recommend', 'Recommend', 'Recommend', 'Recommend', 'Develop', 'Manage', 'Decide', 'Conduct'],
        'Subsidiary CEO': ['Input', 'Propose', 'Propose', 'Recommend', 'Implement', 'Execute', 'Execute', 'Report'],
        'Subsidiary Board': ['Review', 'Review', 'Review', 'Approve', 'Review', 'Monitor', 'Oversight', 'Approve']
    }
    
    df_authority = pd.DataFrame(authority_data)
    st.dataframe(df_authority, use_container_width=True, hide_index=True)

# Timeline Page (keeping the existing enhanced timeline from previous version)
elif page == "timeline":
    st.markdown('<div class="sub-header">⏱️ Rencana Kerja 60 Hari - Agustus 2025</div>', unsafe_allow_html=True)
    
    # Timeline content here (keeping the existing comprehensive timeline)
    timeline_data = get_timeline_data()
    df_timeline = pd.DataFrame(timeline_data)
    
    fig = px.timeline(
        df_timeline,
        x_start="Start Date",
        x_end="End Date", 
        y="Phase",
        color="Progress",
        title="Project Timeline - 60 Days (Agustus - Oktober 2025)",
        color_continuous_scale="viridis",
        hover_data=["Key Deliverable", "Status"]
    )
    
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=60, b=20))
    st.plotly_chart(fig, use_container_width=True)

# Keep other pages (monitoring, documentation, nextsteps) similar to original
elif page == "monitoring":
    st.markdown('<div class="sub-header">📈 Real-time Monitoring Dashboard</div>', unsafe_allow_html=True)
    st.info("Monitoring dashboard content here...")

elif page == "documentation":
    st.markdown('<div class="sub-header">📁 Comprehensive Documentation Center</div>', unsafe_allow_html=True)
    st.info("Documentation center content here...")

elif page == "nextsteps":
    st.markdown('<div class="sub-header">🎯 Expected Outcomes & Strategic Action Plan</div>', unsafe_allow_html=True)
    st.info("Next steps and action plan content here...")

# Enhanced Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #666; padding: 2rem; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 10px; margin-top: 2rem;">
    <h3 style="color: #1f4e79; margin-bottom: 1rem;">🏢 Pemutakhiran Pedoman Tata Kelola Terintegrasi</h3>
    <h4 style="color: #2c5282;">PT Surveyor Indonesia</h4>
    <p style="font-size: 1.1rem; margin: 1rem 0;"><strong>Agustus 2025 - Timeline Intensif 60 Hari Kerja</strong></p>
    <p style="font-style: italic; color: #4a5568;">Excellence in Corporate Governance & Strategic Control Model</p>
    
    <div style="margin-top: 1rem;">
        <p style="font-size: 0.9rem; color: #1f4e79;"><strong>Dashboard Version 3.0 - Agustus 2025</strong></p>
        <p style="font-size: 0.9rem;">Last Updated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
        <p style="font-size: 0.9rem;">🚀 Powered by Streamlit | 📊 Real-time Analytics | 🎯 Strategic Excellence</p>
    </div>
</div>
""", unsafe_allow_html=True)
