# MONGO DB LEARNING
_resource:_ https://www.w3schools.com/python/python_mongodb_getstarted.asp

## __Mongo DB__ 
It is one of the most popular NoSQL database. MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable.

To experiment with the code examples, you'll need to a MongoDB database.

You can download a free MongoDB database at https://www.mongodb.com.

Or get started right away with a MongoDB cloud service at https://www.mongodb.com/cloud/atlas.

## __PyMongo__ 
It needs a MongoDB driver to access the MongoDB database. Thus, we'll use the MongoDB driver "PyMongo".
Use PIP to install "PyMongo".
In the command, type the following: `pip install pymongo`

__Test PyMongo:__
To test if the installation was successful, or if you already have "pymongo" installed, create a Python page with the following content:

`import pymongo`
If it runs without error, pymongo is successfully installed

### Advantages of Mongobd:
Mongo db has advantage over structured databases like sql:
- __Scalability:__ As data grows larger it is easy to scale in an unstructured db like Mongodb
- __Elasticity:__ Structured databases need data in a predefined format. If the data doesn't follow the predefined format, it won't be stored.

__Comparison below:__
content  |  Structured Databases  | 	Unstructured Databases
-------  | ---------              | ---------
Structure: |	Every element has the same number of attributes	| Different elements can have different number of attributes.
Latency: | 	Comparatively slower storage	| Faster storage
Ease of learning:   |	Easy to learn   |	Comparatively tougher to learn
Storage Volume  |	Not appropriate for storing Big Data    | Can handle Big Data as well
Type of Data Stored:    |	Generally textual data is stored    |	Any type of data can be stored (Audio, Video, Clickstraem etc)
Examples:   |	MySQL, PostgreSQL   |	MongoDB, RavenDB

## The Architecture of a MongoDB Database
The information in MongoDB is stored in documents. Here, a document is analogous to rows in structured databases.

- Each document is a collection of key-value pairs
- Each key-value pair is called a field
- Every document has an _id  field, which uniquely identifies the documents
- A document may also contain nested documents
- Documents may have a varying number of fields (they can be blank as well)
- These documents are stored in a collection. A collection is literally a collection of documents in MongoDB.

## Creating Database
To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct ip address and the name of the database you want to create.

MongoDB will create the database if it does not exist, and make a connection to it.