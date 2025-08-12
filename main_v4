#!/usr/bin/env python3
"""
main_updated.py
Streamlit Application untuk Materi Sosialisasi Tata Kelola Hubungan Induk dan Anak Perusahaan
PT Surveyor Indonesia - Updated dengan Pedoman Eksisting

Berdasarkan: SKD-002/DRU-XII/DPKMR/2023 - Pedoman Tata Kelola Hubungan Induk dan Anak Perusahaan

Untuk menjalankan:
streamlit run main_updated.py
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
    page_title="PTSI Governance Framework - SKD-002",
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
    
    .pedoman-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-left: 4px solid #2a5298;
        margin: 1rem 0;
    }
    
    .unit-kerja-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem;
    }
    
    .bab-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem;
    }
    
    .status-item {
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
    
    .regulatory-box {
        background: #d1ecf1;
        padding: 1rem;
        border-radius: 6px;
        border-left: 4px solid #17a2b8;
        margin: 1rem 0;
    }
    
    .akhlak-card {
        background: linear-gradient(135deg, #dc3545 0%, #fd7e14 100%);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        text-align: center;
        margin: 0.3rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Data functions based on real pedoman
def get_existing_structure_data():
    """Data struktur governance yang sudah ada"""
    return pd.DataFrame({
        'Entitas': ['PT Surveyor Indonesia', 'PT Surveyor Carbon Consulting Indonesia (SCCI)'],
        'Status': ['Anak Perusahaan PT BKI', 'Anak Perusahaan PTSI'],
        'Ownership': ['100% PT BKI (Persero)', '100% PT Surveyor Indonesia'],
        'Governance_Score': [75, 70],
        'Established': ['1985', '2020']
    })

def get_unit_kerja_mapping():
    """Mapping unit kerja berdasarkan pedoman eksisting"""
    return pd.DataFrame({
        'Bab': ['Ketentuan Umum', 'Arah dan Kebijakan', 'Seleksi & Pengangkatan', 'Remunerasi', 
                'RUPS', 'Pendanaan & Investasi', 'Perencanaan', 'Operasional', 'Pelaporan', 
                'Penilaian Kinerja', 'Dividen', 'Restrukturisasi'],
        'Unit_Kerja_Utama': ['SP', 'DPKMR', 'DHC', 'DHC', 'SP', 'DKA', 'DPKMR', 'Multiple', 
                             'DPKMR', 'DPKMR', 'DKA', 'DKA'],
        'Unit_Kerja_Pendukung': ['DPKMR', 'DHC/SP', 'SP', 'SP', 'DPKMR', 'DPKMR', 'DHC', 
                                'SP/SPI/DTI', 'DKA/SP', 'DHC/SP', 'SP', 'SP/DPKMR'],
        'Kompleksitas': ['Medium', 'High', 'High', 'Medium', 'Medium', 'High', 'High', 
                        'Very High', 'Medium', 'High', 'Medium', 'High']
    })

def get_regulatory_basis():
    """Dasar hukum pedoman"""
    return [
        "UU No. 19 Tahun 2003 tentang Badan Usaha Milik Negara",
        "UU No. 40 Tahun 2007 tentang Perseroan Terbatas", 
        "Perpu No. 2 Tahun 2022 tentang Cipta Kerja",
        "PMK BUMN No. PER-04/MBU/2014 tentang Pedoman Penetapan Penghasilan",
        "PMK BUMN No. PER-2/MBU/03/2023 tentang Pedoman Tata Kelola dan Kegiatan Korporasi Signifikan",
        "Anggaran Dasar PT Surveyor Indonesia",
        "RJPP PT Surveyor Indonesia 2020-2024 revisi Covid"
    ]

def get_akhlak_values():
    """Nilai-nilai AKHLAK"""
    return [
        ("Amanah", "Memegang teguh kepercayaan yang diberikan"),
        ("Kompeten", "Terus belajar dan mengembangkan kapabilitas"),
        ("Harmoni", "Saling peduli dan menghargai perbedaan"), 
        ("Loyal", "Berdedikasi dan mengutamakan kepentingan bangsa"),
        ("Adaptif", "Terus berinovasi dan antusias dalam menggerakkan perubahan"),
        ("Kolaboratif", "Membangun kerja sama yang sinergis")
    ]

def get_gap_analysis_current():
    """Gap analysis berdasarkan struktur pedoman yang ada"""
    return pd.DataFrame({
        'Area_Governance': [
            'Ketentuan Umum Tata Kelola',
            'Koordinasi Induk-Anak', 
            'Seleksi & Pengangkatan Organ',
            'Sistem Remunerasi',
            'Pengelolaan RUPS',
            'Perencanaan Terintegrasi',
            'Manajemen Operasional',
            'Sistem Pelaporan',
            'Performance Management',
            'Manajemen Dividen'
        ],
        'Status_Eksisting': [80, 75, 85, 70, 80, 65, 70, 75, 60, 75],
        'Target_Benchmark': [90, 88, 92, 85, 85, 90, 88, 85, 90, 85],
        'Priority_Level': ['Medium', 'High', 'Medium', 'High', 'Medium', 'Very High', 
                          'High', 'Medium', 'Very High', 'Medium']
    })

# Main application
def main():
    load_css()
    
    # Sidebar navigation
    st.sidebar.title("🏢 PTSI Governance Framework")
    st.sidebar.markdown("**SKD-002/DRU-XII/DPKMR/2023**")
    st.sidebar.markdown("---")
    
    # Add document info
    st.sidebar.info("""
    **Dokumen:** SKD-002  
    **Revisi:** 00  
    **Tanggal:** 22 Desember 2023  
    **Status:** Berlaku  
    **Halaman:** 99 halaman
    """)
    
    page = st.sidebar.selectbox(
        "Pilih Halaman:",
        [
            "🏠 Overview Pedoman",
            "📊 Struktur Governance Eksisting", 
            "🔍 Gap Analysis Detail",
            "📋 14 Bab Pedoman",
            "🏗️ Unit Kerja & Tanggung Jawab",
            "⚖️ Dasar Hukum & Regulasi",
            "🎯 Nilai AKHLAK",
            "🔄 Proses Governance",
            "📈 Assessment Current State",
            "🚀 Improvement Opportunities",
            "📊 Implementation Monitoring",
            "📋 Kesimpulan Review"
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
    
    # Main content based on page selection
    try:
        if page == "🏠 Overview Pedoman":
            show_overview_pedoman()
        elif page == "📊 Struktur Governance Eksisting":
            show_struktur_eksisting()
        elif page == "🔍 Gap Analysis Detail":
            show_gap_analysis_detail()
        elif page == "📋 14 Bab Pedoman":
            show_14_bab_pedoman()
        elif page == "🏗️ Unit Kerja & Tanggung Jawab":
            show_unit_kerja()
        elif page == "⚖️ Dasar Hukum & Regulasi":
            show_dasar_hukum()
        elif page == "🎯 Nilai AKHLAK":
            show_nilai_akhlak()
        elif page == "🔄 Proses Governance":
            show_proses_governance()
        elif page == "📈 Assessment Current State":
            show_assessment_current()
        elif page == "🚀 Improvement Opportunities":
            show_improvement_opportunities()
        elif page == "📊 Implementation Monitoring":
            show_implementation_monitoring()
        elif page == "📋 Kesimpulan Review":
            show_kesimpulan_review()
    except Exception as e:
        st.error(f"Error loading page: {str(e)}")
        st.info("Please try refreshing the page or contact support.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; padding: 20px;">
        <p><strong>PT Surveyor Indonesia - SKD-002 Governance Framework Review</strong></p>
        <p><strong>👨‍💼 Narasumber:</strong> M Sopian Hadianto, SE, Ak, CA, MM, QIA, GRCP, GRCA, CACP, CCFA, CGP</p>
        <p><strong>🏢 KIM Consulting 2025</strong></p>
        <p style="font-size: 0.9em; font-style: italic; color: #dc3545;">⚠️ Disclaimer: Materi sosialisasi untuk kalangan terbatas PT Surveyor Indonesia</p>
    </div>
    """, unsafe_allow_html=True)

