var config = {
    "_id": "iabdrs",
    "version": 1,
    "members": [
        {
            "_id": 1,
            "host": "mongo1:27017",
            "priority": 2
        },
        {
            "_id": 2,
            "host": "mongo2:27017",
            "priority": 1
        },
        {
            "_id": 3,
            "host": "mongo3:27017",
            "priority": 1
        },
        {
            "_id": 4,
            "host": "mongo4:27017",
            "priority": 1
        }
    ]
};
rs.initiate(config, { force: true });
rs.status();
