rs.initiate(
  {
     _id: "rshard3",
     version: 1,
     members: [
        { _id: 0, host : "shard3a:27017" },
        { _id: 1, host : "shard3b:27017" },
     ]
  }
)