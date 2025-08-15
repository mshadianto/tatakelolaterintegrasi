<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PT Surveyor Indonesia - Pemutakhiran Pedoman Tata Kelola Terintegrasi</title>
    <style>
        @page {
            size: A4 landscape;
            margin: 0.5in;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.4;
            color: #333;
            background: #f8f9fa;
        }
        
        .slide {
            width: 100%;
            min-height: 100vh;
            padding: 2rem;
            page-break-after: always;
            background: white;
            border: 1px solid #ddd;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .slide:last-child {
            page-break-after: avoid;
        }
        
        .slide-header {
            background: linear-gradient(135deg, #1f4e79 0%, #2c5282 100%);
            color: white;
            padding: 1.5rem;
            margin: -2rem -2rem 2rem -2rem;
            border-radius: 10px 10px 0 0;
        }
        
        .slide-title {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        
        .slide-subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .main-title {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            padding: 3rem;
            margin: -2rem -2rem 2rem -2rem;
            border-radius: 10px 10px 0 0;
        }
        
        .main-title h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .main-title h2 {
            font-size: 1.5rem;
            opacity: 0.9;
            margin-bottom: 0.5rem;
        }
        
        .main-title p {
            font-size: 1rem;
            opacity: 0.8;
        }
        
        .content-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            margin: 1.5rem 0;
        }
        
        .content-grid-three {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 1.5rem;
            margin: 1.5rem 0;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            border-left: 5px solid #3182ce;
            text-align: center;
        }
        
        .metric-card h3 {
            color: #1f4e79;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }
        
        .metric-card .number {
            font-size: 2.5rem;
            font-weight: bold;
            color: #e53e3e;
            margin: 0.5rem 0;
        }
        
        .metric-card .unit {
            font-size: 1.2rem;
            color: #e53e3e;
            font-weight: bold;
        }
        
        .benchmark-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
        }
        
        .benchmark-card h3 {
            margin-bottom: 1rem;
            font-size: 1.3rem;
        }
        
        .benchmark-card ul {
            list-style: none;
            padding-left: 0;
        }
        
        .benchmark-card li {
            margin: 0.5rem 0;
            padding-left: 1rem;
            position: relative;
        }
        
        .benchmark-card li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #90cdf4;
        }
        
        .parenting-model {
            background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
            margin: 1rem 0;
        }
        
        .parenting-model h4 {
            color: #2d3748;
            margin-bottom: 1rem;
            font-size: 1.2rem;
        }
        
        .timeline-chart {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin: 1.5rem 0;
        }
        
        .timeline-item {
            display: flex;
            align-items: center;
            padding: 1rem;
            margin: 0.5rem 0;
            background: #f8f9fa;
            border-left: 5px solid #28a745;
            border-radius: 8px;
        }
        
        .timeline-item .activity {
            font-weight: bold;
            width: 200px;
            color: #2d3748;
        }
        
        .timeline-item .period {
            width: 150px;
            color: #4a5568;
        }
        
        .timeline-item .description {
            flex: 1;
            color: #718096;
            font-size: 0.9rem;
        }
        
        .gcg-principle {
            background: white;
            padding: 1.2rem;
            border-radius: 10px;
            border-left: 4px solid #3182ce;
            margin: 0.8rem 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        .gcg-principle h4 {
            color: #2d3748;
            margin-bottom: 0.8rem;
        }
        
        .gcg-principle ul {
            list-style: none;
            padding-left: 0;
        }
        
        .gcg-principle li {
            margin: 0.3rem 0;
            padding-left: 1rem;
            position: relative;
        }
        
        .gcg-principle li:before {
            content: "•";
            position: absolute;
            left: 0;
            color: #3182ce;
        }
        
        .info-box {
            background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%);
            border: 2px solid #17a2b8;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
        }
        
        .warning-box {
            background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
            border: 2px solid #ffc107;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
        }
        
        .success-box {
            background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
            border: 2px solid #28a745;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
        }
        
        .table-container {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin: 1.5rem 0;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
        }
        
        th {
            background: #3182ce;
            color: white;
            padding: 1rem;
            text-align: left;
            font-weight: 600;
        }
        
        td {
            padding: 0.8rem 1rem;
            border-bottom: 1px solid #e2e8f0;
        }
        
        tr:nth-child(even) {
            background: #f8f9fa;
        }
        
        .footer {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 2rem;
            margin: 2rem -2rem -2rem -2rem;
            border-radius: 0 0 10px 10px;
            text-align: center;
            color: #4a5568;
        }
        
        .footer h3 {
            color: #1f4e79;
            margin-bottom: 1rem;
        }
        
        .footer-grid {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 2rem;
            margin-top: 1.5rem;
        }
        
        .slide-number {
            position: absolute;
            bottom: 1rem;
            right: 2rem;
            background: #3182ce;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
        }
        
        @media print {
            .slide {
                margin-bottom: 0;
                box-shadow: none;
                border: none;
            }
        }
    </style>
</head>
<body>

