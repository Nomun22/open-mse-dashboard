import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# -----------------------------
# BASIC CONFIG
# -----------------------------
st.set_page_config(
    page_title="MSE Market Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# LANGUAGE TOGGLE
# -----------------------------
if "lang" not in st.session_state:
    st.session_state["lang"] = "en"

def t(key: str) -> str:
    """Simple translation helper."""
    lang = st.session_state["lang"]
    labels = {
        "app_title": {"en": "MSE Market Dashboard", "mn": "МХБ Зах зээлийн хяналтын самбар"},
        "hero_market_overview": {"en": "Market Overview", "mn": "Зах зээлийн тойм"},
        "index_performance": {"en": "Index Performance", "mn": "Индексийн гүйцэтгэл"},
        "breadth_header": {"en": "Market Breadth & Sentiment", "mn": "Зах зээлийн өргөн ба сэтгэлзүй"},
        "sector_header": {"en": "Sector Performance", "mn": "Салбаруудын гүйцэтгэл"},
        "top20_header": {"en": "Top 20 Companies", "mn": "Хамгийн идэвхтэй 20 хувьцаа"},
        "disclosures_header": {"en": "Latest Disclosures", "mn": "Сүүлд гарсан мэдээлэл"},
        "meetings_header": {"en": "Shareholders’ Meetings", "mn": "Хувьцаа эзэмшигчдийн хурал"},
        "news_header": {"en": "Market News", "mn": "Зах зээлийн мэдээ"},
        "kpi_top20": {"en": "TOP-20 Index", "mn": "ТОП-20 индекс"},
        "kpi_mse_all": {"en": "MSE ALL Index", "mn": "МХБ Нийт индекс"},
        "kpi_trading_value": {"en": "Daily Trading Value", "mn": "Өдрийн арилжааны үнийн дүн"},
        "kpi_market_cap": {"en": "Total Market Capitalization", "mn": "Зах зээлийн нийт үнэлгээ"},
        "kpi_listed_comp": {"en": "Listed Companies", "mn": "Бүртгэлтэй компани"},
        "breadth_adv": {"en": "Advancing", "mn": "Өссөн"},
        "breadth_dec": {"en": "Declining", "mn": "Уналттай"},
        "breadth_unch": {"en": "Unchanged", "mn": "Хувираагүй"},
        "breadth_sentiment": {"en": "Market Sentiment", "mn": "Зах зээлийн сэтгэлзүй"},
        "sentiment_bull": {"en": "Bullish", "mn": "Өсөлт давамгай"},
        "sector": {"en": "Sector", "mn": "Салбар"},
        "change_today": {"en": "Change today", "mn": "Өнөөдрийн өөрчлөлт"},
        "top20_ticker": {"en": "Ticker", "mn": "Тикер"},
        "top20_name": {"en": "Company", "mn": "Компанийн нэр"},
        "top20_price": {"en": "Price (MNT)", "mn": "Ханш (₮)"},
        "top20_change": {"en": "Change (%)", "mn": "Өөрчлөлт (%)"},
        "top20_value": {"en": "Turnover (MNT M)", "mn": "Эргэлт (сая ₮)"},
        "nav_contact": {"en": "Contact us", "mn": "Холбоо барих"},
        "nav_support": {"en": "Support", "mn": "Тусламж"},
        "nav_lang": {"en": "EN / MN", "mn": "MN / EN"},
        "hero_subtitle": {
            "en": "Live market snapshot for the Mongolian Stock Exchange.",
            "mn": "Монголын Хөрөнгийн биржийн өнөөгийн зах зээлийн тойм.",
        },
    }
    return labels.get(key, {}).get(lang, key)

# -----------------------------
# TOP NAV BAR
# -----------------------------
def render_top_nav():
    col_logo, col_spacer, col_lang, col_contact, col_support = st.columns(
        [3, 6, 1.5, 1.5, 1.5]
    )

    with col_logo:
        st.markdown(
            """
            <div style="
                font-size:22px;
                font-weight:700;
                color:#004187;
                padding:8px 0;
            ">
                MSE | Mongolian Stock Exchange
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_lang:
        if st.button(t("nav_lang")):
            st.session_state["lang"] = "mn" if st.session_state["lang"] == "en" else "en"

    with col_contact:
        st.button(t("nav_contact"))

    with col_support:
        st.button(t("nav_support"))

render_top_nav()

st.markdown("---")

# -----------------------------
# SAMPLE DATA (STATIC PLACEHOLDERS)
# -----------------------------
dates = pd.date_range(end=datetime.now(), periods=60, freq="D")

def make_index_series(base: float, drift: float) -> pd.Series:
    return pd.Series(
        [base + i * drift + (i % 5) * drift * 1.8 for i in range(len(dates))],
        index=dates,
    )

top20_series = make_index_series(50000, 55)
mse_all_series = make_index_series(48000, 40)
mse_b_series = make_index_series(28000, 25)

# KPIs (placeholder numbers)
kpi_values = {
    "top20": {"value": "55,047.72", "change": "+2.36%"},
    "mse_all": {"value": "48,410.33", "change": "+1.12%"},
    "trading_value": {"value": "₮26.8B", "change": "+5.2%"},
    "market_cap": {"value": "₮13.1T", "change": "+0.9%"},
    "listed_comp": {"value": "261", "change": "+0"},
}

# Top 20 table (simplified)
top20_data = pd.DataFrame(
    {
        "rank": list(range(1, 21)),
        "ticker": [
            "KHAN",
            "TTL",
            "ERDN",
            "GLMT",
            "APU",
            "XAC",
            "TDB",
            "INV",
            "SBM",
            "CUMN",
            "MIK",
            "SUU",
            "GOV",
            "LEND",
            "UID",
            "MDIC",
            "MSE",
            "GTL",
            "MGLA",
            "MLG",
        ],
        "name_en": [
            "Khan Bank",
            "Tavan Tolgoi",
            "Erdenes Resource Development",
            "Golomt Bank",
            "APU",
            "Xac Bank",
            "Khan Bank JSC",
            "Invescore NBFI",
            "State Bank",
            "Premium Nexus",
            "MIK Holding",
            "Suu",
            "Gobi",
            "LendMN NBFI",
            "Usnii Ikh Delguur",
            "Mongol Daatgal",
            "Mongolian Stock Exchange",
            "Gutal",
            "Mongolian Gold",
            "Monlogistics Holding",
        ],
        "name_mn": [
            "Хаан банк",
            "Таван толгой",
            "Эрдэнэс ресурс девелопмент",
            "Голомт банк",
            "АПУ",
            "Хас банк",
            "Худалдаа хөгжлийн банк",
            "Инвескор ББСБ",
            "Төрийн банк",
            "Премиум нексус",
            "МИК холдинг",
            "Сүү",
            "Говь",
            "ЛэндМН ББСБ",
            "Үсрийн их дэлгүүр",
            "Монгол даатгал",
            "Монголын хөрөнгийн бирж",
            "Гутал",
            "Монголын алт",
            "Монложистикс холдинг",
        ],
        "price": [
            1380,
            31440,
            20340,
            1332,
            976.29,
            922,
            19220,
            800,
            4080,
            3966.57,
            3144.45,
            622.81,
            62.03,
            800.0,
            340.0,
            12181.45,
            351.0,
            709.0,
            2086.0,
            7621.18,
        ],
        "change_pct": [
            1.61,
            -7.52,
            12.08,
            7.25,
            -2.40,
            -0.85,
            -23.07,
            -3.80,
            -2.47,
            2.09,
            2.24,
            41.45,
            0.10,
            -3.80,
            -2.50,
            1.40,
            -1.97,
            0.58,
            3.27,
            2.10,
        ],
        "turnover_m": [
            3735.5,
            360.5,
            122.9,
            80.9,
            69.7,
            20.9,
            18.6,
            10.4,
            48.1,
            39.3,
            22.7,
            19.0,
            7.8,
            80.0,
            4.1,
            6.4,
            16.4,
            3.5,
            3.3,
            2.2,
        ],
    }
)

# Disclosures, meetings, and news (shortened)
disclosures = pd.DataFrame(
    {
        "date": ["2026-05-12", "2026-05-11", "2026-05-10", "2026-05-09"],
        "ticker": ["APU", "GLMT", "GOV", "AIC"],
        "title_en": [
            "Q1 2026 Financial Report",
            "Annual General Meeting Notice",
            "Board Decision",
            "Dividend Announcement",
        ],
        "title_mn": [
            "2026.I улирлын санхүүгийн тайлан",
            "Жилийн ээлжит хурлын мэдэгдэл",
            "ТУЗ-ийн шийдвэр",
            "Ногдол ашиг хуваарилах тухай",
        ],
    }
)

meetings = pd.DataFrame(
    {
        "date": ["2026-05-20", "2026-05-18", "2026-05-15", "2026-05-10"],
        "ticker": ["APU", "GLMT", "MNDL", "ERDN"],
        "type_en": ["AGM", "EGM", "AGM", "Board meeting"],
        "type_mn": ["Жилийн хурал", "Онцгой хурал", "Жилийн хурал", "ТУЗ-ийн хурал"],
    }
)

news_items = [
    {
        "date": "2026-05-12",
        "title_en": "Total trading volume reached 26.8 billion MNT today",
        "title_mn": "Өнөөдрийн нийт арилжааны үнийн дүн 26.8 тэрбум төгрөгт хүрлээ",
        "summary_en": "The exchange organized trading worth 26.8 billion MNT across equities and bonds.",
        "summary_mn": "Хувьцаа болон бондын зах зээл дээрх нийт арилжааны үнийн дүн 26.8 тэрбум төгрөг байв.",
    },
    {
        "date": "2026-05-11",
        "title_en": "Government bond auction successfully completed",
        "title_mn": "Засгийн газрын үнэт цаасны дуудлага худалдаа амжилттай боллоо",
        "summary_en": "More than 9.5 billion MNT of government securities were placed in the primary market.",
        "summary_mn": "Анхдагч зах зээл дээр 9.5 тэрбум төгрөгийн засгийн газрын үнэт цаасыг арилжлаа.",
    },
    {
        "date": "2026-05-10",
        "title_en": "MSE celebrates 35 years of operation",
        "title_mn": "МХБ 35 жилийн ойгоо тэмдэглэлээ",
        "summary_en": "The Mongolian Stock Exchange marks 35 years of transparent and fair market operations.",
        "summary_mn": "Монголын Хөрөнгийн бирж ил тод, шударга арилжааны 35 жилийн ойг тэмдэглэж байна.",
    },
]

# -----------------------------
# HERO SECTION – MARKET OVERVIEW
# -----------------------------
st.title(t("app_title"))
st.caption(t("hero_subtitle"))

# KPI cards
kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)

def render_kpi_card(col, label_key, value, change):
    change_val = change.strip().replace("%", "")
    try:
        change_float = float(change_val)
    except ValueError:
        change_float = 0.0
    color = "#10b981" if change_float > 0 else "#ef4444" if change_float < 0 else "#6b7280"
    with col:
        st.markdown(
            f"""
            <div style="
                background:white;
                border-radius:10px;
                padding:14px 18px;
                border-left:4px solid #004187;
                box-shadow:0 2px 6px rgba(0,0,0,0.08);
                margin-bottom:8px;
            ">
              <div style="font-size:11px;text-transform:uppercase;color:#6b7280;font-weight:600;">
                {t(label_key)}
              </div>
              <div style="font-size:24px;font-weight:700;color:#111827;margin-top:6px;">
                {value}
              </div>
              <div style="font-size:13px;font-weight:600;color:{color};margin-top:2px;">
                {change}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

render_kpi_card(kpi_col1, "kpi_top20", kpi_values["top20"]["value"], kpi_values["top20"]["change"])
render_kpi_card(
    kpi_col2, "kpi_mse_all", kpi_values["mse_all"]["value"], kpi_values["mse_all"]["change"]
)
render_kpi_card(
    kpi_col3,
    "kpi_trading_value",
    kpi_values["trading_value"]["value"],
    kpi_values["trading_value"]["change"],
)
render_kpi_card(
    kpi_col4,
    "kpi_market_cap",
    kpi_values["market_cap"]["value"],
    kpi_values["market_cap"]["change"],
)
render_kpi_card(
    kpi_col5,
    "kpi_listed_comp",
    kpi_values["listed_comp"]["value"],
    kpi_values["listed_comp"]["change"],
)

# -----------------------------
# INDEX PERFORMANCE CHARTS
# -----------------------------
st.markdown(f"### {t('index_performance')}")

chart_col1, chart_col2, chart_col3 = st.columns(3)

def render_index_chart(col, title_en, title_mn, series, color):
    title = title_en if st.session_state["lang"] == "en" else title_mn
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=series.index,
            y=series.values,
            mode="lines",
            line=dict(color=color, width=2),
            fill="tozeroy",
            fillcolor=color.replace("#", "rgba(")[:-1] + ",0.08)",
        )
    )
    fig.update_layout(
        title=title,
        xaxis_title="",
        yaxis_title="",
        margin=dict(l=10, r=10, t=40, b=10),
        height=260,
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(size=11),
    )
    with col:
        st.plotly_chart(fig, use_container_width=True)

