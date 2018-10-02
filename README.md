# dataflow

A flexible, lightweight ORM for C++.

## Ideas

- Data I/O from/to data sources *can* be done through visitors
    - Data export is easy with visitors 
    - Data import can be done with visitors that set each object property
        - Could also be done with factories
- Objects
    - Set of **members**
        - Either **primitive members** (std::string for varchar, int for int etc.)
        - Or **complex members** (when member is a foreign key)
            - Value is another object
            - Additionally has the foreign key names and values
        - All members have
            - A value (storage)
                - Can be initialized (if object was constructed or fetched) or not (by default) --> optional
                - Private
            - A value getter method
                - Primitive members have getters that just return the value
                - Complex members have blocking getters that the user can wrap in std::async calls or whichever technology he chooses.
                    - **How to specify where to get the value from?** Objects know their key fields and key values --> getters call static Object::fetchOne(Query), set the optional and return the value if the optional is not yet set, and simply return the value otherwise 
            - The field name
    - Table name (object name)
    - Static factory methods
        - Object::fetchOne(Query, Factory)
        - Object::fetchAll(Query, Factory)
        - These just call Factory::fetchXYZ(Query)