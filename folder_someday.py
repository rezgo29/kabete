import streamlit as st

def main():
    st.title("My Folder")

    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Go to", ["2024", "2025", "2026", "2027", "2028"])

    if selected_page == "2024":
        page_2024()
    elif selected_page == "2025":
        page_2025()
    elif selected_page == "2026":
        page_2026()
    elif selected_page == "2027":
        page_2027()
    elif selected_page == "2028":
        page_2028()

def add_copyright():
    st.write("---")
    st.write("© Imam Nur Rizky Gusman 5003211121")

def page_2024():
    st.write("---")
    st.write("# Welcome to 2024")
    st.write("""
             ## Pencapaian
            - Memiliki pengalaman magang minimal satu kali
            - Mengikuti program Bangkit Academy
             ## Rencana
             - Meningkatkan IPK
             - Lulus nilai minimum TOEFL
             - Menyelesaikan Studi
             - Meningkatkan penjualan usaha (Amway Product)
             - Merancang ide bisnis untuk orang tua
             """)
    add_copyright()

def page_2025():
    st.write("---")
    st.write("# Welcome to 2025")
    st.write("""
            ## Rencana
             - Menyelesaikan studi bila rencana 2024 belum terpenuhi
             - Bekerja di perusahaan multinasional
             - Memulai bisnis yang sudah dirancang di tahun 2024
             - Menemukan pasangan
             """)
    add_copyright()

def page_2026():
    st.write("---")
    st.write("# Welcome to 2026")
    st.write("""
            ## Rencana
             - Meningkatkan karir di company
             - Memperluas relasi bisnis
             - Memiliki rumah dan kendaraan lengkap
             - Married
             """)
    add_copyright()

def page_2027():
    st.write("---")
    st.write("# Welcome to 2027")
    st.write("""
            ## Rencana
             - Mengembangkan lini bisnis
             - Mendirikan kerajaan bisnis
             - Mempelajari peta politik Indonesia
             - Memiliki networking yang kuat dengan pejabat negara dan pengendali ekonomi Indonesia
             """)
    add_copyright()

def page_2028():
    st.write("---")
    st.write("# Welcome to 2028")
    st.write("""
            ## Rencana
             - Mengembangkan kerajaan bisnis
             - Masuk kabinet pemerintahan 2024-2029
             - Mempersiapkan diri menuju kabinet pemerintahan Indonesia 2029
             """)
    add_copyright()

if __name__ == "__main__":
    main()
