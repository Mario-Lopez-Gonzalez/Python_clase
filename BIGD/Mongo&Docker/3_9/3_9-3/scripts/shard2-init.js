rs.initiate(
  {
     _id: "rshard2",
     version: 1,
     members: [
        { _id: 0, host : "shard2a:27017" },
        { _id: 1, host : "shard2b:27017" },
     ]
  }
)
