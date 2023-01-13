# Query Bab 14 MDPL

show databases;
create database bab14_stdcase;
use bab14_stdcase;
show tables;

-- DROP table cabang, pinjaman, peminjaman, namanasabah, penabung, rekening;

-- pembuatan tabel

create table Cabang(
  NamaCabang varchar(25),
  KotaCabang varchar(25),
  Asset int(11),
  CONSTRAINT pk_cabang PRIMARY KEY(NamaCabang)
);

create table Pinjaman(
  NomorPinjaman char(4),
  NamaCabang varchar(25),
  Saldo int(11),
  CONSTRAINT pk_Pinjaman PRIMARY KEY (NomorPinjaman),
  CONSTRAINT fk_Pinjaman_Cabang FOREIGN KEY (NamaCabang) REFERENCES
  Cabang(NamaCabang) ON DELETE CASCADE ON UPDATE CASCADE
);

create table Peminjaman(
  NomorPinjaman char(4),
  NamaNasabah varchar(25),
  CONSTRAINT fk_Peminjaman_Pinjaman FOREIGN KEY (NomorPinjaman) 
  REFERENCES Pinjaman(NomorPinjaman) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_Peminjaman_NamaNasabah FOREIGN KEY (NamaNasabah)
  REFERENCES NamaNasabah(NamaNasabah) ON DELETE CASCADE ON UPDATE CASCADE
);

create table NamaNasabah(
  NamaNasabah varchar(25),
  JalanNasabah varchar(55),
  KotaNasabah varchar(25),
  CONSTRAINT pk_NamaNasabah PRIMARY KEY (NamaNasabah)
 );

create table Penabung(
   NamaNasabah varchar(25),
   NomorRekening varchar(25),
   CONSTRAINT fk_Penabung_NamaNasabah FOREIGN KEY (NamaNasabah)
   REFERENCES NamaNasabah(NamaNasabah) ON DELETE CASCADE ON UPDATE CASCADE,
   CONSTRAINT fk_Penabung_Rekening FOREIGN KEY(NomorRekening) 
   REFERENCES Rekening(NomorRekening) ON DELETE CASCADE ON UPDATE CASCADE
);

create table Rekening(
   NomorRekening varchar(25),
   NamaCabang varchar(25),
   Saldo int(11),
   CONSTRAINT pk_Rekening PRIMARY KEY (NomorRekening),
   CONSTRAINT fk_Rekening_Cabang FOREIGN KEY (NamaCabang) 
   REFERENCES Cabang(NamaCabang) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Input data 

insert into Cabang values 
("PT.Rambutan", "Cirebon", 10000000),
("PT.Semangka", "Indramayu", 15000000),
("PT.Jeruk", "Ciamis", 20000000),
("PT.Strawberry", "Jakarta", 30000000),
("PT.Anggur", "Bogor", 25000000),

("PT.Manggis", "Kerawang", 28000000),
("PT.Durian", "Yogyakarta", 18000000),
("PT.Quldi", "Surabaya", 8000000),
("PT.Kopi", "Solo", 8000000),
("PT.Salak", "Malang", 13000000);

insert into Pinjaman values
("ABC1","PT.Rambutan", 5000000),
("ABC2", "PT.Semangka", 6000000),
("ABC3", "PT.Jeruk", 3000000),
("ABC4", "PT.Strawberry", 4500000),
("ABC5", "PT.Anggur", 5000000),

("ABC6", "PT.Manggis", 3000000),
("ABC7", "PT.Durian",  8000000),
("ABC8","PT.Quldi", 600000),
("ABC9", "PT.Kopi", 4000000),
("ABD1", "PT.Salak", 3000000);

insert into peminjaman values 
("ABC1", "Karnoto"),
("ABC2", "Sarnoto"),
("ABC3", "Sarjono"),
("ABC4", "Saiminih"),
("ABC5", "Saman"),
("ABC6", "Sadinah"),
("ABC7", "Taiminih"),
("ABC8", "Samandika"),
("ABC9", "Arabandi"),
("ABD1", "Bagas");

insert into namanasabah values 
("Karnoto", "Jl.Jendral sudirman", "Cirebon"),
("Sarnoto", "Jl.Bongas", "Indramayu"),
("Sarjono", "Jl.Gangreng no 17", "Ciamis"),
("Saiminih", "Jl.Kein jeruk", "Jakarta"),
("Saman", "Jl.Pelangi", "Bogor"),

("Sadinah", "JL.Bagarana no 16", "Kerawang"),
("Taiminih", "JL.ring road jakal", "Yogyakarta"),
("Samandika", "Jl.selatan no 18", "Surabaya"),
("Arabandi", "Jl.Kabupaten", "Solo"),
("Bagas", "Jl. arek no 19", "Malang");

insert into penabung values 
("Karnoto", "1234567891"),
("Sarnoto", "1234567892"),
("Sarjono","1234567893"),
("Saiminih", "1234567894"),
("Saman", "1234567895"),

("Sadinah", "1234567896"),
("Taiminih", "1234567897"),
("Samandika", "1234567898"),
("Arabandi","1234567899"),
("Bagas", "123456788");

insert into rekening values 
("1234567891", "PT.Rambutan", 2000000),
("1234567892", "PT.Semangka", 3000000),
("1234567893", "PT.Jeruk", 4000000),
("1234567894", "PT.Strawberry", 5000000),
("1234567895", "PT.Anggur", 6000000),

("1234567896", "PT.Manggis", 6500000),
("1234567897", "PT.Durian", 7500000),
("1234567898", "PT.Quldi", 3500000),
("1234567899", "PT.Kopi", 4500000),
("123456788", "PT.Salak", 5500000);

-- query utama

select * from cabang;
select * from pinjaman;
select * from peminjaman;
select * from penabung;
select * from namanasabah;
select * from rekening;

select distinct NamaNasabah
from peminjaman
where NamaNasabah not in (
  select NamaNasabah from penabung
);

select penabung.NamaNasabah, avg(saldo)
from penabung, rekening, namanasabah
where penabung.NomorRekening = rekening.NomorRekening
AND penabung.NamaNasabah = namanasabah.NamaNasabah
AND KotaNasabah = "Yogyakarta";

select penabung.NamaNasabah, avg(saldo)
from penabung, rekening, namanasabah
where penabung.NomorRekening = rekening.NomorRekening
AND penabung.NamaNasabah = namanasabah.NamaNasabah
AND KotaNasabah = "Yogyakarta"
group by penabung.NamaNasabah
having count (distinct penabung.NomorRekening) >= 4;

select distinct NamaNasabah
from peminjaman, pinjaman
where peminjaman.NomorPinjaman = pinjaman.NomorPinjaman
AND NamaCabang = "Yogyakarta"
AND (NamaCabang, NamaNasabah) in(
  select NamaCabang, NamaNasabah
  from penabung, rekening
  where penabung.NomorRekening=rekening.NomorRekening
);

select distinct T.NamaCabang
from cabang as T, cabang as S
where T.Asset > S.Asset AND S.KotaCabang = "Yogyakarta";