<!-- Slide 1: Title Slide -->
<div class="slide">
    <div class="main-title">
        <h1>🏢 Pemutakhiran Pedoman Tata Kelola Terintegrasi</h1>
        <h2>PT Surveyor Indonesia (Persero)</h2>
        <p>Timeline 8 Minggu - Bulan 1 - Excellence in Corporate Governance</p>
        <p style="margin-top: 1rem; font-size: 1.1rem;">Strategic Control Model & GRC Framework Development</p>
    </div>
    
    <div class="content-grid" style="margin-top: 3rem;">
        <div class="metric-card">
            <h3>⏰ Timeline</h3>
            <div class="number">8</div>
            <div class="unit">Minggu</div>
            <p>Bulan 1 Implementation</p>
        </div>
        <div class="metric-card">
            <h3>📋 Activities</h3>
            <div class="number">7</div>
            <div class="unit">Utama</div>
            <p>Overlapping Timeline</p>
        </div>
    </div>
    
    <div class="warning-box">
        <h4 style="color: #856404; margin: 0;">⚠️ FRAMEWORK DISCLAIMER</h4>
        <p style="color: #856404; margin: 0.5rem 0;">
            <strong>Dashboard ini menyajikan framework governance dan metodologi konseptual.</strong><br>
            Data finansial menggunakan periode 2024-2025 untuk akurasi terkini.
            Materi untuk penggunaan internal PT Surveyor Indonesia dalam konteks pengembangan governance framework.
        </p>
    </div>
    
    <div class="footer">
        <h3>PT Surveyor Indonesia - Governance Excellence</h3>
        <div class="footer-grid">
            <div>
                <strong>Version 6.0</strong><br>
                Strategic Control Framework
            </div>
            <div>
                <strong>Created by</strong><br>
                MS Hadianto - KIM Consulting 2025
            </div>
            <div>
                <strong>Data Period</strong><br>
                Financial Data: 2024-2025
            </div>
        </div>
    </div>
    <div class="slide-number">1/10</div>
</div>

<!-- Slide 2: Executive Overview -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">📊 Executive Overview - Project Status</div>
        <div class="slide-subtitle">Key Metrics & Strategic Focus</div>
    </div>
    
    <div class="content-grid">
        <div>
            <h3>🎯 Project Highlights</h3>
            <div class="metric-card">
                <h3>Current Focus</h3>
                <div class="number">Week 1</div>
                <div class="unit">of 8</div>
                <p>Bulan 1 - Kick-Off & Document Review</p>
            </div>
            
            <div class="info-box">
                <h4>🎯 Week 1 Active Activities</h4>
                <ul>
                    <li>🔄 Kick-Off Meeting</li>
                    <li>🔄 Document Review</li>
                    <li>⏳ Team Setup & Stakeholder Alignment</li>
                </ul>
            </div>
        </div>
        
        <div>
            <h3>📋 Strategic Objectives</h3>
            <div class="gcg-principle">
                <h4>🏛️ Pemutakhiran Pedoman Goals</h4>
                <ul>
                    <li>Landasan PT Surveyor Indonesia sebagai Perusahaan Induk</li>
                    <li>Pedoman Anak Perusahaan yang selaras</li>
                    <li>Penerapan GRC (Governance, Risk & Compliance)</li>
                    <li>Strategic Control Model implementation</li>
                </ul>
            </div>
            
            <div class="success-box">
                <h4>✅ Target Structure</h4>
                <p><strong>8 Entities Optimal Structure</strong> - Strategic Control Model mengikuti best practice Telkom Indonesia & Pertamina</p>
            </div>
        </div>
    </div>
    
    <div class="content-grid-three">
        <div class="metric-card">
            <h3>📋 KPI: Stakeholder Satisfaction</h3>
            <div class="number">82%</div>
            <div class="unit">Current</div>
            <p>Target: 85% | ↗️ +3% trend</p>
        </div>
        <div class="metric-card">
            <h3>⏱️ KPI: Timeline Adherence</h3>
            <div class="number">88%</div>
            <div class="unit">Current</div>
            <p>Target: 90% | ↗️ +2% trend</p>
        </div>
        <div class="metric-card">
            <h3>🎯 KPI: Quality Score</h3>
            <div class="number">85%</div>
            <div class="unit">Current</div>
            <p>Target: 90% | ↗️ +4% trend</p>
        </div>
    </div>
    
    <div class="slide-number">2/10</div>
</div>

