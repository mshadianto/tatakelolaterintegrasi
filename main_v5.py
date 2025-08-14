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
    st.session_state.overall_progress = 15  # Illustrative progress for project planning

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

# Add important disclaimer at the top
st.markdown("""
<div style="background: #fff3cd; border: 2px solid #ffc107; border-radius: 10px; padding: 1rem; margin: 1rem 0;">
    <h4 style="color: #856404; margin: 0;">⚠️ FRAMEWORK DISCLAIMER</h4>
    <p style="color: #856404; margin: 0.5rem 0; font-size: 0.9rem;">
        <strong>Dashboard ini menyajikan framework governance dan metodologi konseptual.</strong><br>
        Data numerik bersifat ilustratif untuk keperluan perencanaan dan benchmarking framework, bukan data finansial aktual.
        Materi untuk penggunaan internal PT Surveyor Indonesia dalam konteks pengembangan governance framework.
    </p>
</div>
""", unsafe_allow_html=True)

# Helper functions
@st.cache_data
def get_benchmark_data():
    # Note: Data illustrative untuk framework comparison - bukan data aktual
    return {
        'BUMN': ['Pertamina*', 'Telkom', 'Bank Mandiri', 'Surveyor Indonesia (Target)'],
        'Governance Score': ['Excellent', 'Good', 'Excellent', 'Target: Excellent'],
        'Digital Integration': ['Developing', 'Advanced', 'Developing', 'Target: Advanced'],
        'Synergy Optimization': ['Good', 'Developing', 'Excellent', 'Target: Excellent'],
        'Risk Management': ['Excellent', 'Good', 'Good', 'Target: Excellent'],
        'Subsidiaries': [12, 12, 11, 8],  # Data struktur organisasi yang dapat diverifikasi
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
    # Note: Illustrative target metrics for framework implementation
    return {
        'KPI': ['Stakeholder Satisfaction', 'Timeline Adherence', 'Quality Score', 'Budget Adherence'],
        'Current': [82, 88, 85, 96],  # Illustrative baseline for project planning
        'Target': [85, 90, 90, 95],   # Best practice targets for governance projects
        'Trend': [3, 2, 4, 1]         # Illustrative improvement trajectory
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
                   [{"type": "indicator"}, {"type": "indicator"}]],
            vertical_spacing=0.25,
            horizontal_spacing=0.1
        )
        
        # Overall Progress
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=st.session_state.overall_progress,
                title={'text': "Overall Progress", 'font': {'size': 16}},
                number={'suffix': "%", 'font': {'size': 20}},
                gauge={
                    'axis': {'range': [None, 100], 'tickwidth': 1},
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
                title={'text': "Current Phase", 'font': {'size': 16}},
                number={'suffix': "%", 'font': {'size': 20}},
                gauge={
                    'axis': {'range': [None, 100], 'tickwidth': 1},
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
                title={'text': "Quality Score", 'font': {'size': 16}},
                number={'suffix': "%", 'font': {'size': 20}},
                gauge={
                    'axis': {'range': [None, 100], 'tickwidth': 1},
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
                title={'text': "Resource Utilization", 'font': {'size': 16}},
                number={'suffix': "%", 'font': {'size': 20}},
                gauge={
                    'axis': {'range': [None, 100], 'tickwidth': 1},
                    'bar': {'color': "#e53e3e"},
                    'steps': [{'range': [0, 100], 'color': "#fff5f5"}],
                }
            ),
            row=2, col=2
        )
        
        fig.update_layout(
            height=500, 
            margin=dict(l=30, r=30, t=80, b=30),
            font=dict(size=12),
            showlegend=False
        )
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
        
        # Create KPI metrics with proper spacing
        kpi_container = st.container()
        with kpi_container:
            for i, kpi in enumerate(kpi_data['KPI']):
                current = kpi_data['Current'][i]
                target = kpi_data['Target'][i]
                trend = kpi_data['Trend'][i]
                
                # Create individual metric container
                st.markdown(f"""
                <div class="metric-container" style="margin-bottom: 0.8rem;">
                    <h5 style="margin: 0; color: #1f4e79;">{kpi}</h5>
                    <h2 style="margin: 0.2rem 0; color: #2d3748;">{current}%</h2>
                    <p style="margin: 0; color: {'#38a169' if trend >= 0 else '#e53e3e'};">
                        {'↗️' if trend >= 0 else '↘️'} {trend:+d}% trend
                    </p>
                    <div style="background: #e2e8f0; border-radius: 4px; height: 4px; margin-top: 0.5rem;">
                        <div style="background: #3182ce; height: 4px; border-radius: 4px; width: {min(current/target*100, 100)}%;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

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
        'PT SI Framework Fit': [60, 90, 75, 40],  # Theoretical fit assessment based on business model analysis
        'Implementation Complexity': [25, 60, 85, 45]  # Relative complexity assessment based on management literature
    }
    
    df_parenting = pd.DataFrame(parenting_models)
    
    # Model comparison visualization
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Framework Fit Assessment', 'Implementation Complexity'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    fig.add_trace(
        go.Bar(
            x=df_parenting['Model'],
            y=df_parenting['PT SI Framework Fit'],
            name='Framework Fit',
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
    
    fig.update_layout(height=400, showlegend=True, title="Corporate Parenting Model Assessment (Theoretical Framework Analysis)")
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
        st.markdown("#### 🏢 Peran Perusahaan Induk")
        
        st.markdown("**Sebagai Pemegang Saham Pengendali:**")
        st.markdown("""
        • **Strategic Direction:** Menetapkan visi, misi, dan strategi korporat  
        • **Capital Allocation:** Optimasi alokasi sumber daya dan investasi  
        • **Performance Oversight:** Monitoring dan evaluasi kinerja anak perusahaan  
        • **Risk Management:** Penetapan risk appetite dan framework  
        • **Compliance Assurance:** Memastikan kepatuhan regulasi
        """)
        
        st.markdown("**Sebagai Corporate Parent:**")
        st.markdown("""
        • **Value Creation:** Menciptakan sinergi dan value-added activities  
        • **Capability Building:** Pengembangan kapabilitas dan competency  
        • **Knowledge Management:** Transfer knowledge dan best practices  
        • **Resource Sharing:** Optimasi penggunaan sumber daya bersama  
        • **Brand Management:** Pengelolaan reputasi dan brand portfolio
        """)
    
    with col2:
        st.markdown("#### 🏭 Tanggung Jawab Anak Perusahaan")
        
        st.markdown("**Operational Excellence:**")
        st.markdown("""
        • Mencapai target kinerja yang ditetapkan  
        • Menjalankan operasional sesuai standar korporat  
        • Melaporkan kinerja secara transparan dan akurat
        """)
        
        st.markdown("**Compliance & Governance:**")
        st.markdown("""
        • Mematuhi kebijakan dan prosedur induk perusahaan  
        • Menerapkan sistem governance yang efektif  
        • Melaksanakan manajemen risiko sesuai framework korporat
        """)
        
        st.markdown("**Strategic Alignment:**")
        st.markdown("""
        • Menyelaraskan strategi dengan arah korporat  
        • Berkontribusi pada pencapaian target konsolidasi  
        • Berpartisipasi aktif dalam inisiatif sinergi
        """)
    
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
        st.markdown("#### 🎯 Core Business Strengthening")
        for item in strategic_directions['Core Business Strengthening']:
            st.markdown(f"• {item}")
    
    with col2:
        st.markdown("#### 🔄 Adjacent Business Development")
        for item in strategic_directions['Adjacent Business Development']:
            st.markdown(f"• {item}")
    
    with col3:
        st.markdown("#### 🚀 New Growth Opportunities")
        for item in strategic_directions['New Growth Opportunities']:
            st.markdown(f"• {item}")

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
            <p><strong>Transformasi Struktur:</strong> Konsolidasi anak perusahaan (2021)</p>
            <p><strong>Struktur Organisasi:</strong></p>
            <ul>
                <li>Holding company dengan subholding structure</li>
                <li>Portfolio management terintegrasi</li>
                <li>Strategic control implementation</li>
            </ul>
            <p><strong>Best Practice Focus:</strong></p>
            <ul>
                <li>Portfolio optimization strategy</li>
                <li>Integrated governance framework</li>
                <li>Regulatory compliance excellence</li>
                <li>Operational efficiency improvement</li>
            </ul>
            <p><strong>Governance Maturity:</strong> <span style="font-size: 1.5em;">Excellent</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="benchmark-card">
            <h3>📡 PT Telkom Indonesia</h3>
            <p><strong>Model:</strong> Strategic Integration Holding</p>
            <p><strong>Struktur:</strong> Multiple subsidiary management</p>
            <p><strong>Organizational Structure:</strong></p>
            <ul>
                <li>Integrated telecommunications ecosystem</li>
                <li>Digital transformation focus</li>
                <li>Infrastructure optimization</li>
            </ul>
            <p><strong>Best Practice Focus:</strong></p>
            <ul>
                <li>Digital governance integration</li>
                <li>Technology-enabled operations</li>
                <li>Strategic business unit coordination</li>
                <li>Innovation management framework</li>
            </ul>
            <p><strong>Governance Maturity:</strong> <span style="font-size: 1.5em;">Good</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="benchmark-card">
            <h3>🏦 PT Bank Mandiri</h3>
            <p><strong>Model:</strong> Financial Holdings dengan Cross-selling</p>
            <p><strong>Struktur:</strong> Integrated financial services</p>
            <p><strong>Organizational Structure:</strong></p>
            <ul>
                <li>Financial services ecosystem</li>
                <li>Subsidiary synergy optimization</li>
                <li>Cross-selling integration</li>
            </ul>
            <p><strong>Best Practice Focus:</strong></p>
            <ul>
                <li>Financial services integration</li>
                <li>Customer ecosystem development</li>
                <li>Digital banking transformation</li>
                <li>Sustainable finance framework</li>
            </ul>
            <p><strong>Governance Maturity:</strong> <span style="font-size: 1.5em;">Excellent</span></p>
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
        'Baseline Assessment': [82, 78, 85, 72, 80],  # Illustrative baseline for framework development
        'Target Framework': [90, 88, 92, 85, 88],     # Best practice targets based on governance standards
        'Development Gap': [8, 10, 7, 13, 8],         # Framework improvement areas
        'Priority': ['High', 'High', 'Medium', 'Critical', 'High']
    }
    
    # GCG Interactive Assessment
    col1, col2 = st.columns([2, 1])
    
    with col1:
        df_gcg = pd.DataFrame(gcg_principles)
        
        fig = px.bar(
            df_gcg, 
            x='Prinsip', 
            y=['Baseline Assessment', 'Target Framework'],
            title="GCG Framework Development Assessment - PT Surveyor Indonesia (Illustrative)",
            barmode='group',
            color_discrete_sequence=['#e53e3e', '#38a169']
        )
        
        fig.add_scatter(
            x=df_gcg['Prinsip'], 
            y=df_gcg['Development Gap'],
            mode='markers+text',
            text=df_gcg['Development Gap'],
            textposition="top center",
            name='Development Gap',
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
                Development Gap: {row['Development Gap']} points {priority_color}<br>
                <small>Priority: {row['Priority']}</small><br>
                <small style="color: #666;">{row['Definisi']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    # GRC Integration
    st.markdown("### 🔗 Governance, Risk, and Compliance (GRC) Integration")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🏛️ Governance Layer")
        st.markdown("""
        • **Board effectiveness dan oversight**  
        • Management accountability  
        • Strategic decision making process  
        • Stakeholder governance
        """)
    
    with col2:
        st.markdown("#### ⚠️ Risk Management Layer")
        st.markdown("""
        • **Enterprise risk management framework**  
        • Risk appetite dan tolerance setting  
        • Risk monitoring dan reporting  
        • Crisis management protocols
        """)
    
    with col3:
        st.markdown("#### ✅ Compliance Layer")
        st.markdown("""
        • **Regulatory compliance management**  
        • Internal control systems  
        • Audit dan assurance functions  
        • Ethics dan conduct standards
        """)
    
    # Authority Matrix
    st.markdown("### 📊 Authority Matrix & Decision Rights")
    
    # Indonesian Corporate Governance Structure
    authority_data = {
        'Decision Type': [
            'Strategic Planning', 'Budget Approval', 'Investment >50M', 'Investment 10M-50M', 'Investment <10M',
            'Key Personnel Appointment', 'CEO/Direktur Utama Appointment', 'Policy Changes (Major)',
            'Policy Changes (Operational)', 'Risk Management Framework', 'Operational Decisions',
            'Performance Review', 'Dividend Distribution', 'Capital Structure Changes',
            'Merger & Acquisition', 'Related Party Transactions', 'Compliance Monitoring'
        ],
        'RUPS Induk': [
            'Approve', 'Approve', 'Approve', 'Informed', 'Informed',
            'Approve', 'Approve', 'Approve', 'Informed', 'Approve',
            'Informed', 'Review', 'Approve', 'Approve',
            'Approve', 'Approve', 'Review'
        ],
        'Dewan Komisaris Induk': [
            'Review', 'Review', 'Review', 'Approve', 'Oversight',
            'Recommend', 'Recommend', 'Review', 'Oversight', 'Oversight',
            'Oversight', 'Conduct', 'Recommend', 'Review',
            'Review', 'Review', 'Monitor'
        ],
        'Direksi Induk': [
            'Develop', 'Develop', 'Recommend', 'Recommend', 'Approve',
            'Recommend', 'Propose', 'Develop', 'Approve', 'Develop',
            'Decide', 'Report', 'Propose', 'Propose',
            'Execute', 'Execute', 'Implement'
        ],
        'RUPS Anak': [
            'Informed', 'Informed', 'Informed', 'Approve', 'Informed',
            'Approve', 'Approve', 'Informed', 'Informed', 'Informed',
            'Informed', 'Informed', 'Approve', 'Approve',
            'Approve', 'Approve', 'Informed'
        ],
        'Dewan Komisaris Anak': [
            'Review', 'Review', 'Review', 'Review', 'Oversight',
            'Recommend', 'Recommend', 'Review', 'Oversight', 'Monitor',
            'Oversight', 'Conduct', 'Recommend', 'Review',
            'Review', 'Review', 'Monitor'
        ],
        'Direksi Anak': [
            'Input', 'Propose', 'Propose', 'Propose', 'Decide',
            'Propose', 'Propose', 'Implement', 'Implement', 'Execute',
            'Execute', 'Report', 'Propose', 'Propose',
            'Execute', 'Execute', 'Execute'
        ]
    }
    
    df_authority = pd.DataFrame(authority_data)
    
    # Display the authority matrix with enhanced formatting
    st.markdown("#### 🏛️ Struktur Kewenangan Indonesian Corporate Governance")
    
    # Create styled dataframe
    def highlight_authority(val):
        color_map = {
            'Approve': 'background-color: #d4edda; font-weight: bold',
            'Decide': 'background-color: #d4edda; font-weight: bold', 
            'Recommend': 'background-color: #fff3cd',
            'Develop': 'background-color: #fff3cd',
            'Propose': 'background-color: #feebc8',
            'Input': 'background-color: #fed7d7',
            'Review': 'background-color: #e2e8f0',
            'Oversight': 'background-color: #e2e8f0',
            'Monitor': 'background-color: #e2e8f0',
            'Conduct': 'background-color: #d1ecf1',
            'Execute': 'background-color: #d1ecf1',
            'Implement': 'background-color: #d1ecf1',
            'Report': 'background-color: #f0f8ff',
            'Informed': 'background-color: #f8f9fa'
        }
        return color_map.get(val, '')
    
    styled_df = df_authority.style.applymap(highlight_authority, subset=[
        'RUPS Induk', 'Dewan Komisaris Induk', 'Direksi Induk', 
        'RUPS Anak', 'Dewan Komisaris Anak', 'Direksi Anak'
    ])
    
    st.dataframe(styled_df, use_container_width=True, hide_index=True)
    
    # Legend for Authority Matrix
    st.markdown("#### 🎨 Legend - Authority Matrix")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Decision Authority:**
        - 🟢 **Approve/Decide:** Final decision authority
        - 🟡 **Recommend/Develop:** Proposal and recommendation
        - 🟠 **Propose:** Initiative and suggestion
        """)
    
    with col2:
        st.markdown("""
        **Oversight & Monitoring:**
        - 🔵 **Review/Oversight:** Supervisory function
        - 🔵 **Monitor:** Ongoing supervision
        - 💙 **Conduct:** Active evaluation
        """)
    
    with col3:
        st.markdown("""
        **Implementation & Reporting:**
        - 🔷 **Execute/Implement:** Operational execution
        - 💫 **Report:** Information provision
        - 📋 **Input/Informed:** Consultation/notification
        """)
    
    # Key Principles
    st.markdown("#### 📋 Key Principles of Authority Matrix")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🏛️ Parent Company (Induk):**")
        st.markdown("""
        • **RUPS Induk:** Ultimate authority untuk strategic decisions dan struktur modal  
        • **Dewan Komisaris Induk:** Oversight dan supervisory functions  
        • **Direksi Induk:** Strategic development dan corporate management  
        • **Delegation Principle:** Clear authority delegation dengan accountability
        """)
    
    with col2:
        st.markdown("**🏭 Subsidiary Company (Anak):**")
        st.markdown("""
        • **RUPS Anak:** Authority dalam batas yang ditetapkan induk perusahaan  
        • **Dewan Komisaris Anak:** Local oversight sesuai governance framework  
        • **Direksi Anak:** Operational execution dan local management  
        • **Coordination Principle:** Alignment dengan strategic direction induk
        """)
    
    # Decision Flow Framework
    st.markdown("#### 🔄 Decision Flow Framework")
    
    decision_flow = {
        'Investment Decisions': {
            '>50M': 'RUPS Induk → Dewan Komisaris Induk → Direksi Induk → Implementation',
            '10M-50M': 'Dewan Komisaris Induk → Direksi Induk → RUPS Anak → Implementation', 
            '<10M': 'Direksi Induk → Direksi Anak → Implementation'
        },
        'Personnel Decisions': {
            'CEO/Direktur Utama': 'RUPS → Dewan Komisaris → Final Decision',
            'Key Personnel': 'Dewan Komisaris → Direksi → Implementation',
            'Operational Staff': 'Direksi → Implementation'
        },
        'Policy Decisions': {
            'Major Policy': 'RUPS Induk → Dewan Komisaris → Development → Implementation',
            'Operational Policy': 'Direksi Induk → Direksi Anak → Implementation'
        }
    }
    
    for category, flows in decision_flow.items():
        with st.expander(f"🔍 {category} Decision Flow"):
            for decision_type, flow in flows.items():
                st.markdown(f"**{decision_type}:** {flow}")
    
    # Escalation Matrix
    st.markdown("#### ⬆️ Escalation Matrix")
    
    escalation_data = {
        'Scenario': [
            'Budget Overrun >10%', 'Strategic Deviation', 'Compliance Issue',
            'Risk Threshold Breach', 'Stakeholder Conflict', 'Performance Below Target'
        ],
        'First Level': [
            'Direksi Anak', 'Direksi Anak', 'Direksi Anak',
            'Direksi Anak', 'Dewan Komisaris Anak', 'Direksi Anak'
        ],
        'Second Level': [
            'Direksi Induk', 'Direksi Induk', 'Dewan Komisaris Anak',
            'Dewan Komisaris Induk', 'Dewan Komisaris Induk', 'Direksi Induk'
        ],
        'Final Authority': [
            'Dewan Komisaris Induk', 'Dewan Komisaris Induk', 'RUPS Induk',
            'RUPS Induk', 'RUPS Induk', 'Dewan Komisaris Induk'
        ]
    }
    
    df_escalation = pd.DataFrame(escalation_data)
    st.dataframe(df_escalation, use_container_width=True, hide_index=True)

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

# Keep other pages (monitoring, documentation, nextsteps) with proper implementation
elif page == "monitoring":
    st.markdown('<div class="sub-header">📈 Real-time Monitoring Dashboard</div>', unsafe_allow_html=True)
    
    # Real-time metrics
    col1, col2, col3, col4 = st.columns(4)
    
    kpi_data = get_kpi_data()
    
    for i, col in enumerate([col1, col2, col3, col4]):
        with col:
            current = kpi_data['Current'][i]
            target = kpi_data['Target'][i]
            trend = kpi_data['Trend'][i]
            
            st.markdown(f"""
            <div class="metric-container">
                <h5 style="margin: 0; color: #1f4e79;">{kpi_data['KPI'][i]}</h5>
                <h2 style="margin: 0.2rem 0; color: #2d3748;">{current}%</h2>
                <p style="margin: 0; color: {'#38a169' if trend >= 0 else '#e53e3e'};">
                    {'↗️' if trend >= 0 else '↘️'} {trend:+d}% trend
                </p>
                <div style="background: #e2e8f0; border-radius: 4px; height: 4px; margin-top: 0.5rem;">
                    <div style="background: #3182ce; height: 4px; border-radius: 4px; width: {min(current/target*100, 100)}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Performance Trends")
    
    # Generate realistic trend data
    dates = pd.date_range(start='2025-08-01', periods=14, freq='D')
    trend_data = {
        'Date': dates,
        'Overall Progress': np.linspace(10, 15, 14) + np.random.normal(0, 1, 14),
        'Quality Score': np.linspace(82, 85, 14) + np.random.normal(0, 0.5, 14),
        'Stakeholder Satisfaction': np.linspace(80, 82, 14) + np.random.normal(0, 0.8, 14)
    }
    
    df_trends = pd.DataFrame(trend_data)
    
    fig = px.line(
        df_trends, 
        x='Date', 
        y=['Overall Progress', 'Quality Score', 'Stakeholder Satisfaction'],
        title='Key Metrics Trend (August 2025)'
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == "documentation":
    st.markdown('<div class="sub-header">📁 Comprehensive Documentation Center</div>', unsafe_allow_html=True)
    
    # Document categories
    doc_categories = ['Assessment Reports', 'Framework Documents', 'Implementation Plans', 'Templates & Tools']
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        selected_category = st.selectbox("Select Document Category:", doc_categories)
        
        # Sample documents
        documents = {
            'Assessment Reports': [
                {'name': 'Current State Assessment', 'status': 'Completed', 'date': '2025-08-10'},
                {'name': 'Gap Analysis Report', 'status': 'In Progress', 'date': '2025-08-15'},
                {'name': 'Benchmarking Study', 'status': 'Draft', 'date': '2025-08-20'}
            ],
            'Framework Documents': [
                {'name': 'Governance Framework Design', 'status': 'Draft', 'date': '2025-08-25'},
                {'name': 'Authority Matrix', 'status': 'Review', 'date': '2025-08-22'},
                {'name': 'GCG Implementation Guide', 'status': 'Planned', 'date': '2025-08-30'}
            ],
            'Implementation Plans': [
                {'name': '60-Day Implementation Roadmap', 'status': 'Approved', 'date': '2025-08-01'},
                {'name': 'Change Management Plan', 'status': 'Draft', 'date': '2025-08-18'},
                {'name': 'Training & Communication Plan', 'status': 'In Progress', 'date': '2025-08-20'}
            ],
            'Templates & Tools': [
                {'name': 'Governance Scorecard Template', 'status': 'Available', 'date': '2025-08-05'},
                {'name': 'Risk Assessment Matrix', 'status': 'Available', 'date': '2025-08-05'},
                {'name': 'Performance Dashboard Template', 'status': 'Draft', 'date': '2025-08-12'}
            ]
        }
        
        for doc in documents.get(selected_category, []):
            status_color = {'Completed': '🟢', 'In Progress': '🟡', 'Draft': '🟠', 'Review': '🔵', 'Planned': '⚪', 'Available': '✅', 'Approved': '✅'}
            
            # Use expander for cleaner display
            with st.expander(f"{doc['name']} {status_color.get(doc['status'], '⚪')}"):
                st.markdown(f"**Status:** {doc['status']}")
                st.markdown(f"**Date:** {doc['date']}")
                st.button("📥 Download", key=f"download_{doc['name']}", help="Download document")
    
    with col2:
        st.markdown("### 📊 Document Statistics")
        
        total_docs = sum(len(docs) for docs in documents.values())
        completed_docs = sum(1 for docs in documents.values() for doc in docs if doc['status'] in ['Completed', 'Available', 'Approved'])
        
        st.metric("Total Documents", total_docs)
        st.metric("Completed", completed_docs)
        st.metric("Completion Rate", f"{completed_docs/total_docs*100:.0f}%")

elif page == "nextsteps":
    st.markdown('<div class="sub-header">🎯 Expected Outcomes & Strategic Action Plan</div>', unsafe_allow_html=True)
    
    # Timeline for next steps
    st.markdown("### 🚀 Immediate Next Steps (August 2025)")
    
    next_steps = [
        {'action': 'Finalize project charter and resource allocation', 'timeline': 'Week 1', 'owner': 'Project Manager', 'priority': 'Critical'},
        {'action': 'Complete stakeholder mapping and engagement', 'timeline': 'Week 1-2', 'owner': 'Governance Team', 'priority': 'High'},
        {'action': 'Conduct current state assessment', 'timeline': 'Week 2-3', 'owner': 'Assessment Team', 'priority': 'High'},
        {'action': 'Develop governance framework draft', 'timeline': 'Week 3-6', 'owner': 'Framework Team', 'priority': 'Critical'}
    ]
    
    for step in next_steps:
        priority_colors = {'Critical': '🔴', 'High': '🟠', 'Medium': '🟡'}
        
        # Use expander for cleaner display
        with st.expander(f"{priority_colors.get(step['priority'], '⚪')} {step['action']} - {step['priority']} Priority"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Timeline:** {step['timeline']}")
            with col2:
                st.markdown(f"**Owner:** {step['owner']}")
    
    # Success metrics
    st.markdown("### 📊 Success Metrics Framework")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🎯 Quality Metrics")
        st.markdown("""
        • Stakeholder satisfaction >85%  
        • Framework completeness >90%  
        • Expert validation approval  
        • Compliance verification 100%
        """)
    
    with col2:
        st.markdown("#### ⚡ Efficiency Metrics")
        st.markdown("""
        • On-time delivery of milestones  
        • Budget adherence ±5%  
        • Resource utilization >80%  
        • Risk mitigation effectiveness
        """)
    
    with col3:
        st.markdown("#### 📈 Effectiveness Metrics")
        st.markdown("""
        • Implementation readiness >85%  
        • Change management adoption  
        • Governance score improvement  
        • Long-term sustainability
        """)

# Enhanced Footer
st.markdown("---")

# Create clean footer without HTML rendering issues
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 10px; margin-top: 2rem;">
    <h3 style="color: #1f4e79; margin-bottom: 1rem;">🏢 Pemutakhiran Pedoman Tata Kelola Terintegrasi</h3>
    <h4 style="color: #2c5282;">PT Surveyor Indonesia</h4>
    <p style="font-size: 1.1rem; margin: 1rem 0;"><strong>Agustus 2025 - Timeline Intensif 60 Hari Kerja</strong></p>
    <p style="font-style: italic; color: #4a5568;">Excellence in Corporate Governance & Strategic Control Model</p>
</div>
""", unsafe_allow_html=True)

# Add footer information separately to avoid HTML rendering issues
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Dashboard Information:**")
    st.markdown("• Version 3.0 - Agustus 2025")
    st.markdown(f"• Last Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

with col2:
    st.markdown("**Created by:**")
    st.markdown("• MS Hadianto")
    st.markdown("• **KIM Consulting 2025**")
    st.markdown("• Strategic Excellence")

with col3:
    st.markdown("**Technology:**")
    st.markdown("• 🚀 Powered by Streamlit")
    st.markdown("• 📊 Real-time Analytics")
    st.markdown("• 🎯 Strategic Excellence")

# Add disclaimer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem; background: #fff3cd; border: 2px solid #ffc107; border-radius: 10px; margin: 1rem 0;">
    <h4 style="color: #856404; margin: 0;">⚠️ COMPREHENSIVE DISCLAIMER</h4>
    <p style="color: #856404; margin: 0.5rem 0; font-size: 0.9rem;">
        <strong>Materi sosialisasi ini untuk digunakan secara terbatas pada PT Surveyor Indonesia.</strong><br>
        Tidak untuk distribusi atau penggunaan eksternal tanpa izin tertulis.<br><br>
        <strong>Data & Metodologi:</strong> Dashboard ini menyajikan framework governance dan metodologi konseptual. 
        Semua data numerik bersifat ilustratif untuk keperluan pengembangan framework dan benchmarking metodologi, 
        bukan data finansial atau kinerja aktual. Penilaian dan skor berdasarkan analisis teoretis untuk keperluan perencanaan strategis.
    </p>
</div>
""", unsafe_allow_html=True)
