
var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database(':memory:');

/*
*  Data set
*  ------
*
*        (INT)      (TEXT)     (FLOAT)
*   ____________________________________
*  /-------------|----------|-----------\
*  |  timestamp  |  metric  |   value   |
*  |-------------|----------|-----------|
*  |  1234567890 |  cpu.5m  |   5.680   |
*  |  1234567890 |  cpu.1m  |   5.000   |
*  |  1234567891 |  cpu.1m  |   3.472   |
*  |  1234567891 |  cpu.5m  |   5.482   |
*  |  1234567892 |  cpu.1m  |   7.583   |
*  |  1234567892 |  cpu.5m  |   6.120   |
*  \_____________|__________|___________/
*
*/

db.serialize(function() {
  db.run("CREATE TABLE IF NOT EXISTS observations (timestamp INT, metric TEXT, value FLOAT)");

  var stmt = db.prepare("INSERT INTO observations VALUES (?, ?, ?)");
  stmt.run(1234567890, 'cpu.5m', 5.68);
  stmt.run(1234567891, 'cpu.5m', 5.482);
  stmt.run(1234567892, 'cpu.5m', 6.12);
  stmt.run(1234567890, 'cpu.1m', 5);
  stmt.run(1234567891, 'cpu.1m', 3.472);
  stmt.run(1234567892, 'cpu.1m', 7.583);
  stmt.finalize();

  db.each("SELECT * FROM observations WHERE timestamp BETWEEN 1234567890 AND 1234567891" + 
  	      " AND metric = 'cpu.5m'", function(err, row) {
    console.log(row.timestamp + "\t" + row.metric + "\t" + row.value);
  });
});

db.close();