<!-- Slide 3: Timeline Implementation -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">⏱️ Timeline Implementation - 8 Minggu Bulan 1</div>
        <div class="slide-subtitle">7 Aktivitas Utama dengan Overlapping Schedule</div>
    </div>
    
    <div class="timeline-chart">
        <h3 style="margin-bottom: 1.5rem; color: #2d3748;">📊 Timeline Pekerjaan - 7 Aktivitas Utama</h3>
        
        <div class="timeline-item">
            <div class="activity">Kick-Off Meeting</div>
            <div class="period">Minggu 1</div>
            <div class="description">Project initiation, team mobilization, dan stakeholder alignment</div>
        </div>
        
        <div class="timeline-item">
            <div class="activity">Review Dokumen</div>
            <div class="period">Minggu 1-3</div>
            <div class="description">Review Pedoman eksisting, regulasi, Anggaran Dasar, Kebijakan Internal</div>
        </div>
        
        <div class="timeline-item">
            <div class="activity">Interview</div>
            <div class="period">Minggu 3-5</div>
            <div class="description">Wawancara dengan Dewan Komisaris, Direksi, dan Unit lain untuk insight dan ekspektasi</div>
        </div>
        
        <div class="timeline-item">
            <div class="activity">Pemutakhiran Pedoman</div>
            <div class="period">Minggu 2-5</div>
            <div class="description">Menyusun draft awal pedoman yang telah dimutakhirkan berdasarkan analisis dan masukan</div>
        </div>
        
        <div class="timeline-item">
            <div class="activity">Validasi Internal</div>
            <div class="period">Minggu 5-6</div>
            <div class="description">Pembahasan draft awal dengan Internal Perusahaan (Dewan Komisaris, Direksi, Unit lain)</div>
        </div>
        
        <div class="timeline-item">
            <div class="activity">Finalisasi Dokumen</div>
            <div class="period">Minggu 6-7</div>
            <div class="description">Menindaklanjuti hasil validasi internal untuk finalisasi draft</div>
        </div>
        
        <div class="timeline-item">
            <div class="activity">Sosialisasi</div>
            <div class="period">Minggu 7-8</div>
            <div class="description">Sosialisasi kepada Insan Perusahaan dan stakeholders</div>
        </div>
    </div>
    
    <div class="info-box">
        <h4>📅 Current Status: Week 1, Bulan 1</h4>
        <p><strong>Focus:</strong> Kick-Off Meeting & Review Dokumen Awal - Timeline menggunakan struktur 8 minggu dengan 7 aktivitas utama overlapping</p>
    </div>
    
    <div class="slide-number">3/10</div>
</div>

<!-- Slide 4: Corporate Parenting Models -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">🏗️ Corporate Parenting Model Framework</div>
        <div class="slide-subtitle">4 Model dengan Contoh Perusahaan Indonesia</div>
    </div>
    
    <div class="content-grid">
        <div class="parenting-model">
            <h4>🏛️ Financial Control Model</h4>
            <p><strong>Karakteristik:</strong></p>
            <ul>
                <li>Focus pada financial performance</li>
                <li>Limited strategic intervention</li>
                <li>Decentralized decision making</li>
            </ul>
            <p><strong>🇮🇩 Contoh Indonesia:</strong> Astra International (sebagian unit), Salim Group</p>
            <p><strong>Cocok untuk:</strong> Portfolio dengan bisnis yang tidak saling terkait</p>
        </div>
        
        <div class="parenting-model" style="border: 3px solid #28a745;">
            <h4>🏛️ Strategic Control Model ⭐ RECOMMENDED</h4>
            <p><strong>Karakteristik:</strong></p>
            <ul>
                <li>Balance antara financial dan strategic control</li>
                <li>Selective intervention pada strategic decisions</li>
                <li>Coordination pada key initiatives</li>
            </ul>
            <p><strong>🇮🇩 Contoh Indonesia:</strong> PT Telkom Indonesia, PT Pertamina, Sinar Mas Group</p>
            <p><strong>Cocok untuk:</strong> Related diversification strategy</p>
        </div>
    </div>
    
    <div class="content-grid">
        <div class="parenting-model">
            <h4>🏛️ Strategic Planning Model</h4>
            <p><strong>Karakteristik:</strong></p>
            <ul>
                <li>Centralized strategic planning</li>
                <li>Detailed performance monitoring</li>
                <li>Extensive coordination mechanisms</li>
            </ul>
            <p><strong>🇮🇩 Contoh Indonesia:</strong> PT Pupuk Indonesia, PT Semen Indonesia</p>
            <p><strong>Cocok untuk:</strong> Integrated business portfolio</p>
        </div>
        
        <div class="parenting-model">
            <h4>🏛️ Financial Engineering Model</h4>
            <p><strong>Karakteristik:</strong></p>
            <ul>
                <li>Focus pada financial restructuring</li>
                <li>Short to medium-term value creation</li>
                <li>Active portfolio management</li>
            </ul>
            <p><strong>🇮🇩 Contoh Indonesia:</strong> BPPN (historical), holding BUMN dalam restrukturisasi</p>
            <p><strong>Cocok untuk:</strong> Turnaround situations</p>
        </div>
    </div>
    
    <div class="success-box">
        <h4>⭐ Rekomendasi untuk PT Surveyor Indonesia</h4>
        <p><strong>Strategic Control Model</strong> - Medium business diversity, medium synergy potential, collaborative management approach. Mengikuti best practice Telkom Indonesia & Pertamina.</p>
    </div>
    
    <div class="slide-number">4/10</div>
</div>

