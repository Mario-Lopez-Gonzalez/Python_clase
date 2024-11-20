rs.initiate(
  {
     _id: "rshard1",
     version: 1,
     members: [
        { _id: 0, host : "shard1a:27017" },
        { _id: 1, host : "shard1b:27017" },
     ]
  }
)
