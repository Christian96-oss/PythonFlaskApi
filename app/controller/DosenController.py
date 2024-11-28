from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app import response, app, db
from flask import request

def index():
    try:
        dosen = Dosen.query.all()
        data = formatarray(dosen)
        return response.success(data, "success")
    except Exception as e:
        print(e)
        return response.badRequest([], "Terjadi kesalahan")

def formatarray(data):
    array = []
    for i in data:
        array.append(singleObject(i))
    return array

def singleObject(data):
    return {
        'id': data.id,
        'nidn': data.nidn,
        'nama': data.nama,
        'phone': data.phone,
        'alamat': data.alamat
    }

def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter(
            (Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id)
        ).all()
        
        if not dosen:
            return response.badRequest([], 'tidak ada data dosen')

        datamahasiswa = formatMahasiswa(mahasiswa)
        data = singleDetailMahasiswa(dosen, datamahasiswa)
        return response.success(data, "success")
    
    except Exception as e:
        print(e)
        return response.badRequest([], "Terjadi kesalahan")

def formatMahasiswa(data):
    array = []
    for i in data:
        array.append(singleMahasiswa(i))
    return array

def save():
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')
        
        dosens = Dosen(nidn=nidn, nama=nama, phone=phone, alamat=alamat)
        db.session.add(dosens)
        db.session.commit()
        
        return response.success('', 'sukses menambahkan data Dosen')
    except Exception as e:
        print(e)

def ubah(id):
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')
        
        input = [
            {
                'nidn': nidn,
                'nama': nama,
                'phone': phone,
                'alamat': alamat
            }
        ]
        
        dosen = Dosen.query.filter_by(id=id).first()
        dosen.nidn = nidn
        dosen.nama = nama
        dosen.phone = phone
        dosen.alamat = alamat
        
        db.session.commit()
        return response.success(input, 'Sukses update data')
    except Exception as e:
        print(e)

def hapus(id):
    try:  # Memastikan blok try memiliki indentasi yang benar
        dosen = Dosen.query.filter_by(id=id).first()
        if not dosen:
            return response.badRequest([], 'Data Dosen Kosong ....')
        
        db.session.delete(dosen)
        db.session.commit()
        
        return response.success('', 'berhasil menghapus data')
    except Exception as e:
        print(e)

def singleMahasiswa(mahasiswa):
    return {
        'id': mahasiswa.id,
        'nim': mahasiswa.nim,
        'nama': mahasiswa.nama,
        'phone': mahasiswa.phone
    }

def singleDetailMahasiswa(dosen, mahasiswa):
    return {
        'id': dosen.id,
        'nidn': dosen.nidn,
        'nama': dosen.nama,
        'phone': dosen.phone,
        'mahasiswa': mahasiswa
    }