<!-- Slide 5: Indonesian Success Stories -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">🏆 Success Stories Corporate Parenting Indonesia</div>
        <div class="slide-subtitle">Financial Data 2024-2025 - Evidence-Based Framework</div>
    </div>
    
    <div class="content-grid">
        <div class="benchmark-card">
            <h3>🏢 PT Telkom Indonesia (Strategic Control)</h3>
            <p><strong>Struktur:</strong> Holding Company dengan 12+ subsidiaries</p>
            <p><strong>Key Achievements (2024-2025):</strong></p>
            <ul>
                <li>Revenue TTM: $9.58B USD (Feb 2025)</li>
                <li>Market cap: $14.7B USD (Apr 2025)</li>
                <li>Telkomsel: 169.5 juta pelanggan</li>
                <li>Digital transformation & regional expansion (10 negara)</li>
            </ul>
            <p><small><strong>Referensi:</strong> CompaniesMarketCap.com, SEC Filings 2024-2025</small></p>
        </div>
        
        <div class="benchmark-card">
            <h3>🚗 PT Astra International (Mixed Model)</h3>
            <p><strong>Struktur:</strong> Diversified Conglomerate</p>
            <p><strong>Key Achievements (2024-2025):</strong></p>
            <ul>
                <li>Revenue TTM: $20.81B USD (May 2025)</li>
                <li>Market cap: $12.6B USD (July 2025)</li>
                <li>7 sektor bisnis: Automotive, Financial, Energy, etc.</li>
                <li>32+ anak perusahaan terintegrasi</li>
            </ul>
            <p><small><strong>Referensi:</strong> CompaniesMarketCap.com, PitchBook 2025</small></p>
        </div>
    </div>
    
    <div class="content-grid">
        <div class="benchmark-card">
            <h3>🏭 PT Pupuk Indonesia (Strategic Planning)</h3>
            <p><strong>Struktur:</strong> Functional Holding Company</p>
            <p><strong>Key Achievements (2024-2025):</strong></p>
            <ul>
                <li>Kapasitas produksi: 8.2 juta ton/tahun</li>
                <li>Konsolidasi 5 BUMN pupuk sejak 2012</li>
                <li>Excellence in Performance Awards 2025 🏆</li>
                <li>Program Makmur: 1,000 kiosk pupuk</li>
            </ul>
            <p><small><strong>Referensi:</strong> Investortrust.id 2025, Fortune Indonesia 100</small></p>
        </div>
        
        <div class="benchmark-card">
            <h3>🌿 Sinar Mas Group (Strategic Control)</h3>
            <p><strong>Struktur:</strong> Multi-industry Holding</p>
            <p><strong>Key Achievements (H1 2025):</strong></p>
            <ul>
                <li>SMAR (Agro): Revenue $5.34B, Market cap $736M</li>
                <li>Sinarmas Land: Revenue $1.12B, Market cap $1.24B</li>
                <li>7 pilar bisnis independen dengan shared values</li>
                <li>Mixed performance - SMMA & SMAR growth leaders</li>
            </ul>
            <p><small><strong>Referensi:</strong> PitchBook 2025, Bisnis.com H1-2025</small></p>
        </div>
    </div>
    
    <div class="slide-number">5/10</div>
</div>

<!-- Slide 6: GCG Framework -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">📋 Good Corporate Governance (GCG) Framework</div>
        <div class="slide-subtitle">5 Prinsip Fundamental & GRC Integration</div>
    </div>
    
    <div class="content-grid">
        <div>
            <div class="gcg-principle">
                <h4>🔍 1. Transparency (Keterbukaan)</h4>
                <ul>
                    <li><strong>Financial reporting</strong> yang akurat dan tepat waktu</li>
                    <li><strong>Disclosure kebijakan</strong> dan strategi material</li>
                    <li><strong>Open communication</strong> dengan stakeholders</li>
                </ul>
            </div>
            
            <div class="gcg-principle">
                <h4>📊 2. Accountability (Akuntabilitas)</h4>
                <ul>
                    <li><strong>Clear roles</strong> dan responsibilities</li>
                    <li><strong>Performance measurement</strong> yang objektif</li>
                    <li><strong>Regular evaluation</strong> dan feedback</li>
                </ul>
            </div>
            
            <div class="gcg-principle">
                <h4>🎯 3. Responsibility (Pertanggungjawaban)</h4>
                <ul>
                    <li><strong>Compliance</strong> terhadap regulasi dan standar</li>
                    <li><strong>Environmental dan social</strong> responsibility</li>
                    <li><strong>Stakeholder engagement</strong> yang efektif</li>
                </ul>
            </div>
        </div>
        
        <div>
            <div class="gcg-principle">
                <h4>⚖️ 4. Independence (Kemandirian)</h4>
                <ul>
                    <li><strong>Independent oversight</strong> melalui komisaris independen</li>
                    <li><strong>Objective decision making</strong> process</li>
                    <li><strong>Conflict of interest</strong> management</li>
                </ul>
            </div>
            
            <div class="gcg-principle">
                <h4>🤝 5. Fairness (Kesetaraan)</h4>
                <ul>
                    <li><strong>Fair treatment</strong> untuk semua stakeholders</li>
                    <li><strong>Equal access</strong> terhadap informasi material</li>
                    <li><strong>Protection of minority</strong> shareholders rights</li>
                </ul>
            </div>
        </div>
    </div>
    
    <h3 style="margin: 2rem 0 1rem 0; color: #2d3748;">🔗 Governance, Risk, and Compliance (GRC) Integration</h3>
    
    <div class="content-grid-three">
        <div class="parenting-model">
            <h4>🏛️ Governance Layer</h4>
            <ul>
                <li><strong>Board effectiveness</strong> dan oversight</li>
                <li><strong>Management accountability</strong></li>
                <li><strong>Strategic decision making</strong> process</li>
            </ul>
        </div>
        
        <div class="parenting-model">
            <h4>⚠️ Risk Management Layer</h4>
            <ul>
                <li><strong>Enterprise risk management</strong> framework</li>
                <li><strong>Risk appetite</strong> dan tolerance setting</li>
                <li><strong>Risk monitoring</strong> dan reporting</li>
            </ul>
        </div>
        
        <div class="parenting-model">
            <h4>✅ Compliance Layer</h4>
            <ul>
                <li><strong>Regulatory compliance</strong> management</li>
                <li><strong>Internal control</strong> systems</li>
                <li><strong>Audit dan assurance</strong> functions</li>
            </ul>
        </div>
    </div>
    
    <div class="slide-number">6/10</div>
