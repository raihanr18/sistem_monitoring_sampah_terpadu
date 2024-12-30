from . import db

class Simpul(db.Model):
    __tablename__ = 'simpul'
    id_simpul = db.Column(db.Integer, primary_key=True)
    nama_simpul = db.Column(db.String(100))
    jenis_simpul = db.Column(db.Enum('TPS', 'TPA', 'JALAN'))
    latitude = db.Column(db.Numeric(10, 8))
    longitude = db.Column(db.Numeric(11, 8))

class Graf(db.Model):
    __tablename__ = 'graf'
    id_graf = db.Column(db.Integer, primary_key=True)
    id_simpul_mulai = db.Column(db.Integer, db.ForeignKey('simpul.id_simpul'))
    id_simpul_tujuan = db.Column(db.Integer, db.ForeignKey('simpul.id_simpul'))
    jarak = db.Column(db.Numeric(10, 2))

class Tps(db.Model):
    __tablename__ = 'tps'
    id_tps = db.Column(db.Integer, primary_key=True)
    nama_tps = db.Column(db.String(100))
    alamat_tps = db.Column(db.String(255))
    volume = db.Column(db.Integer)
    id_simpul = db.Column(db.Integer, db.ForeignKey('simpul.id_simpul'))

class Tpa(db.Model):
    __tablename__ = 'tpa'
    id_tpa = db.Column(db.Integer, primary_key=True)
    nama_tpa = db.Column(db.String(100))
    alamat_tpa = db.Column(db.String(255))
    id_simpul = db.Column(db.Integer, db.ForeignKey('simpul.id_simpul'))

class Armada(db.Model):
    __tablename__ = 'armada'
    id_armada = db.Column(db.Integer, primary_key=True)
    plat_nomor = db.Column(db.String(20))
    alamat_armada = db.Column(db.String(255))
    kapasitas = db.Column(db.Integer)
    id_simpul = db.Column(db.Integer, db.ForeignKey('simpul.id_simpul'))
