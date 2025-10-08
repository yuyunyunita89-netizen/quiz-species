# quiz_bilangan_bulat_streamlit.py
import streamlit as st

questions = [
    {"soal": "Hasil dari 5 + (-3) adalah ...", "options": ["8", "2", "-2", "-8"], "answer": "2"},
    {"soal": "Hasil dari (-7) + 4 adalah ...", "options": ["11", "-3", "3", "-11"], "answer": "-3"},
    {"soal": "Hasil dari (-12) - (-5) adalah ...", "options": ["-17", "-7", "7", "17"], "answer": "-7"},
    {"soal": "Hasil dari 15 - 20 adalah ...", "options": ["-5", "5", "-35", "35"], "answer": "-5"},
    {"soal": "Hasil dari (-6) × 3 adalah ...", "options": ["-18", "18", "-9", "9"], "answer": "-18"},
    {"soal": "Hasil dari (-8) × (-2) adalah ...", "options": ["16", "-16", "10", "-10"], "answer": "16"},
    {"soal": "Hasil dari 25 ÷ (-5) adalah ...", "options": ["5", "-5", "20", "-20"], "answer": "-5"},
    {"soal": "Hasil dari (-36) ÷ (-6) adalah ...", "options": ["-6", "6", "-12", "12"], "answer": "6"},
    {"soal": "Nilai dari | -15 | adalah ...", "options": ["-15", "0", "15", "30"], "answer": "15"},
    {"soal": "Nilai dari | 12 | adalah ...", "options": ["-12", "0", "12", "24"], "answer": "12"},
    {"soal": "Hasil dari (-4)² adalah ...", "options": ["-16", "16", "-8", "8"], "answer": "16"},
    {"soal": "Hasil dari (-5)³ adalah ...", "options": ["-125", "125", "-15", "15"], "answer": "-125"},
    {"soal": "Hasil dari 0 ÷ (-7) adalah ...", "options": ["0", "-7", "1", "Tidak terdefinisi"], "answer": "0"},
    {"soal": "Hasil dari (-20) ÷ 0 adalah ...", "options": ["0", "Tak terdefinisi", "20", "-20"], "answer": "Tak terdefinisi"},
    {"soal": "Hasil dari 9 + (-12) adalah ...", "options": ["21", "-3", "3", "-21"], "answer": "-3"},
    {"soal": "Hasil dari (-30) - 15 adalah ...", "options": ["-15", "15", "-45", "45"], "answer": "-45"},
    {"soal": "Hasil dari 18 ÷ (-3) adalah ...", "options": ["6", "-6", "15", "-15"], "answer": "-6"},
    {"soal": "Hasil dari (-2) × (-9) adalah ...", "options": ["-18", "18", "-11", "11"], "answer": "18"},
    {"soal": "Nilai dari | -25 | + | 10 | adalah ...", "options": ["-15", "15", "35", "-35"], "answer": "35"},
    {"soal": "Hasil dari (-50) + (-25) adalah ...", "options": ["-75", "75", "-25", "25"], "answer": "-75"}
]

st.title("Quiz Bilangan Bulat Matematika")

score = 0

# Buat form untuk setiap soal
for i, q in enumerate(questions, start=1):
    st.subheader(f"Soal {i}: {q['soal']}")
    pilihan = st.radio("Pilih jawabanmu:", q["options"], key=i)
    if st.button("Cek Jawaban", key=f"cek{i}"):
        if pilihan == q["answer"]:
            st.success("✅ Benar!")
            score += 1
        else:
            st.error(f"❌ Salah! Jawaban benar: {q['answer']}")

# Tampilkan hasil akhir
st.subheader("Hasil Quiz")
st.write(f"Skor: {score} dari {len(questions)}")
nilai = (score / len(questions)) * 100
st.write(f"Nilai akhir: {nilai:.2f}")
