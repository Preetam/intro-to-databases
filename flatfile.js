

var fs = require('fs');

var db = {
  get: function(key, cb) {
    fs.readFile('data/'+key+'.json', function(err, data) {
      cb(err, JSON.parse(data));
    });
  },
  set: function(key, val, cb) {
    fs.writeFile('data/'+key+'.json', JSON.stringify(val), cb);
  }
};


db.set('foo', {title: 'foo', content: 'content here'}, function() {
  db.get('foo', function(err, val) {
    console.log(err, val);
  });
});

