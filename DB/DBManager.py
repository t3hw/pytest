import sqlite3
from sqlite3 import Error
import os.path

class DBManager:
    conn = None

    queryArgs = (None,             # 1
                 None,             # 2
                 None,             # 3
                 None,             # 4
                 None,             # 5
                 ('USA', 2011),  # 6
                 None)             # 7

    queries = (  # 1 song list with data
                "select t.name TrackName, r.name ArtistName, a.title AlbumTitle, t.composer, g.name Genre " 
                "  from tracks t, albums a, genres g, artists r " 
                " where t.albumid = a.albumid " 
                "   and t.genreid = g.genreid " 
                "   and a.artistid = r.artistid " 
                "order by r.name, a.title"
                ,
                # 2 list of customers with customer data
                "select firstname "
                "      ,lastname "
                "      ,phone "
                "      ,email " 
                "      ,address || " 
                "       CASE WHEN postalcode IS NULL THEN '' ELSE ' ' || postalcode END || " 
                "           ' ' || city || " 
                "       CASE WHEN state IS NULL THEN '' ELSE ' ' || state END || " 
                "           ' ' || country as full_address " 
                " from customers"
                ,
                # 3 distinct emails per country
                "select distinct country " 
                "      ,(select count(distinct email) " 
                "            from customers c2 " 
                "              where c1.country = c2.country) distinct_emails " 
                "     from customers c1"
                ,
                # 4 how many distinct albums were sold in each country. each sale can have multiple distinct albums.
                #   for our purposes 2 tracks from the same album in the same invoice would only count as 1 "
                "select billingcountry, sum(iic.count) sum "
                " from invoices inv "
                #       for each invoice, how many distinct albums "
                "      ,(select i.InvoiceId "
                "              ,count(distinct a.albumid) count "
                "          from invoice_items i "
                "              ,tracks t "
                "              ,albums a "
                "         where i.trackid = t.trackid "
                "           and t.albumid = a.albumid "
                "        group by i.invoiceid) iic "
                " where inv.invoiceid = iic.invoiceid "
                "  group by billingcountry"
                ,
                # 5 most popular album for each country
                # (if are multiple albums tied with the same sales count, get all of the ones tied for 1st place)
                "with w_count(billingcountry, albumid,count) as " 
                #   select sales count per country "
                "  (select v.billingcountry, i.albumid, count(*) count " 
                "     from invoices v " +
                #          for each invoice, get the albums that were purchased in it
                "        ,(select i1.InvoiceId, a.AlbumId " 
                "          from invoice_items i1 " 
                "              ,tracks t " 
                "              ,albums a " 
                "          where i1.trackid = t.trackid " 
                "            and t.albumid = a.albumid "
                "          group by i1.invoiceid, a.AlbumId) i " 
                "   where v.invoiceid = i.invoiceid " 
                "   group by v.billingcountry, i.albumid) " 
                "select w.billingcountry, a.title, count " 
                "from w_count w " 
                "    ,(select billingcountry, max(count) max " 
                "      from w_count " 
                "      group by billingcountry) m " 
                "    ,albums a " 
                "where w.billingcountry = m.billingcountry " 
                "  and w.count = m.max " 
                "  and a.albumid = w.albumid " 
                "order by count desc "
                ,
                # 6 get the most popular albums in USA since 2011
                "with w_count(invoiceid, title, count) as " 
                "(select v.invoiceid, a.title, count(*) " 
                "  from invoices v " 
                "      ,invoice_items i " 
                "      ,tracks t " 
                "      ,albums a " 
                " where v.billingcountry = ? " 
                "   and CAST(strftime('%Y',v.invoicedate) as decimal) > ? " 
                "   and v.invoiceid = i.invoiceid " 
                "   and i.trackid = t.trackid " 
                "   and t.albumid = a.albumid " 
                "group by i.invoiceid, a.title) " 
                "select * " 
                "from w_count w " 
                "where w.count = (select max(count) from w_count)"
                ,
                # 7 customers for invoices with 2 or more missing fields
                "select distinct c.firstname || ' ' || c.lastname " 
                "from invoices i " 
                "    ,customers c " 
                "where (select count(*) " 
                "         from (with tab(cols) as " 
                "                  (select * from (values (i.billingaddress) " 
                "                                        ,(i.billingcity) " 
                "                                        ,(i.billingstate) " 
                "                                        ,(i.billingcountry) " 
                "                                        ,(i.billingpostalcode))) " 
                "select cols from tab) " 
                " where cols is null) >= 2 " 
                "   and c.customerid = i.customerid"
    )

    @staticmethod
    def getConnection(db_file):
        try:
            if DBManager.conn is None:
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.join(BASE_DIR, db_file + ".db")
                DBManager.conn = sqlite3.connect(db_path)
        except Error as e:
            print(e)

    @staticmethod
    def closeConnection():
        if DBManager.conn is not None:
            DBManager.conn.close()

    @staticmethod
    def select(statement, args):
        cur = DBManager.conn.cursor()

        if args is None:
            cur.execute(statement)
        else:
            cur.execute(statement, args)

        rows = cur.fetchall()
        return rows

    @staticmethod
    def insert(statement, args):
        cur = DBManager.conn.cursor()
        cur.execute(statement, args)
        return cur.lastrowid

    @staticmethod
    def executeQuery(query, *args):
        *params, = args
        print(query, params[0])
        result = DBManager.select(query, params[0])
        return result

    @staticmethod
    def executeAllQueries(dbFile):
        DBManager.getConnection(dbFile)

        results = []

        for i, query in enumerate(DBManager.queries):
            results.append(DBManager.executeQuery(query, DBManager.queryArgs[i]))

        DBManager.closeConnection()

        return results