</div>

<!-- Slide 7: GCG Assessment -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">📊 GCG Development Priority Matrix</div>
        <div class="slide-subtitle">Assessment & Target Framework Development</div>
    </div>
    
    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th>Prinsip GCG</th>
                    <th>Baseline Assessment (%)</th>
                    <th>Target Framework (%)</th>
                    <th>Development Gap</th>
                    <th>Priority Level</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Transparency</strong></td>
                    <td>82</td>
                    <td>90</td>
                    <td>8</td>
                    <td><span style="color: #e53e3e; font-weight: bold;">High</span></td>
                </tr>
                <tr>
                    <td><strong>Accountability</strong></td>
                    <td>78</td>
                    <td>88</td>
                    <td>10</td>
                    <td><span style="color: #e53e3e; font-weight: bold;">High</span></td>
                </tr>
                <tr>
                    <td><strong>Responsibility</strong></td>
                    <td>85</td>
                    <td>92</td>
                    <td>7</td>
                    <td><span style="color: #f56500; font-weight: bold;">Medium</span></td>
                </tr>
                <tr>
                    <td><strong>Independence</strong></td>
                    <td>72</td>
                    <td>85</td>
                    <td>13</td>
                    <td><span style="color: #c53030; font-weight: bold;">Critical</span></td>
                </tr>
                <tr>
                    <td><strong>Fairness</strong></td>
                    <td>80</td>
                    <td>88</td>
                    <td>8</td>
                    <td><span style="color: #e53e3e; font-weight: bold;">High</span></td>
                </tr>
            </tbody>
        </table>
    </div>
    
    <div class="content-grid">
        <div class="info-box">
            <h4>🎯 Key Development Areas</h4>
            <ul>
                <li><strong>Critical Priority:</strong> Independence (Gap: 13%)</li>
                <li><strong>High Priority:</strong> Accountability (Gap: 10%)</li>
                <li><strong>Focus Areas:</strong> Independent oversight, objective decision making</li>
                <li><strong>Implementation:</strong> Komisaris independen, conflict of interest management</li>
            </ul>
        </div>
        
        <div class="warning-box">
            <h4>⚠️ Implementation Strategy</h4>
            <ul>
                <li><strong>Phase 1:</strong> Address Critical & High priority items</li>
                <li><strong>Phase 2:</strong> Strengthen Medium priority areas</li>
                <li><strong>Continuous:</strong> Monitor and evaluate progress</li>
                <li><strong>Target:</strong> Achieve 88-92% across all principles</li>
            </ul>
        </div>
    </div>
    
    <div class="slide-number">7/10</div>
</div>

