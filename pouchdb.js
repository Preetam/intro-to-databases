
var PouchDB = require('pouchdb');
var db = new PouchDB('data/pouch');


// bulk insert docs into the database
db.bulkDocs({docs: [
  {
    _id: 'post_1',
    title: 'Hello, world',
    content: 'This is my first blog post!',
    tags: ['general']
  },
  {
    _id: 'post_2',
    title: 'Databases',
    content: 'I <3 databases!',
    tags: ['databases', 'general']
  },
  {
    _id: 'post_3',
    title: 'Fluent 2014',
    content: 'I went to Fluent and it was super fun!',
    tags: ['travel']
  }
]}).then(function() {
  db.query(
    {
      map: function(doc) {
        for(var i in doc.tags) {
          emit(doc.tags[i], null);
        }
      },
      reduce: false
    },
    {
      keys: ['general']
    },
    function(err, response) {
      console.log(err, response);
    }
  );
});

