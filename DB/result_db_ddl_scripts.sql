CREATE TABLE IF NOT EXISTS Query1 (
    TrackName  CHAR,
    ArtistName CHAR,
    AlbumTitle CHAR,
    Composer   CHAR,
    Genre      CHAR
);

CREATE TABLE IF NOT EXISTS Query2 (
    FirstName     CHAR,
    LastName      CHAR,
    Phone         CHAR,
    Email         CHAR,
    full_address  CHAR
);

CREATE TABLE IF NOT EXISTS Query3 (
    Country         CHAR,
    distinct_emails CHAR
);

CREATE TABLE IF NOT EXISTS Query4 (
    BillingCountry  CHAR,
    sum CHAR
);

CREATE TABLE IF NOT EXISTS Query5 (
    billingcountry  CHAR,
    Title           CHAR,
    count           CHAR
);

CREATE TABLE IF NOT EXISTS Query6 (
    title  CHAR,
    count  CHAR
);

CREATE TABLE IF NOT EXISTS Query7 (
    customername  CHAR
);


    delete from Query1;
    delete from Query2;
    delete from Query3;
    delete from Query4;
    delete from Query5;
    delete from Query6;
    delete from Query7;
