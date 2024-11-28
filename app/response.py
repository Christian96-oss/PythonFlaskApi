from flask import jsonify, make_response

# Fungsi untuk response sukses
def success(values, message):
    res = {
        'data': values, 
        'message': message
    }
    return make_response(jsonify(res), 200)  # Pastikan tidak ada koma di sini

# Fungsi untuk response Bad Request
def badRequest(values, message):
    res = {
        'data': values,
        'message': message
    }
    return make_response(jsonify(res), 400)  # Pastikan tidak ada koma di sini