def show_overview_pedoman():
    st.markdown("""
    <div class="main-header">
        <h1>📋 Review Pedoman Tata Kelola</h1>
        <h2>SKD-002/DRU-XII/DPKMR/2023</h2>
        <h3>Hubungan Perusahaan Induk dan Anak Perusahaan</h3>
        <h4>PT Surveyor Indonesia</h4>
        <br>
        <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin-top: 20px;">
            <h4>👨‍💼 Narasumber:</h4>
            <p style="font-size: 1.1em; font-weight: 500;">M Sopian Hadianto, SE, Ak, CA, MM, QIA, GRCP, GRCA, CACP, CCFA, CGP</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Document Status
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Dokumen", "SKD-002", "Active")
    with col2:
        st.metric("Total Halaman", "99", "Comprehensive")
    with col3:
        st.metric("Tanggal Berlaku", "22 Des 2023", "Current")
    with col4:
        st.metric("Revisi", "00", "First Edition")
    
    # Executive Summary
    st.markdown("""
    <div class="highlight-box">
        <h3>📌 Executive Summary Pedoman Eksisting</h3>
        <p>PT Surveyor Indonesia telah memiliki pedoman tata kelola yang komprehensif dengan 99 halaman 
        yang mengatur 14 aspek utama hubungan induk dan anak perusahaan. Pedoman ini diterbitkan pada 
        22 Desember 2023 sebagai Surat Keputusan Direksi untuk memastikan penerapan Good Corporate 
        Governance yang konsisten dan berkelanjutan.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Features
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="pedoman-card">
            <h4>🎯 Ruang Lingkup Pedoman</h4>
            <ul>
                <li><strong>14 Bab Komprehensif:</strong> Dari ketentuan umum hingga restrukturisasi</li>
                <li><strong>Unit Kerja Mapping:</strong> Pembagian tanggung jawab yang jelas</li>
                <li><strong>Compliance Framework:</strong> Selaras dengan regulasi BUMN</li>
                <li><strong>Operational Excellence:</strong> Fokus pada efektivitas operasional</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="pedoman-card">
            <h4>🏗️ Struktur Governance</h4>
            <ul>
                <li><strong>Perusahaan Induk:</strong> PT Surveyor Indonesia</li>
                <li><strong>Anak Perusahaan:</strong> PT SCCI (100% ownership)</li>
                <li><strong>Holding Structure:</strong> Bagian dari IDSurvey</li>
                <li><strong>Governance Model:</strong> Strategic Parent with GCG principles</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Current Implementation Status
    st.markdown("### 📊 Status Implementasi Current")
    
    # Create status chart
    status_data = pd.DataFrame({
        'Aspek': ['Documentation', 'Structure', 'Process', 'Monitoring', 'Compliance'],
        'Status': [90, 85, 75, 70, 80],
        'Target': [95, 90, 85, 85, 90]
    })
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Current Status', x=status_data['Aspek'], y=status_data['Status'], 
                        marker_color='#2a5298'))
    fig.add_trace(go.Bar(name='Target', x=status_data['Aspek'], y=status_data['Target'], 
                        marker_color='#28a745'))
    
    fig.update_layout(title="Status Implementasi vs Target", barmode='group', height=400)
    st.plotly_chart(fig, use_container_width=True)

