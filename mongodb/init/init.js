var user = {
    user: "www",
    pwd: "password",
    roles: [
      {
        role: "readWrite",
        db: "test"
      }
    ]
  };
  
  db.createUser(user);
  db.createCollection('cve');