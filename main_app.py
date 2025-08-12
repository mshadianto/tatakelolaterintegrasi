import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import base64

# Page config
st.set_page_config(
    page_title="Framework Tata Kelola PT Surveyor Indonesia",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        font-weight: 300;
    }
    .main-header .subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    .best-practice {
        background: #e8f5e8;
        border-left: 4px solid #27ae60;
        padding: 1.5rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    .gap-analysis {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1.5rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    .recommendation {
        background: #d1ecf1;
        border-left: 4px solid #17a2b8;
        padding: 1.5rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    .critical-point {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 1.5rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-left: 4px solid #3498db;
        margin: 1rem 0;
    }
    .timeline-item {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .quick-win {
        border-left: 4px solid #27ae60;
    }
    .medium-term {
        border-left: 4px solid #f39c12;
    }
    .long-term {
        border-left: 4px solid #9b59b6;
    }
    .executive-summary {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 8px;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); padding: 2rem; border-radius: 10px; text-align: center; color: white; margin-bottom: 2rem;">
        <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem; font-weight: 300;">Framework Tata Kelola Hubungan Induk dan Anak Perusahaan</h1>
        <div style="font-size: 1.2rem; opacity: 0.9;">PT Surveyor Indonesia (Persero)</div>
        <div style="font-size: 1.2rem; opacity: 0.9;">Governance, Risk Management & Compliance (GRC)</div>
        <hr style="margin: 1.5rem 0; opacity: 0.3; border: none; height: 1px; background-color: rgba(255,255,255,0.3);">
        <div style="font-size: 1rem; opacity: 0.9;">
            <strong>Narasumber:</strong> M Sopian Hadianto, SE, Ak, MM, CA, GRCP, GRCA, CACP, CCFA, CGP
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar Navigation
    st.sidebar.title("🧭 Navigasi")
    
    # Narasumber info in sidebar
    st.sidebar.markdown("""
    <div style="background-color: #f8f9fa; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; border-left: 4px solid #3498db;">
        <h4 style="margin: 0; color: #2c3e50; font-size: 0.9rem;">👨‍🏫 NARASUMBER</h4>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; color: #34495e; font-weight: 600;">
            M Sopian Hadianto<br>
            <span style="font-size: 0.7rem; opacity: 0.8;">SE, Ak, MM, CA, GRCP, GRCA,<br>CACP, CCFA, CGP</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Disclaimer in sidebar
    st.sidebar.markdown("""
    <div style="background-color: #fff3cd; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; border-left: 4px solid #ffc107;">
        <h4 style="margin: 0; color: #856404; font-size: 0.8rem;">⚠️ DISCLAIMER</h4>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.7rem; color: #856404;">
            Dokumen ini digunakan untuk kalangan terbatas di PT Surveyor Indonesia
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    sections = [
        "Executive Summary",
        "Benchmarking BUMN",
        "Review Eksisting", 
        "Rencana Kerja",
        "Framework Tata Kelola",
        "Prinsip Dasar GCG",
        "Corporate Parenting Model",
        "Implementation Roadmap",
        "Success Metrics",
        "Dashboard Analytics",
        "Conclusion"
    ]
    
    selected_section = st.sidebar.selectbox("Pilih Bagian:", sections)
    
    # KIM Consulting branding in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 1rem; background-color: #2c3e50; color: white; border-radius: 8px;">
        <h4 style="margin: 0; color: #3498db;">KIM Consulting</h4>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; opacity: 0.8;">Professional GRC Advisory Services</p>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.7rem; opacity: 0.6;">© 2025</p>
    </div>
    """, unsafe_allow_html=True)

    # Executive Summary
    if selected_section == "Executive Summary":
        st.markdown("""
        <div class="executive-summary">
            <h2>📋 Executive Summary</h2>
            <p>Dokumen ini menyajikan framework komprehensif untuk pemutakhiran pedoman tata kelola hubungan induk dan anak perusahaan PT Surveyor Indonesia, berdasarkan praktik terbaik BUMN Indonesia dan standar internasional Good Corporate Governance (GCG) serta Governance, Risk Management & Compliance (GRC).</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Target ROI Improvement", "15%", "3% from current")
            st.metric("Compliance Rate Target", "98%", "8% improvement needed")
        
        with col2:
            st.metric("Risk Incident Target", "<5/year", "Current: 12/year")
            st.metric("Board Meeting Attendance", ">95%", "Current: 87%")
        
        with col3:
            st.metric("Cost Synergy Target", "5%", "IDR 2.5B potential")
            st.metric("Revenue Synergy Target", "10%", "IDR 8.3B potential")

        st.markdown("""
        ### 🎯 Key Objectives
        1. **Strengthening Governance Structure** - Formalisasi framework tata kelola anak perusahaan
        2. **Risk Management Integration** - Implementasi enterprise risk management terintegrasi
        3. **Compliance Enhancement** - Alignment dengan Permen BUMN No. PER-2/MBU/03/2023
        4. **Value Creation** - Optimalisasi sinergi antara induk dan anak perusahaan
        """)

    # Benchmarking BUMN
    elif selected_section == "Benchmarking BUMN":
        st.header("🏆 Benchmarking Praktik Terbaik BUMN Indonesia")
        
        tab1, tab2, tab3 = st.tabs(["Perum BULOG", "Holding IDSurvey", "BUMN Konstruksi"])
        
        with tab1:
            st.subheader("Perum BULOG - Model Tata Kelola Terintegrasi")
            
            st.markdown("""
            <div style="background: #e8f5e8; border-left: 4px solid #27ae60; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1rem 0;">
                <h4>🌟 Praktik Unggulan:</h4>
                <ul>
                    <li>Implementasi hard structure dan soft structure GCG yang komprehensif</li>
                    <li>Penggunaan Pedoman Umum Governansi Korporasi Indonesia (PUG-KI) sebagai framework assessment</li>
                    <li>Pembentukan fungsi pembinaan GCG di bawah Sekretaris Perusahaan</li>
                    <li>Sistem pelaporan pelanggaran (Whistleblowing System) yang terintegrasi</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # BULOG Structure Visualization
            fig_bulog = go.Figure(data=go.Sankey(
                node = dict(
                    pad = 15,
                    thickness = 20,
                    line = dict(color = "black", width = 0.5),
                    label = ["Board of Directors", "Hard Structure", "Soft Structure", "Dewan Pengawas", "Komite", "GCG Code", "Board Manual", "SOP", "Code of Conduct"],
                    color = "blue"
                ),
                link = dict(
                    source = [0, 0, 1, 1, 2, 2, 2, 2],
                    target = [1, 2, 3, 4, 5, 6, 7, 8],
                    value = [1, 1, 1, 1, 1, 1, 1, 1]
                )
            ))
            fig_bulog.update_layout(title_text="BULOG Governance Structure", font_size=10)
            st.plotly_chart(fig_bulog, use_container_width=True)
        
        with tab2:
            st.subheader("Holding IDSurvey - Internal Benchmark")
            
            st.markdown("""
            <div style="background: #e8f5e8; border-left: 4px solid #27ae60; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1rem 0;">
                <h4>🔗 Framework Holding Company:</h4>
                <ul>
                    <li>PT Surveyor Indonesia sebagai bagian dari holding IDSurvey bersama PT Sucofindo</li>
                    <li>Implementasi sinergi operasional dan strategic alignment</li>
                    <li>Standardisasi tata kelola di seluruh entitas grup</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # IDSurvey holding structure
            holding_data = {
                'Entity': ['IDSurvey Holding', 'PT Surveyor Indonesia', 'PT Sucofindo', 'PT SCCI'],
                'Revenue (IDR B)': [2.8, 1.2, 1.4, 0.2],
                'Employees': [3500, 1200, 1800, 500],
                'Services': ['Holding Management', 'TIC Services', 'Inspection Services', 'Mining Services']
            }
            
            df_holding = pd.DataFrame(holding_data)
            
            col1, col2 = st.columns(2)
            with col1:
                fig_revenue = px.pie(df_holding, values='Revenue (IDR B)', names='Entity', 
                                   title='Revenue Distribution IDSurvey Group')
                st.plotly_chart(fig_revenue, use_container_width=True)
            
            with col2:
                fig_employees = px.bar(df_holding, x='Entity', y='Employees', 
                                     title='Employee Distribution')
                st.plotly_chart(fig_employees, use_container_width=True)
        
        with tab3:
            st.subheader("BUMN Konstruksi - Subsidiaries Management")
            
            st.markdown("""
            <div style="background: #e8f5e8; border-left: 4px solid #27ae60; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1rem 0;">
                <h4>📚 Pembelajaran Kunci:</h4>
                <ul>
                    <li>Penerapan transaction cost theory untuk optimalisasi kontrol operasional</li>
                    <li>Portfolio management dan sinergi antar anak perusahaan</li>
                    <li>Diversifikasi korporat dengan oversight mechanism yang ketat</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    # Review Eksisting
    elif selected_section == "Review Eksisting":
        st.header("🔍 Review Eksisting Pedoman Tata Kelola")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Kondisi Eksisting PT Surveyor Indonesia")
            
            st.markdown("""
            <div style="background: #e8f5e8; border-left: 4px solid #27ae60; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1rem 0;">
                <h4>🏢 Struktur Anak Perusahaan Saat Ini:</h4>
                <ul>
                    <li><strong>PT Surveyor Carbon Consulting Indonesia (SCCI)</strong> - 99% ownership</li>
                    <li><strong>Struktur kepemilikan:</strong> PT Surveyor Indonesia (99%), Koperasi Surveyor Indonesia (1%)</li>
                    <li><strong>Bisnis focus:</strong> Mining inspection & coal analysis services</li>
                    <li><strong>Established:</strong> 2002 (original JV), 2011 (full ownership)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Ownership structure pie chart
            ownership_data = {'Owner': ['PT Surveyor Indonesia', 'Koperasi Surveyor Indonesia'], 
                            'Percentage': [99, 1]}
            df_ownership = pd.DataFrame(ownership_data)
            
            fig_ownership = px.pie(df_ownership, values='Percentage', names='Owner', 
                                 title='SCCI Ownership Structure')
            st.plotly_chart(fig_ownership, use_container_width=True)
        
        st.subheader("Gap Analysis")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="background: #fff3cd; border-left: 4px solid #ffc107; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1rem 0;">
                <h4>⚠️ Governance Structure Gap</h4>
                <ul>
                    <li>Belum terlihat framework formal untuk subsidiary governance</li>
                    <li>Perlu penguatan oversight mechanism</li>
                    <li>Standardisasi proses pengambilan keputusan strategis</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: #fff3cd; border-left: 4px solid #ffc107; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1rem 0;">
                <h4>🎯 Risk Management Gap</h4>
                <ul>
                    <li>Belum ada framework terintegrasi risk management</li>
                    <li>Perlu implementasi enterprise risk management across subsidiaries</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="background: #fff3cd; border-left: 4px solid #ffc107; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1rem 0;">
                <h4>📋 Compliance Gap</h4>
                <ul>
                    <li>Perlu alignment dengan Peraturan Menteri BUMN No. PER-2/MBU/03/2023</li>
                    <li>Implementasi whistleblowing system yang komprehensif</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    # Rencana Kerja
    elif selected_section == "Rencana Kerja":
        st.header("📅 Rencana Kerja Pelaksanaan Pemutakhiran")
        
        # Interactive timeline
        phases = ["Fase Persiapan", "Fase Pengembangan", "Fase Implementasi"]
        selected_phase = st.selectbox("Pilih Fase:", phases)
        
        if selected_phase == "Fase Persiapan":
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin: 1rem 0; border-left: 4px solid #27ae60;">
                <h3>🚀 Fase Persiapan (Bulan 1-2)</h3>
            </div>
            """, unsafe_allow_html=True)
            
            tab1, tab2, tab3 = st.tabs(["Assessment", "Stakeholder Engagement", "Draft Framework"])
            
            with tab1:
                st.markdown("""
                **📊 Assessment Komprehensif**
                1. Evaluation current subsidiary governance practices
                2. Risk assessment pada seluruh anak perusahaan  
                3. Benchmarking dengan BUMN best practices
                """)
                
                # Progress tracker
                assessment_progress = st.progress(0)
                if st.button("Start Assessment"):
                    for i in range(101):
                        assessment_progress.progress(i)
                    st.success("Assessment completed!")
            
            with tab2:
                st.markdown("""
                **👥 Stakeholder Engagement**
                1. Workshop dengan Direksi dan Komisaris
                2. Focus Group Discussion dengan manajemen anak perusahaan
                3. Konsultasi dengan regulator (Kementerian BUMN)
                """)
                
                stakeholders = ["Direksi", "Komisaris", "Manajemen SCCI", "Kementerian BUMN"]
                engagement_status = {}
                for stakeholder in stakeholders:
                    engagement_status[stakeholder] = st.checkbox(f"Workshop {stakeholder} completed")
            
            with tab3:
                st.markdown("""
                **📝 Penyusunan Draft Framework**
                1. Drafting subsidiary governance charter
                2. Risk management framework design
                3. Compliance monitoring system design
                """)
        
        elif selected_phase == "Fase Pengembangan":
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin: 1rem 0; border-left: 4px solid #f39c12;">
                <h3>🛠️ Fase Pengembangan (Bulan 3-4)</h3>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **📋 Policy Development**
                - Penyusunan Pedoman Tata Kelola Hubungan Induk-Anak Perusahaan
                - Board Manual untuk subsidiary oversight
                - Risk Management Manual terintegrasi
                """)
            
            with col2:
                st.markdown("""
                **💻 System Development**
                - Implementasi reporting system
                - Dashboard monitoring key performance indicators
                - Whistleblowing system establishment
                """)
        
        else:  # Fase Implementasi
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin: 1rem 0; border-left: 4px solid #9b59b6;">
                <h3>🎯 Fase Implementasi (Bulan 5-6)</h3>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **🚀 Rollout Program**
                - Training dan sosialisasi ke seluruh entitas
                - Implementasi system dan procedure
                - Monitoring dan evaluation system activation
                """)
            
            with col2:
                st.markdown("""
                **✅ Quality Assurance**
                - Internal audit subsidiary governance
                - Compliance testing
                - Feedback collection dan improvement
                """)

    # Framework Tata Kelola
    elif selected_section == "Framework Tata Kelola":
        st.header("🏗️ Framework Tata Kelola Hubungan Induk dan Anak Perusahaan")
        
        # Interactive framework visualization
        view_type = st.radio("Pilih Perspektif:", ["Peran Induk Perusahaan", "Peran Anak Perusahaan", "Framework Terintegrasi"])
        
        if view_type == "Peran Induk Perusahaan":
            st.subheader("🏢 Peran dan Tanggung Jawab Perusahaan Induk")
            
            role_type = st.selectbox("Pilih Kapasitas:", ["Sebagai Pemegang Saham", "Sebagai Entitas Pengendali"])
            
            if role_type == "Sebagai Pemegang Saham":
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown("""
                    <div style="background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #3498db; margin: 1rem 0;">
                        <h4>🎯 Strategic Oversight</h4>
                        <ul>
                            <li>Menetapkan strategic direction dan business portfolio</li>
                            <li>Approval terhadap corporate strategy anak perusahaan</li>
                            <li>Investment decision dan capital allocation</li>
                            <li>Monitoring strategic performance indicators</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown("""
                    <div style="background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #3498db; margin: 1rem 0;">
                        <h4>👨‍💼 Governance Oversight</h4>
                        <ul>
                            <li>Appointment dan evaluation of subsidiary board members</li>
                            <li>Approval corporate governance framework anak perusahaan</li>
                            <li>Oversight compliance dengan regulatory requirements</li>
                            <li>Risk management framework implementation</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown("""
                    <div style="background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #3498db; margin: 1rem 0;">
                        <h4>💰 Value Creation</h4>
                        <ul>
                            <li>Synergy identification dan realization</li>
                            <li>Resource sharing dan optimization</li>
                            <li>Best practice sharing across subsidiaries</li>
                            <li>Innovation dan digital transformation coordination</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
            
            else:  # Sebagai Entitas Pengendali
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown("""
                    <div class="metric-card">
                        <h4>⚙️ Operational Control</h4>
                        <ul>
                            <li>Establishment of management reporting systems</li>
                            <li>Performance monitoring dan evaluation</li>
                            <li>Resource allocation optimization</li>
                            <li>Operational synergy implementation</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown("""
                    <div class="metric-card">
                        <h4>🛡️ Risk Management Control</h4>
                        <ul>
                            <li>Enterprise risk management coordination</li>
                            <li>Risk appetite setting dan monitoring</li>
                            <li>Crisis management coordination</li>
                            <li>Business continuity planning</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown("""
                    <div class="metric-card">
                        <h4>📊 Compliance Control</h4>
                        <ul>
                            <li>Regulatory compliance monitoring</li>
                            <li>Internal audit coordination</li>
                            <li>External audit oversight</li>
                            <li>Reporting standardization</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
        
        elif view_type == "Peran Anak Perusahaan":
            st.subheader("🏭 Peran dan Tanggung Jawab Anak Perusahaan")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                <div class="metric-card">
                    <h4>🎯 Operational Excellence</h4>
                    <ul>
                        <li>Execution of approved business strategy</li>
                        <li>Achievement of agreed performance targets</li>
                        <li>Operational efficiency optimization</li>
                        <li>Customer satisfaction maintenance</li>
                        <li>Financial performance delivery</li>
                        <li>Cash flow management</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="metric-card">
                    <h4>📋 Governance Compliance</h4>
                    <ul>
                        <li>Independent decision making within approved framework</li>
                        <li>Compliance dengan parent company policies</li>
                        <li>Regular reporting to parent company</li>
                        <li>Stakeholder management</li>
                        <li>Risk identification dan mitigation</li>
                        <li>Incident reporting dan management</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        
        else:  # Framework Terintegrasi
            # Interactive org chart
            st.subheader("🔗 Framework Terintegrasi")
            
            # Create interactive organizational chart
            fig_org = go.Figure(data=go.Sankey(
                node = dict(
                    pad = 15,
                    thickness = 20,
                    line = dict(color = "black", width = 0.5),
                    label = ["PT Surveyor Indonesia", "Strategic Oversight", "Governance Oversight", 
                            "Value Creation", "PT SCCI", "Operational Excellence", "Governance Compliance"],
                    color = ["blue", "green", "green", "green", "orange", "red", "red"]
                ),
                link = dict(
                    source = [0, 0, 0, 1, 2, 3],
                    target = [1, 2, 3, 4, 4, 4],
                    value = [3, 3, 3, 2, 2, 2]
                )
            ))
            fig_org.update_layout(title_text="Integrated Governance Framework", font_size=12)
            st.plotly_chart(fig_org, use_container_width=True)

    # Prinsip Dasar GCG
    elif selected_section == "Prinsip Dasar GCG":
        st.header("⚖️ Prinsip Dasar Tata Kelola Terintegrasi")
        
        # Interactive principle selector
        principle_category = st.selectbox("Pilih Kategori:", 
                                        ["Prinsip Hubungan Induk-Anak", "Lima Prinsip GCG BUMN", "GRC Integration"])
        
        if principle_category == "Prinsip Hubungan Induk-Anak":
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                <div class="best-practice">
                    <h4>🔗 Prinsip Sinergi</h4>
                    <p><strong>Definition:</strong> Optimalisasi value creation melalui koordinasi strategis dan operasional antara induk dan anak perusahaan.</p>
                    <ul>
                        <li>Strategic alignment pada business portfolio</li>
                        <li>Resource sharing untuk cost optimization</li>
                        <li>Knowledge sharing untuk capability enhancement</li>
                        <li>Joint initiative untuk market expansion</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                <div class="best-practice">
                    <h4>🏛️ Prinsip Subsidiaritas</h4>
                    <p><strong>Definition:</strong> Delegation of decision-making authority ke level yang paling dekat dengan operasi, sambil mempertahankan strategic control.</p>
                    <ul>
                        <li>Clear delegation of authority matrix</li>
                        <li>Decentralized operational decision making</li>
                        <li>Centralized strategic decision making</li>
                        <li>Balanced autonomy dan accountability</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="best-practice">
                    <h4>🌐 Prinsip Transparansi</h4>
                    <p><strong>Definition:</strong> Keterbukaan informasi dan komunikasi yang efektif antara semua stakeholders.</p>
                    <ul>
                        <li>Regular dan comprehensive reporting</li>
                        <li>Open communication channels</li>
                        <li>Clear governance documentation</li>
                        <li>Stakeholder engagement programs</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                <div class="best-practice">
                    <h4>🎯 Prinsip Akuntabilitas</h4>
                    <p><strong>Definition:</strong> Pertanggungjawaban yang jelas untuk setiap level manajemen dalam mencapai objectives.</p>
                    <ul>
                        <li>Clear performance metrics dan targets</li>
                        <li>Regular performance review dan evaluation</li>
                        <li>Consequence management untuk achievement/non-achievement</li>
                        <li>Continuous improvement culture</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        
        elif principle_category == "Lima Prinsip GCG BUMN":
            # GCG Principles Radar Chart
            principles = ['Transparansi', 'Akuntabilitas', 'Responsibilitas', 'Independensi', 'Kewajaran']
            current_score = [3.2, 3.5, 3.8, 3.1, 3.6]
            target_score = [4.5, 4.5, 4.5, 4.5, 4.5]
            
            fig_radar = go.Figure()
            
            fig_radar.add_trace(go.Scatterpolar(
                r=current_score,
                theta=principles,
                fill='toself',
                name='Current Score',
                line_color='blue'
            ))
            
            fig_radar.add_trace(go.Scatterpolar(
                r=target_score,
                theta=principles,
                fill='toself',
                name='Target Score',
                line_color='red'
            ))
            
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 5]
                    )),
                showlegend=True,
                title="GCG Principles Assessment"
            )
            
            st.plotly_chart(fig_radar, use_container_width=True)
            
            # Detailed explanation
            selected_principle = st.selectbox("Pilih Prinsip untuk Detail:", principles)
            
            principle_details = {
                'Transparansi': "Disclosure of material information, Open communication dengan stakeholders, Clear reporting mechanisms, Public accountability",
                'Akuntabilitas': "Clear roles dan responsibilities, Performance measurement systems, Regular evaluation dan review, Corrective action implementation",
                'Responsibilitas': "Compliance dengan laws dan regulations, Social dan environmental responsibility, Stakeholder consideration, Sustainable business practices",
                'Independensi': "Independent decision making, Avoidance of conflicts of interest, Objective business judgment, Professional board composition",
                'Kewajaran': "Equal treatment of stakeholders, Fair business practices, Equitable resource allocation, Balanced interest consideration"
            }
            
            st.markdown(f"""
            <div class="recommendation">
                <h4>{selected_principle}</h4>
                <p>{principle_details[selected_principle]}</p>
            </div>
            """, unsafe_allow_html=True)
        
        else:  # GRC Integration
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <div class="metric-card">
                    <h4>🏛️ Governance Component</h4>
                    <ul>
                        <li>Board effectiveness dan oversight</li>
                        <li>Management accountability</li>
                        <li>Strategic decision making</li>
                        <li>Stakeholder engagement</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="metric-card">
                    <h4>🛡️ Risk Management Component</h4>
                    <ul>
                        <li>Enterprise risk management framework</li>
                        <li>Risk identification dan assessment</li>
                        <li>Risk mitigation dan monitoring</li>
                        <li>Risk reporting dan communication</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                <div class="metric-card">
                    <h4>📋 Compliance Component</h4>
                    <ul>
                        <li>Regulatory compliance monitoring</li>
                        <li>Policy compliance enforcement</li>
                        <li>Audit dan assurance programs</li>
                        <li>Violation reporting dan remediation</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

    # Corporate Parenting Model
    elif selected_section == "Corporate Parenting Model":
        st.header("👨‍👩‍👧‍👦 Corporate Parenting Model")
        
        # Interactive model selector
        model_view = st.radio("Pilih View:", ["Model Comparison", "Decision Matrix", "Recommendation"])
        
        if model_view == "Model Comparison":
            parenting_models = ["Financial Control", "Strategic Control", "Strategic Planning", "Synergistic"]
            selected_model = st.selectbox("Pilih Model untuk Detail:", parenting_models)
            
            model_details = {
                "Financial Control": {
                    "karakteristik": "Focus pada financial performance, Minimal operational intervention, Decentralized decision making, Performance-based management",
                    "aplikasi": "Suitable untuk anak perusahaan dengan mature business model, Emphasis pada ROI dan profitability targets, Quarterly financial review dan monitoring",
                    "color": "#e74c3c"
                },
                "Strategic Control": {
                    "karakteristik": "Balance antara strategic guidance dan operational autonomy, Strategic planning coordination, Resource allocation oversight, Performance monitoring dengan strategic context",
                    "aplikasi": "Ideal untuk current situation dengan SCCI, Strategic alignment dalam survey dan inspection services, Coordinated market approach dan business development",
                    "color": "#f39c12"
                },
                "Strategic Planning": {
                    "karakteristik": "High level strategic integration, Centralized strategic planning, Coordinated resource allocation, Integrated performance management",
                    "aplikasi": "Future model untuk expanded subsidiary portfolio, Integrated service offering across entities, Coordinated innovation dan digital transformation",
                    "color": "#2ecc71"
                },
                "Synergistic": {
                    "karakteristik": "Maximum value creation melalui synergies, High level coordination dan integration, Shared resources dan capabilities, Joint strategic initiatives",
                    "aplikasi": "Long-term aspiration untuk IDSurvey holding, Integration dengan PT Sucofindo untuk comprehensive service portfolio, Shared technology platform dan expertise",
                    "color": "#9b59b6"
                }
            }
            
            st.markdown(f"""
            <div class="metric-card" style="border-left-color: {model_details[selected_model]['color']}">
                <h4>{selected_model} Model</h4>
                <p><strong>Karakteristik:</strong> {model_details[selected_model]['karakteristik']}</p>
                <p><strong>Aplikasi di PT Surveyor Indonesia:</strong> {model_details[selected_model]['aplikasi']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        elif model_view == "Decision Matrix":
            # Interactive decision matrix
            criteria_weights = {
                "Business Maturity": st.slider("Business Maturity Weight (%)", 0, 50, 25),
                "Synergy Potential": st.slider("Synergy Potential Weight (%)", 0, 50, 30),
                "Parent Expertise": st.slider("Parent Expertise Weight (%)", 0, 50, 20),
                "Resource Requirements": st.slider("Resource Requirements Weight (%)", 0, 30, 15),
                "Risk Profile": st.slider("Risk Profile Weight (%)", 0, 20, 10)
            }
            
            # Normalize weights to 100%
            total_weight = sum(criteria_weights.values())
            if total_weight != 100:
                st.warning(f"Total weight: {total_weight}%. Please adjust to 100%.")
            
            # Decision matrix data
            matrix_data = {
                'Criteria': list(criteria_weights.keys()),
                'Weight': [f"{w}%" for w in criteria_weights.values()],
                'Financial Control': ['High', 'Low', 'Low', 'Low', 'High'],
                'Strategic Control': ['Medium', 'Medium', 'High', 'Medium', 'Medium'],
                'Strategic Planning': ['Low', 'High', 'High', 'High', 'Low'],
                'Synergistic': ['Medium', 'Very High', 'Very High', 'Very High', 'Medium']
            }
            
            df_matrix = pd.DataFrame(matrix_data)
            st.dataframe(df_matrix, use_container_width=True)
            
            # Calculate scores (simplified)
            score_mapping = {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4}
            
            scores = {}
            for model in ['Financial Control', 'Strategic Control', 'Strategic Planning', 'Synergistic']:
                weighted_score = 0
                for i, criteria in enumerate(criteria_weights.keys()):
                    score = score_mapping[matrix_data[model][i]]
                    weight = criteria_weights[criteria] / 100
                    weighted_score += score * weight
                scores[model] = round(weighted_score, 2)
            
            # Visualize scores
            fig_scores = px.bar(
                x=list(scores.keys()), 
                y=list(scores.values()),
                title="Parenting Model Scores",
                labels={'x': 'Model', 'y': 'Weighted Score'}
            )
            st.plotly_chart(fig_scores, use_container_width=True)
        
        else:  # Recommendation
            st.markdown("""
            <div class="recommendation">
                <h4>🎯 Rekomendasi untuk PT Surveyor Indonesia</h4>
                <p><strong>Strategic Control Model</strong> merupakan pilihan optimal untuk implementasi immediate, dengan pertimbangan:</p>
                <ul>
                    <li>Balance antara strategic guidance dan operational autonomy untuk SCCI</li>
                    <li>Strategic alignment dalam survey dan inspection services</li>
                    <li>Coordinated market approach dan business development</li>
                    <li>Preparation untuk evolusi ke model yang lebih sophisticated</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # Evolution roadmap
            st.subheader("🛣️ Evolution Roadmap")
            
            roadmap_data = {
                'Phase': ['Current (2025)', 'Short Term (2026)', 'Medium Term (2027-2028)', 'Long Term (2029+)'],
                'Model': ['Ad-hoc', 'Strategic Control', 'Strategic Planning', 'Synergistic'],
                'Focus': ['Basic oversight', 'Strategic alignment', 'Integrated planning', 'Full synergy'],
                'Investment': ['Low', 'Medium', 'High', 'Very High']
            }
            
            df_roadmap = pd.DataFrame(roadmap_data)
            st.dataframe(df_roadmap, use_container_width=True)

    # Implementation Roadmap
    elif selected_section == "Implementation Roadmap":
        st.header("🗺️ Implementation Roadmap")
        
        # Interactive timeline
        timeline_view = st.selectbox("Pilih Timeline View:", ["Overview", "Detailed Phase", "Progress Tracker"])
        
        if timeline_view == "Overview":
            # Gantt-like chart
            phases_data = {
                'Phase': ['Quick Wins', 'Medium Term', 'Long Term'],
                'Start': ['2025-01', '2025-07', '2026-07'],
                'Duration': [6, 12, 18],
                'Progress': [25, 10, 0]
            }
            
            fig_timeline = px.timeline(
                phases_data,
                x_start='Start',
                x_end=None,  # Will be calculated
                y='Phase',
                title='Implementation Timeline Overview'
            )
            st.plotly_chart(fig_timeline, use_container_width=True)
            
            # Progress overview
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Quick Wins Progress", "25%", "On track")
                st.progress(0.25)
            
            with col2:
                st.metric("Medium Term Progress", "10%", "Planning phase")
                st.progress(0.10)
            
            with col3:
                st.metric("Long Term Progress", "0%", "Not started")
                st.progress(0.0)
        
        elif timeline_view == "Detailed Phase":
            phase = st.selectbox("Pilih Phase:", ["Quick Wins (0-6 Bulan)", "Medium Term (6-18 Bulan)", "Long Term (18-36 Bulan)"])
            
            if phase == "Quick Wins (0-6 Bulan)":
                st.markdown("""
                <div class="timeline-item quick-win">
                    <h3>🚀 Quick Wins (0-6 Bulan)</h3>
                </div>
                """, unsafe_allow_html=True)
                
                quick_wins = [
                    "Governance Structure Enhancement",
                    "Reporting System Improvement", 
                    "Risk Management Foundation"
                ]
                
                for i, item in enumerate(quick_wins):
                    with st.expander(f"{i+1}. {item}"):
                        if item == "Governance Structure Enhancement":
                            st.write("""
                            - Formalisasi subsidiary board composition
                            - Implementation of regular board meetings
                            - Establishment of audit committee di SCCI
                            """)
                        elif item == "Reporting System Improvement":
                            st.write("""
                            - Monthly financial dan operational reporting
                            - Quarterly strategic review meetings
                            - Annual subsidiary performance evaluation
                            """)
                        else:
                            st.write("""
                            - Risk register establishment
                            - Basic risk monitoring procedures
                            - Incident reporting system
                            """)
            
            elif phase == "Medium Term (6-18 Bulan)":
                st.markdown("""
                <div class="timeline-item medium-term">
                    <h3>🛠️ Medium Term Initiatives (6-18 Bulan)</h3>
                </div>
                """, unsafe_allow_html=True)
                
                # Implementation checklist
                medium_tasks = [
                    "Policy Framework Development",
                    "System Integration",
                    "Capability Building"
                ]
                
                for task in medium_tasks:
                    completed = st.checkbox(f"✅ {task}")
                    if completed:
                        st.success(f"{task} marked as completed!")
            
            else:  # Long Term
                st.markdown("""
                <div class="timeline-item long-term">
                    <h3>🎯 Long Term Vision (18-36 Bulan)</h3>
                </div>
                """, unsafe_allow_html=True)
                
                long_term_initiatives = [
                    "Advanced Analytics Implementation",
                    "Portfolio Optimization",
                    "Digital Transformation"
                ]
                
                for initiative in long_term_initiatives:
                    st.info(f"🔮 {initiative} - Planning phase")
        
        else:  # Progress Tracker
            st.subheader("📊 Progress Tracker")
            
            # Overall progress
            overall_progress = st.progress(0)
            overall_percentage = 15  # Example
            overall_progress.progress(overall_percentage / 100)
            st.write(f"Overall Implementation Progress: {overall_percentage}%")
            
            # Detailed progress by category
            categories = ["Governance", "Risk Management", "Compliance", "Technology", "Training"]
            progress_data = [20, 15, 10, 8, 12]
            
            fig_progress = px.bar(
                x=categories,
                y=progress_data,
                title="Progress by Category (%)",
                color=progress_data,
                color_continuous_scale='RdYlGn'
            )
            st.plotly_chart(fig_progress, use_container_width=True)

    # Success Metrics
    elif selected_section == "Success Metrics":
        st.header("📈 Success Metrics and KPIs")
        
        metric_category = st.selectbox("Pilih Kategori Metrics:", 
                                     ["Governance Effectiveness", "Financial Performance", "Risk Management", "All Metrics"])
        
        if metric_category == "Governance Effectiveness":
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Board Meeting Attendance Rate", "87%", "Target: >95%", delta="-8%")
                st.metric("Policy Compliance Rate", "92%", "Target: >98%", delta="-6%")
            
            with col2:
                st.metric("Audit Finding Resolution Time", "45 days", "Target: <30 days", delta="15 days")
                st.metric("Stakeholder Satisfaction Index", "3.7/5.0", "Target: >4.0/5.0", delta="-0.3")
            
            # Governance metrics trend
            governance_trend_data = {
                'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                'Attendance': [82, 85, 87, 89, 87, 87],
                'Compliance': [88, 90, 91, 92, 92, 92],
                'Satisfaction': [3.5, 3.6, 3.6, 3.7, 3.7, 3.7]
            }
            
            df_gov_trend = pd.DataFrame(governance_trend_data)
            
            fig_gov = px.line(df_gov_trend, x='Month', y=['Attendance', 'Compliance'], 
                            title='Governance Metrics Trend')
            st.plotly_chart(fig_gov, use_container_width=True)
        
        elif metric_category == "Financial Performance":
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Subsidiary ROI", "12%", "Target: >15%", delta="-3%")
                st.metric("Cost Synergy Realization", "2%", "Target: 5%", delta="-3%")
            
            with col2:
                st.metric("Revenue Synergy Achievement", "5%", "Target: 10%", delta="-5%")
                st.metric("Cash Flow Optimization", "8%", "Target: 15%", delta="-7%")
            
            # Financial performance simulation
            st.subheader("💰 Financial Impact Simulation")
            
            synergy_slider = st.slider("Cost Synergy Achievement (%)", 0, 10, 2)
            revenue_slider = st.slider("Revenue Synergy Achievement (%)", 0, 15, 5)
            
            # Calculate impact
            base_revenue = 1200  # IDR Billion
            base_cost = 1000    # IDR Billion
            
            cost_saving = base_cost * (synergy_slider / 100)
            revenue_increase = base_revenue * (revenue_slider / 100)
            
            st.write(f"💰 Estimated Cost Saving: IDR {cost_saving:.1f} Billion")
            st.write(f"📈 Estimated Revenue Increase: IDR {revenue_increase:.1f} Billion")
            st.write(f"🎯 Total Financial Impact: IDR {cost_saving + revenue_increase:.1f} Billion")
        
        elif metric_category == "Risk Management":
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Risk Incident Frequency", "12/year", "Target: <5/year", delta="7 incidents")
                st.metric("Risk Mitigation Effectiveness", "75%", "Target: >90%", delta="-15%")
            
            with col2:
                st.metric("Compliance Violations", "3 incidents", "Target: 0", delta="3 incidents")
                st.metric("Business Continuity Uptime", "98.5%", "Target: 99.9%", delta="-1.4%")
            
            # Risk heatmap
            risk_categories = ['Operational', 'Financial', 'Compliance', 'Strategic', 'Technology']
            risk_likelihood = [3, 2, 4, 2, 3]
            risk_impact = [4, 4, 5, 3, 3]
            
            fig_risk = px.scatter(
                x=risk_likelihood, 
                y=risk_impact,
                text=risk_categories,
                title='Risk Assessment Heatmap',
                labels={'x': 'Likelihood', 'y': 'Impact'},
                size_max=60
            )
            fig_risk.update_traces(textposition="top center")
            st.plotly_chart(fig_risk, use_container_width=True)
        
        else:  # All Metrics
            # Comprehensive dashboard
            st.subheader("📊 Comprehensive Metrics Dashboard")
            
            # Summary cards
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Overall Score", "78%", "Target: 90%")
            with col2:
                st.metric("Governance Score", "82%", "+2%")
            with col3:
                st.metric("Financial Score", "75%", "-1%")
            with col4:
                st.metric("Risk Score", "77%", "+3%")
            
            # All metrics table
            all_metrics_data = {
                'Category': ['Governance', 'Governance', 'Financial', 'Financial', 'Risk', 'Risk'],
                'Metric': ['Board Attendance', 'Policy Compliance', 'ROI', 'Cost Synergy', 'Incidents', 'Mitigation'],
                'Current': ['87%', '92%', '12%', '2%', '12/year', '75%'],
                'Target': ['>95%', '>98%', '>15%', '5%', '<5/year', '>90%'],
                'Status': ['Below Target', 'Below Target', 'Below Target', 'Below Target', 'Above Target', 'Below Target']
            }
            
            df_all_metrics = pd.DataFrame(all_metrics_data)
            
            # Color code status
            def color_status(val):
                if val == 'Below Target':
                    return 'background-color: #ffebee'
                elif val == 'Above Target':
                    return 'background-color: #fff3e0'
                else:
                    return 'background-color: #e8f5e8'
            
            styled_df = df_all_metrics.style.applymap(color_status, subset=['Status'])
            st.dataframe(styled_df, use_container_width=True)

    # Dashboard Analytics
    elif selected_section == "Dashboard Analytics":
        st.header("📊 Dashboard Analytics")
        
        # Real-time metrics simulation
        st.subheader("🔴 Real-time Monitoring")
        
        # Auto-refresh option
        auto_refresh = st.checkbox("Auto-refresh data (10s)")
        
        if auto_refresh:
            import time
            placeholder = st.empty()
            
            for i in range(10):
                with placeholder.container():
                    # Simulate real-time data
                    import random
                    
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        value = 87 + random.randint(-2, 3)
                        st.metric("Board Attendance", f"{value}%", f"{value-87:+d}%")
                    
                    with col2:
                        value = 92 + random.randint(-1, 2)
                        st.metric("Compliance Rate", f"{value}%", f"{value-92:+d}%")
                    
                    with col3:
                        value = 12 + random.randint(-1, 2)
                        st.metric("ROI", f"{value}%", f"{value-12:+d}%")
                    
                    with col4:
                        value = 12 + random.randint(-3, 1)
                        st.metric("Risk Incidents", f"{value}", f"{value-12:+d}")
                
                time.sleep(1)
        
        # Performance analytics
        st.subheader("📈 Performance Analytics")
        
        # Performance comparison
        performance_data = {
            'Metric': ['Governance', 'Financial', 'Risk', 'Compliance'],
            'Q1 2024': [75, 70, 65, 80],
            'Q2 2024': [80, 72, 70, 85],
            'Q3 2024': [82, 75, 75, 87],
            'Q4 2024': [85, 77, 77, 90],
            'Target': [90, 85, 85, 95]
        }
        
        df_performance = pd.DataFrame(performance_data)
        
        fig_performance = px.line(
            df_performance, 
            x='Metric', 
            y=['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 'Target'],
            title='Quarterly Performance Trend'
        )
        st.plotly_chart(fig_performance, use_container_width=True)
        
        # Predictive analytics
        st.subheader("🔮 Predictive Analytics")
        
        # Simple prediction model
        prediction_horizon = st.slider("Prediction Horizon (months)", 1, 12, 6)
        
        # Generate prediction data
        months = [f"Month {i+1}" for i in range(prediction_horizon)]
        predicted_governance = [85 + i*0.5 for i in range(prediction_horizon)]
        predicted_financial = [77 + i*0.8 for i in range(prediction_horizon)]
        predicted_risk = [77 + i*1.2 for i in range(prediction_horizon)]
        
        prediction_df = pd.DataFrame({
            'Month': months,
            'Governance': predicted_governance,
            'Financial': predicted_financial,
            'Risk': predicted_risk
        })
        
        fig_prediction = px.line(
            prediction_df,
            x='Month',
            y=['Governance', 'Financial', 'Risk'],
            title=f'Performance Prediction - Next {prediction_horizon} Months'
        )
        st.plotly_chart(fig_prediction, use_container_width=True)
        
        # Scenario analysis
        st.subheader("🎭 Scenario Analysis")
        
        scenario = st.selectbox("Select Scenario:", ["Best Case", "Base Case", "Worst Case"])
        
        scenario_multipliers = {
            "Best Case": 1.2,
            "Base Case": 1.0,
            "Worst Case": 0.8
        }
        
        multiplier = scenario_multipliers[scenario]
        
        scenario_data = {
            'Metric': ['Governance Effectiveness', 'Financial Performance', 'Risk Management'],
            'Current': [82, 75, 77],
            f'{scenario} Projection': [82*multiplier, 75*multiplier, 77*multiplier]
        }
        
        df_scenario = pd.DataFrame(scenario_data)
        
        fig_scenario = px.bar(
            df_scenario,
            x='Metric',
            y=[f'{scenario} Projection'],
            title=f'{scenario} Scenario Analysis'
        )
        st.plotly_chart(fig_scenario, use_container_width=True)

    # Conclusion
    elif selected_section == "Conclusion":
        st.header("🎯 Conclusion dan Rekomendasi")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="recommendation">
                <h3>🔑 Key Recommendations:</h3>
                <ol>
                    <li><strong>Immediate Implementation</strong> dari Strategic Control Model untuk SCCI</li>
                    <li><strong>Development</strong> comprehensive subsidiary governance framework</li>
                    <li><strong>Investment</strong> dalam technology platform untuk integrated monitoring</li>
                    <li><strong>Establishment</strong> regular review dan improvement mechanisms</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="best-practice">
                <h3>🌟 Critical Success Factors:</h3>
                <ol>
                    <li><strong>Leadership Commitment</strong> dari top management</li>
                    <li><strong>Clear Communication</strong> strategy implementation</li>
                    <li><strong>Adequate Resource Allocation</strong> untuk system dan capability building</li>
                    <li><strong>Continuous Monitoring</strong> dan improvement culture</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="critical-point">
                <h3>⚠️ Risk Mitigation Strategies:</h3>
                <ol>
                    <li><strong>Change Management</strong> program untuk smooth transition</li>
                    <li><strong>Training dan Development</strong> untuk capability enhancement</li>
                    <li><strong>Phased Implementation</strong> untuk risk minimization</li>
                    <li><strong>Regular Review</strong> untuk course correction</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
        
        # Implementation priority matrix
        st.subheader("📋 Implementation Priority Matrix")
        
        priority_data = {
            'Initiative': ['Board Structure Enhancement', 'Reporting System', 'Risk Framework', 
                          'Policy Development', 'System Integration', 'Digital Transformation'],
            'Impact': [4, 3, 4, 5, 3, 5],
            'Effort': [2, 2, 3, 4, 4, 5],
            'Priority': ['High', 'High', 'Medium', 'Medium', 'Medium', 'Low']
        }
        
        df_priority = pd.DataFrame(priority_data)
        
        fig_priority = px.scatter(
            df_priority,
            x='Effort',
            y='Impact',
            text='Initiative',
            color='Priority',
            size_max=60,
            title='Implementation Priority Matrix'
        )
        fig_priority.update_traces(textposition="top center")
        st.plotly_chart(fig_priority, use_container_width=True)
        
        # Final recommendation
        st.markdown("""
        <div class="executive-summary">
            <h3>🎯 Final Recommendation</h3>
            <p>PT Surveyor Indonesia disarankan untuk mengimplementasikan <strong>Strategic Control Model</strong> sebagai starting point, 
            dengan fokus pada quick wins dalam 6 bulan pertama. Framework ini akan memberikan foundation yang solid untuk 
            evolusi menuju model parenting yang lebih sophisticated seiring dengan pertumbuhan portfolio anak perusahaan.</p>
            
            <p>Investasi pada teknologi dan capability building dalam medium term akan memungkinkan perusahaan untuk 
            mencapai target sinergi IDR 10.8 Billion dalam 3 tahun ke depan, sambil meningkatkan governance effectiveness 
            dan risk management maturity.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Action items
        st.subheader("✅ Next Steps - Action Items")
        
        action_items = [
            "Schedule board workshop untuk framework approval - Week 1",
            "Form implementation steering committee - Week 2", 
            "Conduct subsidiary governance assessment - Month 1",
            "Develop subsidiary governance charter - Month 2",
            "Implement monthly reporting system - Month 3",
            "Launch risk management framework - Month 4"
        ]
        
        for i, item in enumerate(action_items):
            completed = st.checkbox(f"{item}")
            if completed:
                st.success(f"✅ Action item {i+1} completed!")

    # Footer
    st.markdown("---")
    
    # Create footer using columns for better responsiveness
    st.markdown("""
    <div style="background-color: #2c3e50; color: white; border-radius: 8px; padding: 2rem; margin-top: 3rem;">
        <div style="text-align: center; margin-bottom: 2rem;">
            <h4 style="margin: 0; color: white;">Framework Tata Kelola Hubungan Induk dan Anak Perusahaan PT Surveyor Indonesia</h4>
            <p style="margin: 1rem 0; opacity: 0.9;">Dokumen ini merupakan framework komprehensif yang dapat diadaptasi sesuai dengan perkembangan bisnis dan regulasi yang berlaku. Review dan update secara berkala sangat direkomendasikan untuk memastikan relevansi dan efektivitas implementasi.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer information in columns
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.markdown("""
        <div style="background-color: #34495e; padding: 1rem; border-radius: 8px; text-align: center;">
            <h4 style="color: #3498db; margin: 0;">KIM Consulting</h4>
            <p style="color: white; margin: 0.5rem 0; font-size: 0.9rem;">Professional GRC Advisory Services</p>
            <p style="color: #95a5a6; margin: 0; font-size: 0.8rem;">© 2025</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #34495e; padding: 1rem; border-radius: 8px; text-align: center;">
            <h4 style="color: #e67e22; margin: 0;">👨‍🏫 Narasumber</h4>
            <p style="color: white; margin: 0.5rem 0; font-weight: bold;">M Sopian Hadianto</p>
            <p style="color: #95a5a6; margin: 0; font-size: 0.8rem;">SE, Ak, MM, CA, GRCP, GRCA, CACP, CCFA, CGP</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background-color: #e74c3c; padding: 1rem; border-radius: 8px; text-align: center;">
            <h4 style="color: white; margin: 0;">⚠️ DISCLAIMER</h4>
            <p style="color: white; margin: 0.5rem 0; font-size: 0.9rem; font-weight: bold;">Kalangan Terbatas</p>
            <p style="color: #fadbd8; margin: 0; font-size: 0.8rem;">PT Surveyor Indonesia</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()