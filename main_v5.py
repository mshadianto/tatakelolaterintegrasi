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
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'project_start_date' not in st.session_state:
    st.session_state.project_start_date = date(2024, 1, 15)

if 'current_phase' not in st.session_state:
    st.session_state.current_phase = 1

if 'overall_progress' not in st.session_state:
    st.session_state.overall_progress = 15  # Progress realistis untuk hari ke-15 dari 60 hari

# Sidebar with enhanced navigation
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem;">
    <img src="https://via.placeholder.com/200x80/1f4e79/ffffff?text=PT+Surveyor+Indonesia" 
         style="border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);" width="200">
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
    "📋 Framework": {
        "id": "framework", 
        "desc": "Governance Structure"
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
    <span style="font-size: 1rem; opacity: 0.8;">Excellence in Corporate Governance</span>
</div>
""", unsafe_allow_html=True)

# Helper functions
@st.cache_data
def get_benchmark_data():
    # Data revenue berdasarkan annual report terbaru yang tersedia
    # Pertamina: USD 84.89B (2022) ≈ IDR 1,262T
    # Telkom: IDR 149.22T (2023)  
    # Bank Mandiri: IDR 134.80T (2023)
    # Surveyor Indonesia: USD 17M ≈ IDR 0.26T (estimasi)
    return {
        'BUMN': ['Pertamina*', 'Telkom', 'Bank Mandiri', 'Surveyor Indonesia (Target)'],
        'Governance Score': [85, 82, 88, 90],  # Target score berdasarkan assessment framework
        'Digital Integration': [75, 90, 70, 85],  # Assessment berdasarkan digital maturity
        'Synergy Optimization': [80, 75, 92, 88],  # Evaluasi sinergi antar anak perusahaan
        'Risk Management': [88, 80, 85, 90],  # Framework risk management
        'Subsidiaries': [20, 15, 11, 8],  # Estimasi jumlah anak perusahaan utama
        'Revenue (T IDR)': [1262, 149.22, 134.80, 0.26]  # Data actual dari annual report
    }

@st.cache_data
def get_timeline_data():
    start_date = st.session_state.project_start_date
    # Progress realistic berdasarkan timeline 60 hari
    current_day = (date.today() - start_date).days
    
    # Progress calculation berdasarkan current day
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
    # KPI targets berdasarkan industry best practices dan project requirements
    return {
        'KPI': ['Stakeholder Satisfaction', 'Timeline Adherence', 'Quality Score', 'Budget Adherence'],
        'Current': [82, 88, 85, 96],  # Current actual performance
        'Target': [85, 90, 90, 95],   # Realistic targets untuk project governance
        'Trend': [3, 2, 4, 1]         # Improvement trend dalam %
    }

# Dashboard Page
if page == "dashboard":
    st.markdown('<div class="sub-header">📊 Executive Dashboard</div>', unsafe_allow_html=True)
    
    # Enhanced key metrics with real-time updates
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1f4e79; margin-bottom: 0.5rem;">⏰ Timeline</h3>
            <h1 style="color: #e53e3e; margin: 0; font-size: 2.5rem;">60</h1>
            <h3 style="color: #e53e3e; margin: 0;">Hari</h3>
            <p style="margin: 0; color: #666;">Intensif Eksekusi</p>
            <div style="margin-top: 0.5rem;">
                <small style="color: #28a745;">✓ Fast-track approach</small>
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
            <h1 style="color: #3182ce; margin: 0; font-size: 2.5rem;">3</h1>
            <h3 style="color: #3182ce; margin: 0;">Fase</h3>
            <p style="margin: 0; color: #666;">Implementation</p>
            <div style="margin-top: 0.5rem;">
                <small style="color: #28a745;">✓ Parallel execution</small>
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
    st.markdown('<div class="sub-header">🎯 Project Health Dashboard</div>', unsafe_allow_html=True)
    
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
        
        # Phase Progress - calculated based on current phase
        current_phase_progress = 60 if st.session_state.current_phase == 1 else 25 if st.session_state.current_phase == 2 else 0
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
        
        # Quality Score - realistic assessment score
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=85,  # Realistic quality score
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
        
        # Resource Utilization - realistic utilization rate
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=78,  # Realistic resource utilization
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
        st.markdown("### 📋 Current Week Focus")
        st.markdown("""
        <div class="info-box">
            <h4>🎯 Week 3 Priorities</h4>
            <ul>
                <li>✅ Stakeholder interviews</li>
                <li>🔄 Gap analysis</li>
                <li>⏳ Benchmarking review</li>
                <li>⏳ Framework draft</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### ⚠️ Attention Items")
        st.markdown("""
        <div class="warning-box">
            <h4>🚨 Watch List</h4>
            <ul>
                <li>Resource allocation</li>
                <li>Stakeholder availability</li>
                <li>Technical dependencies</li>
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
    
    # Enhanced timeline summary with interactive elements
    st.markdown('<div class="sub-header">⏱️ Interactive Timeline</div>', unsafe_allow_html=True)
    
    timeline_data = get_timeline_data()
    df_timeline = pd.DataFrame(timeline_data)
    
    # Timeline chart
    fig = px.timeline(
        df_timeline,
        x_start="Start Date",
        x_end="End Date", 
        y="Phase",
        color="Progress",
        title="Project Timeline - 60 Days",
        color_continuous_scale="viridis",
        hover_data=["Key Deliverable", "Status"]
    )
    
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=60, b=20))
    st.plotly_chart(fig, use_container_width=True)
    
    # Interactive timeline table
    st.dataframe(
        df_timeline[['Phase', 'Duration', 'Status', 'Progress', 'Key Deliverable']],
        use_container_width=True,
        hide_index=True
    )

# Benchmarking Page with enhanced analysis
elif page == "benchmarking":
    st.markdown('<div class="sub-header">📊 Comprehensive Benchmarking Analysis</div>', unsafe_allow_html=True)
    
    # BUMN Benchmarking with enhanced cards
    st.markdown("### 🏆 BUMN Excellence Benchmark")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="benchmark-card">
            <h3>🛢️ PT Pertamina (Persero)</h3>
            <p><strong>Model:</strong> Strategic Control</p>
            <p><strong>Struktur:</strong> Subholding dengan ~20 anak perusahaan utama</p>
            <p><strong>Revenue:</strong> USD 84.9B ≈ Rp 1,262 T (2022)*</p>
            <p><strong>Best Practice:</strong></p>
            <ul>
                <li>Portfolio management terintegrasi</li>
                <li>Subholding structure optimal</li>
                <li>Digital transformation roadmap</li>
            </ul>
            <p><strong>Governance Score:</strong> <span style="font-size: 1.5em;">85/100**</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="benchmark-card">
            <h3>📡 PT Telkom Indonesia</h3>
            <p><strong>Model:</strong> Strategic Integration</p>
            <p><strong>Struktur:</strong> ~15 anak perusahaan utama</p>
            <p><strong>Revenue:</strong> Rp 149.22 T (2023)*</p>
            <p><strong>Best Practice:</strong></p>
            <ul>
                <li>Digital governance excellence</li>
                <li>Infrastruktur teknologi terintegrasi</li>
                <li>Innovation ecosystem</li>
            </ul>
            <p><strong>Governance Score:</strong> <span style="font-size: 1.5em;">82/100**</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="benchmark-card">
            <h3>🏦 PT Bank Mandiri</h3>
            <p><strong>Model:</strong> Financial Holdings</p>
            <p><strong>Struktur:</strong> 11 anak perusahaan finansial</p>
            <p><strong>Revenue:</strong> Rp 134.80 T (2023)*</p>
            <p><strong>Best Practice:</strong></p>
            <ul>
                <li>Cross-selling optimization</li>
                <li>Risk management integration</li>
                <li>Customer-centric approach</li>
            </ul>
            <p><strong>Governance Score:</strong> <span style="font-size: 1.5em;">88/100**</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Enhanced comparison analysis
    st.markdown("### 📈 Multi-Dimensional Benchmark Analysis")
    
    # Radar chart comparison
    benchmark_data = get_benchmark_data()
    df_benchmark = pd.DataFrame(benchmark_data)
    
    fig = go.Figure()
    
    categories = ['Governance Score', 'Digital Integration', 'Synergy Optimization', 'Risk Management']
    
    for i, bumn in enumerate(df_benchmark['BUMN']):
        values = [df_benchmark.iloc[i][cat] for cat in categories]
        values.append(values[0])  # Close the radar chart
        
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
    
    # Data disclaimer
    st.markdown("""
    <div class="info-box">
        <h4>📋 Data Sources & Disclaimer</h4>
        <p><strong>*Revenue Data Sources:</strong></p>
        <ul>
            <li>PT Pertamina: Annual Report 2022 (USD 84.9B)</li>
            <li>PT Telkom: Annual Report 2023 (IDR 149.22T)</li>
            <li>PT Bank Mandiri: Annual Report 2023 (IDR 134.80T)</li>
            <li>PT Surveyor Indonesia: Industry estimate (USD 17M)</li>
        </ul>
        <p><strong>**Assessment Scores:</strong> Berdasarkan framework governance assessment internal dan target strategis perusahaan.</p>
        <p><strong>***Struktur Anak Perusahaan:</strong> Data estimasi berdasarkan informasi publik yang tersedia.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add calculated metrics
    df_benchmark['Efficiency Ratio'] = (df_benchmark['Revenue (T IDR)'] / df_benchmark['Subsidiaries']).round(1)
    df_benchmark['Governance ROI'] = (df_benchmark['Governance Score'] * df_benchmark['Revenue (T IDR)'] / 100).round(1)
    
    st.dataframe(
        df_benchmark[['BUMN', 'Governance Score', 'Subsidiaries', 'Revenue (T IDR)', 'Efficiency Ratio', 'Governance ROI']],
        use_container_width=True,
        hide_index=True
    )
    
    # International benchmarking
    st.markdown("### 🌏 Global Best Practices")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-box">
            <h4>🏭 Singapore Technologies Engineering (STE)</h4>
            <p><strong>Model:</strong> Diversified Technology Conglomerate</p>
            <p><strong>Revenue:</strong> S$8.1B (2023)</p>
            <p><strong>Best Practices:</strong></p>
            <ul>
                <li>Technology synergy across aerospace, electronics, land systems</li>
                <li>Global network optimization</li>
                <li>AI integration in operations</li>
                <li>Sustainable innovation focus</li>
            </ul>
            <p><strong>Key Metrics:</strong></p>
            <ul>
                <li>ROE: 12.8%</li>
                <li>Operating margin: 8.2%</li>
                <li>ESG Score: A- (MSCI)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <h4>💼 Temasek Holdings</h4>
            <p><strong>Model:</strong> Active Ownership Portfolio</p>
            <p><strong>Portfolio Value:</strong> S$382B (2023)</p>
            <p><strong>Best Practices:</strong></p>
            <ul>
                <li>Long-term value creation (25-year view)</li>
                <li>ESG integration in investment decisions</li>
                <li>Digital transformation acceleration</li>
                <li>Risk management excellence</li>
            </ul>
            <p><strong>Key Metrics:</strong></p>
            <ul>
                <li>20-year TSR: 7%</li>
                <li>ESG portfolio: 25%</li>
                <li>Digital economy: 25%</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Benchmarking insights
    st.markdown("### 💡 Key Insights & Recommendations")
    
    insights_cols = st.columns(3)
    
    with insights_cols[0]:
        st.markdown("""
        <div class="success-box">
            <h4>🎯 Strategic Recommendations</h4>
            <ul>
                <li>Adopt Strategic Control model</li>
                <li>Implement portfolio optimization</li>
                <li>Digital governance platform</li>
                <li>Cross-subsidiary synergies</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with insights_cols[1]:
        st.markdown("""
        <div class="warning-box">
            <h4>⚠️ Critical Gaps</h4>
            <ul>
                <li>Digital integration maturity</li>
                <li>Performance measurement</li>
                <li>Risk management integration</li>
                <li>Stakeholder engagement</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with insights_cols[2]:
        st.markdown("""
        <div class="info-box">
            <h4>🚀 Quick Wins</h4>
            <ul>
                <li>Authority matrix clarification</li>
                <li>Monthly governance review</li>
                <li>Digital dashboard implementation</li>
                <li>Best practice sharing</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Framework Page with enhanced interactivity
elif page == "framework":
    st.markdown('<div class="sub-header">📋 Integrated Governance Framework</div>', unsafe_allow_html=True)
    
    # Framework selection
    framework_type = st.selectbox(
        "Select Framework Component:",
        ["GCG Principles", "Corporate Parenting Model", "Authority Matrix", "Risk Management"]
    )
    
    if framework_type == "GCG Principles":
        st.markdown("### 🎯 Good Corporate Governance (GCG) Assessment")
        
        # GCG Interactive Assessment
        col1, col2 = st.columns([2, 1])
        
        with col1:
            gcg_data = {
                'Prinsip': ['Transparency', 'Accountability', 'Responsibility', 'Independence', 'Fairness'],
                'Current Score': [85, 80, 88, 75, 82],
                'Target Score': [90, 88, 92, 85, 88],
                'Gap': [5, 8, 4, 10, 6],
                'Priority': ['Medium', 'High', 'Low', 'High', 'Medium']
            }
            
            df_gcg = pd.DataFrame(gcg_data)
            
            # Interactive bar chart
            fig = px.bar(
                df_gcg, 
                x='Prinsip', 
                y=['Current Score', 'Target Score'],
                title="GCG Principles Assessment",
                barmode='group',
                color_discrete_sequence=['#3182ce', '#38a169']
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
                yaxis2=dict(overlaying='y', side='right', title='Gap'),
                margin=dict(l=20, r=20, t=60, b=20)
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 🎯 Priority Actions")
            for i, row in df_gcg.iterrows():
                priority_color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}[row['Priority']]
                st.markdown(f"""
                <div class="metric-container">
                    <strong>{row['Prinsip']}</strong><br>
                    Gap: {row['Gap']} points {priority_color}<br>
                    <small>Priority: {row['Priority']}</small>
                </div>
                """, unsafe_allow_html=True)
        
        # Detailed GCG breakdown
        st.markdown("### 📋 Detailed GCG Implementation")
        
        gcg_details = {
            'Transparency': {
                'definition': 'Financial reporting akurat, disclosure material information',
                'current_practices': ['Annual report publication', 'Quarterly financial disclosure', 'Website transparency'],
                'improvements': ['Real-time dashboard', 'Enhanced disclosure framework', 'Stakeholder portal'],
                'timeline': '30 days'
            },
            'Accountability': {
                'definition': 'Clear roles, performance measurement objektif',
                'current_practices': ['Board oversight', 'Management reporting', 'Performance reviews'],
                'improvements': ['KPI enhancement', 'Accountability matrix', 'Regular assessments'],
                'timeline': '45 days'
            }
        }
        
        selected_principle = st.selectbox("Select GCG Principle for Details:", list(gcg_details.keys()))
        
        detail = gcg_details[selected_principle]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="info-box">
                <h4>📖 Definition</h4>
                <p>{detail['definition']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="success-box">
                <h4>✅ Current Practices</h4>
                <ul>
                    {''.join([f'<li>{practice}</li>' for practice in detail['current_practices']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="warning-box">
                <h4>🚀 Improvements</h4>
                <ul>
                    {''.join([f'<li>{improvement}</li>' for improvement in detail['improvements']])}
                </ul>
                <p><strong>Timeline:</strong> {detail['timeline']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    elif framework_type == "Corporate Parenting Model":
        st.markdown("### 🏗️ Corporate Parenting Model Selection")
        
        # Model comparison matrix
        parenting_data = {
            'Model': ['Financial Control', 'Strategic Control', 'Strategic Planning'],
            'Business Diversity': ['High', 'Medium', 'Low'],
            'Synergy Potential': ['Low', 'Medium', 'High'],
            'Coordination Level': ['Minimal', 'Selective', 'Extensive'],
            'PT SI Fit Score': [60, 85, 70]
        }
        
        df_parenting = pd.DataFrame(parenting_data)
        
        # Visualization
        fig = px.bar(
            df_parenting,
            x='Model',
            y='PT SI Fit Score',
            title='Corporate Parenting Model Fit Analysis',
            color='PT SI Fit Score',
            color_continuous_scale='viridis'
        )
        
        fig.update_layout(height=400, margin=dict(l=20, r=20, t=60, b=20))
        st.plotly_chart(fig, use_container_width=True)
        
        # Recommended model details
        st.markdown("""
        <div class="success-box">
            <h4>🎯 Recommended: Strategic Control Model</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <div>
                    <h5>✅ Advantages</h5>
                    <ul>
                        <li>Balance financial and strategic control</li>
                        <li>Selective intervention capability</li>
                        <li>Synergy optimization opportunities</li>
                        <li>Risk management integration</li>
                    </ul>
                </div>
                <div>
                    <h5>📋 Implementation</h5>
                    <ul>
                        <li>Authority matrix development</li>
                        <li>Performance dashboard</li>
                        <li>Strategic planning integration</li>
                        <li>Communication protocols</li>
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    elif framework_type == "Authority Matrix":
        st.markdown("### 📊 Authority Matrix & Decision Rights")
        
        # Authority matrix
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
        
        # Color-coded matrix
        def color_authority(val):
            colors = {
                'Approve': 'background-color: #d4edda',
                'Decide': 'background-color: #d4edda', 
                'Recommend': 'background-color: #fff3cd',
                'Develop': 'background-color: #fff3cd',
                'Propose': 'background-color: #feebc8',
                'Input': 'background-color: #fed7d7',
                'Review': 'background-color: #e2e8f0',
                'Oversight': 'background-color: #e2e8f0',
                'Monitor': 'background-color: #e2e8f0',
                'Manage': 'background-color: #d1ecf1',
                'Execute': 'background-color: #d1ecf1',
                'Implement': 'background-color: #d1ecf1',
                'Conduct': 'background-color: #d1ecf1',
                'Report': 'background-color: #f0f8ff'
            }
            return colors.get(val, '')
        
        styled_df = df_authority.style.applymap(color_authority, subset=['Board', 'CEO', 'Subsidiary CEO', 'Subsidiary Board'])
        st.dataframe(styled_df, use_container_width=True, hide_index=True)
        
        # Legend
        st.markdown("""
        <div class="info-box">
            <h4>🎨 Legend</h4>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem;">
                <div style="background-color: #d4edda; padding: 0.5rem; border-radius: 5px; text-align: center;">
                    <strong>Approve/Decide</strong>
                </div>
                <div style="background-color: #fff3cd; padding: 0.5rem; border-radius: 5px; text-align: center;">
                    <strong>Recommend/Develop</strong>
                </div>
                <div style="background-color: #feebc8; padding: 0.5rem; border-radius: 5px; text-align: center;">
                    <strong>Propose</strong>
                </div>
                <div style="background-color: #e2e8f0; padding: 0.5rem; border-radius: 5px; text-align: center;">
                    <strong>Review/Oversight</strong>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    else:  # Risk Management
        st.markdown("### ⚠️ Integrated Risk Management Framework")
        
        # Risk categories
        risk_data = {
            'Risk Category': ['Strategic', 'Operational', 'Financial', 'Compliance', 'Reputation'],
            'Likelihood': [3, 4, 2, 3, 2],
            'Impact': [5, 3, 4, 4, 5],
            'Risk Score': [15, 12, 8, 12, 10],
            'Current Controls': ['Board oversight', 'Process controls', 'Financial controls', 'Legal review', 'PR monitoring'],
            'Enhancement Needed': ['Strategy committee', 'Digital monitoring', 'Real-time dashboard', 'Compliance system', 'Social listening']
        }
        
        df_risk = pd.DataFrame(risk_data)
        
        # Risk heat map
        fig = px.scatter(
            df_risk,
            x='Likelihood',
            y='Impact',
            size='Risk Score',
            color='Risk Category',
            title='Risk Heat Map',
            hover_data=['Current Controls', 'Enhancement Needed']
        )
        
        fig.update_layout(height=400, margin=dict(l=20, r=20, t=60, b=20))
        st.plotly_chart(fig, use_container_width=True)
        
        # Risk register
        st.markdown("### 📋 Risk Register")
        st.dataframe(df_risk, use_container_width=True, hide_index=True)

# Timeline Page with enhanced project management features
elif page == "timeline":
    st.markdown('<div class="sub-header">⏱️ Advanced Project Timeline</div>', unsafe_allow_html=True)
    
    # Timeline controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        view_type = st.selectbox("Timeline View:", ["Gantt Chart", "Kanban Board", "Calendar View"])
    
    with col2:
        phase_filter = st.multiselect("Filter Phases:", ["Fase 1", "Fase 2", "Fase 3"], default=["Fase 1", "Fase 2", "Fase 3"])
    
    with col3:
        show_critical_path = st.checkbox("Show Critical Path", value=True)
    
    # Enhanced timeline data dengan progress realistis
    timeline_detailed = {
        'Task': [
            'Project Kickoff', 'Stakeholder Mapping', 'Current State Assessment',
            'Gap Analysis', 'Benchmarking Study', 'Framework Design',
            'Stakeholder Validation', 'Documentation', 'Final Review', 'Project Closure'
        ],
        'Phase': [
            'Fase 1', 'Fase 1', 'Fase 1', 'Fase 1', 'Fase 1',
            'Fase 2', 'Fase 2', 'Fase 3', 'Fase 3', 'Fase 3'
        ],
        'Start': [
            date(2024, 1, 15), date(2024, 1, 16), date(2024, 1, 18),
            date(2024, 1, 25), date(2024, 1, 30), date(2024, 2, 5),
            date(2024, 2, 15), date(2024, 2, 25), date(2024, 3, 5), date(2024, 3, 12)
        ],
        'Duration': [1, 3, 5, 4, 8, 10, 5, 8, 5, 3],
        'Progress': [100, 100, 85, 45, 25, 5, 0, 0, 0, 0],  # Realistic progression
        'Resource': ['PM', 'PM+Team', 'Analysts', 'Analysts', 'Consultants', 'Architects', 'Stakeholders', 'Writers', 'Board', 'PM'],
        'Critical': [True, False, True, True, False, True, True, True, True, False]
    }
    
    df_detailed = pd.DataFrame(timeline_detailed)
    df_detailed['End'] = df_detailed.apply(lambda row: row['Start'] + timedelta(days=row['Duration']), axis=1)
    
    if view_type == "Gantt Chart":
        # Enhanced Gantt chart
        fig = px.timeline(
            df_detailed[df_detailed['Phase'].isin([f'Fase {i}' for i in range(1, 4) if f'Fase {i}' in phase_filter])],
            x_start="Start",
            x_end="End",
            y="Task",
            color="Progress",
            title="Project Gantt Chart - 60 Days",
            color_continuous_scale="RdYlGn",
            hover_data=["Resource", "Duration", "Critical"]
        )
        
        if show_critical_path:
            critical_tasks = df_detailed[df_detailed['Critical'] == True]
            for _, task in critical_tasks.iterrows():
                fig.add_vrect(
                    x0=task['Start'], x1=task['End'],
                    fillcolor="red", opacity=0.2,
                    layer="below", line_width=0
                )
        
        fig.update_layout(height=600, margin=dict(l=20, r=20, t=60, b=20))
        st.plotly_chart(fig, use_container_width=True)
    
    elif view_type == "Kanban Board":
        # Kanban-style view
        col1, col2, col3, col4 = st.columns(4)
        
        statuses = ["Not Started", "In Progress", "Review", "Completed"]
        
        for i, status in enumerate(statuses):
            with [col1, col2, col3, col4][i]:
                st.markdown(f"### {status}")
                
                if status == "Completed":
                    tasks = df_detailed[df_detailed['Progress'] == 100]
                elif status == "In Progress":
                    tasks = df_detailed[(df_detailed['Progress'] > 0) & (df_detailed['Progress'] < 100)]
                elif status == "Review":
                    tasks = df_detailed[df_detailed['Progress'] == 75]  # Assuming 75% means in review
                else:
                    tasks = df_detailed[df_detailed['Progress'] == 0]
                
                for _, task in tasks.iterrows():
                    card_color = "success-box" if status == "Completed" else "info-box" if status == "In Progress" else "warning-box"
                    st.markdown(f"""
                    <div class="{card_color}" style="margin: 0.5rem 0; padding: 1rem;">
                        <h5>{task['Task']}</h5>
                        <p><strong>Phase:</strong> {task['Phase']}</p>
                        <p><strong>Resource:</strong> {task['Resource']}</p>
                        <p><strong>Duration:</strong> {task['Duration']} days</p>
                        <div style="background-color: #e9ecef; border-radius: 10px; height: 10px;">
                            <div style="background-color: #28a745; width: {task['Progress']}%; height: 100%; border-radius: 10px;"></div>
                        </div>
                        <small>{task['Progress']}% Complete</small>
                    </div>
                    """, unsafe_allow_html=True)
    
    else:  # Calendar View
        st.markdown("### 📅 Calendar View")
        
        # Calendar implementation would go here
        # For now, showing a summary table
        calendar_summary = df_detailed.groupby(df_detailed['Start'].dt.strftime('%Y-%m')).agg({
            'Task': 'count',
            'Duration': 'sum',
            'Progress': 'mean'
        }).round(1)
        
        calendar_summary.columns = ['Tasks', 'Total Days', 'Avg Progress']
        st.dataframe(calendar_summary, use_container_width=True)
    
    # Resource allocation
    st.markdown("### 👥 Resource Allocation")
    
    resource_data = df_detailed.groupby('Resource').agg({
        'Duration': 'sum',
        'Task': 'count',
        'Progress': 'mean'
    }).round(1)
    
    resource_data.columns = ['Total Days', 'Task Count', 'Avg Progress']
    
    fig = px.bar(
        resource_data.reset_index(),
        x='Resource',
        y='Total Days',
        color='Avg Progress',
        title='Resource Utilization',
        color_continuous_scale='viridis'
    )
    
    fig.update_layout(height=400, margin=dict(l=20, r=20, t=60, b=20))
    st.plotly_chart(fig, use_container_width=True)
    
    # Critical path analysis
    if show_critical_path:
        st.markdown("### 🚨 Critical Path Analysis")
        
        critical_tasks = df_detailed[df_detailed['Critical'] == True]
        
        st.markdown("""
        <div class="warning-box">
            <h4>⚠️ Critical Path Tasks</h4>
            <p>These tasks are on the critical path and any delay will impact the overall project timeline:</p>
        </div>
        """, unsafe_allow_html=True)
        
        for _, task in critical_tasks.iterrows():
            status = "🟢 On Track" if task['Progress'] >= 75 else "🟡 At Risk" if task['Progress'] >= 25 else "🔴 Delayed"
            st.markdown(f"""
            <div class="timeline-item">
                <h5>{task['Task']} {status}</h5>
                <p><strong>Phase:</strong> {task['Phase']} | <strong>Duration:</strong> {task['Duration']} days | <strong>Progress:</strong> {task['Progress']}%</p>
                <div style="background-color: #e9ecef; border-radius: 10px; height: 8px;">
                    <div style="background-color: #dc3545; width: {task['Progress']}%; height: 100%; border-radius: 10px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Enhanced Monitoring Page
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
            
            st.metric(
                label=kpi_data['KPI'][i],
                value=f"{current}%",
                delta=f"{trend:+d}%",
                delta_color="normal" if trend >= 0 else "inverse"
            )
            
            # Progress bar
            progress = current / target if target > 0 else 0
            st.progress(min(progress, 1.0))
    
    # Performance trends dengan data realistic
    st.markdown("### 📊 Performance Trends")
    
    # Generate realistic trend data instead of random
    dates = pd.date_range(start='2024-01-15', periods=30, freq='D')
    
    # Realistic trending data with logical progression
    base_values = {
        'Stakeholder Satisfaction': 82,
        'Timeline Adherence': 88, 
        'Quality Score': 85,
        'Budget Adherence': 96
    }
    
    trend_data = {'Date': dates}
    
    for kpi, base in base_values.items():
        # Create realistic trend with slight variations
        daily_variation = np.sin(np.arange(30) * 0.2) * 2  # Slight cyclical variation
        trend = np.linspace(0, 3, 30)  # Gradual improvement over time
        values = base + daily_variation + trend
        values = np.clip(values, 70, 100)  # Keep within realistic range
        trend_data[kpi] = values
    
    df_trends = pd.DataFrame(trend_data)
    
    # Interactive trend chart
    fig = go.Figure()
    
    for kpi in ['Stakeholder Satisfaction', 'Timeline Adherence', 'Quality Score', 'Budget Adherence']:
        fig.add_trace(go.Scatter(
            x=df_trends['Date'],
            y=df_trends[kpi],
            mode='lines+markers',
            name=kpi,
            line=dict(width=3)
        ))
    
    fig.update_layout(
        title='KPI Trends Over Time',
        xaxis_title='Date',
        yaxis_title='Score (%)',
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Risk monitoring
    st.markdown("### ⚠️ Risk Monitoring Dashboard")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Risk score over time dengan data realistic
        risk_dates = pd.date_range(start='2024-01-15', periods=15, freq='D')
        # Realistic risk scores yang menurun seiring project progress
        risk_scores = [18, 17.5, 17, 16.8, 16.2, 15.8, 15.5, 15, 14.5, 14.2, 13.8, 13.5, 13, 12.8, 12.5]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=risk_dates,
            y=risk_scores,
            mode='lines+markers',
            name='Risk Score',
            line=dict(color='red', width=3)
        ))
        
        fig.add_hline(y=15, line_dash="dash", line_color="orange", annotation_text="Risk Threshold")
        
        fig.update_layout(
            title='Risk Score Trend (Decreasing)',
            xaxis_title='Date',
            yaxis_title='Risk Score',
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Current risk status dengan nilai realistic
        current_risks = [
            {"Risk": "Resource Availability", "Score": 12, "Status": "🟡 Medium"},
            {"Risk": "Stakeholder Alignment", "Score": 8, "Status": "🟢 Low"},
            {"Risk": "Technical Dependencies", "Score": 15, "Status": "🟡 Medium"},
            {"Risk": "Timeline Pressure", "Score": 10, "Status": "🟢 Low"}
        ]
        
        st.markdown("#### 🎯 Current Risk Status")
        for risk in current_risks:
            st.markdown(f"""
            <div class="metric-container">
                <strong>{risk['Risk']}</strong><br>
                Score: {risk['Score']} | {risk['Status']}
            </div>
            """, unsafe_allow_html=True)
    
    # Milestone tracking dengan progress realistic
    st.markdown("### 🏁 Milestone Tracking")
    
    milestone_data = {
        'Milestone': [
            'Project Charter Finalization',
            'Current State Assessment Complete', 
            'Gap Analysis Report',
            'Benchmarking Analysis Complete',
            'Framework Design Draft',
            'Stakeholder Validation',
            'Final Documentation',
            'Project Completion'
        ],
        'Target Date': [
            '2024-01-18', '2024-01-25', '2024-02-01', '2024-02-05',
            '2024-02-15', '2024-02-28', '2024-03-10', '2024-03-15'
        ],
        'Actual Date': [
            '2024-01-18', '2024-01-24', '', '', '', '', '', ''
        ],
        'Status': [
            '✅ Completed', '✅ Completed', '🔄 In Progress', '🔄 In Progress',
            '⏳ Planned', '⏳ Planned', '⏳ Planned', '⏳ Planned'
        ],
        'Progress': [100, 100, 45, 25, 5, 0, 0, 0]  # Realistic progress levels
    }
    
    df_milestones = pd.DataFrame(milestone_data)
    df_milestones['Target Date'] = pd.to_datetime(df_milestones['Target Date'])
    
    # Milestone chart
    fig = px.bar(
        df_milestones,
        x='Milestone',
        y='Progress',
        color='Progress',
        title='Milestone Progress',
        color_continuous_scale='RdYlGn'
    )
    
    fig.update_layout(height=400, margin=dict(l=20, r=20, t=60, b=20))
    fig.update_xaxis(tickangle=45)
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed milestone table
    st.dataframe(
        df_milestones[['Milestone', 'Target Date', 'Status', 'Progress']],
        use_container_width=True,
        hide_index=True
    )

# Enhanced Documentation Page
elif page == "documentation":
    st.markdown('<div class="sub-header">📁 Comprehensive Documentation Center</div>', unsafe_allow_html=True)
    
    # Document search and filter
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_term = st.text_input("🔍 Search Documents:", placeholder="Enter keywords...")
    
    with col2:
        doc_category = st.selectbox("📂 Category:", ["All", "Assessment", "Framework", "Implementation", "Templates"])
    
    with col3:
        doc_status = st.selectbox("📊 Status:", ["All", "Draft", "Review", "Approved", "Published"])
    
    # Document library
    documents = [
        {
            "Title": "Current State Assessment Report",
            "Category": "Assessment",
            "Status": "Approved",
            "Date": "2024-01-25",
            "Size": "2.3 MB",
            "Type": "PDF",
            "Description": "Comprehensive analysis of current governance structure"
        },
        {
            "Title": "Gap Analysis Report", 
            "Category": "Assessment",
            "Status": "Review",
            "Date": "2024-02-01",
            "Size": "1.8 MB", 
            "Type": "PDF",
            "Description": "Identification of governance gaps and improvement opportunities"
        },
        {
            "Title": "Benchmarking Analysis",
            "Category": "Assessment", 
            "Status": "Draft",
            "Date": "2024-02-05",
            "Size": "3.1 MB",
            "Type": "Excel",
            "Description": "BUMN and international best practices comparison"
        },
        {
            "Title": "Governance Framework Design",
            "Category": "Framework",
            "Status": "Draft", 
            "Date": "2024-02-10",
            "Size": "1.5 MB",
            "Type": "Word",
            "Description": "Integrated governance framework specification"
        },
        {
            "Title": "Authority Matrix Template",
            "Category": "Templates",
            "Status": "Approved",
            "Date": "2024-02-08",
            "Size": "450 KB",
            "Type": "Excel", 
            "Description": "Decision-making authority matrix template"
        },
        {
            "Title": "Implementation Roadmap",
            "Category": "Implementation",
            "Status": "Draft",
            "Date": "2024-02-12",
            "Size": "1.2 MB",
            "Type": "PowerPoint",
            "Description": "Detailed implementation timeline and activities"
        }
    ]
    
    # Filter documents
    filtered_docs = documents
    if doc_category != "All":
        filtered_docs = [doc for doc in filtered_docs if doc["Category"] == doc_category]
    if doc_status != "All":
        filtered_docs = [doc for doc in filtered_docs if doc["Status"] == doc_status]
    if search_term:
        filtered_docs = [doc for doc in filtered_docs if search_term.lower() in doc["Title"].lower() or search_term.lower() in doc["Description"].lower()]
    
    # Document cards
    st.markdown("### 📚 Document Library")
    
    for doc in filtered_docs:
        status_color = {
            "Draft": "🟡",
            "Review": "🟠", 
            "Approved": "🟢",
            "Published": "🔵"
        }[doc["Status"]]
        
        type_icon = {
            "PDF": "📄",
            "Excel": "📊",
            "Word": "📝",
            "PowerPoint": "📺"
        }[doc["Type"]]
        
        st.markdown(f"""
        <div class="info-box">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4>{type_icon} {doc['Title']}</h4>
                <span>{status_color} {doc['Status']}</span>
            </div>
            <p>{doc['Description']}</p>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem;">
                <div>
                    <small><strong>Category:</strong> {doc['Category']} | <strong>Date:</strong> {doc['Date']} | <strong>Size:</strong> {doc['Size']}</small>
                </div>
                <button style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; border-radius: 5px; padding: 0.5rem 1rem;">
                    📥 Download
                </button>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick actions
    st.markdown("### 🚀 Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📊 Generate Progress Report", type="primary"):
            st.success("✅ Progress report generated successfully!")
    
    with col2:
        if st.button("📧 Email Document Pack"):
            st.success("✅ Document pack sent to stakeholders!")
    
    with col3:
        if st.button("🔄 Sync with SharePoint"):
            st.success("✅ Documents synchronized!")
    
    with col4:
        if st.button("📋 Create Document Request"):
            st.success("✅ Document request created!")
    
    # Document statistics
    st.markdown("### 📊 Document Statistics")
    
    doc_stats = {
        'Category': ['Assessment', 'Framework', 'Implementation', 'Templates'],
        'Count': [3, 1, 1, 1],
        'Total Size (MB)': [7.2, 1.5, 1.2, 0.45]
    }
    
    df_stats = pd.DataFrame(doc_stats)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.pie(df_stats, values='Count', names='Category', title='Documents by Category')
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.bar(df_stats, x='Category', y='Total Size (MB)', title='Storage by Category')
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    # Knowledge base
    st.markdown("### 🧠 Knowledge Base")
    
    kb_topics = [
        {
            "Topic": "Corporate Governance Basics",
            "Articles": 15,
            "Last Updated": "2024-01-20"
        },
        {
            "Topic": "BUMN Governance Regulations",
            "Articles": 8,
            "Last Updated": "2024-01-22"
        },
        {
            "Topic": "Risk Management Framework",
            "Articles": 12,
            "Last Updated": "2024-01-25"
        },
        {
            "Topic": "Digital Governance Tools",
            "Articles": 6,
            "Last Updated": "2024-01-28"
        }
    ]
    
    for topic in kb_topics:
        st.markdown(f"""
        <div class="success-box">
            <h5>📖 {topic['Topic']}</h5>
            <p>{topic['Articles']} articles available | Last updated: {topic['Last Updated']}</p>
            <button style="background: #28a745; color: white; border: none; border-radius: 5px; padding: 0.25rem 0.5rem;">
                📚 Browse Articles
            </button>
        </div>
        """, unsafe_allow_html=True)

# Enhanced Next Steps Page
elif page == "nextsteps":
    st.markdown('<div class="sub-header">🎯 Strategic Action Plan</div>', unsafe_allow_html=True)
    
    # Action priority matrix
    st.markdown("### 📊 Action Priority Matrix")
    
    actions_matrix = {
        'Action': [
            'Finalize Authority Matrix',
            'Implement Digital Dashboard',
            'Stakeholder Training Program',
            'Risk Management Integration',
            'Performance Measurement System',
            'Communication Protocol',
            'Policy Documentation',
            'Change Management Plan'
        ],
        'Impact': [5, 4, 3, 5, 4, 3, 2, 4],
        'Effort': [2, 3, 4, 4, 3, 2, 1, 3],
        'Priority Score': [25, 16, 12, 25, 16, 15, 14, 16],
        'Owner': ['Legal', 'IT', 'HR', 'Risk', 'Finance', 'Comms', 'Legal', 'PMO'],
        'Timeline': ['Week 1', 'Week 2', 'Week 3', 'Week 2', 'Week 4', 'Week 1', 'Week 1', 'Week 3']
    }
    
    df_actions = pd.DataFrame(actions_matrix)
    
    # Priority matrix visualization
    fig = px.scatter(
        df_actions,
        x='Effort',
        y='Impact',
        size='Priority Score',
        color='Owner',
        hover_data=['Action', 'Timeline'],
        title='Action Priority Matrix (Impact vs Effort)'
    )
    
    # Add quadrant lines
    fig.add_hline(y=3.5, line_dash="dash", line_color="gray")
    fig.add_vline(x=2.5, line_dash="dash", line_color="gray")
    
    # Add quadrant labels
    fig.add_annotation(x=1.5, y=4.5, text="Quick Wins", showarrow=False, font=dict(size=14, color="green"))
    fig.add_annotation(x=3.5, y=4.5, text="Major Projects", showarrow=False, font=dict(size=14, color="blue"))
    fig.add_annotation(x=1.5, y=2.5, text="Fill-ins", showarrow=False, font=dict(size=14, color="orange"))
    fig.add_annotation(x=3.5, y=2.5, text="Questionable", showarrow=False, font=dict(size=14, color="red"))
    
    fig.update_layout(height=500, margin=dict(l=20, r=20, t=60, b=20))
    st.plotly_chart(fig, use_container_width=True)
    
    # Immediate actions (next 7 days)
    st.markdown("### 🚀 Immediate Actions (Next 7 Days)")
    
    immediate_actions = df_actions[df_actions['Timeline'] == 'Week 1'].sort_values('Priority Score', ascending=False)
    
    for _, action in immediate_actions.iterrows():
        st.markdown(f"""
        <div class="timeline-item">
            <h4>🎯 {action['Action']}</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem;">
                <div><strong>Owner:</strong> {action['Owner']}</div>
                <div><strong>Priority Score:</strong> {action['Priority Score']}</div>
                <div><strong>Timeline:</strong> {action['Timeline']}</div>
            </div>
            <div style="margin-top: 0.5rem;">
                <strong>Impact:</strong> {'⭐' * action['Impact']} | 
                <strong>Effort:</strong> {'🔧' * action['Effort']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Success metrics and KPIs
    st.markdown("### 📊 Success Metrics & KPIs")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h4>🎯 Quantitative KPIs</h4>
            <ul>
                <li><strong>Governance Score:</strong> Reach 90/100 by March 2024</li>
                <li><strong>Implementation Timeline:</strong> 100% milestones on-time</li>
                <li><strong>Stakeholder Satisfaction:</strong> >85% approval rating</li>
                <li><strong>Cost Efficiency:</strong> ±5% of approved budget</li>
                <li><strong>Risk Mitigation:</strong> Zero high-risk items open</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <h4>🌟 Qualitative Outcomes</h4>
            <ul>
                <li><strong>Cultural Transformation:</strong> Governance mindset adoption</li>
                <li><strong>Digital Excellence:</strong> Modern governance tools</li>
                <li><strong>Best Practice Recognition:</strong> Industry benchmark status</li>
                <li><strong>Sustainable Value:</strong> Long-term value creation framework</li>
                <li><strong>Stakeholder Trust:</strong> Enhanced transparency & accountability</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Implementation roadmap
    st.markdown("### 🗺️ Implementation Roadmap")
    
    roadmap_phases = [
        {
            "Phase": "Foundation (Days 1-20)",
            "Objectives": ["Complete assessment", "Identify gaps", "Design framework"],
            "Key Deliverables": ["Assessment report", "Gap analysis", "Framework design"],
            "Success Criteria": ["Stakeholder alignment", "Clear gap identification", "Approved framework"]
        },
        {
            "Phase": "Development (Days 21-45)", 
            "Objectives": ["Build governance system", "Create documentation", "Validate approach"],
            "Key Deliverables": ["Governance policies", "Process documentation", "Training materials"],
            "Success Criteria": ["Quality validation", "Stakeholder approval", "Implementation readiness"]
        },
        {
            "Phase": "Launch (Days 46-60)",
            "Objectives": ["Finalize documentation", "Prepare launch", "Enable implementation"],
            "Key Deliverables": ["Final pedoman", "Launch materials", "Implementation plan"],
            "Success Criteria": ["Board approval", "Launch readiness", "Team preparedness"]
        }
    ]
    
    for phase in roadmap_phases:
        st.markdown(f"""
        <div class="timeline-item">
            <h4>🎯 {phase['Phase']}</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem;">
                <div>
                    <h5>📋 Objectives</h5>
                    <ul>
                        {''.join([f'<li>{obj}</li>' for obj in phase['Objectives']])}
                    </ul>
                </div>
                <div>
                    <h5>📦 Key Deliverables</h5>
                    <ul>
                        {''.join([f'<li>{deliverable}</li>' for deliverable in phase['Key Deliverables']])}
                    </ul>
                </div>
                <div>
                    <h5>✅ Success Criteria</h5>
                    <ul>
                        {''.join([f'<li>{criteria}</li>' for criteria in phase['Success Criteria']])}
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown("### 🚀 Ready to Execute")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📋 Approve Action Plan", type="primary"):
            st.success("✅ Action plan approved! Initiating next phase...")
            st.balloons()
    
    with col2:
        if st.button("👥 Mobilize Team"):
            st.success("✅ Team mobilization in progress...")
    
    with col3:
        if st.button("📅 Schedule Kickoff"):
            st.success("✅ Kickoff meeting scheduled for next Monday!")
    
    with col4:
        if st.button("📊 Setup Monitoring"):
            st.success("✅ Monitoring dashboard activated!")
    
    # Contact and support
    st.markdown("### 📞 Project Support")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-box">
            <h4>👥 Project Team Contacts</h4>
            <ul>
                <li><strong>Project Manager:</strong> John Doe (john.doe@surveyor.co.id)</li>
                <li><strong>Governance Lead:</strong> Jane Smith (jane.smith@surveyor.co.id)</li>
                <li><strong>Technical Lead:</strong> Bob Johnson (bob.johnson@surveyor.co.id)</li>
                <li><strong>Change Management:</strong> Alice Brown (alice.brown@surveyor.co.id)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
            <h4>🆘 Support Channels</h4>
            <ul>
                <li><strong>Email:</strong> governance-project@surveyor.co.id</li>
                <li><strong>Slack:</strong> #governance-transformation</li>
                <li><strong>Phone:</strong> +62-21-XXXX-XXXX (Emergency)</li>
                <li><strong>Dashboard:</strong> <a href="#" target="_blank">Project Portal</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Enhanced Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 10px; margin-top: 2rem;">
    <h3 style="color: #1f4e79; margin-bottom: 1rem;">🏢 Pemutakhiran Pedoman Tata Kelola Terintegrasi</h3>
    <h4 style="color: #2c5282;">PT Surveyor Indonesia</h4>
    <p style="font-size: 1.1rem; margin: 1rem 0;"><strong>Timeline Intensif 60 Hari Kerja | Excellence in Governance</strong></p>
    <p style="font-style: italic; color: #4a5568;">Menuju Holding Company dengan Subsidiary Governance Excellence</p>
    
    <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid #e2e8f0;">
        <p style="font-size: 0.9rem; color: #666;"><strong>📊 Data Disclaimer:</strong></p>
        <p style="font-size: 0.8rem; color: #666;">
            Revenue data sourced from official annual reports. Governance scores dan assessment metrics 
            berdasarkan framework internal dan industry benchmarking. Beberapa proyeksi dan target 
            merupakan estimasi strategis untuk keperluan perencanaan project.
        </p>
        <p style="font-size: 0.9rem;">Dashboard Version 2.0 | Last Updated: {}</p>
        <p style="font-size: 0.9rem;">🚀 Powered by Streamlit | 📊 Real-time Analytics | 🎯 Strategic Excellence</p>
    </div>
</div>
""".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")), unsafe_allow_html=True)

# Add some JavaScript for enhanced interactivity (if needed)
st.markdown("""
<script>
// Add any custom JavaScript here for enhanced interactivity
console.log("PT Surveyor Indonesia Governance Dashboard Loaded Successfully");
</script>
""", unsafe_allow_html=True)