render_index_chart(
    chart_col1,
    "TOP-20 Index (last 60 days)",
    "ТОП-20 индекс (сүүлийн 60 өдөр)",
    top20_series,
    "#004187",
)
render_index_chart(
    chart_col2,
    "MSE ALL Index (last 60 days)",
    "МХБ Нийт индекс (сүүлийн 60 өдөр)",
    mse_all_series,
    "#10b981",
)
render_index_chart(
    chart_col3,
    "MSE B Index (last 60 days)",
    "МХБ B индекс (сүүлийн 60 өдөр)",
    mse_b_series,
    "#ef4444",
)

# -----------------------------
# MARKET BREADTH & SENTIMENT
# -----------------------------
st.markdown(f"### {t('breadth_header')}")

b_col1, b_col2, b_col3, b_col4 = st.columns(4)

def simple_card(col, label, value, color="#111827", subtitle=None):
    with col:
        st.markdown(
            f"""
            <div style="
                background:white;
                border-radius:10px;
                padding:14px 18px;
                box-shadow:0 2px 6px rgba(0,0,0,0.06);
                margin-bottom:8px;
            ">
              <div style="font-size:11px;color:#6b7280;font-weight:600;text-transform:uppercase;">
                {label}
              </div>
              <div style="font-size:24px;font-weight:700;color:{color};margin-top:6px;">
                {value}
              </div>
              {f'<div style="font-size:12px;color:#6b7280;margin-top:2px;">{subtitle}</div>' if subtitle else ''}
            </div>
            """,
            unsafe_allow_html=True,
        )

