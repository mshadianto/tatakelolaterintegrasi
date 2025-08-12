#!/usr/bin/env python3
"""
main_1.py
Streamlit Application untuk Materi Sosialisasi Tata Kelola Hubungan Induk dan Anak Perusahaan
PT Surveyor Indonesia

Untuk menjalankan:
streamlit run main_1.py

Untuk deploy ke Streamlit Cloud:
1. Push ke GitHub repository
2. Connect ke Streamlit Cloud
3. Deploy aplikasi
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import base64
from io import BytesIO

# Error handling for missing dependencies
try:
    import plotly.express as px
    import plotly.graph_objects as go
except ImportError as e:
    st.error(f"Missing required dependency: {e}")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="PTSI Governance Framework",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def load_css():
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .section-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        margin: 1rem 0;
    }
    
    .benchmark-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-left: 4px solid #2a5298;
        margin: 1rem 0;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem;
    }
    
    .principle-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem;
    }
    
    .timeline-item {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    
    .highlight-box {
        background: #fff3cd;
        padding: 1rem;
        border-radius: 6px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    
    .recommendation-box {
        background: #d1ecf1;
        padding: 1rem;
        border-radius: 6px;
        border-left: 4px solid #17a2b8;
        margin: 1rem 0;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #f0f2f6;
        border-radius: 4px 4px 0 0;
        gap: 1px;
        padding-left: 20px;
        padding-right: 20px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #2a5298;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Data for charts and tables
def get_benchmark_data():
    return pd.DataFrame({
        'Perusahaan': ['PT Pertamina', 'PT PLN', 'PT BULOG', 'General Electric', 'Berkshire Hathaway'],
        'Model Parenting': ['Strategic Parent', 'Integrator Parent', 'Architect Parent', 'Strategic Parent', 'Financial Parent'],
        'Jumlah Anak Perusahaan': [17, 12, 8, 25, 60],
        'Score Governance': [85, 82, 78, 92, 88],
        'Kategori': ['BUMN', 'BUMN', 'BUMN', 'International', 'International']
    })

def get_gap_analysis_data():
    return pd.DataFrame({
        'Area': ['Strategic Clarity', 'Governance Structure', 'Performance Management', 'Risk Management', 'Talent Management'],
        'Current Score': [60, 65, 58, 62, 55],
        'Target Score': [85, 88, 85, 87, 80],
        'Gap': [25, 23, 27, 25, 25]
    })

def get_timeline_data():
    start_date = datetime.now()
    return pd.DataFrame({
        'Phase': ['Persiapan', 'Pengembangan', 'Implementasi'],
        'Start': [start_date, start_date + timedelta(days=60), start_date + timedelta(days=120)],
        'End': [start_date + timedelta(days=60), start_date + timedelta(days=120), start_date + timedelta(days=180)],
        'Duration': ['2 Bulan', '2 Bulan', '2 Bulan'],
        'Status': ['Planning', 'Development', 'Implementation']
    })

def get_parenting_matrix_data():
    return pd.DataFrame({
        'Model': ['Financial Parent', 'Strategic Parent', 'Synergistic Parent', 'Functional Parent'],
        'Business Relatedness': ['Low', 'Medium', 'High', 'Medium-High'],
        'Synergy Potential': ['Low', 'Medium', 'High', 'Medium'],
        'Parent Expertise': ['Financial', 'Strategic', 'Operational', 'Functional'],
        'Subsidiary Autonomy': ['High', 'Medium', 'Low', 'Medium'],
        'Management Complexity': ['Low', 'Medium', 'High', 'Medium'],
        'Fit Score': [60, 85, 75, 70]
    })

# Download function
def get_download_link(content, filename, link_text):
    b64 = base64.b64encode(content.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">{link_text}</a>'
    return href

# Main application
def main():
    load_css()
    
    # Sidebar navigation
    st.sidebar.title("🏢 PTSI Governance Framework")
    st.sidebar.markdown("---")
    
    # Add version and info
    st.sidebar.info("""
    **Version:** 1.0  
    **Last Updated:** August 2025  
    **Consultant:** KIM Consulting  
    **Framework:** Streamlit App
    """)
    
    page = st.sidebar.selectbox(
        "Pilih Halaman:",
        [
            "🏠 Overview",
            "📊 Benchmarking",
            "🔍 Gap Analysis", 
            "📅 Rencana Kerja",
            "🤝 Peran & Tanggung Jawab",
            "⚖️ Prinsip Tata Kelola",
            "🎯 Corporate Parenting",
            "🚀 Implementation",
            "📈 Success Metrics",
            "📋 Kesimpulan",
            "🛠️ Setup & Deploy"
        ]
    )
    
    # Add disclaimer in sidebar
    st.sidebar.warning("""
    ⚠️ **Disclaimer**  
    Materi sosialisasi untuk kalangan terbatas PT Surveyor Indonesia
    """)
    
    # Add consultant info in sidebar
    with st.sidebar.expander("👨‍💼 Narasumber"):
        st.write("""
        **M Sopian Hadianto**  
        SE, Ak, CA, MM, QIA, GRCP, GRCA, CACP, CCFA, CGP
        
        **KIM Consulting**  
        Tata Kelola Terintegrasi
        """)
    
    # Add setup info in sidebar
    with st.sidebar.expander("ℹ️ App Info"):
        st.write("""
        **Tech Stack:**
        - Streamlit
        - Plotly
        - Pandas
        
        **Features:**
        - Interactive charts
        - Responsive design
        - Download reports
        - Multi-page navigation
        """)
    
    # Main content based on page selection
    try:
        if page == "🏠 Overview":
            show_overview()
        elif page == "📊 Benchmarking":
            show_benchmarking()
        elif page == "🔍 Gap Analysis":
            show_gap_analysis()
        elif page == "📅 Rencana Kerja":
            show_work_plan()
        elif page == "🤝 Peran & Tanggung Jawab":
            show_roles_responsibilities()
        elif page == "⚖️ Prinsip Tata Kelola":
            show_governance_principles()
        elif page == "🎯 Corporate Parenting":
            show_corporate_parenting()
        elif page == "🚀 Implementation":
            show_implementation()
        elif page == "📈 Success Metrics":
            show_success_metrics()
        elif page == "📋 Kesimpulan":
            show_conclusion()
        elif page == "🛠️ Setup & Deploy":
            show_setup_instructions()
    except Exception as e:
        st.error(f"Error loading page: {str(e)}")
        st.info("Please try refreshing the page or contact support.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; padding: 20px;">
        <p><strong>PT Surveyor Indonesia - Governance Framework Application</strong></p>
        <p><strong>👨‍💼 Narasumber:</strong> M Sopian Hadianto, SE, Ak, CA, MM, QIA, GRCP, GRCA, CACP, CCFA, CGP</p>
        <p><strong>🏢 KIM Consulting 2025</strong></p>
        <p style="font-size: 0.9em; font-style: italic; color: #dc3545;">⚠️ Disclaimer: Materi sosialisasi untuk kalangan terbatas PT Surveyor Indonesia</p>
    </div>
    """, unsafe_allow_html=True)

