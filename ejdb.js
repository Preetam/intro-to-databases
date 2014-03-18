
var ejdb = require('ejdb');
var db = ejdb.open("data/animals", ejdb.DEFAULT_OPEN_MODE | ejdb.JBOTRUNC);

var pets = [
  {
    type: 'cat',
    name: 'Foo',
    age: 1
  },
  {
    name: 'bar',
    age: 3
  },
  {
    type: 'dog',
    name: 'Doge',
    age: 0.5,
    meme: true
  },
  {
    _id: '1234567890abcdef12345678',
    name: 'Wilbur',
    age: 2,
    fictional: true
  }
];

db.save('pets', pets, function(err, oids) {
  db.find('pets', {'age': {'$bt': [1,5]}}, function(err, cursor, close) {
    while(cursor.next()) {
      console.log(cursor.field('name') + " is " + cursor.field('age') + ' years old.');
    }
  });

  db.find('pets', {'type': 'dog'}, function(err, cursor, close) {
    while(cursor.next()) {
      console.log(cursor.field('name') + " is a dog.");
    }
  });

  db.load('pets', '1234567890abcdef12345678', function(err, doc) {
    console.log("Wilbur's doc:\n", doc);
  });
})