simple_card(b_col1, t("breadth_adv"), "48", "#10b981", "companies")
simple_card(b_col2, t("breadth_dec"), "28", "#ef4444", "companies")
simple_card(b_col3, t("breadth_unch"), "6", "#6b7280", "companies")
sent_label = f"{t('sentiment_bull')} · 58% "
simple_card(b_col4, t("breadth_sentiment"), sent_label, "#10b981")

# -----------------------------
# SECTOR PERFORMANCE
# -----------------------------
st.markdown(f"### {t('sector_header')}")

sector_items = [
    {"en": "Banking", "mn": "Банк", "change": 0.39},
    {"en": "Mining", "mn": "Уул уурхай", "change": -1.76},
    {"en": "Insurance", "mn": "Даатгал", "change": 0.18},
    {"en": "Manufacturing", "mn": "Үйлдвэрлэл", "change": -0.44},
    {"en": "Retail", "mn": "Жижиглэн худалдаа", "change": -0.48},
    {"en": "Energy", "mn": "Эрчим хүч", "change": -0.58},
    {"en": "Finance", "mn": "Санхүү", "change": -2.18},
    {"en": "Information & Telecom", "mn": "Мэдээлэл, харилцаа", "change": -0.33},
]

s_cols = st.columns(4)
for i, sec in enumerate(sector_items):
    col = s_cols[i % 4]
    name = sec["en"] if st.session_state["lang"] == "en" else sec["mn"]
    change = sec["change"]
    color = "#10b981" if change > 0 else "#ef4444" if change < 0 else "#6b7280"
    with col:
        st.markdown(
            f"""
            <div style="
                background:white;
                border-radius:10px;
                padding:12px 14px;
                text-align:left;
                box-shadow:0 1px 4px rgba(0,0,0,0.06);
                margin-bottom:10px;
            ">
              <div style="font-size:12px;color:#6b7280;font-weight:600;">
                {name}
              </div>
              <div style="font-size:20px;font-weight:700;color:{color};margin-top:4px;">
                {change:+.2f}%
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------
# TOP 20 COMPANIES TABLE
# -----------------------------
st.markdown(f"### {t('top20_header')}")

df_top20 = top20_data.copy()
df_top20["name"] = df_top20["name_en"]
if st.session_state["lang"] == "mn":
    df_top20["name"] = df_top20["name_mn"]

df_view = df_top20[
    ["rank", "ticker", "name", "price", "change_pct", "turnover_m"]
].rename(
    columns={
        "rank": "#",
        "ticker": t("top20_ticker"),
        "name": t("top20_name"),
        "price": t("top20_price"),
        "change_pct": t("top20_change"),
        "turnover_m": t("top20_value"),
    }
)

def style_change(val):
    color = "#10b981" if val > 0 else "#ef4444" if val < 0 else "#6b7280"
    return f"color:{color};font-weight:600;"

styled = df_view.style.applymap(style_change, subset=[t("top20_change")])

st.dataframe(
    styled,
    use_container_width=True,
    hide_index=True,
    height=420,
)

# -----------------------------
# DISCLOSURES & MEETINGS
# -----------------------------
col_disc, col_meet = st.columns(2)

with col_disc:
    st.markdown(f"### {t('disclosures_header')}")
    df_d = disclosures.copy()
    df_d["title"] = df_d["title_en"]
    if st.session_state["lang"] == "mn":
        df_d["title"] = df_d["title_mn"]
    df_d = df_d[["date", "ticker", "title"]].rename(
        columns={
            "date": "Date",
            "ticker": t("top20_ticker"),
            
