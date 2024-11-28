from app.model.mahasiswa import Mahasiswa
from app import response, app, db
from flask import request

# Fungsi untuk mendapatkan daftar Mahasiswa
def index():
    try:
        mahasiswa = Mahasiswa.query.all()  # Ambil data mahasiswa dari database
        data = formatarray(mahasiswa)  # Format data agar sesuai dengan response
        return response.success(data, "success")  # Mengembalikan response success
        except Exception as e:
        print(e)  # Tampilkan error jika ada
        return response.badRequest([], "Terjadi kesalahan")

# Fungsi untuk memformat data dosen menjadi array
def formatarray(data):
    array = []
    
    for i in data:  # Perbaiki 'datas' menjadi 'data'
        array.append(singleObject(i))  # Memasukkan data dalam format tertentu
        
    return array  # Pastikan return di luar loop agar semua data dikembalikan

# Fungsi untuk memformat data dosen menjadi dictionary
def singleObject(data):
    return {  # Format data dosen
        'id': data.id,
        'nidn': data.nim,
        'nama': data.nama,
        'phone': data.phone,
        'alamat': data.alamat,
        'dosen_satu': data.dosen_satu,
        'dosen_dua': data.dosen_dua
    }
