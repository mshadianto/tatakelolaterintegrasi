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
    
    .metric-container {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
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
    
    .week-container {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 100%);
        padding: 1.2rem;
        border-radius: 12px;
        border-left: 4px solid #3182ce;
        margin: 0.8rem 0;
        box-shadow: 0 3px 12px rgba(0,0,0,0.08);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state with timeline 56 hari (8 weeks)
if 'project_start_date' not in st.session_state:
    st.session_state.project_start_date = date(2025, 8, 1)  # Agustus 2025 start

if 'current_week' not in st.session_state:
    current_day = (date.today() - st.session_state.project_start_date).days + 1
    st.session_state.current_week = max(1, (current_day - 1) // 7 + 1)  # Week 1-8

if 'project_day' not in st.session_state:
    current_day = (date.today() - st.session_state.project_start_date).days + 1
    st.session_state.project_day = max(1, current_day)

if 'overall_progress' not in st.session_state:
    st.session_state.overall_progress = min((st.session_state.project_day / 56) * 100, 100)

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
    "🏠 Dashboard": {"id": "dashboard", "desc": "Overview & Key Metrics"},
    "📊 Benchmarking": {"id": "benchmarking", "desc": "Best Practices Analysis"},
    "🏗️ Corporate Parenting": {"id": "parenting", "desc": "Parent-Subsidiary Model"},
    "📋 GCG Framework": {"id": "framework", "desc": "Governance Structure & GRC"},
    "⏱️ Timeline 60 Hari": {"id": "timeline", "desc": "Week-based Schedule"},
    "📈 Monitoring": {"id": "monitoring", "desc": "Progress & KPIs"},
    "📁 Dokumentasi": {"id": "documentation", "desc": "Resources & Files"},
    "🎯 Next Steps": {"id": "nextsteps", "desc": "Action Plans"}
}

# Create enhanced sidebar menu
selected_page = st.sidebar.selectbox(
    "Pilih Halaman",
    list(pages.keys()),
    format_func=lambda x: f"{x} - {pages[x]['desc']}"
)

page = pages[selected_page]["id"]

# Progress indicator in sidebar
st.sidebar.markdown("### 📊 Overall Progress")
progress_bar = st.sidebar.progress(st.session_state.overall_progress / 100)
st.sidebar.write(f"{st.session_state.overall_progress:.1f}% Complete")

# Quick stats in sidebar
st.sidebar.markdown("### 📈 Quick Stats")
st.sidebar.metric("Project Day", f"Day {st.session_state.project_day}/56")
st.sidebar.metric("Current Week", f"Week {st.session_state.current_week}/8")
st.sidebar.metric("Active Activities", "7")

# Main header
st.markdown("""
<div class="main-header">
    🏢 Pemutakhiran Pedoman Tata Kelola Terintegrasi<br>
    <span style="font-size: 1.5rem; opacity: 0.9;">PT Surveyor Indonesia</span><br>
    <span style="font-size: 1rem; opacity: 0.8;">Timeline 56 Hari - Agustus 2025 - Excellence in Corporate Governance</span>
</div>
""", unsafe_allow_html=True)

# Add disclaimer
st.markdown(f"""
<div class="warning-box">
    <h4 style="color: #856404; margin: 0;">⚠️ FRAMEWORK DISCLAIMER - Day {st.session_state.project_day}</h4>
    <p style="color: #856404; margin: 0.5rem 0; font-size: 0.9rem;">
        <strong>Dashboard ini menyajikan framework governance dan metodologi konseptual.</strong><br>
        Data numerik bersifat ilustratif untuk keperluan perencanaan dan benchmarking framework, bukan data finansial aktual.
        Materi untuk penggunaan internal PT Surveyor Indonesia dalam konteks pengembangan governance framework.
    </p>
</div>
""", unsafe_allow_html=True)

# Helper functions
@st.cache_data
def get_timeline_data():
    start_date = st.session_state.project_start_date
    current_day = st.session_state.project_day
    
    # Timeline Pekerjaan - 7 Aktivitas Utama (56 hari = 8 minggu)
    timeline_activities = [
        {
            'Activity': 'Kick-Off Meeting',
            'Week': 'Minggu Ke-1',
            'Days': 'Hari 1-7',
            'Start_Day': 1,
            'End_Day': 7,
            'Description': 'Project initiation, team mobilization, dan stakeholder alignment'
        },
        {
            'Activity': 'Review Dokumen',
            'Week': 'Minggu Ke-1 s/d Ke-3', 
            'Days': 'Hari 1-21',
            'Start_Day': 1,
            'End_Day': 21,
            'Description': 'Review Pedoman eksisting, regulasi, Anggaran Dasar, Kebijakan Internal'
        },
        {
            'Activity': 'Interview',
            'Week': 'Minggu Ke-3 s/d Ke-4',
            'Days': 'Hari 22-36', 
            'Start_Day': 22,
            'End_Day': 36,
            'Description': 'Melakukan wawancara dengan Dewan Komisaris, Direksi, dan Unit lain untuk mendapatkan insight serta mengetahui tantangan dan ekspektasi dalam hubungan kerja organisasi (Induk Perusahaan) dan Anak Perusahaan'
        },
        {
            'Activity': 'Pemutakhiran Pedoman',
            'Week': 'Minggu Ke-2 s/d Ke-5',
            'Days': 'Hari 8-30',
            'Start_Day': 8, 
            'End_Day': 30,
            'Description': 'Menyusun draft awal pedoman yang telah dimutakhirkan berdasarkan hasil analisis, diskusi, dan masukan dari seluruh pemangku kepentingan yang terlibat'
        },
        {
            'Activity': 'Validasi Internal',
            'Week': 'Minggu Ke-5 s/d Ke-6',
            'Days': 'Hari 29-42',
            'Start_Day': 29,
            'End_Day': 42,
            'Description': 'Pembahasan draft awal dengan Internal Perusahaan (Dewan Komisaris, Direksi, dan Unit lain yang diperlukan)'
        },
        {
            'Activity': 'Finalisasi Dokumen',
            'Week': 'Minggu Ke-6 s/d Ke-7',
            'Days': 'Hari 31-49',
            'Start_Day': 31,
            'End_Day': 49,
            'Description': 'Menindaklanjuti hasil validasi internal untuk finalisasi draft'
        },
        {
            'Activity': 'Sosialisasi',
            'Week': 'Minggu Ke-7 s/d Ke-8', 
            'Days': 'Hari 43-56',
            'Start_Day': 43,
            'End_Day': 56,
            'Description': 'Sosialisasi kepada Insan Perusahaan dan stakeholders'
        }
    ]
    
    # Calculate progress for each activity
    for activity in timeline_activities:
        if current_day < activity['Start_Day']:
            activity['Progress'] = 0
            activity['Status'] = '⏳ Planned'
        elif current_day > activity['End_Day']:
            activity['Progress'] = 100
            activity['Status'] = '✅ Completed'
        else:
            days_in_activity = activity['End_Day'] - activity['Start_Day'] + 1
            days_completed = current_day - activity['Start_Day'] + 1
            activity['Progress'] = round((days_completed / days_in_activity) * 100)
            activity['Status'] = '🔄 In Progress'
    
    return timeline_activities

@st.cache_data
def get_benchmark_data():
    return {
        'BUMN': ['Pertamina', 'Telkom', 'Bank Mandiri', 'Surveyor Indonesia (Target)'],
        'Governance Score': [88, 85, 90, 88],
        'Digital Integration': [82, 92, 87, 85],
        'Synergy Optimization': [85, 80, 88, 86],
        'Risk Management': [90, 83, 92, 89]
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
    st.markdown(f'<div class="sub-header">📊 Executive Dashboard - Week {st.session_state.current_week}, Day {st.session_state.project_day}</div>', unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #1f4e79; margin-bottom: 0.5rem;">⏰ Timeline</h3>
            <h1 style="color: #e53e3e; margin: 0; font-size: 2.5rem;">56</h1>
            <h3 style="color: #e53e3e; margin: 0;">Hari</h3>
            <p style="margin: 0; color: #666;">Agustus 2025 - 8 Minggu</p>
            <div style="margin-top: 0.5rem;">
                <small style="color: #28a745;">✓ Currently Day {st.session_state.project_day}</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1f4e79; margin-bottom: 0.5rem;">📋 Activities</h3>
            <h1 style="color: #38a169; margin: 0; font-size: 2.5rem;">7</h1>
            <h3 style="color: #38a169; margin: 0;">Utama</h3>
            <p style="margin: 0; color: #666;">Timeline Overlapping</p>
            <div style="margin-top: 0.5rem;">
                <small style="color: #28a745;">✓ Agustus 2025</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #1f4e79; margin-bottom: 0.5rem;">📅 Current</h3>
            <h1 style="color: #3182ce; margin: 0; font-size: 2.5rem;">{st.session_state.current_week}</h1>
            <h3 style="color: #3182ce; margin: 0;">Week</h3>
            <p style="margin: 0; color: #666;">of 8 Total Weeks</p>
            <div style="margin-top: 0.5rem;">
                <small style="color: #28a745;">✓ Week-based Tracking</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1f4e79; margin-bottom: 0.5rem;">🌟 Target</h3>
            <h1 style="color: #805ad5; margin: 0; font-size: 2.5rem;">8</h1>
            <h3 style="color: #805ad5; margin: 0;">Entities</h3>
            <p style="margin: 0; color: #666;">Optimal Structure</p>
            <div style="margin-top: 0.5rem;">
                <small style="color: #28a745;">✓ Strategic Control</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Project health dashboard
    st.markdown(f'<div class="sub-header">🎯 Project Health Dashboard - Week {st.session_state.current_week}</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        # Progress visualization
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Overall Progress', 'Week Progress', 'Quality Score', 'Resource Utilization'),
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
                title={'text': "Overall Progress"},
                number={'suffix': "%"},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#3182ce"},
                    'steps': [
                        {'range': [0, 25], 'color': "#fed7d7"},
                        {'range': [25, 50], 'color': "#feebc8"},
                        {'range': [50, 75], 'color': "#c6f6d5"},
                        {'range': [75, 100], 'color': "#9ae6b4"}
                    ]
                }
            ),
            row=1, col=1
        )
        
        # Week Progress
        week_progress = ((st.session_state.project_day - 1) % 7 + 1) / 7 * 100
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=week_progress,
                title={'text': "Week Progress"},
                number={'suffix': "%"},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#38a169"}
                }
            ),
            row=1, col=2
        )
        
        # Quality Score
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=85,
                title={'text': "Quality Score"},
                number={'suffix': "%"},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#805ad5"}
                }
            ),
            row=2, col=1
        )
        
        # Resource Utilization
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=82,
                title={'text': "Resource Utilization"},
                number={'suffix': "%"},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#e53e3e"}
                }
            ),
            row=2, col=2
        )
        
        fig.update_layout(height=500, margin=dict(l=30, r=30, t=80, b=30), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(f"### 📋 Week {st.session_state.current_week} Focus")
        
        timeline_activities = get_timeline_data()
        active_activities = [act for act in timeline_activities if act['Status'] == '🔄 In Progress']
        
        focus_items = []
        if active_activities:
            for activity in active_activities:
                focus_items.append(f"🔄 {activity['Activity']} ({activity['Progress']}%)")
        
        if not focus_items:
            if st.session_state.current_week <= 1:
                focus_items = ["🔄 Kick-Off Meeting", "🔄 Document Review", "⏳ Team Setup"]
            elif st.session_state.current_week <= 3:
                focus_items = ["🔄 Document Assessment", "🔄 Framework Analysis", "⏳ Interview Prep"]
            elif st.session_state.current_week <= 5:
                focus_items = ["🔄 Stakeholder Interviews", "🔄 Framework Development", "⏳ Validation Prep"]
            else:
                focus_items = ["🔄 Document Finalization", "🔄 Socialization", "⏳ Implementation Prep"]
        
        st.markdown(f"""
        <div class="info-box">
            <h4>🎯 Active Activities</h4>
            <ul>
                {''.join([f'<li>{item}</li>' for item in focus_items])}
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

# Timeline Page with week-based structure
elif page == "timeline":
    st.markdown('<div class="sub-header">⏱️ Timeline 56 Hari - Agustus 2025 Implementation Schedule</div>', unsafe_allow_html=True)
    
    # Current status indicator
    st.markdown(f"""
    <div class="info-box">
        <h4 style="color: #1f4e79; margin: 0;">📅 Current Status: Week {st.session_state.current_week}, Day {st.session_state.project_day}</h4>
        <p style="color: #1f4e79; margin: 0.5rem 0;">
            Progress: {st.session_state.overall_progress:.1f}% | Timeline: Agustus 2025 - 56 Hari (8 Minggu)
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get timeline data
    timeline_activities = get_timeline_data()
    
    # Create timeline visualization
    st.markdown("### 📊 Timeline Pekerjaan - 7 Aktivitas Utama")
    
    # Create Gantt-style chart
    fig = go.Figure()
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FCEA2B', '#FF9F43', '#AA7CB3']
    
    for i, activity in enumerate(timeline_activities):
        fig.add_trace(go.Scatter(
            x=[activity['Start_Day'], activity['End_Day']],
            y=[i, i],
            mode='lines+markers',
            line=dict(width=20, color=colors[i]),
            marker=dict(size=12),
            name=activity['Activity'],
            hovertemplate=f"<b>{activity['Activity']}</b><br>" +
                         f"Period: {activity['Days']}<br>" +
                         f"Week: {activity['Week']}<br>" +
                         f"Progress: {activity['Progress']}%<br>" +
                         f"Status: {activity['Status']}<extra></extra>"
        ))
    
    # Add current day indicator
    fig.add_vline(x=st.session_state.project_day, line_dash="dash", line_color="red", 
                  annotation_text=f"Day {st.session_state.project_day}", annotation_position="top")
    
    # Add week markers
    for week in range(1, 9):
        week_day = (week - 1) * 7 + 1
        if week_day <= 56:
            fig.add_vline(x=week_day, line_dash="dot", line_color="gray", opacity=0.5,
                          annotation_text=f"W{week}", annotation_position="bottom")
    
    fig.update_layout(
        title="Timeline 56 Hari - Agustus 2025 - Aktivitas Overlapping",
        xaxis_title="Project Day",
        yaxis_title="Activities",
        yaxis=dict(
            tickmode='array',
            tickvals=list(range(len(timeline_activities))),
            ticktext=[activity['Activity'] for activity in timeline_activities]
        ),
        height=500,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Weekly breakdown
    st.markdown("### 📅 Breakdown per Minggu - Agustus 2025")
    
    # Create weekly structure for 8 weeks
    weeks = [
        {"week": 1, "period": "Minggu Ke-1", "focus": "Kick-Off Meeting & Review Dokumen Awal"},
        {"week": 2, "period": "Minggu Ke-2", "focus": "Review Dokumen Lanjutan & Pemutakhiran Pedoman Awal"},
        {"week": 3, "period": "Minggu Ke-3", "focus": "Review Dokumen Selesai & Interview Dimulai"},
        {"week": 4, "period": "Minggu Ke-4", "focus": "Interview & Pemutakhiran Pedoman Berlanjut"},
        {"week": 5, "period": "Minggu Ke-5", "focus": "Pemutakhiran Pedoman Selesai & Validasi Internal Dimulai"},
        {"week": 6, "period": "Minggu Ke-6", "focus": "Validasi Internal & Finalisasi Dokumen Dimulai"},
        {"week": 7, "period": "Minggu Ke-7", "focus": "Finalisasi Dokumen & Sosialisasi Dimulai"},
        {"week": 8, "period": "Minggu Ke-8", "focus": "Sosialisasi & Persiapan Implementasi"}
    ]
    
    for week_info in weeks:
        week_num = week_info["week"]
        is_current = week_num == st.session_state.current_week
        is_completed = week_num < st.session_state.current_week
        
        # Get activities for this week
        week_activities = []
        for activity in timeline_activities:
            week_start = (week_num - 1) * 7 + 1
            week_end = week_num * 7
            if (activity['Start_Day'] <= week_end and activity['End_Day'] >= week_start):
                week_activities.append(activity)
        
        status_icon = "✅" if is_completed else "🔄" if is_current else "⏳"
        box_class = "success-box" if is_completed else "info-box" if is_current else "warning-box"
        
        st.markdown(f"""
        <div class="{box_class}">
            <h4>{status_icon} Week {week_num}: {week_info['period']}</h4>
            <p><strong>Focus:</strong> {week_info['focus']}</p>
            <p><strong>Key Activities:</strong></p>
            <ul>
                {''.join([f'<li>{act["Activity"]} ({act["Status"]})</li>' for act in week_activities])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Detailed activity breakdown
    st.markdown("### 📋 Detailed Activity Breakdown")
    
    for i, activity in enumerate(timeline_activities, 1):
        status_box = "success-box" if activity['Status'] == '🔄 In Progress' else "info-box" if activity['Status'] == '✅ Completed' else "warning-box"
        
        st.markdown(f"""
        <div class="{status_box}">
            <h4>{i}. {activity['Activity']} {activity['Status']}</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem;">
                <div>
                    <strong>Timeline:</strong> {activity['Week']}<br>
                    <strong>Days:</strong> {activity['Days']}
                </div>
                <div>
                    <strong>Progress:</strong> {activity['Progress']}%<br>
                    <strong>Duration:</strong> {activity['End_Day'] - activity['Start_Day'] + 1} days
                </div>
                <div>
                    <div style="background: #e2e8f0; border-radius: 4px; height: 8px;">
                        <div style="background: #3182ce; height: 8px; border-radius: 4px; width: {activity['Progress']}%;"></div>
                    </div>
                </div>
            </div>
            <p style="margin-top: 1rem;"><strong>Description:</strong> {activity['Description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Corporate Parenting Page (keeping existing structure)
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

# Benchmarking Page
elif page == "benchmarking":
    st.markdown('<div class="sub-header">📊 Comprehensive Benchmarking Analysis</div>', unsafe_allow_html=True)
    
    # BUMN Benchmarking
    st.markdown("### 🏆 BUMN Excellence Benchmark")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="benchmark-card">
            <h3>🛢️ PT Pertamina (Persero)</h3>
            <p><strong>Model:</strong> Strategic Control Holding Company</p>
            <p><strong>Transformasi Struktur:</strong> Konsolidasi anak perusahaan (2021)</p>
            <p><strong>Best Practice Focus:</strong></p>
            <ul>
                <li>Portfolio optimization strategy</li>
                <li>Integrated governance framework</li>
                <li>Regulatory compliance excellence</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="benchmark-card">
            <h3>📡 PT Telkom Indonesia</h3>
            <p><strong>Model:</strong> Strategic Integration Holding</p>
            <p><strong>Best Practice Focus:</strong></p>
            <ul>
                <li>Digital governance integration</li>
                <li>Technology-enabled operations</li>
                <li>Strategic business unit coordination</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="benchmark-card">
            <h3>🏦 PT Bank Mandiri</h3>
            <p><strong>Model:</strong> Financial Holdings dengan Cross-selling</p>
            <p><strong>Best Practice Focus:</strong></p>
            <ul>
                <li>Financial services integration</li>
                <li>Customer ecosystem development</li>
                <li>Digital banking transformation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Benchmark comparison chart
    st.markdown("### 📈 Multi-Dimensional Benchmark Analysis")
    
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
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        title="Governance Excellence Radar Analysis",
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Framework Page
elif page == "framework":
    st.markdown('<div class="sub-header">📋 Good Corporate Governance (GCG) & GRC Framework</div>', unsafe_allow_html=True)
    
    st.markdown("### 🎯 Good Corporate Governance (GCG) Framework")
    
    gcg_principles = {
        'Prinsip': ['Transparency', 'Accountability', 'Responsibility', 'Independence', 'Fairness'],
        'Baseline Assessment': [82, 78, 85, 72, 80],
        'Target Framework': [90, 88, 92, 85, 88],
        'Development Gap': [8, 10, 7, 13, 8],
        'Priority': ['High', 'High', 'Medium', 'Critical', 'High']
    }
    
    df_gcg = pd.DataFrame(gcg_principles)
    
    fig = px.bar(
        df_gcg, 
        x='Prinsip', 
        y=['Baseline Assessment', 'Target Framework'],
        title="GCG Framework Development Assessment (Illustrative)",
        barmode='group',
        color_discrete_sequence=['#e53e3e', '#38a169']
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Monitoring Page
elif page == "monitoring":
    st.markdown('<div class="sub-header">📈 Real-time Monitoring Dashboard</div>', unsafe_allow_html=True)
    
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

# Documentation Page
elif page == "documentation":
    st.markdown('<div class="sub-header">📁 Comprehensive Documentation Center</div>', unsafe_allow_html=True)
    
    doc_categories = ['Assessment Reports', 'Framework Documents', 'Implementation Plans', 'Templates & Tools']
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        selected_category = st.selectbox("Select Document Category:", doc_categories)
        
        documents = {
            'Assessment Reports': [
                {'name': 'Current State Assessment', 'status': 'Completed', 'date': '2025-08-10'},
                {'name': 'Gap Analysis Report', 'status': 'In Progress', 'date': '2025-08-15'},
                {'name': 'Benchmarking Study', 'status': 'Draft', 'date': '2025-08-20'}
            ]
        }
        
        for doc in documents.get(selected_category, []):
            status_color = {'Completed': '🟢', 'In Progress': '🟡', 'Draft': '🟠'}
            
            with st.expander(f"{doc['name']} {status_color.get(doc['status'], '⚪')}"):
                st.markdown(f"**Status:** {doc['status']}")
                st.markdown(f"**Date:** {doc['date']}")
    
    with col2:
        st.markdown("### 📊 Document Statistics")
        st.metric("Total Documents", 12)
        st.metric("Completed", 4)
        st.metric("Completion Rate", "33%")

# Next Steps Page
elif page == "nextsteps":
    st.markdown('<div class="sub-header">🎯 Expected Outcomes & Strategic Action Plan</div>', unsafe_allow_html=True)
    
    st.markdown(f"### 🚀 Immediate Next Steps (Week {st.session_state.current_week}, Day {st.session_state.project_day})")
    
    next_steps = [
        {'action': 'Complete Current Week Activities', 'timeline': f'Week {st.session_state.current_week}', 'owner': 'Project Team', 'priority': 'Critical'},
        {'action': 'Prepare for Next Week', 'timeline': f'Week {min(st.session_state.current_week + 1, 8)}', 'owner': 'Project Manager', 'priority': 'High'},
        {'action': 'Update Documentation', 'timeline': 'Ongoing', 'owner': 'Documentation Team', 'priority': 'Medium'}
    ]
    
    for step in next_steps:
        priority_colors = {'Critical': '🔴', 'High': '🟠', 'Medium': '🟡'}
        
        with st.expander(f"{priority_colors.get(step['priority'], '⚪')} {step['action']} - {step['priority']} Priority"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Timeline:** {step['timeline']}")
            with col2:
                st.markdown(f"**Owner:** {step['owner']}")
    
    # Success metrics
    st.markdown("### 📊 Success Metrics Framework - Timeline 56 Hari")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🎯 Quality Metrics")
        st.markdown("""
        • Stakeholder satisfaction >85%  
        • Framework completeness >90%  
        • BUMN best practice integration >95%
        • Expert validation approval  
        • Compliance verification 100%
        """)
    
    with col2:
        st.markdown("#### ⚡ Efficiency Metrics")
        st.markdown(f"""
        • Week {st.session_state.current_week}/8 timeline adherence  
        • Budget adherence ±5%  
        • Resource utilization >80%  
        • Risk mitigation effectiveness
        • 7 aktivitas overlapping efficiency
        """)
    
    with col3:
        st.markdown("#### 📈 Effectiveness Metrics")
        st.markdown("""
        • Implementation readiness >85%  
        • Change management adoption  
        • Governance score improvement  
        • Long-term sustainability
        • BUMN benchmark achievement
        """)

# Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #666; padding: 2rem; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 10px; margin-top: 2rem;">
    <h3 style="color: #1f4e79; margin-bottom: 1rem;">🏢 Pemutakhiran Pedoman Tata Kelola Terintegrasi</h3>
    <h4 style="color: #2c5282;">PT Surveyor Indonesia</h4>
    <p style="font-size: 1.1rem; margin: 1rem 0;"><strong>Week {st.session_state.current_week}/8 - Day {st.session_state.project_day}/56 Implementation</strong></p>
    <p style="font-style: italic; color: #4a5568;">Agustus 2025 - Excellence in Corporate Governance & Strategic Control Model</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Dashboard Information:**")
    st.markdown(f"• Version 4.0 - Week {st.session_state.current_week}")
    st.markdown(f"• Last Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    st.markdown("• 56-Day Timeline Agustus 2025")

with col2:
    st.markdown("**Created by:**")
    st.markdown("• MS Hadianto")
    st.markdown("• **KIM Consulting 2025**")
    st.markdown("• Strategic Excellence")

with col3:
    st.markdown("**Methodology:**")
    st.markdown("• 🚀 Agustus 2025 - 56 Hari")
    st.markdown("• 📅 8 Minggu, 7 Aktivitas")
    st.markdown("• 🎯 Strategic Control Framework")

st.markdown("---")
st.markdown(f"""
<div style="text-align: center; padding: 1rem; background: #fff3cd; border: 2px solid #ffc107; border-radius: 10px; margin: 1rem 0;">
    <h4 style="color: #856404; margin: 0;">⚠️ COMPREHENSIVE DISCLAIMER - Week {st.session_state.current_week}</h4>
    <p style="color: #856404; margin: 0.5rem 0; font-size: 0.9rem;">
        <strong>Materi sosialisasi ini untuk digunakan secara terbatas pada PT Surveyor Indonesia.</strong><br>
        Timeline menggunakan struktur 56 hari (8 minggu) dengan 7 aktivitas utama overlapping - Agustus 2025.
        BUMN structure analysis berdasarkan Annual Reports. Semua data numerik bersifat ilustratif 
        untuk keperluan pengembangan framework dan benchmarking metodologi, bukan data aktual.
    </p>
</div>
""", unsafe_allow_html=True)
