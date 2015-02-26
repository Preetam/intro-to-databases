import sqlite3
import unittest
import timeit

class E(unittest.TestCase):
    def test_exercise_1(self):
        cur = self.con.cursor()

        #############################
        # Exercise 1
        #
        # Select every column from every row in `users`.
        cur.execute('SELECT * FROM users')
        #
        #
        #############################

        data = cur.fetchall()
        cur.close()
        self.assertTrue(len(data) == 30)


    def test_exercise_2(self):
        cur = self.con.cursor()

        #############################
        # Exercise 2
        #
        # Select the number of rows in the `users` table.
        cur.execute('SELECT count(*) FROM users')
        #
        #
        #############################

        data = cur.fetchall()
        cur.close()
        self.assertTrue(data[0][0] == 30)


    def test_exercise_3(self):
        cur = self.con.cursor()

        #############################
        # Exercise 3
        cur.executescript("""
        /*
            Create a table "colors" with a single column called "name".
            The column type is VARCHAR.
        */

            CREATE TABLE colors (
                name VARCHAR
            );

        /*
            Add the colors red, orange, yellow, green, and blue.
        */

            INSERT INTO colors VALUES ("blue");
            INSERT INTO colors VALUES ("red");
            INSERT INTO colors VALUES ("orange");
            INSERT INTO colors VALUES ("yellow");
            INSERT INTO colors VALUES ("green");

        """)
        #
        #
        #############################
        cur.execute('SELECT name FROM colors ORDER BY name ASC LIMIT 5')
        data = cur.fetchall()
        cur.close()
        self.assertTrue(data ==
            [(u'blue',), (u'green',), (u'orange',), (u'red',), (u'yellow',)])


    def test_exercise_4(self):
        con = self.con
        con.isolation_level = None
        cur = con.cursor()

        #############################
        # Exercise 4
        #
        # Select (username, state) rows using the following tables.
        # How many JOINs do you need?
        cur.execute('select users.username, states.code from users join states join locations on users.id = locations.user and states.id = locations.state')
        #
        #
        #############################

        data = cur.fetchall()
        cur.close()
        self.assertTrue(data ==
            [(u'mreynolds0', u'NM'),
            (u'rbishop1', u'WA'),
            (u'rfisher2', u'OH'),
            (u'rrichards3', u'MT'),
            (u'aellis4', u'IL'),
            (u'drobinson5', u'VA'),
            (u'anelson6', u'PA'),
            (u'rcunningham7', u'LA'),
            (u'srice8', u'SD'),
            (u'kphillips9', u'WA'),
            (u'tstonea', u'OH'),
            (u'sburnsb', u'OH'),
            (u'ljamesc', u'ME'),
            (u'tboydd', u'OR'),
            (u'cpricee', u'DE'),
            (u'sgarrettf', u'WV'),
            (u'ccookg', u'CT'),
            (u'swilsonh', u'DE'),
            (u'lwagneri', u'OR'),
            (u'lmartinj', u'VA'),
            (u'jwheelerk', u'CT'),
            (u'hstanleyl', u'VA'),
            (u'gbellm', u'AK'),
            (u'jadamsn', u'VA'),
            (u'arichardso', u'SC'),
            (u'ssnyderp', u'CT'),
            (u'srobertsq', u'VA'),
            (u'arichardsonr', u'MO'),
            (u'phansens', u'NJ'),
            (u'vfishert', u'WI')]
            )

    def test_exercise_5(self):
        con = self.con
        con.isolation_level = None
        cur = con.cursor()

        #############################
        # Exercise 5
        #
        # Start a transaction, insert a new row, and select the number
        # of users.
        cur.execute('BEGIN')
        cur.execute('INSERT INTO users (username, first_name, last_name) VALUES ("jdoe1", "Jane", "Doe")')
        cur.execute('SELECT count(*) FROM users')
        #
        #
        #############################

        data = cur.fetchall()
        self.assertTrue(data[0][0] == 31)

        #############################
        # Exercise 5 (continued)
        #
        # Rollback the transaction.
        cur.execute('ROLLBACK')
        #
        #
        #############################

        cur.execute('SELECT count(*) FROM users')
        data = cur.fetchall()
        cur.close()
        self.assertTrue(data[0][0] == 30)


    def test_exercise_6(self):
        con = self.con
        con.isolation_level = None
        cur = con.cursor()

        N = 30000

        #############################
        # Exercise 6
        #
        # Change the following schema to include an index on column "a".
        cur.execute('CREATE TABLE "numbers" (a INTEGER PRIMARY KEY)')
        #
        #
        #############################

        rows = []
        for i in range(0, N):
            rows.append( (i,) )
        
        cur.executemany('INSERT INTO "numbers" VALUES (?)', rows)
 
        start_time = timeit.default_timer()
        cur.execute('select min(a) from numbers')
        print("exercise_6: That took %f ms." % ((timeit.default_timer() - start_time) * 1000,))

        data = cur.fetchall()
        cur.close()
        self.assertTrue(data[0][0] == 0)