def show_overview():
    st.markdown("""
    <div class="main-header">
        <h1>🏢 Materi Sosialisasi</h1>
        <h2>Tata Kelola Hubungan Induk dan Anak Perusahaan</h2>
        <h3>PT Surveyor Indonesia</h3>
        <br>
        <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin-top: 20px;">
            <h4>👨‍💼 Narasumber:</h4>
            <p style="font-size: 1.1em; font-weight: 500;">M Sopian Hadianto, SE, Ak, CA, MM, QIA, GRCP, GRCA, CACP, CCFA, CGP</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 10px; border-radius: 8px; margin-top: 10px;">
            <p style="font-size: 0.9em; font-style: italic;">⚠️ Disclaimer: Materi sosialisasi untuk kalangan terbatas PT Surveyor Indonesia</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Executive Summary
    st.markdown("""
    <div class="highlight-box">
        <h3>📌 Executive Summary</h3>
        <p>Sebagai bagian dari transformasi tata kelola PT Surveyor Indonesia dalam era holding IDSurvey, 
        diperlukan pemutakhiran pedoman tata kelola hubungan induk dan anak perusahaan yang komprehensif, 
        selaras dengan best practices BUMN dan framework Corporate Parenting Model terkini.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Information
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**Status PTSI**\n\nAnak perusahaan PT Biro Klasifikasi Indonesia (Persero)")
    
    with col2:
        st.info("**Holding Structure**\n\nBagian dari IDSurvey sejak 2021")
    
    with col3:
        st.info("**Anak Perusahaan**\n\nPT Surveyor Carbon Consulting Indonesia (SCCI)")
    
    # Context
    st.markdown("### 📍 Konteks Transformasi")
    st.write("""
    PT Surveyor Indonesia telah mengalami transformasi signifikan sebagai bagian dari pembentukan 
    holding BUMN IDSurvey. Dalam konteks ini, diperlukan framework tata kelola yang:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🎯 Strategis:**
        - Selaras dengan visi IDSurvey
        - Mengoptimalkan sinergi grup
        - Meningkatkan daya saing
        """)
    
    with col2:
        st.markdown("""
        **⚙️ Operasional:**
        - Efisiensi proses bisnis
        - Risk management terintegrasi
        - Performance excellence
        """)
    
    # Download Section
    st.markdown("### 📥 Download Materi")
    if st.button("📄 Generate Full Report"):
        report_content = generate_full_report()
        st.download_button(
            label="Download PDF Report",
            data=report_content,
            file_name="PTSI_Governance_Framework.txt",
            mime="text/plain"
        )

def show_benchmarking():
    st.markdown("""
    <div class="section-header">
        <h2>📊 Benchmarking BUMN & International Best Practices</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Chart: Governance Score Comparison
    df_benchmark = get_benchmark_data()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = px.bar(
            df_benchmark, 
            x='Perusahaan', 
            y='Score Governance',
            color='Kategori',
            title="Perbandingan Score Governance",
            color_discrete_map={'BUMN': '#2a5298', 'International': '#28a745'}
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.metric("Average BUMN Score", "75", "15%")
        st.metric("Average International", "90", "8%")
        st.metric("Target PTSI", "85", "25%")
    
    # Detailed Benchmarking
    st.markdown("### 🏆 Best Practice BUMN Indonesia")
    
    tab1, tab2, tab3 = st.tabs(["PT Pertamina", "PT PLN", "PT BULOG"])
    
    with tab1:
        st.markdown("""
        <div class="benchmark-card">
            <h4>🛢️ PT Pertamina (Persero)</h4>
            <p><strong>Model:</strong> Strategic Parent</p>
            <p><strong>Struktur:</strong> Holding company dengan 17+ anak perusahaan</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Key Success Factors:**")
        st.write("""
        - ✅ Board Manual yang komprehensif mengatur hubungan induk-anak perusahaan
        - ✅ Komitmen/hubungan Induk dan Anak Perusahaan yang jelas
        - ✅ Sistem pelaporan terintegrasi
        - ✅ Risk management cascade dari induk ke anak perusahaan
        """)
    
    with tab2:
        st.markdown("""
        <div class="benchmark-card">
            <h4>⚡ PT PLN (Persero)</h4>
            <p><strong>Model:</strong> Integrator Parent</p>
            <p><strong>Struktur:</strong> Multi-business energy holding</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Key Success Factors:**")
        st.write("""
        - ✅ Centralized strategic planning dengan decentralized execution
        - ✅ Shared services untuk fungsi support
        - ✅ Performance management system terintegrasi
        - ✅ Talent mobility antar anak perusahaan
        """)
    
    with tab3:
        st.markdown("""
        <div class="benchmark-card">
            <h4>🌾 PT Perum BULOG</h4>
            <p><strong>Model:</strong> Architect Parent</p>
            <p><strong>Struktur:</strong> Multi-business food security</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Key Success Factors:**")
        st.write("""
        - ✅ Hard Structure: Organ Dewan Pengawas dan Direksi dengan komite pendukung
        - ✅ Soft Structure: Code of Corporate Governance, Board Manual, SOP terintegrasi
        - ✅ Whistleblowing System (WBS) group-wide
        - ✅ Asesmen GCG berkelanjutan
        """)
    
    # International Best Practices
    st.markdown("### 🌍 International Best Practice")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="benchmark-card">
            <h4>🏭 General Electric (GE)</h4>
            <p><strong>Corporate Parenting Excellence:</strong> Talent development dan performance management</p>
            <p><strong>Key Innovation:</strong> GE Leadership Development sebagai competitive advantage</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="benchmark-card">
            <h4>💼 Berkshire Hathaway</h4>
            <p><strong>Corporate Parenting Model:</strong> Investor Parent</p>
            <p><strong>Key Feature:</strong> Minimal interference dengan strong financial oversight</p>
        </div>
        """, unsafe_allow_html=True)

def show_gap_analysis():
    st.markdown("""
    <div class="section-header">
        <h2>🔍 Gap Analysis Pedoman Eksisting PTSI</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Gap Analysis Chart
    df_gap = get_gap_analysis_data()
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Current Score',
        x=df_gap['Area'],
        y=df_gap['Current Score'],
        marker_color='#ff7f7f'
    ))
    fig.add_trace(go.Bar(
        name='Target Score',
        x=df_gap['Area'],
        y=df_gap['Target Score'],
        marker_color='#2a5298'
    ))
    
    fig.update_layout(
        title="Gap Analysis: Current vs Target Performance",
        xaxis_title="Area Tata Kelola",
        yaxis_title="Score",
        barmode='group',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed Gap Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📋 Struktur Governance Saat Ini")
        st.write("""
        - **Status:** Anak perusahaan PT Biro Klasifikasi Indonesia (Persero)
        - **Holding:** Bagian dari IDSurvey sejak 2021
        - **Anak Perusahaan:** PT Surveyor Carbon Consulting Indonesia (SCCI) - 100% ownership
        """)
    
    with col2:
        st.markdown("### ⚠️ Identifikasi Gap Utama")
        for _, row in df_gap.iterrows():
            st.metric(
                label=row['Area'],
                value=f"{row['Current Score']}%",
                delta=f"Gap: {row['Gap']}%"
            )
    
    # Gap Details
    st.markdown("### 🎯 Area Perbaikan Prioritas")
    
    gap_expander = st.expander("📊 Detail Gap Analysis", expanded=True)
    with gap_expander:
        for _, row in df_gap.iterrows():
            progress = row['Current Score'] / 100
            st.markdown(f"**{row['Area']}**")
            st.progress(progress)
            st.caption(f"Current: {row['Current Score']}% | Target: {row['Target Score']}% | Gap: {row['Gap']}%")
            st.markdown("---")

def show_work_plan():
    st.markdown("""
    <div class="section-header">
        <h2>📅 Rencana Kerja Pelaksanaan Pemutakhiran Pedoman</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Timeline Chart using Gantt-style bar chart
    df_timeline = get_timeline_data()
    
    # Create a Gantt-style chart using bar chart
    fig = go.Figure()
    
    colors = {'Planning': '#ffc107', 'Development': '#17a2b8', 'Implementation': '#28a745'}
    
    for i, row in df_timeline.iterrows():
        fig.add_trace(go.Bar(
            name=row['Phase'],
            x=[row['Duration']],
            y=[row['Phase']],
            orientation='h',
            marker_color=colors.get(row['Status'], '#6c757d'),
            text=row['Duration'],
            textposition='middle center'
        ))
    
    fig.update_layout(
        title="Timeline Implementasi (6 Bulan)",
        xaxis_title="Durasi",
        yaxis_title="Phase",
        height=300,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed Timeline
    tab1, tab2, tab3 = st.tabs(["📋 Tahap Persiapan", "🔧 Tahap Pengembangan", "🚀 Tahap Implementasi"])
    
    with tab1:
        st.markdown("""
        <div class="timeline-item">
            <h4>Bulan 1-2: Tahap Persiapan</h4>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Week 1-2: Diagnostic & Assessment**")
            st.write("""
            **Aktivitas:**
            - Stakeholder mapping dan interview
            - Document review pedoman eksisting
            - Benchmarking study completion
            - Gap analysis detil
            
            **Deliverable:**
            - Assessment report
            - Stakeholder requirement matrix
            - Gap analysis comprehensive
            """)
        
        with col2:
            st.markdown("**Week 3-4: Framework Development**")
            st.write("""
            **Aktivitas:**
            - Corporate Parenting Model selection
            - Governance structure design
            - Decision rights matrix development
            - Performance framework design
            
            **Deliverable:**
            - Conceptual framework
            - Governance blueprint
            - Decision authority matrix
            """)
    
    with tab2:
        st.markdown("""
        <div class="timeline-item">
            <h4>Bulan 3-4: Tahap Pengembangan</h4>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Month 3: Content Development**")
            st.write("""
            **Aktivitas:**
            - Penyusunan draft pedoman baru
            - Policy dan prosedur development
            - Template dan tools creation
            - Stakeholder consultation
            
            **Deliverable:**
            - Draft Pedoman Tata Kelola
            - Policy documents
            - Implementation tools
            """)
        
        with col2:
            st.markdown("**Month 4: Validation & Refinement**")
            st.write("""
            **Aktivitas:**
            - Internal review dan validation
            - Legal compliance check
            - Stakeholder feedback incorporation
            - Final refinement
            
            **Deliverable:**
            - Final Pedoman Tata Kelola
            - Implementation roadmap
            - Training materials
            """)
    
    with tab3:
        st.markdown("""
        <div class="timeline-item">
            <h4>Bulan 5-6: Tahap Implementasi</h4>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Month 5: Rollout Preparation**")
            st.write("""
            **Aktivitas:**
            - Change management planning
            - Training program development
            - Communication strategy implementation
            - System dan process setup
            """)
        
        with col2:
            st.markdown("**Month 6: Implementation & Monitoring**")
            st.write("""
            **Aktivitas:**
            - Formal rollout
            - Training delivery
            - Monitoring dan adjustment
            - Performance tracking setup
            """)

def show_roles_responsibilities():
    st.markdown("""
    <div class="section-header">
        <h2>🤝 Peran dan Tanggung Jawab Induk dan Anak Perusahaan</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #dc3545 0%, #fd7e14 100%); padding: 1.5rem; border-radius: 10px; color: white; margin-bottom: 1rem;">
            <h3>🏢 Perusahaan Induk</h3>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["Strategic", "Governance", "Value Creation"])
        
        with tab1:
            st.markdown("**Strategic Roles:**")
            st.write("""
            - 🎯 **Portfolio Management:** Optimasi portofolio bisnis grup
            - 📊 **Strategic Planning:** Penetapan visi, misi, dan strategi grup
            - 💰 **Resource Allocation:** Alokasi sumber daya optimal
            - 📈 **Performance Oversight:** Monitoring dan evaluasi kinerja
            """)
        
        with tab2:
            st.markdown("**Governance Roles:**")
            st.write("""
            - 👥 **Board Oversight:** Pengawasan melalui board representation
            - 📋 **Policy Setting:** Penetapan kebijakan grup
            - ⚠️ **Risk Management:** Framework manajemen risiko grup
            - ✅ **Compliance Oversight:** Memastikan kepatuhan grup
            """)
        
        with tab3:
            st.markdown("**Value Creation Roles:**")
            st.write("""
            - 🔗 **Synergy Realization:** Identifikasi dan realisasi sinergi
            - 🚀 **Capability Building:** Pengembangan kapabilitas grup
            - 💡 **Knowledge Sharing:** Fasilitasi sharing best practice
            - 🏷️ **Brand Management:** Pengelolaan brand grup
            """)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #007bff 0%, #6610f2 100%); padding: 1.5rem; border-radius: 10px; color: white; margin-bottom: 1rem;">
            <h3>🏬 Anak Perusahaan</h3>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["Operational", "Governance", "Strategic"])
        
        with tab1:
            st.markdown("**Operational Excellence:**")
            st.write("""
            - ⚙️ **Business Operations:** Menjalankan operasi bisnis sesuai standar
            - 🥇 **Market Leadership:** Mencapai posisi kompetitif di pasar
            - 😊 **Customer Satisfaction:** Mempertahankan kepuasan pelanggan
            - 💡 **Innovation:** Mengembangkan inovasi produk/layanan
            """)
        
        with tab2:
            st.markdown("**Governance Compliance:**")
            st.write("""
            - 📊 **Reporting:** Pelaporan berkala sesuai requirement
            - 📋 **Policy Compliance:** Kepatuhan pada kebijakan grup
            - ⚠️ **Risk Management:** Implementasi framework risk management
            - 🔒 **Internal Control:** Penerapan sistem pengendalian internal
            """)
        
        with tab3:
            st.markdown("**Strategic Contribution:**")
            st.write("""
            - 🎯 **Strategy Implementation:** Implementasi strategi grup di level bisnis
            - 🔗 **Synergy Support:** Mendukung inisiatif sinergi grup
            - 💡 **Best Practice Sharing:** Berkontribusi pada knowledge sharing
            - 👥 **Talent Development:** Mengembangkan talent untuk kepentingan grup
            """)

def show_governance_principles():
    st.markdown("""
    <div class="section-header">
        <h2>⚖️ Prinsip Tata Kelola Terintegrasi</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # 5 Prinsip GCG
    st.markdown("### 🏛️ 5 Prinsip Good Corporate Governance")
    
    principles = [
        ("Transparency", "Transparansi", "Information Sharing, Open Communication, Performance Visibility"),
        ("Accountability", "Akuntabilitas", "Clear Roles, Performance Responsibility, Decision Ownership"),
        ("Responsibility", "Responsibilitas", "Stakeholder Care, Sustainable Business, Social Responsibility"),
        ("Independence", "Kemandirian", "Business Autonomy, Decision Independence, Market Responsiveness"),
        ("Fairness", "Kewajaran", "Equal Treatment, Resource Allocation, Opportunity Access")
    ]
    
    cols = st.columns(5)
    for i, (eng, ind, desc) in enumerate(principles):
        with cols[i]:
            st.markdown(f"""
            <div class="principle-card">
                <h4>{eng}</h4>
                <h5>{ind}</h5>
                <p style="font-size: 0.9em;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Detailed Principles
    st.markdown("### 📋 Detail Prinsip Tata Kelola")
    
    tab1, tab2, tab3 = st.tabs(["Unity of Purpose", "Differentiated Management", "Performance Excellence"])
    
    with tab1:
        st.markdown("**🎯 Unity of Purpose**")
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
            - **Alignment:** Keselarasan visi, misi, dan strategi
            - **Coordination:** Koordinasi aktivitas lintas entitas
            """)
        with col2:
            st.write("""
            - **Synergy:** Optimasi sinergi grup
            - **Value Creation:** Fokus pada penciptaan nilai bersama
            """)
    
    with tab2:
        st.markdown("**🔄 Differentiated Management**")
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
            - **Fit for Purpose:** Pendekatan sesuai karakteristik bisnis
            - **Autonomy Balance:** Keseimbangan antara otonomi dan kontrol
            """)
        with col2:
            st.write("""
            - **Local Responsiveness:** Responsif terhadap kondisi lokal
            - **Global Consistency:** Konsistensi standar global
            """)
    
    with tab3:
        st.markdown("**📈 Performance Excellence**")
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
            - **Clear Accountability:** Akuntabilitas yang jelas
            - **Performance Transparency:** Transparansi kinerja
            """)
        with col2:
            st.write("""
            - **Continuous Improvement:** Perbaikan berkelanjutan
            - **Value Optimization:** Optimasi nilai grup
            """)

def show_corporate_parenting():
    st.markdown("""
    <div class="section-header">
        <h2>🎯 Corporate Parenting Model</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Parenting Models Overview
    st.markdown("### 🏗️ 4 Model Corporate Parenting")
    
    models = [
        ("Financial Parent", "Investor Model", "#17a2b8", "Minimal intervention, Financial focus"),
        ("Strategic Parent", "Architect Model", "#28a745", "Strategic guidance, Selective intervention"),
        ("Synergistic Parent", "Integrator Model", "#ffc107", "High integration, Operational synergies"),
        ("Functional Parent", "Service Provider", "#dc3545", "Specialized services, Efficiency focus")
    ]
    
    cols = st.columns(4)
    for i, (name, subtitle, color, desc) in enumerate(models):
        with cols[i]:
            st.markdown(f"""
            <div style="background: {color}; padding: 1.5rem; border-radius: 10px; color: white; text-align: center; margin: 0.5rem 0;">
                <h4>{name}</h4>
                <h6>{subtitle}</h6>
                <p style="font-size: 0.9em;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Fit Assessment Matrix
    st.markdown("### 📊 Fit Assessment Matrix")
    
    df_matrix = get_parenting_matrix_data()
    
    # Create heatmap for fit scores
    fig = px.bar(
        df_matrix, 
        x='Model', 
        y='Fit Score',
        color='Fit Score',
        title="Fit Score untuk PT Surveyor Indonesia",
        color_continuous_scale='RdYlGn'
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed comparison table
    st.markdown("### 📋 Perbandingan Detail Model")
    st.dataframe(df_matrix, use_container_width=True)
    
    # Recommendation
    st.markdown("""
    <div class="recommendation-box">
        <h4>🎯 Rekomendasi untuk PT Surveyor Indonesia</h4>
        <h5><strong>Strategic Parent dengan elemen Synergistic Parent</strong></h5>
        <p>Berdasarkan analisis, model ini paling sesuai karena:</p>
        <ul>
            <li>✅ Strategic Alignment: Sejalan dengan strategi IDSurvey</li>
            <li>✅ Synergy Realization: Optimasi sinergi dalam grup</li>
            <li>✅ Market Competitiveness: Mempertahankan daya saing</li>
            <li>✅ Operational Excellence: Efisiensi operasional</li>
            <li>✅ Risk Management: Manajemen risiko terintegrasi</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def show_implementation():
    st.markdown("""
    <div class="section-header">
        <h2>🚀 Implementation Roadmap</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Implementation phases
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffc107 0%, #fd7e14 100%); padding: 1.5rem; border-radius: 10px; color: white;">
            <h4>🏃‍♂️ Quick Wins</h4>
            <h6>0-3 Months</h6>
            <ul style="color: white;">
                <li>Formalisasi structure governance</li>
                <li>Regular communication forums</li>
                <li>Basic performance reporting</li>
                <li>Decision rights clarity</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #17a2b8 0%, #6610f2 100%); padding: 1.5rem; border-radius: 10px; color: white;">
            <h4>🏗️ Foundation Building</h4>
            <h6>3-12 Months</h6>
            <ul style="color: white;">
                <li>Comprehensive governance manual</li>
                <li>New parenting model implementation</li>
                <li>Shared services establishment</li>
                <li>Talent mobility program</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%); padding: 1.5rem; border-radius: 10px; color: white;">
            <h4>🏆 Excellence Achievement</h4>
            <h6>12-24 Months</h6>
            <ul style="color: white;">
                <li>Advanced analytics & reporting</li>
                <li>Synergy realization tracking</li>
                <li>Best practice standardization</li>
                <li>Continuous improvement culture</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Implementation Progress Tracker
    st.markdown("### 📊 Progress Tracker")
    
    progress_data = {
        'Phase': ['Quick Wins', 'Foundation Building', 'Excellence Achievement'],
        'Progress': [75, 45, 15],
        'Timeline': ['0-3 Months', '3-12 Months', '12-24 Months']
    }
    
    for i, (phase, progress, timeline) in enumerate(zip(progress_data['Phase'], progress_data['Progress'], progress_data['Timeline'])):
        st.markdown(f"**{phase} ({timeline})**")
        st.progress(progress / 100)
        st.caption(f"Progress: {progress}%")
        st.markdown("---")

def show_success_metrics():
    st.markdown("""
    <div class="section-header">
        <h2>📈 Success Metrics</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>📊 Governance Effectiveness</h4>
            <ul style="text-align: left; color: white;">
                <li>Decision speed improvement</li>
                <li>Compliance score enhancement</li>
                <li>Stakeholder satisfaction</li>
                <li>Risk management maturity</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>💰 Financial Performance</h4>
            <ul style="text-align: left; color: white;">
                <li>Revenue growth acceleration</li>
                <li>Cost synergy realization</li>
                <li>ROI improvement</li>
                <li>Cash flow optimization</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h4>🎯 Strategic Impact</h4>
            <ul style="text-align: left; color: white;">
                <li>Market share growth</li>
                <li>Customer satisfaction</li>
                <li>Innovation pipeline</li>
                <li>Talent retention</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Metrics Dashboard
    st.markdown("### 📊 Metrics Dashboard")
    
    # Sample metrics visualization
    metrics_data = {
        'Metric': ['Governance Score', 'Financial Performance', 'Strategic Impact', 'Operational Excellence'],
        'Current': [65, 70, 60, 68],
        'Target': [85, 88, 82, 85],
        'Category': ['Governance', 'Financial', 'Strategic', 'Operational']
    }
    
    df_metrics = pd.DataFrame(metrics_data)
    
    # Create radar chart using graph_objects
    fig = go.Figure()
    
    # Add current performance
    fig.add_trace(go.Scatterpolar(
        r=df_metrics['Current'],
        theta=df_metrics['Metric'],
        fill='toself',
        name='Current',
        fillcolor='rgba(255, 0, 0, 0.3)',
        line_color='red'
    ))
    
    # Add target line
    fig.add_trace(go.Scatterpolar(
        r=df_metrics['Target'],
        theta=df_metrics['Metric'],
        fill='toself',
        name='Target',
        fillcolor='rgba(42, 82, 152, 0.3)',
        line_color='#2a5298'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title="Current Performance vs Target"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # KPI Table
    st.markdown("### 📋 Key Performance Indicators")
    
    kpi_data = {
        'KPI': [
            'Decision Speed Improvement',
            'Compliance Score',
            'Revenue Growth',
            'Cost Synergy Realization',
            'Market Share Growth',
            'Customer Satisfaction',
            'Talent Retention'
        ],
        'Current': ['5 days', '75%', '8%', '2.5%', '12%', '78%', '85%'],
        'Target': ['2 days', '90%', '12%', '5%', '15%', '85%', '90%'],
        'Timeline': ['6 months', '12 months', '12 months', '18 months', '24 months', '12 months', '6 months']
    }
    
    st.dataframe(pd.DataFrame(kpi_data), use_container_width=True)

def show_conclusion():
    st.markdown("""
    <div class="section-header">
        <h2>📋 Kesimpulan dan Next Steps</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Takeaways
    st.markdown("""
    <div class="highlight-box">
        <h3>🎯 Key Takeaways</h3>
        <ol>
            <li><strong>Strategic Clarity:</strong> Perlu clarity dalam corporate parenting model</li>
            <li><strong>Governance Excellence:</strong> Focus pada value creation ketimbang compliance</li>
            <li><strong>Synergy Optimization:</strong> Maksimalisasi sinergi dalam IDSurvey ecosystem</li>
            <li><strong>Performance Culture:</strong> Membangun budaya performance excellence</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Next Steps
    st.markdown("""
    <div class="recommendation-box">
        <h3>🚀 Next Steps</h3>
        <ol>
            <li><strong>Approval framework dan approach</strong></li>
            <li><strong>Kick-off implementation team</strong></li>
            <li><strong>Stakeholder engagement intensif</strong></li>
            <li><strong>Pilot implementation untuk selected areas</strong></li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Action Items
    st.markdown("### ✅ Action Items")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Immediate Actions (Next 30 Days):**")
        st.write("""
        - [ ] Finalize governance framework approach
        - [ ] Establish project steering committee
        - [ ] Conduct stakeholder mapping
        - [ ] Develop communication plan
        """)
    
    with col2:
        st.markdown("**Medium-term Actions (Next 90 Days):**")
        st.write("""
        - [ ] Complete detailed gap analysis
        - [ ] Design new governance structure
        - [ ] Develop implementation roadmap
        - [ ] Create change management plan
        """)
    
    # Contact Information
    st.markdown("---")
    st.markdown("### 📞 Contact Information")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **👨‍💼 Narasumber**
        
        M Sopian Hadianto  
        SE, Ak, CA, MM, QIA, GRCP, GRCA, CACP, CCFA, CGP
        
        📧 kim.consulting@email.com
        """)
    
    with col2:
        st.info("""
        **🏢 KIM Consulting**
        
        Tata Kelola Terintegrasi
        
        📧 info@kimconsulting.co.id
        """)
    
    with col3:
        st.info("""
        **🏭 Client**
        
        PT Surveyor Indonesia
        
        📧 corporate@ptsi.co.id
        """)
    
    # Final Disclaimer
    st.markdown("---")
    st.markdown("""
    <div style="background: #fff3cd; padding: 15px; border-radius: 8px; border-left: 4px solid #ffc107; text-align: center;">
        <p style="color: #856404; font-weight: bold; margin: 0;">
        ⚠️ Disclaimer: Materi sosialisasi untuk kalangan terbatas PT Surveyor Indonesia
        </p>
    </div>
    """, unsafe_allow_html=True)

def generate_full_report():
    """Generate full report content for download"""
    return """
PT SURVEYOR INDONESIA
MATERI SOSIALISASI TATA KELOLA HUBUNGAN INDUK DAN ANAK PERUSAHAAN

═══════════════════════════════════════════════════════════════════════

NARASUMBER:
M Sopian Hadianto, SE, Ak, CA, MM, QIA, GRCP, GRCA, CACP, CCFA, CGP

KONSULTAN:
KIM Consulting 2025

DISCLAIMER:
⚠️ Materi sosialisasi untuk kalangan terbatas PT Surveyor Indonesia

═══════════════════════════════════════════════════════════════════════

EXECUTIVE SUMMARY
Sebagai bagian dari transformasi tata kelola PT Surveyor Indonesia dalam era holding IDSurvey, 
diperlukan pemutakhiran pedoman tata kelola hubungan induk dan anak perusahaan yang komprehensif, 
selaras dengan best practices BUMN dan framework Corporate Parenting Model terkini.

REKOMENDASI UTAMA:
1. Adopsi Strategic Parent Model dengan elemen Synergistic
2. Implementasi framework governance terintegrasi
3. Pengembangan sistem performance management cascading
4. Penguatan mekanisme sinergi grup

KEY TAKEAWAYS:
1. Strategic Clarity: Perlu clarity dalam corporate parenting model
2. Governance Excellence: Focus pada value creation ketimbang compliance
3. Synergy Optimization: Maksimalisasi sinergi dalam IDSurvey ecosystem
4. Performance Culture: Membangun budaya performance excellence

NEXT STEPS:
1. Approval framework dan approach
2. Kick-off implementation team
3. Stakeholder engagement intensif
4. Pilot implementation untuk selected areas

═══════════════════════════════════════════════════════════════════════

Generated by PTSI Governance Framework Application
Powered by KIM Consulting 2025
Streamlit Framework | Version 1.0 | August 2025

⚠️ CONFIDENTIAL: Materi sosialisasi untuk kalangan terbatas PT Surveyor Indonesia
"""

def generate_requirements_txt():
    """Generate requirements.txt content"""
    return """streamlit>=1.28.0
plotly>=5.15.0
pandas>=2.0.0
datetime
base64
io
"""

def show_setup_instructions():
    """Show setup and deployment instructions"""
    
    # Speaker and Consultant Info
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px;">
        <h3>👨‍💼 Presenter Information</h3>
        <p><strong>Narasumber:</strong> M Sopian Hadianto, SE, Ak, CA, MM, QIA, GRCP, GRCA, CACP, CCFA, CGP</p>
        <p><strong>Konsultan:</strong> KIM Consulting 2025</p>
        <p><strong>Client:</strong> PT Surveyor Indonesia</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Disclaimer
    st.warning("⚠️ **Disclaimer:** Materi sosialisasi untuk kalangan terbatas PT Surveyor Indonesia")
    
    st.markdown("### 🛠️ Setup Instructions")
    
    st.code("""
# Install dependencies
pip install streamlit plotly pandas

# Run locally
streamlit run main_1.py

# Deploy to Streamlit Cloud
# 1. Push to GitHub
# 2. Connect to share.streamlit.io
# 3. Deploy with auto-sync
    """, language="bash")
    
    st.markdown("### 📄 Requirements.txt")
    requirements_content = generate_requirements_txt()
    st.download_button(
        label="📥 Download requirements.txt",
        data=requirements_content,
        file_name="requirements.txt",
        mime="text/plain"
    )
    
    # App Information
    st.markdown("### 📊 Application Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🎯 Content Features:**
        - 10 comprehensive sections
        - Interactive benchmarking
        - Gap analysis visualization
        - Corporate parenting models
        - Implementation roadmap
        """)
    
    with col2:
        st.markdown("""
        **💻 Technical Features:**
        - Responsive design
        - Interactive charts (Plotly)
        - Download functionality
        - Multi-page navigation
        - Professional styling
        """)
    
    # Deployment Guide
    st.markdown("### ☁️ Deployment to Streamlit Cloud")
    
    st.markdown("""
    **Step-by-step deployment:**
    
    1. **Prepare Repository:**
       - Create GitHub repository
       - Upload `main_1.py`
       - Add `requirements.txt`
    
    2. **Deploy to Streamlit Cloud:**
       - Visit [share.streamlit.io](https://share.streamlit.io)
       - Connect GitHub account
       - Select repository and main file
       - Deploy automatically
    
    3. **Access Application:**
       - Get public URL from Streamlit Cloud
       - Share with PT Surveyor Indonesia team
       - Monitor usage and performance
    """)
    
    # Security Note
    st.markdown("""
    <div style="background: #d1ecf1; padding: 15px; border-radius: 8px; border-left: 4px solid #17a2b8;">
        <h4>🔒 Security Considerations</h4>
        <p>Karena materi ini untuk <strong>kalangan terbatas PT Surveyor Indonesia</strong>, 
        pertimbangkan untuk menggunakan:</p>
        <ul>
            <li>Private GitHub repository</li>
            <li>Password protection pada aplikasi</li>
            <li>Restricted access URL sharing</li>
            <li>Regular monitoring akses aplikasi</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
