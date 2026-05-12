import streamlit as st
import pandas as pd

st.set_page_config(page_title="Open MSE Dashboard", page_icon="📈", layout="wide")

st.markdown("""
<style>
.kpi-card{background:white;border-radius:10px;padding:20px;border-left:4px solid #004187;margin-bottom:10px;box-shadow:0 1px 4px rgba(0,0,0,0.08)}
.kpi-label{font-size:13px;color:#6b7280;font-weight:500;margin-bottom:4px}
.kpi-value{font-size:26px;font-weight:700;color:#111827}
.green{font-size:13px;color:#10b981;font-weight:600}
.red{font-size:13px;color:#ef4444;font-weight:600}
</style>""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 📈 Open MSE")
    st.markdown("---")
    page = st.radio("Navigate", ["🏠 Market Overview","📊 Securities Overview","🏢 Listed Companies","📋 Other Securities","ℹ️ About"], label_visibility="collapsed")
    st.markdown("---")
    st.caption("Data: open.mse.mn · mse.mn")

listed = [("APU","АПУ ХК"),("AIC","Ард Даатгал ХК"),("ADB","Ард кредит ББСБ ХК"),("AARD","Ард санхүүгийн нэгдэл ХК"),("BDS","Би ди сек ХК"),("GOV","Говь ХК"),("GLMT","Голомт Банк ХК"),("NEH","Дархан нэхий ХК"),("INV","Инвескор ББСБ ХК"),("LEND","ЛэндМН ББСБ ХК"),("MIK","МИК Хөрөнгө Оруулалт ХК"),("MNB","Монгол банк бонд"),("MSE","Монголын Хөрөнгийн Бирж"),("MNDV","Мандал Даатгал ХК"),("MNGL","Монголын Алт ХК"),("BN","Богд Банк ХК"),("TDBM","ТДБ Банк ХК"),("GOVI","Говийн Өмнөд ХК"),("MNTK","Монтек ХК"),("UNIS","Юнивишн ХК")]
debt = [("MNB001","Монгол банк бонд 1","2026-12-31"),("MNB002","Монгол банк бонд 2","2027-06-30"),("GOV001","Засгийн газрын бонд 1","2028-01-15"),("GOV002","Засгийн газрын бонд 2","2029-03-20"),("GLMT01","Голомт Банк бонд","2027-09-01"),("ADB001","Ард кредит бонд","2026-08-15")]
abs_ = [("ABS001","МИК АБС 1","2027-06-30"),("ABS002","МИК АБС 2","2028-12-31"),("ABS003","Гэр АБС 1","2026-09-15"),("ABS004","Гэр АБС 2","2027-03-20"),("ABS005","Хас АБС 1","2028-06-01"),("ABS006","Хас АБС 2","")]
funds = [("FUND001","Ард Глобал ХАМ"),("FUND002","Мандал Өсөлтийн ХАМ"),("FUND003","Голомт Тэнцвэрт ХАМ")]

df_co = pd.DataFrame(listed, columns=["Symbol","Company Name"])
df_co.index = range(1, len(df_co)+1)
df_debt = pd.DataFrame(debt, columns=["Symbol","Security Name","Maturity Date"])
df_debt.index = range(1, len(df_debt)+1)
df_abs = pd.DataFrame(abs_, columns=["Symbol","Security Name","Maturity Date"])
df_abs.index = range(1, len(df_abs)+1)
df_funds = pd.DataFrame(funds, columns=["Symbol","Fund Name"])
df_funds.index = range(1, len(df_funds)+1)

if page == "🏠 Market Overview":
    st.title("Market Overview")
    st.caption("Mongolian Stock Exchange — Dashboard Concept")
    st.markdown("---")
    c1,c2,c3,c4 = st.columns(4)
    with c1: st.markdown("<div class='kpi-card'><div class='kpi-label'>TOP-20 Index</div><div class='kpi-value'>34,821</div><div class='green'>▲ +1.2%</div></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='kpi-card'><div class='kpi-label'>MSE ALL</div><div class='kpi-value'>28,410</div><div class='red'>▼ -0.4%</div></div>", unsafe_allow_html=True)
    with c3: st.markdown("<div class='kpi-card'><div class='kpi-label'>Market Cap</div><div class='kpi-value'>₮6.2T</div><div class='green'>▲ +0.8%</div></div>", unsafe_allow_html=True)
    with c4: st.markdown("<div class='kpi-card'><div class='kpi-label'>Daily Trading</div><div class='kpi-value'>₮1.4B</div><div class='green'>▲ +5.2%</div></div>", unsafe_allow_html=True)
    st.markdown("### 📰 Latest Disclosures")
    st.dataframe(pd.DataFrame({"Date":["2026-05-12","2026-05-11","2026-05-10"],"Company":["APU","GLMT","GOV"],"Title":["Q1 2026 Financial Report","AGM Notice","Board Decision"],"Type":["Report","Meeting","Decision"]}), use_container_width=True, hide_index=True)
    st.markdown("### 📋 Financial Reports")
    st.dataframe(pd.DataFrame({"Date":["2026-05-08","2026-05-07"],"Company":["GLMT","APU"],"Period":["Q1 2026","Q1 2026"],"Type":["Quarterly","Quarterly"]}), use_container_width=True, hide_index=True)

elif page == "📊 Securities Overview":
    st.title("Securities Overview")
    st.caption("Full securities universe from open.mse.mn")
    st.markdown("---")
    c1,c2,c3,c4 = st.columns(4)
    with c1: st.markdown("<div class='kpi-card'><div class='kpi-label'>Listed Companies</div><div class='kpi-value'>261</div><div class='green'>Equity</div></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='kpi-card'><div class='kpi-label'>Debt Instruments</div><div class='kpi-value'>42</div><div class='green'>Bonds</div></div>", unsafe_allow_html=True)
    with c3: st.markdown("<div class='kpi-card'><div class='kpi-label'>ABS</div><div class='kpi-value'>16</div><div class='green'>Asset-backed</div></div>", unsafe_allow_html=True)
    with c4: st.markdown("<div class='kpi-card'><div class='kpi-label'>Investment Funds</div><div class='kpi-value'>3</div><div class='green'>Mutual Funds</div></div>", unsafe_allow_html=True)
    st.markdown("---")
    c_l, c_r = st.columns(2)
    with c_l:
        st.markdown("### 🏢 Listed Companies (preview)")
        st.dataframe(df_co.head(5), use_container_width=True)
    with c_r:
        st.markdown("### 📋 Debt Instruments (preview)")
        st.dataframe(df_debt.head(5), use_container_width=True)

elif page == "🏢 Listed Companies":
    st.title("Listed Companies")
    st.caption("261 companies listed on MSE")
    st.markdown("---")
    search = st.text_input("🔍 Search by symbol or name", placeholder="e.g. APU or Голомт")
    filtered = df_co[df_co["Symbol"].str.contains(search, case=False) | df_co["Company Name"].str.contains(search, case=False)] if search else df_co
    st.caption(f"Showing {len(filtered)} results (sample of 20)")
    st.dataframe(filtered, use_container_width=True)

elif page == "📋 Other Securities":
    st.title("Other Securities")
    st.caption("Debt · ABS · Funds")
    st.markdown("---")
    t1,t2,t3 = st.tabs(["📄 Debt Instruments (42)","🏦 ABS (16)","💼 Funds (3)"])
    with t1: st.dataframe(df_debt, use_container_width=True)
    with t2: st.dataframe(df_abs, use_container_width=True)
    with t3: st.dataframe(df_funds, use_container_width=True)

elif page == "ℹ️ About":
    st.title("About")
    st.markdown("""
### 📈 Open MSE Dashboard
Dashboard prototype built using public MSE data.

**Sources:** open.mse.mn/securities · mse.mn  
**Built by:** MSE Intern — May 2026  
**Stack:** Python · Streamlit · Pandas

> KPI numbers are illustrative placeholders for the prototype.
    """)
