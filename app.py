
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cau hinh trang web
st.set_page_config(
    page_title="Quan ly diem sinh vien",
    page_icon="📚",
    layout="wide"
)

st.title("QUAN LY DIEM SINH VIEN")
st.write("Ung dung tinh diem tong ket va xep loai sinh vien")

# Tao du lieu 10 sinh vien
data = {
    "Ho_ten": [
        "An", "Binh", "Cuong", "Dung", "Giang",
        "Huy", "Lan", "Minh", "Nam", "Phuong"
    ],
    "Chuyen_can": [9, 8, 7, 10, 6, 9, 8, 7, 5, 10],
    "Giua_ky": [8, 7, 6, 9, 5, 8, 9, 6, 4, 9],
    "Cuoi_ky": [9, 8, 7, 9, 6, 8, 9, 7, 5, 10]
}

df = pd.DataFrame(data)

# Tinh diem tong ket
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
)

# Xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Hien thi bang diem
st.header("1. Bang diem sinh vien")
st.dataframe(
    df.round(2),
    use_container_width=True,
    hide_index=True
)

# Thong ke
st.header("2. Thong ke ket qua")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Diem trung binh", f"{df['Tong_ket'].mean():.2f}")
col2.metric("Diem cao nhat", f"{df['Tong_ket'].max():.2f}")
col3.metric("Diem thap nhat", f"{df['Tong_ket'].min():.2f}")
col4.metric("So sinh vien dat", int((df["Tong_ket"] >= 5).sum()))

# Xem chi tiet mot sinh vien
st.header("3. Chi tiet sinh vien")

ten = st.selectbox("Chon sinh vien", df["Ho_ten"])
sv = df[df["Ho_ten"] == ten].iloc[0]

st.write("Ho ten:", sv["Ho_ten"])
st.write("Diem chuyen can:", sv["Chuyen_can"])
st.write("Diem giua ky:", sv["Giua_ky"])
st.write("Diem cuoi ky:", sv["Cuoi_ky"])
st.write("Diem tong ket:", round(sv["Tong_ket"], 2))
st.write("Xep loai:", sv["Xep_loai"])

# Bieu do diem
st.header("4. Bieu do diem tong ket")

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_xlabel("Sinh vien")
ax.set_ylabel("Diem tong ket")
ax.set_title("Diem tong ket cua 10 sinh vien")
ax.set_ylim(0, 10)

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# Thong tin nguoi thuc hien
st.divider()
st.write("Nguoi thuc hien: Tran Quoc Viet")
st.write("Ma sinh vien: 58")
