from app import db
from app.model.dosen import Dosen  # Pastikan Dosen diimpor dengan benar

class Mahasiswa(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)  # ID mahasiswa
    nim = db.Column(db.String(30), nullable=False)
    nama = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    dosen_satu = db.Column(db.BigInteger, db.ForeignKey(Dosen.id, ondelete='CASCADE'))  # Perbaiki dengan Dosen.id
    dosen_dua = db.Column(db.BigInteger, db.ForeignKey(Dosen.id, ondelete='CASCADE'))  # Perbaiki dengan Dosen.id
    
    def __repr__(self):
        return '<Mahasiswa {}>'.format(self.nama)
