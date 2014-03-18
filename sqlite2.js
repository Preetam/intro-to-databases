
var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database(':memory:');

db.serialize(function() {
  db.run("CREATE TABLE IF NOT EXISTS users (username TEXT, first_name TEXT, last_name TEXT)");

  var stmt = db.prepare("INSERT INTO users VALUES (?, ?, ?)");
  stmt.run('bob', 'Bob', 'Barker');
  stmt.run('alice', 'Alice', 'Cooper');
  stmt.run('pj', 'Preetam', 'Jinka');
  stmt.finalize();

  db.run("CREATE TABLE IF NOT EXISTS languages (username TEXT, language TEXT)");
  var stmt = db.prepare("INSERT INTO languages VALUES (?, ?)");
  stmt.run('bob', 'JavaScript');
  stmt.run('alice', 'C++');
  stmt.run('pj', 'Go');
  stmt.finalize();

  db.each("SELECT * FROM users WHERE username in (SELECT username FROM languages WHERE language = 'Go' OR language = 'C++')", function(err, row) {
      console.log(row);
  });
});

db.close();