def show_struktur_eksisting():
    st.markdown("""
    <div class="section-header">
        <h2>📊 Struktur Governance Eksisting PT Surveyor Indonesia</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Current Structure
    df_structure = get_existing_structure_data()
    
    # Organizational Chart
    st.markdown("### 🏗️ Struktur Organisasi Korporat")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        ```
        PT Biro Klasifikasi Indonesia (Persero)
                        |
                        | 100%
                        ▼
            PT Surveyor Indonesia
                        |
                        | 100%
                        ▼
        PT Surveyor Carbon Consulting Indonesia (SCCI)
        ```
        """)
    
    # Detailed Structure
    st.markdown("### 📋 Detail Struktur Entitas")
    st.dataframe(df_structure, use_container_width=True)
    
    # Organ Perusahaan
    st.markdown("### 👥 Organ Perusahaan")
    
    tab1, tab2, tab3 = st.tabs(["RUPS", "Dewan Komisaris", "Direksi"])
    
    with tab1:
        st.markdown("""
        <div class="pedoman-card">
            <h4>📊 Rapat Umum Pemegang Saham (RUPS)</h4>
            <p><strong>Fungsi:</strong> Organ tertinggi dalam struktur governance</p>
            <p><strong>Kewenangan Utama:</strong></p>
            <ul>
                <li>Penetapan dan perubahan Anggaran Dasar</li>
                <li>Pengangkatan dan pemberhentian Dewan Komisaris dan Direksi</li>
                <li>Pengesahan RJPP dan RKAP</li>
                <li>Pengesahan Laporan Tahunan dan penggunaan laba</li>
                <li>Penetapan remunerasi Dewan Komisaris dan Direksi</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="pedoman-card">
            <h4>👁️ Dewan Komisaris</h4>
            <p><strong>Fungsi:</strong> Pengawasan dan pemberian nasihat</p>
            <p><strong>Tanggung Jawab:</strong></p>
            <ul>
                <li>Pengawasan pelaksanaan pengurusan perusahaan</li>
                <li>Pemberian nasihat kepada Direksi</li>
                <li>Monitoring implementasi GCG</li>
                <li>Oversight terhadap sistem pengendalian internal</li>
                <li>Evaluasi kinerja Direksi</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="pedoman-card">
            <h4>⚙️ Direksi</h4>
            <p><strong>Fungsi:</strong> Pengurusan dan pengelolaan perusahaan</p>
            <p><strong>Tanggung Jawab:</strong></p>
            <ul>
                <li>Pengurusan perusahaan sesuai maksud dan tujuan</li>
                <li>Implementasi strategi dan kebijakan</li>
                <li>Pengelolaan operasional dan bisnis</li>
                <li>Pelaporan kepada Dewan Komisaris dan RUPS</li>
                <li>Memastikan compliance terhadap regulasi</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Current Governance Assessment
    st.markdown("### 📈 Assessment Governance Score")
    
    governance_metrics = pd.DataFrame({
        'Metric': ['Board Effectiveness', 'Transparency', 'Risk Management', 'Performance Management', 'Stakeholder Relations'],
        'Score': [82, 78, 75, 70, 80],
        'Benchmark': [85, 85, 80, 85, 85]
    })
    
    fig = px.radar(
        governance_metrics, 
        r='Score', 
        theta='Metric',
        title="Governance Assessment vs Benchmark",
        range_r=[0, 100]
    )
    fig.add_trace(go.Scatterpolar(
        r=governance_metrics['Benchmark'],
        theta=governance_metrics['Metric'],
        fill='toself',
        name='Benchmark'
    ))
    
    st.plotly_chart(fig, use_container_width=True)

def show_gap_analysis_detail():
    st.markdown("""
    <div class="section-header">
        <h2>🔍 Gap Analysis Detail Berdasarkan Pedoman Eksisting</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Gap Analysis Chart
    df_gap = get_gap_analysis_current()
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Status Eksisting',
        x=df_gap['Area_Governance'],
        y=df_gap['Status_Eksisting'],
        marker_color='#ff7f7f'
    ))
    fig.add_trace(go.Bar(
        name='Target Benchmark',
        x=df_gap['Area_Governance'],
        y=df_gap['Target_Benchmark'],
        marker_color='#2a5298'
    ))
    
    fig.update_layout(
        title="Gap Analysis: Status Eksisting vs Target Benchmark",
        xaxis_title="Area Governance",
        yaxis_title="Score (%)",
        barmode='group',
        height=500,
        xaxis_tickangle=-45
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Priority Matrix
    st.markdown("### 🎯 Priority Matrix Improvement")
    
    # Calculate gap and create priority matrix
    df_gap['Gap'] = df_gap['Target_Benchmark'] - df_gap['Status_Eksisting']
    
    fig_scatter = px.scatter(
        df_gap, 
        x='Status_Eksisting', 
        y='Gap',
        color='Priority_Level',
        size='Gap',
        hover_data=['Area_Governance'],
        title="Priority Matrix: Current Status vs Improvement Gap",
        color_discrete_map={
            'Very High': '#dc3545',
            'High': '#fd7e14', 
            'Medium': '#ffc107'
        }
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Detailed Gap Analysis
    st.markdown("### 📊 Analisis Gap per Area")
    
    for _, row in df_gap.iterrows():
        with st.expander(f"📋 {row['Area_Governance']} - Priority: {row['Priority_Level']}"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Status Eksisting", f"{row['Status_Eksisting']}%")
            with col2:
                st.metric("Target Benchmark", f"{row['Target_Benchmark']}%")
            with col3:
                st.metric("Gap", f"{row['Gap']}%", f"{row['Priority_Level']} Priority")
            
            # Progress bar
            progress = row['Status_Eksisting'] / 100
            st.progress(progress)
            
            # Recommendations based on area
            if 'Perencanaan' in row['Area_Governance']:
                st.markdown("""
                **🔧 Area Improvement:**
                - Integrasi RJPP dan RKAP dengan strategi IDSurvey
                - Penguatan KPI cascading dari induk ke anak perusahaan
                - Implementasi dashboard monitoring real-time
                """)
            elif 'Performance' in row['Area_Governance']:
                st.markdown("""
                **🔧 Area Improvement:**
                - Pengembangan balanced scorecard terintegrasi
                - Penguatan sistem evaluasi kinerja individu dan kolegial
                - Implementasi early warning system
                """)

def show_14_bab_pedoman():
    st.markdown("""
    <div class="section-header">
        <h2>📋 14 Bab Pedoman Tata Kelola (SKD-002)</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Create tabs for each major section
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Bab 1-3: Dasar", "Bab 4-6: Organ", "Bab 7-9: Operasional", 
        "Bab 10-12: Monitoring", "Bab 13-14: Strategis"
    ])
    
    with tab1:
        st.markdown("### 📚 Bab 1-3: Ketentuan Dasar")
        
        chapters_1_3 = [
            ("Bab 1", "Pendahuluan", "Latar belakang, maksud dan tujuan, dasar hukum, ruang lingkup"),
            ("Bab 2", "Ketentuan Umum Tata Kelola", "Prinsip GCG, pendirian anak perusahaan, anggaran dasar, organ perusahaan"),
            ("Bab 3", "Arah dan Kebijakan", "Struktur organisasi, koordinasi dan konsultasi, aksi korporasi, pengawasan, sinergi")
        ]
        
        for bab, title, content in chapters_1_3:
            with st.expander(f"{bab}: {title}"):
                st.markdown(f"""
                <div class="bab-card">
                    <h4>{title}</h4>
                    <p><strong>Konten Utama:</strong> {content}</p>
                </div>
                """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 👥 Bab 4-6: Organ Perusahaan")
        
        chapters_4_6 = [
            ("Bab 4", "Seleksi, Pengangkatan dan Pemberhentian", "Fit and proper test, seleksi komisaris dan direksi, masa jabatan"),
            ("Bab 5", "Remunerasi Direksi, Komisaris dan Komite", "Struktur gaji, tunjangan, fasilitas, tantiem/insentif kinerja"),
            ("Bab 6", "Rapat Umum Pemegang Saham", "RUPS tahunan, RUPS luar biasa, penanggung jawab penyelenggaraan")
        ]
        
        for bab, title, content in chapters_4_6:
            with st.expander(f"{bab}: {title}"):
                st.markdown(f"""
                <div class="bab-card">
                    <h4>{title}</h4>
                    <p><strong>Konten Utama:</strong> {content}</p>
                </div>
                """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### ⚙️ Bab 7-9: Aspek Operasional")
        
        chapters_7_9 = [
            ("Bab 7", "Pendanaan dan Investasi", "Kebijakan pendanaan, pengawasan dan evaluasi, pelaporan investasi"),
            ("Bab 8", "Perencanaan", "RJPP, RKAP, kontrak manajemen dan KPI, RKAT dewan komisaris"),
            ("Bab 9", "Kebijakan Pengelolaan Operasional", "10 area: hukum, SPI, keuangan, SDM, pengadaan, TI, risiko, mutu, K3L, TJSL")
        ]
        
        for bab, title, content in chapters_7_9:
            with st.expander(f"{bab}: {title}"):
                st.markdown(f"""
                <div class="bab-card">
                    <h4>{title}</h4>
                    <p><strong>Konten Utama:</strong> {content}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if "Operasional" in title:
                    st.markdown("**10 Area Kebijakan Operasional:**")
                    operational_areas = [
                        "9.1 Hukum dan Kepatuhan", "9.2 Sistem Pengendalian Internal", 
                        "9.3 Keuangan dan Akuntansi", "9.4 Sumber Daya Manusia",
                        "9.5 Pengadaan Barang & Jasa", "9.6 Sistem Teknologi Informasi",
                        "9.7 Manajemen Risiko", "9.8 Manajemen Mutu",
                        "9.9 K3L", "9.10 Tanggung Jawab Sosial dan Lingkungan"
                    ]
                    
                    cols = st.columns(2)
                    for i, area in enumerate(operational_areas):
                        with cols[i % 2]:
                            st.markdown(f"✅ {area}")
    
    with tab4:
        st.markdown("### 📊 Bab 10-12: Monitoring & Performance")
        
        chapters_10_12 = [
            ("Bab 10", "Pelaporan Anak Perusahaan", "Laporan manajemen, laporan tahunan, laporan tugas pengawasan komisaris"),
            ("Bab 11", "Penilaian Kinerja", "Kinerja komisaris, direksi, operasional, early warning system"),
            ("Bab 12", "Penggunaan Laba Bersih dan Dividen", "Kebijakan dividen, pembagian laba, tinjauan hukum")
        ]
        
        for bab, title, content in chapters_10_12:
            with st.expander(f"{bab}: {title}"):
                st.markdown(f"""
                <div class="bab-card">
                    <h4>{title}</h4>
                    <p><strong>Konten Utama:</strong> {content}</p>
                </div>
                """, unsafe_allow_html=True)
    
    with tab5:
        st.markdown("### 🎯 Bab 13-14: Aspek Strategis")
        
        chapters_13_14 = [
            ("Bab 13", "Restrukturisasi dan Likuidasi", "Restrukturisasi utang dan perusahaan, pembubaran/likuidasi"),
            ("Bab 14", "Penutup", "Ketentuan penutup dan implementasi")
        ]
        
        for bab, title, content in chapters_13_14:
            with st.expander(f"{bab}: {title}"):
                st.markdown(f"""
                <div class="bab-card">
                    <h4>{title}</h4>
                    <p><strong>Konten Utama:</strong> {content}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Summary Statistics
    st.markdown("### 📊 Statistik Pedoman")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Bab", "14", "Comprehensive")
    with col2:
        st.metric("Sub-bab", "50+", "Detailed")
    with col3:
        st.metric("Operational Areas", "10", "Complete")
    with col4:
        st.metric("Implementation Level", "85%", "Active")

def show_unit_kerja():
    st.markdown("""
    <div class="section-header">
        <h2>🏗️ Mapping Unit Kerja dan Tanggung Jawab</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Unit kerja mapping
    df_unit = get_unit_kerja_mapping()
    
    # Visual mapping
    st.markdown("### 🗺️ Unit Kerja Mapping Matrix")
    
    # Create heatmap showing complexity by unit
    unit_complexity = df_unit.groupby('Unit_Kerja_Utama')['Kompleksitas'].apply(
        lambda x: (x == 'Very High').sum() * 4 + (x == 'High').sum() * 3 + (x == 'Medium').sum() * 2
    ).reset_index()
    unit_complexity.columns = ['Unit_Kerja', 'Complexity_Score']
    
    fig = px.bar(
        unit_complexity, 
        x='Unit_Kerja', 
        y='Complexity_Score',
        title="Complexity Score by Unit Kerja",
        color='Complexity_Score',
        color_continuous_scale='Reds'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed unit kerja breakdown
    st.markdown("### 📋 Detail Unit Kerja")
    
    unit_details = {
        'DPKMR': {
            'name': 'Direktorat Perencanaan, Kinerja dan Manajemen Risiko',
            'role': 'Strategic oversight, planning, performance management',
            'key_responsibilities': [
                'Koordinasi arah dan kebijakan anak perusahaan',
                'Penyusunan RJPP dan RKAP',
                'Monitoring dan evaluasi kinerja',
                'Manajemen risiko terintegrasi',
                'Pelaporan manajemen'
            ]
        },
        'DHC': {
            'name': 'Direktorat Human Capital',
            'role': 'Human resources and governance',
            'key_responsibilities': [
                'Seleksi dan pengangkatan organ perusahaan',
                'Manajemen remunerasi',
                'Pengembangan SDM',
                'Tata kelola kepegawaian'
            ]
        },
        'SP': {
            'name': 'Sekretaris Perusahaan',
            'role': 'Corporate governance and compliance',
            'key_responsibilities': [
                'Penerapan GCG',
                'Pengelolaan RUPS',
                'Compliance oversight',
                'Legal and regulatory affairs'
            ]
        },
        'DKA': {
            'name': 'Direktorat Keuangan dan Akuntansi',
            'role': 'Financial management and reporting',
            'key_responsibilities': [
                'Pendanaan dan investasi',
                'Akuntansi dan pelaporan keuangan',
                'Manajemen dividen',
                'Restrukturisasi keuangan'
            ]
        }
    }
    
    for unit_code, details in unit_details.items():
        with st.expander(f"🏢 {unit_code}: {details['name']}"):
            st.markdown(f"**Role:** {details['role']}")
            st.markdown("**Key Responsibilities:**")
            for resp in details['key_responsibilities']:
                st.markdown(f"• {resp}")
    
    # Detailed mapping table
    st.markdown("### 📊 Detailed Mapping Table")
    st.dataframe(df_unit, use_container_width=True)

def show_dasar_hukum():
    st.markdown("""
    <div class="section-header">
        <h2>⚖️ Dasar Hukum dan Regulasi</h2>
    </div>
    """, unsafe_allow_html=True)
    
    regulatory_basis = get_regulatory_basis()
    
    # Regulatory hierarchy
    st.markdown("### 🏛️ Hierarki Regulasi")
    
    hierarchy_levels = [
        ("Undang-Undang", ["UU No. 19/2003 BUMN", "UU No. 40/2007 PT"]),
        ("Peraturan Pemerintah", ["Perpu No. 2/2022 Cipta Kerja"]),
        ("Peraturan Menteri", ["PMK BUMN PER-04/MBU/2014", "PMK BUMN PER-2/MBU/03/2023"]),
        ("Internal Regulations", ["Anggaran Dasar PTSI", "RJPP 2020-2024"])
    ]
    
    for level, regulations in hierarchy_levels:
        st.markdown(f"**📋 {level}:**")
        for reg in regulations:
            st.markdown(f"  • {reg}")
        st.markdown("---")
    
    # Regulatory compliance matrix
    st.markdown("### ✅ Compliance Assessment Matrix")
    
    compliance_data = pd.DataFrame({
        'Regulasi': [
            'UU No. 19/2003 BUMN',
            'UU No. 40/2007 PT', 
            'PMK BUMN PER-04/MBU/2014',
            'PMK BUMN PER-2/MBU/03/2023',
            'Anggaran Dasar PTSI'
        ],
        'Compliance_Level': [90, 95, 85, 80, 95],
        'Risk_Level': ['Low', 'Low', 'Medium', 'Medium', 'Low'],
        'Action_Required': ['Monitor', 'Maintain', 'Improve', 'Enhance', 'Maintain']
    })
    
    # Compliance chart
    fig = px.bar(
        compliance_data, 
        x='Regulasi', 
        y='Compliance_Level',
        color='Risk_Level',
        title="Regulatory Compliance Assessment",
        color_discrete_map={'Low': '#28a745', 'Medium': '#ffc107', 'High': '#dc3545'}
    )
    fig.update_layout(xaxis_tickangle=-45, height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed regulatory requirements
    st.markdown("### 📋 Key Regulatory Requirements")
    
    tab1, tab2, tab3 = st.tabs(["BUMN Regulations", "Corporate Law", "Internal Governance"])
    
    with tab1:
        st.markdown("""
        <div class="regulatory-box">
            <h4>🏛️ BUMN Regulatory Framework</h4>
            <p><strong>UU No. 19/2003:</strong> Fundamental BUMN governance principles</p>
            <p><strong>PMK BUMN Regulations:</strong> Detailed implementation guidelines</p>
            
            <h5>Key Requirements:</h5>
            <ul>
                <li>Board composition and independence requirements</li>
                <li>Performance management and KPI framework</li>
                <li>Risk management and internal control systems</li>
                <li>Transparency and reporting obligations</li>
                <li>Remuneration and incentive structures</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="regulatory-box">
            <h4>⚖️ Corporate Law Framework</h4>
            <p><strong>UU No. 40/2007:</strong> Limited liability company law</p>
            <p><strong>Perpu No. 2/2022:</strong> Job creation law updates</p>
            
            <h5>Key Requirements:</h5>
            <ul>
                <li>Corporate structure and organ functions</li>
                <li>Shareholder rights and RUPS procedures</li>
                <li>Director and commissioner duties</li>
                <li>Financial reporting and audit requirements</li>
                <li>Corporate actions and restructuring</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="regulatory-box">
            <h4>🏢 Internal Governance Framework</h4>
            <p><strong>Anggaran Dasar:</strong> Corporate constitution</p>
            <p><strong>RJPP:</strong> Strategic planning framework</p>
            
            <h5>Key Components:</h5>
            <ul>
                <li>Vision, mission, and strategic objectives</li>
                <li>Organizational structure and authority</li>
                <li>Business scope and operational guidelines</li>
                <li>Performance targets and measurement</li>
                <li>AKHLAK values implementation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def show_nilai_akhlak():
    st.markdown("""
    <div class="section-header">
        <h2>🎯 Nilai-Nilai AKHLAK BUMN</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # AKHLAK values
    akhlak_values = get_akhlak_values()
    
    # Display AKHLAK in cards
    st.markdown("### 🏆 6 Nilai AKHLAK")
    
    cols = st.columns(3)
    for i, (nilai, deskripsi) in enumerate(akhlak_values):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="akhlak-card">
                <h4>{nilai}</h4>
                <p style="font-size: 0.9em;">{deskripsi}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # AKHLAK Implementation Framework
    st.markdown("### 📋 Framework Implementasi AKHLAK")
    
    tab1, tab2, tab3 = st.tabs(["Individual Level", "Team Level", "Organizational Level"])
    
    with tab1:
        st.markdown("**🎯 Implementasi Level Individu**")
        individual_impl = {
            'Amanah': ['Integritas dalam setiap tindakan', 'Komitmen pada janji dan kesepakatan'],
            'Kompeten': ['Continuous learning', 'Skill development'],
            'Harmoni': ['Menghargai perbedaan', 'Komunikasi efektif'],
            'Loyal': ['Dedikasi pada organisasi', 'Mengutamakan kepentingan bersama'],
            'Adaptif': ['Terbuka pada perubahan', 'Inovasi berkelanjutan'],
            'Kolaboratif': ['Kerja sama tim', 'Knowledge sharing']
        }
        
        for nilai, implementasi in individual_impl.items():
            with st.expander(f"✨ {nilai}"):
                for impl in implementasi:
                    st.markdown(f"• {impl}")
    
    with tab2:
        st.markdown("**👥 Implementasi Level Tim**")
        st.markdown("""
        - **Amanah:** Trust building dalam tim
        - **Kompeten:** Collective capability development
        - **Harmoni:** Team synergy dan conflict resolution
        - **Loyal:** Team commitment pada tujuan bersama
        - **Adaptif:** Agile teamwork dan responsiveness
        - **Kolaboratif:** Cross-functional collaboration
        """)
    
    with tab3:
        st.markdown("**🏢 Implementasi Level Organisasi**")
        st.markdown("""
        - **Amanah:** Corporate integrity dan ethical governance
        - **Kompeten:** Organizational learning dan capability building
        - **Harmoni:** Inclusive culture dan stakeholder engagement
        - **Loyal:** Corporate citizenship dan national contribution
        - **Adaptif:** Organizational agility dan digital transformation
        - **Kolaboratif:** Strategic partnerships dan ecosystem building
        """)
    
    # AKHLAK in Governance Context
    st.markdown("### 🏛️ AKHLAK dalam Konteks Tata Kelola")
    
    governance_akhlak = pd.DataFrame({
        'Nilai_AKHLAK': ['Amanah', 'Kompeten', 'Harmoni', 'Loyal', 'Adaptif', 'Kolaboratif'],
        'Governance_Impact': [95, 90, 85, 88, 82, 87],
        'Implementation_Level': [90, 85, 80, 85, 75, 80]
    })
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=governance_akhlak['Governance_Impact'],
        theta=governance_akhlak['Nilai_AKHLAK'],
        fill='toself',
        name='Governance Impact',
        line_color='#2a5298'
    ))
    fig.add_trace(go.Scatterpolar(
        r=governance_akhlak['Implementation_Level'],
        theta=governance_akhlak['Nilai_AKHLAK'],
        fill='toself',
        name='Implementation Level',
        line_color='#28a745'
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        title="AKHLAK Values: Governance Impact vs Implementation"
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_proses_governance():
    st.markdown("""
    <div class="section-header">
        <h2>🔄 Proses Governance Terintegrasi</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Governance process flow
    st.markdown("### 🔄 Alur Proses Governance")
    
    # Process visualization using mermaid-style text
    st.markdown("""
    ```
    RUPS (Pemegang Saham)
            ↓
    Strategic Direction & Oversight
            ↓
    Dewan Komisaris ←→ Direksi
            ↓              ↓
    Monitoring &     Operations &
    Supervision      Management
            ↓              ↓
    Performance Review & Reporting
            ↓
    Accountability & Improvement
    ```
    """)
    
    # Key governance processes
    st.markdown("### ⚙️ Proses Governance Utama")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Planning", "Implementation", "Monitoring", "Improvement"])
    
    with tab1:
        st.markdown("**📋 Strategic Planning Process**")
        planning_steps = [
            ("RJPP Development", "5-year strategic planning with stakeholder input"),
            ("RKAP Preparation", "Annual operational and financial planning"),
            ("KPI Setting", "Performance indicator cascading"),
            ("Budget Allocation", "Resource allocation optimization"),
            ("Risk Assessment", "Integrated risk evaluation")
        ]
        
        for step, description in planning_steps:
            st.markdown(f"""
            <div class="status-item">
                <h5>{step}</h5>
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("**⚡ Implementation Process**")
        impl_areas = [
            ("Strategy Execution", "Implementation of approved strategic initiatives"),
            ("Operational Management", "Day-to-day business operations"),
            ("Compliance Management", "Regulatory and policy compliance"),
            ("Stakeholder Engagement", "Communication with key stakeholders"),
            ("Change Management", "Managing organizational changes")
        ]
        
        for area, description in impl_areas:
            st.markdown(f"**{area}:** {description}")
    
    with tab3:
        st.markdown("**📊 Monitoring & Oversight Process**")
        monitoring_framework = pd.DataFrame({
            'Level': ['Board Oversight', 'Management Monitoring', 'Operational Control'],
            'Frequency': ['Quarterly', 'Monthly', 'Daily/Weekly'],
            'Focus': ['Strategic & Risk', 'Performance & Compliance', 'Operations & Quality'],
            'Tools': ['Board Reports', 'Management Dashboard', 'KPI Tracking']
        })
        
        st.dataframe(monitoring_framework, use_container_width=True)
    
    with tab4:
        st.markdown("**🚀 Continuous Improvement Process**")
        improvement_cycle = [
            "Performance Review → Gap Analysis → Action Planning → Implementation → Monitoring → Review"
        ]
        
        st.markdown("**Improvement Cycle:**")
        st.markdown(improvement_cycle[0])
        
        st.markdown("**Key Improvement Areas:**")
        st.markdown("""
        - Process optimization and automation
        - System integration and digitalization  
        - Capability building and talent development
        - Innovation and best practice adoption
        - Stakeholder satisfaction enhancement
        """)

def show_assessment_current():
    st.markdown("""
    <div class="section-header">
        <h2>📈 Assessment Current State Governance</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Overall assessment scores
    st.markdown("### 🎯 Overall Governance Assessment")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Overall Score", "77%", "+3% YoY")
    with col2:
        st.metric("Compliance", "85%", "+5% YoY")
    with col3:
        st.metric("Effectiveness", "72%", "+2% YoY")
    with col4:
        st.metric("Efficiency", "75%", "+4% YoY")
    
    # Detailed assessment by dimension
    assessment_data = pd.DataFrame({
        'Dimension': [
            'Board Effectiveness',
            'Strategic Planning', 
            'Risk Management',
            'Performance Management',
            'Compliance Management',
            'Stakeholder Relations',
            'Transparency',
            'Accountability'
        ],
        'Current_Score': [78, 72, 75, 68, 85, 74, 80, 76],
        'Target_Score': [85, 85, 82, 80, 90, 82, 88, 85],
        'Trend': ['↑', '→', '↑', '↓', '↑', '↑', '→', '↑']
    })
    
    # Radar chart for assessment
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=assessment_data['Current_Score'],
        theta=assessment_data['Dimension'],
        fill='toself',
        name='Current Score',
        line_color='#ff7f7f'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=assessment_data['Target_Score'],
        theta=assessment_data['Dimension'],
        fill='toself',
        name='Target Score',
        line_color='#2a5298'
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        title="Governance Assessment: Current vs Target"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed assessment table
    st.markdown("### 📊 Detailed Assessment Results")
    st.dataframe(assessment_data, use_container_width=True)
    
    # Strengths and areas for improvement
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: #d4edda; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">
            <h4>💪 Key Strengths</h4>
            <ul>
                <li><strong>Compliance Management (85%):</strong> Strong regulatory adherence</li>
                <li><strong>Transparency (80%):</strong> Good information disclosure</li>
                <li><strong>Board Effectiveness (78%):</strong> Well-functioning board</li>
                <li><strong>Documentation:</strong> Comprehensive 99-page governance manual</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #f8d7da; padding: 15px; border-radius: 8px; border-left: 4px solid #dc3545;">
            <h4>🎯 Areas for Improvement</h4>
            <ul>
                <li><strong>Performance Management (68%):</strong> Need stronger KPI framework</li>
                <li><strong>Strategic Planning (72%):</strong> Enhanced integration required</li>
                <li><strong>Stakeholder Relations (74%):</strong> More proactive engagement</li>
                <li><strong>Risk Management (75%):</strong> Advanced risk analytics needed</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def show_improvement_opportunities():
    st.markdown("""
    <div class="section-header">
        <h2>🚀 Improvement Opportunities</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Priority improvement matrix
    improvement_data = pd.DataFrame({
        'Opportunity': [
            'Digital Governance Platform',
            'Integrated KPI Dashboard', 
            'Risk Analytics Enhancement',
            'Stakeholder Engagement Portal',
            'Automated Reporting System',
            'Board Portal Implementation',
            'ESG Integration Framework',
            'Succession Planning System'
        ],
        'Impact': [90, 85, 80, 75, 85, 70, 88, 82],
        'Effort': [80, 60, 70, 50, 65, 45, 75, 85],
        'Priority': ['High', 'Very High', 'High', 'Medium', 'High', 'Medium', 'High', 'Medium']
    })
    
    # Impact vs Effort matrix
    fig = px.scatter(
        improvement_data,
        x='Effort',
        y='Impact', 
        color='Priority',
        size='Impact',
        hover_data=['Opportunity'],
        title="Improvement Opportunities: Impact vs Effort Matrix",
        color_discrete_map={
            'Very High': '#dc3545',
            'High': '#fd7e14',
            'Medium': '#28a745'
        }
    )
    
    fig.add_hline(y=80, line_dash="dash", line_color="gray", annotation_text="High Impact Threshold")
    fig.add_vline(x=70, line_dash="dash", line_color="gray", annotation_text="High Effort Threshold")
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Quick wins and strategic initiatives
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: #d1ecf1; padding: 15px; border-radius: 8px; border-left: 4px solid #17a2b8;">
            <h4>⚡ Quick Wins (High Impact, Low Effort)</h4>
            <ul>
                <li><strong>Board Portal Implementation:</strong> Digitize board materials and meetings</li>
                <li><strong>Stakeholder Engagement Portal:</strong> Online stakeholder communication</li>
                <li><strong>Automated Reporting:</strong> Streamline routine reports</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #fff3cd; padding: 15px; border-radius: 8px; border-left: 4px solid #ffc107;">
            <h4>🎯 Strategic Initiatives (High Impact, High Effort)</h4>
            <ul>
                <li><strong>Digital Governance Platform:</strong> Comprehensive governance digitalization</li>
                <li><strong>ESG Integration Framework:</strong> Sustainability governance integration</li>
                <li><strong>Succession Planning System:</strong> Leadership pipeline development</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Detailed improvement roadmap
    st.markdown("### 🗺️ Improvement Roadmap")
    
    roadmap_phases = pd.DataFrame({
        'Phase': ['Phase 1 (0-6 months)', 'Phase 2 (6-12 months)', 'Phase 3 (12-18 months)'],
        'Focus': ['Quick Wins & Foundation', 'System Integration', 'Advanced Analytics & AI'],
        'Key_Initiatives': [
            'Board Portal, Stakeholder Portal, Basic Automation',
            'Integrated KPI Dashboard, Digital Governance Platform',
            'Risk Analytics, AI-powered Insights, ESG Framework'
        ],
        'Expected_Impact': ['15-20% improvement', '25-30% improvement', '35-40% improvement']
    })
    
    st.dataframe(roadmap_phases, use_container_width=True)

def show_implementation_monitoring():
    st.markdown("""
    <div class="section-header">
        <h2>📊 Implementation Monitoring Framework</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # KPI Dashboard simulation
    st.markdown("### 📈 Real-time Governance KPI Dashboard")
    
    # Current month metrics
    current_metrics = {
        'Board Meeting Attendance': 95,
        'Policy Compliance Rate': 88,
        'Report Timeliness': 92,
        'Stakeholder Satisfaction': 78,
        'Risk Mitigation Effectiveness': 82
    }
    
    cols = st.columns(5)
    for i, (metric, value) in enumerate(current_metrics.items()):
        with cols[i]:
            delta = f"+{value-75}%" if value > 75 else f"{value-75}%"
            st.metric(metric.replace(' ', '\n'), f"{value}%", delta)
    
    # Monthly trend chart
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    governance_trends = pd.DataFrame({
        'Month': months,
        'Overall_Score': [72, 74, 76, 75, 77, 79],
        'Compliance': [82, 84, 85, 83, 85, 88],
        'Effectiveness': [68, 70, 72, 71, 72, 75]
    })
    
    fig = px.line(
        governance_trends, 
        x='Month', 
        y=['Overall_Score', 'Compliance', 'Effectiveness'],
        title="Governance Performance Trends (6 Months)",
        markers=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Implementation status tracker
    st.markdown("### 🎯 Implementation Status Tracker")
    
    implementation_status = pd.DataFrame({
        'Initiative': [
            'Digital Governance Platform',
            'Integrated KPI Dashboard',
            'Risk Analytics Enhancement', 
            'Board Portal Implementation',
            'ESG Framework Development'
        ],
        'Progress': [25, 60, 40, 80, 15],
        'Status': ['In Progress', 'On Track', 'In Progress', 'Near Completion', 'Planning'],
        'Target_Completion': ['Q4 2025', 'Q2 2025', 'Q3 2025', 'Q1 2025', 'Q4 2025']
    })
    
    # Progress visualization
    fig = px.bar(
        implementation_status,
        x='Initiative',
        y='Progress',
        color='Status',
        title="Implementation Progress by Initiative",
        color_discrete_map={
            'Planning': '#ffc107',
            'In Progress': '#17a2b8', 
            'On Track': '#28a745',
            'Near Completion': '#6f42c1'
        }
    )
    fig.update_layout(xaxis_tickangle=-45, height=400)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Alerts and notifications
    st.markdown("### 🚨 Governance Alerts & Notifications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("**⚠️ Attention Required:**\n- Performance Management KPI below target (68%)\n- Stakeholder engagement survey response rate declining")
    
    with col2:
        st.success("**✅ Positive Trends:**\n- Compliance rate improved to 88%\n- Board meeting attendance at 95%")

def show_kesimpulan_review():
    st.markdown("""
    <div class="section-header">
        <h2>📋 Kesimpulan Review Pedoman Tata Kelola</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Executive summary of findings
    st.markdown("""
    <div class="highlight-box">
        <h3>📌 Executive Summary Review</h3>
        <p>PT Surveyor Indonesia telah memiliki <strong>pedoman tata kelola yang solid dan komprehensif</strong> 
        dengan 99 halaman yang mengatur 14 aspek governance secara detail. Pedoman SKD-002 menunjukkan 
        <strong>komitmen tinggi terhadap good corporate governance</strong> dan compliance dengan regulasi BUMN.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key findings
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: #d4edda; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">
            <h4>💪 Key Strengths Found</h4>
            <ul>
                <li><strong>Comprehensive Coverage:</strong> 14 bab mencakup semua aspek governance</li>
                <li><strong>Clear Structure:</strong> Pembagian tanggung jawab unit kerja yang jelas</li>
                <li><strong>Regulatory Compliance:</strong> Selaras dengan UU BUMN dan PT</li>
                <li><strong>AKHLAK Integration:</strong> Nilai-nilai BUMN terintegrasi</li>
                <li><strong>Operational Detail:</strong> 10 area kebijakan operasional lengkap</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #fff3cd; padding: 15px; border-radius: 8px; border-left: 4px solid #ffc107;">
            <h4>🎯 Enhancement Opportunities</h4>
            <ul>
                <li><strong>Digital Integration:</strong> Leverage teknologi untuk efisiensi</li>
                <li><strong>Performance Analytics:</strong> Enhanced KPI tracking dan analytics</li>
                <li><strong>Stakeholder Engagement:</strong> Proactive stakeholder management</li>
                <li><strong>Risk Intelligence:</strong> Advanced risk analytics dan early warning</li>
                <li><strong>ESG Integration:</strong> Sustainability governance framework</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Overall assessment radar
    st.markdown("### 📊 Overall Assessment Summary")
    
    assessment_summary = pd.DataFrame({
        'Aspect': ['Documentation', 'Structure', 'Process', 'Compliance', 'Implementation', 'Innovation'],
        'Score': [95, 85, 78, 88, 75, 65],
        'Benchmark': [90, 85, 85, 90, 85, 80]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=assessment_summary['Score'],
        theta=assessment_summary['Aspect'],
        fill='toself',
        name='PTSI Current',
        line_color='#2a5298'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=assessment_summary['Benchmark'],
        theta=assessment_summary['Aspect'],
        fill='toself',
        name='Industry Benchmark',
        line_color='#28a745'
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        title="Overall Governance Assessment vs Benchmark"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Recommendations
    st.markdown("### 🚀 Strategic Recommendations")
    
    recommendations = [
        {
            'title': 'Digital Governance Transformation',
            'description': 'Implement digital platforms untuk board management, reporting automation, dan stakeholder engagement',
            'timeline': '6-12 months',
            'impact': 'High'
        },
        {
            'title': 'Enhanced Performance Management',
            'description': 'Develop integrated KPI dashboard dengan real-time monitoring dan predictive analytics',
            'timeline': '3-6 months', 
            'impact': 'Very High'
        },
        {
            'title': 'Risk Intelligence Upgrade',
            'description': 'Implement advanced risk analytics dengan AI-powered early warning systems',
            'timeline': '9-12 months',
            'impact': 'High'
        },
        {
            'title': 'ESG Integration Framework',
            'description': 'Integrate sustainability governance dengan existing framework governance',
            'timeline': '6-9 months',
            'impact': 'Medium'
        }
    ]
    
    for i, rec in enumerate(recommendations, 1):
        st.markdown(f"""
        <div class="pedoman-card">
            <h4>{i}. {rec['title']}</h4>
            <p><strong>Description:</strong> {rec['description']}</p>
            <p><strong>Timeline:</strong> {rec['timeline']} | <strong>Impact:</strong> {rec['impact']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Next steps
    st.markdown("""
    <div style="background: #e2e3e5; padding: 20px; border-radius: 8px; border-left: 4px solid #6c757d;">
        <h4>📋 Immediate Next Steps</h4>
        <ol>
            <li><strong>Stakeholder Alignment:</strong> Present findings kepada leadership team</li>
            <li><strong>Priority Setting:</strong> Finalize improvement priorities berdasarkan impact/effort</li>
            <li><strong>Resource Planning:</strong> Allocate budget dan human resources untuk implementation</li>
            <li><strong>Project Kick-off:</strong> Launch improvement initiatives dengan clear timeline</li>
            <li><strong>Monitoring Setup:</strong> Establish governance KPI dashboard untuk tracking progress</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Final appreciation
    st.markdown("---")
    st.markdown("### 🙏 Appreciation")
    
    st.success("""
    **Terima kasih kepada tim PT Surveyor Indonesia** yang telah mengembangkan pedoman tata kelola 
    yang komprehensif dan menunjukkan komitmen tinggi terhadap good corporate governance. 
    
    Pedoman SKD-002 merupakan **foundation yang sangat solid** untuk transformasi governance 
    menuju digital excellence dan sustainable leadership dalam era IDSurvey.
    """)

if __name__ == "__main__":
    main()
