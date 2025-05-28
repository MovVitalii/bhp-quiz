import streamlit as st

# Конфігурація сторінки
st.set_page_config(page_title='Test BHP', page_icon='🦺')

# Заголовок
st.title('🦺 Test BHP')

# Список питань
quiz = quiz = [
    {
        "question": "Jaki jest ogólny numer alarmowy w Polsce?",
        "options": ["111", "112", "999"],
        "answer": 1
    },
    {
        "question": "Co powinieneś zrobić, gdy zauważysz pożar na magazynie?",
        "options": [
            "Ukryć się i przeczekać",
            "Natychmiast powiadomić odpowiednie służby i ewakuować się",
            "Zignorować, jeśli jest mały"
        ],
        "answer": 1
    },
    {
        "question": "Gdzie powinien znajdować się gaśnica na magazynie?",
        "options": [
            "W miejscu trudno dostępnym",
            "W wyznaczonym, oznakowanym miejscu",
            "W szafce w biurze kierownika"
        ],
        "answer": 1
    },
    {
        "question": "Jakiego rodzaju gaśnicy używa się do gaszenia urządzeń elektrycznych?",
        "options": ["Wodnej", "Proszkowej", "Pianowej"],
        "answer": 1
    },
    {
        "question": "Czy wolno blokować wyjścia ewakuacyjne?",
        "options": ["Tak, jeśli to tymczasowe", "Nie", "Tak, jeśli jest mało miejsca"],
        "answer": 1
    },
    {
        "question": "Co oznacza czerwony znak z symbolem płomienia?",
        "options": [
            "Strefa zagrożenia pożarowego",
            "Miejsce sprzętu przeciwpożarowego",
            "Zakaz palenia"
        ],
        "answer": 1
    },
    {
        "question": "Jak często powinny być przeprowadzane ćwiczenia ewakuacyjne?",
        "options": ["Co miesiąc", "Co rok", "Co 5 lat"],
        "answer": 1
    },
    {
        "question": "Co należy zrobić w przypadku rozlania substancji łatwopalnej?",
        "options": [
            "Zostawić do wyschnięcia",
            "Zgłosić przełożonemu i usunąć zgodnie z procedurami",
            "Zetrzeć papierem i wyrzucić do kosza"
        ],
        "answer": 1
    },
    {
        "question": "Czy palenie tytoniu w magazynie jest dozwolone?",
        "options": ["Tak, w miejscu pracy", "Tylko przy otwartym oknie", "Nie, jest zabronione"],
        "answer": 2
    },
    {
        "question": "Jakie środki ochrony indywidualnej są obowiązkowe na magazynie?",
        "options": [
            "Okulary przeciwsłoneczne",
            "Kask, kamizelka odblaskowa, obuwie ochronne",
            "T-shirt i dżinsy"
        ],
        "answer": 1
    },
    {
        "question": "Co należy zrobić, jeśli kolega z pracy straci przytomność?",
        "options": [
            "Zignorować, może mu przejdzie",
            "Zastosować pierwszą pomoc i wezwać pomoc",
            "Wyciągnąć telefon i nagrać sytuację"
        ],
        "answer": 1
    },
    {
        "question": "Jakie jest pierwsze działanie przy krwotoku zewnętrznym?",
        "options": [
            "Położyć poszkodowanego i unieść nogi",
            "Zatamować krwawienie uciskiem",
            "Podać wodę"
        ],
        "answer": 1
    },
    {
        "question": "Gdzie należy zgłosić każdy wypadek przy pracy?",
        "options": [
            "Do działu kadr",
            "Do przełożonego lub kierownika zmiany",
            "Nie trzeba zgłaszać"
        ],
        "answer": 1
    },
    {
        "question": "Które przepisy regulują zasady BHP w Polsce?",
        "options": [
            "Kodeks drogowy",
            "Kodeks pracy",
            "Prawo celne"
        ],
        "answer": 1
    },
    {
        "question": "Czy należy przestrzegać wewnętrznych przepisów magazynu?",
        "options": [
            "Tylko jeśli są podpisane przez pracownika",
            "Tak, są obowiązujące dla wszystkich pracowników",
            "Nie, są tylko propozycją"
        ],
        "answer": 1
    },
    
{
    "question": "Podczas pożaru zauważasz kolegę, który nie może sam się ewakuować. Co powinieneś zrobić?",
    "options": [
        "Spróbuj pomóc koledze, ale tylko jeśli nie zagraża to Twojemu życiu i wiesz, jak to zrobić",
        "Zignoruj sytuację i skup się na własnej ewakuacji",
        "Wynieś kolegę bez względu na ryzyko"
    ],
    "answer": 0
}
]


user_answers = []
score = 0

# Форма з тестом
with st.form("quiz_form"):
    st.write("📋 Wybierz prawidłowe odpowiedzi:")
    for i, q in enumerate(quiz):
        st.subheader(f"{i + 1}. {q['question']}")
        answer = st.radio("", q["options"], key=f"q_{i}", index = None)
        user_answers.append(answer)

    submitted = st.form_submit_button("✅ Zakończ test")

# Після відправлення форми
if submitted:
    st.subheader("📊 Wyniki:")
    for i, q in enumerate(quiz):
        correct_option = q["options"][q["answer"]]
        if user_answers[i] == correct_option:
            st.success(f"{i + 1}. ✅ Poprawnie: {q['question']}")
            score += 1
        else:
            st.error(f"{i + 1}. ❌ Niepoprawnie: {q['question']}")
            st.info(f"   ✅ Poprawna odpowiedź: {correct_option}")

    st.markdown("---")
    st.write(f"## 🏁 Twój wynik: **{score} z {len(quiz)}**")

    # Додаткове повідомлення
    if score == len(quiz):
        st.balloons()
        st.success("🎉 Gratulacje! Zdałeś test perfekcyjnie!")
    elif score >= len(quiz) * 0.6:
        st.info("😊 Dobra robota, ale możesz się jeszcze poprawić.")
    else:
        st.warning("⚠️ Warto jeszcze raz przećwiczyć temat BHP.")