<!-- Slide 8: Tata Kelola Hubungan Induk-Anak -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">🏛️ Tata Kelola Hubungan Induk dan Anak Perusahaan</div>
        <div class="slide-subtitle">Roles, Responsibilities & Prinsip Fundamental</div>
    </div>
    
    <div class="content-grid">
        <div>
            <h3>🎯 Peran dan Tanggung Jawab Perusahaan Induk</h3>
            
            <div class="gcg-principle">
                <h4>1. Sebagai Pemegang Saham Pengendali:</h4>
                <ul>
                    <li><strong>Strategic Direction:</strong> Menetapkan visi, misi, dan strategi korporat</li>
                    <li><strong>Capital Allocation:</strong> Optimasi alokasi sumber daya dan investasi</li>
                    <li><strong>Performance Oversight:</strong> Monitoring dan evaluasi kinerja anak perusahaan</li>
                    <li><strong>Risk Management:</strong> Penetapan risk appetite dan framework manajemen risiko</li>
                </ul>
            </div>
            
            <div class="gcg-principle">
                <h4>2. Sebagai Corporate Parent:</h4>
                <ul>
                    <li><strong>Value Creation:</strong> Menciptakan sinergi dan value-added activities</li>
                    <li><strong>Capability Building:</strong> Pengembangan kapabilitas dan competency</li>
                    <li><strong>Knowledge Management:</strong> Transfer knowledge dan best practices</li>
                    <li><strong>Brand Management:</strong> Pengelolaan reputasi dan brand portfolio</li>
                </ul>
            </div>
        </div>
        
        <div>
            <h3>🎯 Tanggung Jawab Anak Perusahaan</h3>
            
            <div class="gcg-principle">
                <h4>1. Operational Excellence:</h4>
                <ul>
                    <li>Mencapai target kinerja yang ditetapkan</li>
                    <li>Menjalankan operasional sesuai standar korporat</li>
                    <li>Melaporkan kinerja secara transparan dan akurat</li>
                </ul>
            </div>
            
            <div class="gcg-principle">
                <h4>2. Compliance & Governance:</h4>
                <ul>
                    <li>Mematuhi kebijakan dan prosedur induk perusahaan</li>
                    <li>Menerapkan sistem governance yang efektif</li>
                    <li>Melaksanakan manajemen risiko sesuai framework korporat</li>
                </ul>
            </div>
            
            <div class="gcg-principle">
                <h4>3. Strategic Alignment:</h4>
                <ul>
                    <li>Menyelaraskan strategi dengan arah korporat</li>
                    <li>Berkontribusi pada pencapaian target konsolidasi</li>
                    <li>Berpartisipasi aktif dalam inisiatif sinergi</li>
                </ul>
            </div>
        </div>
    </div>
    
    <h3 style="margin: 1.5rem 0 1rem 0; color: #2d3748;">🎯 Prinsip Dasar Tata Kelola Terintegrasi</h3>
    
    <div class="content-grid-three">
        <div class="parenting-model">
            <h4>🎯 Unity in Diversity</h4>
            <ul>
                <li><strong>Kesatuan visi dan misi korporat</strong></li>
                <li>Fleksibilitas implementasi sesuai karakteristik bisnis</li>
                <li>Standardisasi pada aspek kritis, lokalisasi pada aspek operasional</li>
            </ul>
        </div>
        
        <div class="parenting-model">
            <h4>💎 Value Creation Focus</h4>
            <ul>
                <li><strong>Orientasi pada penciptaan nilai jangka panjang</strong></li>
                <li>Optimasi sinergi lintas anak perusahaan</li>
                <li>Balance antara growth dan profitability</li>
            </ul>
        </div>
        
        <div class="parenting-model">
            <h4>🛡️ Integrated Risk Management</h4>
            <ul>
                <li><strong>Risk appetite yang selaras di seluruh grup</strong></li>
                <li>Early warning system terintegrasi</li>
                <li>Coordination dalam crisis management</li>
            </ul>
        </div>
    </div>
    
    <div class="slide-number">8/10</div>
</div>

<!-- Slide 9: Review Pedoman -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">📖 Review Pedoman Tata Kelola Terlampir</div>
        <div class="slide-subtitle">SKD-002 Pedoman Tata Kelola Hubungan Perusahaan Induk dan Anak Perusahaan</div>
    </div>
    
    <div class="warning-box">
        <h4 style="color: #c53030; margin: 0;">📋 Dokumen: SKD-002 Pedoman Tata Kelola Hubungan Perusahaan Induk dan Anak Perusahaan</h4>
        <p style="color: #c53030; margin: 0.5rem 0;">
            <strong>PT Surveyor Indonesia | Nomor: SKD-002/DRU-XII/DPKMR/2023 | Tanggal: 22 Desember 2023</strong><br>
            <strong>Total Halaman:</strong> 99 halaman | <strong>Revisi:</strong> 00
        </p>
    </div>
    
    <div class="content-grid">
        <div>
            <h3>🎯 Maksud dan Tujuan Pedoman</h3>
            <div class="gcg-principle">
                <ol>
                    <li><strong>Landasan dan pedoman bagi PT Surveyor Indonesia</strong> sebagai Perusahaan Induk dalam mengelola Anak Perusahaan</li>
                    <li><strong>Pedoman bagi Anak Perusahaan</strong> dalam mengelola perusahaan yang selaras dengan arah dan kebijakan PT Surveyor Indonesia</li>
                    <li><strong>Perangkat pendukung penerapan tata kelola perusahaan yang baik</strong>, berbasis risiko dan kepatuhan (Governance, Risk and Compliance - GRC)</li>
                </ol>
            </div>
        </div>
        
        <div>
            <h3>📋 Struktur Pedoman</h3>
            <div class="metric-card">
                <h3>Komponen Utama</h3>
                <ul style="text-align: left; margin-top: 1rem;">
                    <li><strong>14 Bab Utama</strong></li>
                    <li><strong>99 Halaman</strong></li>
                    <li><strong>7 Aspek Operasional</strong></li>
                    <li><strong>5 Prinsip GCG</strong></li>
                </ul>
            </div>
        </div>
    </div>
    
    <h3 style="margin: 1.5rem 0 1rem 0; color: #2d3748;">🎯 Key Highlights Pedoman</h3>
    
    <div class="content-grid-three">
        <div class="gcg-principle">
            <h4>🏛️ Prinsip GCG (Bab 2)</h4>
            <ul>
                <li><strong>Keterbukaan (Transparency)</strong></li>
                <li><strong>Akuntabilitas (Accountability)</strong></li>
                <li><strong>Pertanggungjawaban (Responsibility)</strong></li>
                <li><strong>Kemandirian (Independency)</strong></li>
                <li><strong>Kewajaran (Fairness)</strong></li>
            </ul>
        </div>
        
        <div class="gcg-principle">
            <h4>📋 Aspek Operasional (Bab 9)</h4>
            <ul>
                <li><strong>Hukum dan Kepatuhan</strong></li>
                <li><strong>Sistem Pengendalian Internal</strong></li>
                <li><strong>Keuangan dan Akuntansi</strong></li>
                <li><strong>Sumber Daya Manusia</strong></li>
                <li><strong>Pengadaan Barang & Jasa</strong></li>
                <li><strong>Teknologi Informasi</strong></li>
                <li><strong>Manajemen Risiko</strong></li>
            </ul>
        </div>
        
        <div class="gcg-principle">
            <h4>🎯 Struktur Korporasi (Bab 3)</h4>
            <ul>
                <li><strong>Perusahaan Induk:</strong> Strategic Control</li>
                <li><strong>Anak Perusahaan PT:</strong> Operational Execution</li>
                <li><strong>Perusahaan Afiliasi:</strong> Strategic Partnership</li>
                <li><strong>Target: 8 Entities</strong> Optimal Structure</li>
            </ul>
        </div>
    </div>
    
    <div class="content-grid">
        <div class="info-box">
            <h4>🌟 Tata Nilai Anak Perusahaan (AKHLAK)</h4>
            <ul>
                <li><strong>A</strong>manah - Dapat dipercaya</li>
                <li><strong>K</strong>ompeten - Profesional dan berkualitas</li>
                <li><strong>H</strong>armoni - Keselarasan dalam bekerja</li>
                <li><strong>L</strong>oyal - Setia pada perusahaan</li>
                <li><strong>A</strong>daptif - Fleksibel menghadapi perubahan</li>
                <li><strong>K</strong>olaboratif - Bekerja sama dengan baik</li>
            </ul>
        </div>
        
        <div class="warning-box">
            <h4>⚖️ Dasar Hukum Utama</h4>
            <ul>
                <li><strong>UU No. 19/2003</strong> - Badan Usaha Milik Negara</li>
                <li><strong>UU No. 40/2007</strong> - Perseroan Terbatas</li>
                <li><strong>Perpu No. 2/2022</strong> - Cipta Kerja</li>
                <li><strong>PER-04/MBU/2014</strong> - Penghasilan Direksi & Komisaris</li>
                <li><strong>PER-2/MBU/03/2023</strong> - Tata Kelola BUMN</li>
            </ul>
        </div>
    </div>
    
    <div class="slide-number">9/10</div>
