CREATE TABLE Query1 (
    TrackName  CHAR,
    ArtistName CHAR,
    AlbumTitle CHAR,
    Composer   CHAR,
    Genre      CHAR
);

CREATE TABLE Query2 (
    FirstName     CHAR,
    LastName      CHAR,
    Phone         CHAR,
    Email         CHAR,
    full_address  CHAR
);

CREATE TABLE Query3 (
    Country         CHAR,
    distinct_emails CHAR
);

CREATE TABLE Query4 (
    BillingCountry  CHAR,
    sum CHAR
);

CREATE TABLE Query5 (
    billingcountry  CHAR,
    Title           CHAR,
    count           CHAR
);

CREATE TABLE Query6 (
    title  CHAR,
    count  CHAR
);

CREATE TABLE Query7 (
    customername  CHAR
);


    delete from Query1;
    delete from Query2;
    delete from Query3;
    delete from Query4;
    delete from Query5;
    delete from Query6;
    delete from Query7;
