from app.model.user import User
from app.model.gambar import Gambar
from app import response, app, db, uploadconfig
import uuid
from werkzeug.utils import secure_filename
from flask import request
import os
from flask_jwt_extended import *
import datetime

def upload():
    try:
        judul = request.form.get('judul')
        
         # Check if file is in the request
        if 'file' not in request.files:
            return response.badRequest([], 'File tidak tersedia')
        
        file = request.files['file']
        
        # Ensure file is not empty
        if file.filename == '':
            return response.badRequest([], 'Silahkan upload file')
        
        # Check if file is allowed
        if file and uploadconfig.allowed_file(file.filename):  # Perhatikan besar kecil huruf 'uploadConfig'
            uid = uuid.uuid4()
            filename = secure_filename(file.filename)
            renamefile = "Flask-"+str(uid)+filename

             # Save file to the configured upload folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))
            
            # Add file information to the database
            upload = gambar(judul=judul, pathname=renamefile)
            db.session.add(upload)
            db.session.commit()

            return response.success(
                {
                    'judul': judul,
                    'pathname': renamefile
                },
                "Sukses upload File"
            )
        else:
            return response.badRequest([], 'File tidak diizinkan')
    
    except Exception as e:
        print(e)


def buatAdmin():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        level = 1
        
        users = User(name=name, email=email, level=level)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()
        
        return response.success('', 'sukses menambahkan Admin')
    except Exception as e:
        print(e)

def singleObject(data):
   data = {
        'id': data.id,
        'name': data.name,
        'email': data.email,
        'level': data.level
    }
   
   return data

def login():
    try:
        # Proses login di sini
        if request.is_json:
            email = request.json.get('email')
            password = request.json.get('password')
        else:
            email = request.form.get('email')
            password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            return response.badRequest([], 'Email tidak terdaftar')

        if not user.checkPassword(password):
            return response.badRequest([], 'Kombinasi password salah')

        data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "level": user.level
        }

        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=7)

        access_token = create_access_token(identity=user.id, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(identity=user.id, expires_delta=expires_refresh)

        return response.success({
            "data": data,
            "access_token": access_token,
            "refresh_token": refresh_token
        }, "Sukses Login!")

    except Exception as e:
        print(e)
        return response.badRequest([], 'Terjadi kesalahan pada server')
    
    # Set untuk daftar hitam token
BLACKLIST = set()

def logout():
    try:
        # Gunakan jwt_required untuk memastikan pengguna sudah login
        @jwt_required()
        def process_logout():
            # Mendapatkan "jti" dari token JWT
            jti = get_jwt()["jti"]
            # Menambahkan jti ke daftar hitam
            BLACKLIST.add(jti)
            return response.success('', 'Logout berhasil')

        return process_logout()
    except Exception as e:
        print(e)
        return response.badRequest([], 'Terjadi kesalahan saat logout')
    

        