</div>

<!-- Slide 10: Summary & Next Steps -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">📊 Executive Summary & Next Steps</div>
        <div class="slide-subtitle">Strategic Recommendations & Implementation Roadmap</div>
    </div>
    
    <div class="content-grid">
        <div>
            <h3>⭐ Key Recommendations</h3>
            
            <div class="success-box">
                <h4>🎯 Strategic Control Model - RECOMMENDED</h4>
                <p><strong>Alasan Pemilihan:</strong></p>
                <ul>
                    <li>Medium business diversity dengan medium synergy potential</li>
                    <li>Collaborative management approach</li>
                    <li>Mengikuti best practice Telkom Indonesia & Pertamina</li>
                    <li>Cocok untuk struktur 8 entities optimal</li>
                </ul>
            </div>
            
            <div class="info-box">
                <h4>🏆 Success Benchmarks</h4>
                <ul>
                    <li><strong>Telkom Indonesia:</strong> $9.58B revenue, 12+ subsidiaries</li>
                    <li><strong>Astra International:</strong> $20.81B revenue, 7 sectors</li>
                    <li><strong>Pupuk Indonesia:</strong> 8.2M ton capacity, 5 BUMN consolidated</li>
                </ul>
            </div>
        </div>
        
        <div>
            <h3>📅 Next Steps - Week 2-8</h3>
            
            <div class="timeline-item">
                <div class="activity">Week 2-3</div>
                <div class="description">Continue Document Review & Analysis</div>
            </div>
            
            <div class="timeline-item">
                <div class="activity">Week 3-5</div>
                <div class="description">Stakeholder Interviews & Framework Development</div>
            </div>
            
            <div class="timeline-item">
                <div class="activity">Week 5-6</div>
                <div class="description">Internal Validation & Draft Review</div>
            </div>
            
            <div class="timeline-item">
                <div class="activity">Week 6-7</div>
                <div class="description">Document Finalization</div>
            </div>
            
            <div class="timeline-item">
                <div class="activity">Week 7-8</div>
                <div class="description">Socialization & Implementation Preparation</div>
            </div>
            
            <div class="warning-box">
                <h4>🔍 Critical Focus Areas</h4>
                <ul>
                    <li><strong>Independence (Critical Priority):</strong> 13% gap to close</li>
                    <li><strong>Accountability (High Priority):</strong> 10% gap to close</li>
                    <li><strong>Strategic Control Implementation:</strong> Executive Board mechanism</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <h3>🏢 Pemutakhiran Pedoman Tata Kelola Terintegrasi - PT Surveyor Indonesia</h3>
        <div class="footer-grid">
            <div>
                <strong>Dashboard Information</strong><br>
                Version 6.0 - Week 1/8<br>
                Financial Data: 2024-2025 Period<br>
                Evidence-based Framework
            </div>
            <div>
                <strong>Created by</strong><br>
                MS Hadianto<br>
                KIM Consulting 2025<br>
                Strategic Excellence
            </div>
            <div>
                <strong>References</strong><br>
                CompaniesMarketCap.com (2025)<br>
                PitchBook Platform, Bisnis.com H1-2025<br>
                Fortune Indonesia 100 (Aug 2025)
            </div>
        </div>
        
        <div style="margin-top: 2rem; padding: 1rem; background: #fff3cd; border: 2px solid #ffc107; border-radius: 10px;">
            <h4 style="color: #856404; margin: 0;">⚠️ COMPREHENSIVE DISCLAIMER</h4>
            <p style="color: #856404; margin: 0.5rem 0; font-size: 0.9rem;">
                <strong>Materi sosialisasi ini untuk digunakan secara terbatas pada PT Surveyor Indonesia.</strong><br>
                Corporate parenting model examples berdasarkan data finansial terkini periode 2024-2025.
                Review pedoman berdasarkan SKD-002/DRU-XII/DPKMR/2023 tanggal 22 Desember 2023.
            </p>
        </div>
    </div>
    
    <div class="slide-number">10/10</div>
