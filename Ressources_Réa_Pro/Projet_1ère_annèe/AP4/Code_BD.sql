drop table if exists Ligues;
drop table if exists Prestation;
drop table if exists Facture;
drop table if exists Ligne_Facture;

CREATE TABLE Ligues(
   compte CHAR(6) NOT NULL,
   intitule VARCHAR(50),
   tresorie VARCHAR(50),
   CONSTRAINT PK_Lig PRIMARY KEY(compte)
)ENGINE = INNODB;

CREATE TABLE Prestation(
   Code_prest VARCHAR(50),
   libelle VARCHAR(50),
   prix_unitaire DECIMAL(5,3),
   CONSTRAINT PK_Pre PRIMARY KEY(Code_prest)
)ENGINE = INNODB;

CREATE TABLE Facture(
   n_facture VARCHAR(10),
   date_fac DATE,
   echeance DATE,
   compte CHAR(6) NOT NULL,
   CONSTRAINT PK_Fac PRIMARY KEY(n_facture)
)ENGINE = INNODB;

CREATE TABLE Ligne_Facture(
   n_facture VARCHAR(10),
   Code_prest VARCHAR(50),
   quantite INTEGER,
   Constraint PK_LignF PRIMARY KEY(n_facture,Code_prest)
)ENGINE = INNODB;



DELETE FROM Ligues;
Insert Into Ligues Values (411007, 'Basket', 'Valerie LAHEURTE');
Insert Into Ligues Values (411008, 'Escrime', 'Pierre LENOIR');
Insert Into Ligues Values (411009, 'Foot', 'Mohamed BOURGARD');
Insert Into Ligues Values (411010, 'Baby-foot', 'Sylvain Delahousse');
SELECT * from Ligues;

DELETE FROM Prestation;
Insert Into Prestation Values ('AFFRAN', 'Affranchissement', 3.330);
Insert Into Prestation Values ('PHOTOCOULEUR', 'Photocopies couleur', 0.240);
Insert Into Prestation Values ('PHOTON&B', 'Photocopies noir et blanc', 0.055);
Insert Into Prestation Values ('TRACEUR', 'Utilisation traceur', 0.356);
SELECT * from Prestation;

DELETE FROM Facture;
Insert Into Facture Values (5172, '2011-04-08', '2011-04-30', 411007);
Insert Into Facture Values (5174, '2012-02-12', '2012-02-29', 411010);
SELECT * from Facture;

DELETE FROM Ligne_Facture;
Insert Into Ligne_Facture Values (5172, 'AFFRAN', 0);
Insert Into Ligne_Facture Values (5172, 'PHOTOCOULEUR', 300);
Insert Into Ligne_Facture Values (5172, 'PHOTON&B', 552);
Insert Into Ligne_Facture Values (5172, 'TRACEUR', 2);
SELECT * from Ligne_Facture;



ALTER TABLE Facture
DROP CONSTRAINT FK_Fac_Lig;
ALTER TABLE Facture
ADD CONSTRAINT FK_Fac_Lig FOREIGN KEY(compte) REFERENCES Ligues(compte);

ALTER TABLE Ligne_Facture
DROP CONSTRAINT FK_LignF_Fac;
ALTER TABLE Ligne_Facture
ADD CONSTRAINT FK_LignF_Fac FOREIGN KEY(n_facture) REFERENCES Facture(n_facture);

ALTER TABLE Ligne_Facture
DROP CONSTRAINT FK_LignF_Pre;
ALTER TABLE Ligne_Facture
ADD CONSTRAINT FK_LignF_Pre FOREIGN KEY(Code_prest) REFERENCES Prestation(Code_prest);