############# Ignore stuff below this line #############

    @classmethod
    def setUpClass(cls):
        # Set up database tables
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        cur.executescript("""
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS "users";
DROP TABLE IF EXISTS "states";
DROP TABLE IF EXISTS "locations";
DROP TABLE IF EXISTS "numbers";
DROP TABLE IF EXISTS "colors";

CREATE TABLE "users" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , "username" VARCHAR NOT NULL UNIQUE , "first_name" VARCHAR NOT NULL, "last_name" VARCHAR NOT NULL );
INSERT INTO "users" VALUES(1,'mreynolds0','Michelle','Reynolds');
INSERT INTO "users" VALUES(2,'rbishop1','Ralph','Bishop');
INSERT INTO "users" VALUES(3,'rfisher2','Roger','Fisher');
INSERT INTO "users" VALUES(4,'rrichards3','Richard','Richards');
INSERT INTO "users" VALUES(5,'aellis4','Aaron','Ellis');
INSERT INTO "users" VALUES(6,'drobinson5','Daniel','Robinson');
INSERT INTO "users" VALUES(7,'anelson6','Andrew','Nelson');
INSERT INTO "users" VALUES(8,'rcunningham7','Ralph','Cunningham');
INSERT INTO "users" VALUES(9,'srice8','Shawn','Rice');
INSERT INTO "users" VALUES(10,'kphillips9','Kenneth','Phillips');
INSERT INTO "users" VALUES(11,'tstonea','Todd','Stone');
INSERT INTO "users" VALUES(12,'sburnsb','Shirley','Burns');
INSERT INTO "users" VALUES(13,'ljamesc','Lawrence','James');
INSERT INTO "users" VALUES(14,'tboydd','Terry','Boyd');
INSERT INTO "users" VALUES(15,'cpricee','Catherine','Price');
INSERT INTO "users" VALUES(16,'sgarrettf','Shawn','Garrett');
INSERT INTO "users" VALUES(17,'ccookg','Clarence','Cook');
INSERT INTO "users" VALUES(18,'swilsonh','Steve','Wilson');
INSERT INTO "users" VALUES(19,'lwagneri','Lori','Wagner');
INSERT INTO "users" VALUES(20,'lmartinj','Laura','Martin');
INSERT INTO "users" VALUES(21,'jwheelerk','Jimmy','Wheeler');
INSERT INTO "users" VALUES(22,'hstanleyl','Helen','Stanley');
INSERT INTO "users" VALUES(23,'gbellm','Gregory','Bell');
INSERT INTO "users" VALUES(24,'jadamsn','Joan','Adams');
INSERT INTO "users" VALUES(25,'arichardso','Anthony','Richards');
INSERT INTO "users" VALUES(26,'ssnyderp','Sarah','Snyder');
INSERT INTO "users" VALUES(27,'srobertsq','Stephen','Roberts');
INSERT INTO "users" VALUES(28,'arichardsonr','Adam','Richardson');
INSERT INTO "users" VALUES(29,'phansens','Phyllis','Hansen');
INSERT INTO "users" VALUES(30,'vfishert','Virginia','Fisher');
CREATE TABLE "states" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "code" VARCHAR NOT NULL UNIQUE);
INSERT INTO "states" VALUES(1,'AL');
INSERT INTO "states" VALUES(2,'AK');
INSERT INTO "states" VALUES(3,'AZ');
INSERT INTO "states" VALUES(4,'AR');
INSERT INTO "states" VALUES(5,'CA');
INSERT INTO "states" VALUES(6,'CO');
INSERT INTO "states" VALUES(7,'CT');
INSERT INTO "states" VALUES(8,'DE');
INSERT INTO "states" VALUES(9,'DC');
INSERT INTO "states" VALUES(10,'FL');
INSERT INTO "states" VALUES(11,'GA');
INSERT INTO "states" VALUES(12,'HI');
INSERT INTO "states" VALUES(13,'ID');
INSERT INTO "states" VALUES(14,'IL');
INSERT INTO "states" VALUES(15,'IN');
INSERT INTO "states" VALUES(16,'IA');
INSERT INTO "states" VALUES(17,'KS');
INSERT INTO "states" VALUES(18,'KY');
INSERT INTO "states" VALUES(19,'LA');
INSERT INTO "states" VALUES(20,'ME');
INSERT INTO "states" VALUES(21,'MD');
INSERT INTO "states" VALUES(22,'MA');
INSERT INTO "states" VALUES(23,'MI');
INSERT INTO "states" VALUES(24,'MN');
INSERT INTO "states" VALUES(25,'MS');
INSERT INTO "states" VALUES(26,'MO');
INSERT INTO "states" VALUES(27,'MT');
INSERT INTO "states" VALUES(28,'NE');
INSERT INTO "states" VALUES(29,'NV');
INSERT INTO "states" VALUES(30,'NH');
INSERT INTO "states" VALUES(31,'NJ');
INSERT INTO "states" VALUES(32,'NM');
INSERT INTO "states" VALUES(33,'NY');
INSERT INTO "states" VALUES(34,'NC');
INSERT INTO "states" VALUES(35,'ND');
INSERT INTO "states" VALUES(36,'OH');
INSERT INTO "states" VALUES(37,'OK');
INSERT INTO "states" VALUES(38,'OR');
INSERT INTO "states" VALUES(39,'PA');
INSERT INTO "states" VALUES(40,'RI');
INSERT INTO "states" VALUES(41,'SC');
INSERT INTO "states" VALUES(42,'SD');
INSERT INTO "states" VALUES(43,'TN');
INSERT INTO "states" VALUES(44,'TX');
INSERT INTO "states" VALUES(45,'UT');
INSERT INTO "states" VALUES(46,'VT');
INSERT INTO "states" VALUES(47,'VA');
INSERT INTO "states" VALUES(48,'WA');
INSERT INTO "states" VALUES(49,'WV');
INSERT INTO "states" VALUES(50,'WI');
INSERT INTO "states" VALUES(51,'WY');
CREATE TABLE "locations" (state INTEGER, user INTEGER, PRIMARY KEY (state, user));
INSERT INTO "locations" VALUES(32,1);
INSERT INTO "locations" VALUES(48,2);
INSERT INTO "locations" VALUES(36,3);
INSERT INTO "locations" VALUES(27,4);
INSERT INTO "locations" VALUES(14,5);
INSERT INTO "locations" VALUES(47,6);
INSERT INTO "locations" VALUES(39,7);
INSERT INTO "locations" VALUES(19,8);
INSERT INTO "locations" VALUES(42,9);
INSERT INTO "locations" VALUES(48,10);
INSERT INTO "locations" VALUES(36,11);
INSERT INTO "locations" VALUES(36,12);
INSERT INTO "locations" VALUES(20,13);
INSERT INTO "locations" VALUES(38,14);
INSERT INTO "locations" VALUES(8,15);
INSERT INTO "locations" VALUES(49,16);
INSERT INTO "locations" VALUES(7,17);
INSERT INTO "locations" VALUES(8,18);
INSERT INTO "locations" VALUES(38,19);
INSERT INTO "locations" VALUES(47,20);
INSERT INTO "locations" VALUES(7,21);
INSERT INTO "locations" VALUES(47,22);
INSERT INTO "locations" VALUES(2,23);
INSERT INTO "locations" VALUES(47,24);
INSERT INTO "locations" VALUES(41,25);
INSERT INTO "locations" VALUES(7,26);
INSERT INTO "locations" VALUES(47,27);
INSERT INTO "locations" VALUES(26,28);
INSERT INTO "locations" VALUES(31,29);
INSERT INTO "locations" VALUES(50,30);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('users',2);
INSERT INTO "sqlite_sequence" VALUES('states',51);
COMMIT;
        """)
        cur.close()
        con.close()
        
    def setUp(self):
        con = sqlite3.connect('db.sqlite')
        self.con = con
        cur = con.cursor()
        cur.execute('pragma synchronous = off;') # fsync gets annoying :)
        cur.close()

if __name__ == '__main__':
    unittest.main()