</div>

<script>
// Enhanced print functionality
window.onload = function() {
    // Create print controls container
    const controlsContainer = document.createElement('div');
    controlsContainer.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        display: flex;
        flex-direction: column;
        gap: 10px;
    `;
    
    // Create print button
    const printButton = document.createElement('button');
    printButton.innerHTML = '🖨️ Print/Save PDF';
    printButton.style.cssText = `
        background: #3182ce;
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 25px;
        font-size: 16px;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transition: all 0.3s ease;
        min-width: 150px;
    `;
    
    // Create download info
    const infoDiv = document.createElement('div');
    infoDiv.innerHTML = `
        <div style="background: white; padding: 10px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 12px; max-width: 200px;">
            <strong>💡 Cara Save PDF:</strong><br>
            1. Klik Print/Save PDF<br>
            2. Pilih "Save as PDF" di destination<br>
            3. Set Layout: Landscape<br>
            4. Margins: Minimum
        </div>
    `;
    infoDiv.style.display = 'none';
    
    // Add hover effects
    printButton.onmouseover = function() {
        this.style.background = '#2c5282';
        this.style.transform = 'translateY(-2px)';
        infoDiv.style.display = 'block';
    };
    
    printButton.onmouseout = function() {
        this.style.background = '#3182ce';
        this.style.transform = 'translateY(0)';
        setTimeout(() => {
            infoDiv.style.display = 'none';
        }, 2000);
    };
    
    // Enhanced print function
    printButton.onclick = function() {
        // Hide all controls before printing
        controlsContainer.style.display = 'none';
        
        // Trigger print dialog
        if (window.print) {
            window.print();
        } else {
            alert('Print function not available. Please use Ctrl+P (Windows) or Cmd+P (Mac)');
        }
        
        // Show controls back after a delay
        setTimeout(() => {
            controlsContainer.style.display = 'flex';
        }, 1000);
    };
    
    // Create download button as backup
    const downloadButton = document.createElement('button');
    downloadButton.innerHTML = '💾 Manual Save';
    downloadButton.style.cssText = `
        background: #28a745;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 20px;
        font-size: 14px;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transition: all 0.3s ease;
        min-width: 150px;
    `;
    
    downloadButton.onclick = function() {
        alert(`📄 Manual Save Instructions:
        
1. Gunakan Ctrl+P (Windows) atau Cmd+P (Mac)
2. Pilih "Save as PDF" di Destination
3. Set Layout: Landscape
4. Paper Size: A4
5. Margins: Minimum
6. Klik Save

Atau gunakan browser menu: File → Print → Save as PDF`);
    };
    
    // Add simple instructions always visible
    const instructionsDiv = document.createElement('div');
    instructionsDiv.innerHTML = `
        <div style="background: #f8f9fa; border: 2px solid #dee2e6; padding: 8px; border-radius: 8px; font-size: 11px; color: #495057; text-align: center;">
            <strong>💡 Quick Save:</strong> Press Ctrl+P → Save as PDF
        </div>
    `;
    
    // Add download button to container
    controlsContainer.appendChild(downloadButton);
    controlsContainer.appendChild(instructionsDiv);
    
    // Add elements to container
    controlsContainer.appendChild(printButton);
    controlsContainer.appendChild(infoDiv);
    document.body.appendChild(controlsContainer);
    
    // Alternative method for browsers that don't support window.print
    document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key === 'p') {
            e.preventDefault();
            printButton.click();
        }
    });
    
    // Add print styles specifically for PDF generation
    const printStyles = document.createElement('style');
    printStyles.textContent = `
        @media print {
            body { 
                background: white !important; 
                -webkit-print-color-adjust: exact !important;
                color-adjust: exact !important;
            }
            .slide { 
                page-break-after: always !important; 
                margin: 0 !important;
                box-shadow: none !important;
                border: none !important;
                background: white !important;
            }
            .slide:last-child { 
                page-break-after: avoid !important; 
            }
            * {
                -webkit-print-color-adjust: exact !important;
                color-adjust: exact !important;
            }
        }
        
        @page {
            size: A4 landscape;
            margin: 0.5in;
        }
    `;
    document.head.appendChild(printStyles);
};

// Fallback function if main print doesn't work
function manualPrint() {
    window.print();
}
</script>

</body>
</html>
