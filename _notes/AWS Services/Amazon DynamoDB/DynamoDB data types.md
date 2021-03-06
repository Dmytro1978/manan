## DynamoDB Data Types
DynamoDB supports many different data types for attributes within a table. They can be categorized as
follows:
* __Scalar Types__ – A scalar type can represent exactly one value. The scalar types are _number_, _string_,
_binary_, _Boolean_, and _null_.
* __Document Types__ – A document type can represent a complex structure with nested attributes—such
as you would find in a JSON document. The document types are list and map.
* __Set Types__ – A set type can represent multiple scalar values. The set types are _string_ set, _number_ set,
and _binary_ set.

DynamoDB is a NoSQL database and is _schemaless_. This means that, other than the primary key
attributes, you don't have to define any attributes or data types when you create tables. By comparison,
relational databases require you to define the names and data types of each column when you create a
table.

### Scalar Types
####  _String_
Strings are Unicode with UTF-8 binary encoding. The length of a string must be greater than zero and is
constrained by the maximum DynamoDB item size limit of 400 KB.
The following additional constraints apply to primary key attributes that are defined as type string:
* For a simple primary key, the maximum length of the first attribute value (the partition key) is 2048
bytes.
* For a composite primary key, the maximum length of the second attribute value (the sort key) is 1024
bytes.

#### _Number_
Numbers can be positive, negative, or zero. Numbers can have up to 38 digits precision. Exceeding this
results in an exception.
* Positive range: 1E-130 to 9.9999999999999999999999999999999999999E+125
* Negative range: -9.9999999999999999999999999999999999999E+125 to -1E-130

In DynamoDB, numbers are represented as variable length. Leading and trailing zeroes are trimmed.
All numbers are sent across the network to DynamoDB as strings, to maximize compatibility across
languages and libraries. However, DynamoDB treats them as number type attributes for mathematical
operations.

__Note__:
If number precision is important, you should pass numbers to DynamoDB using strings that you convert from number type.

#### _Binary_
Binary type attributes can store any binary data, such as _compressed text_, _encrypted data_, or _images_.
Whenever DynamoDB compares binary values, it treats each byte of the binary data as unsigned.
The length of a binary attribute must be greater than zero, and is constrained by the maximum
DynamoDB item size limit of 400 KB.
If you define a primary key attribute as a binary type attribute, the following additional constraints
apply:
* For a simple primary key, the maximum length of the first attribute value (the partition key) is 2048
bytes.
* For a composite primary key, the maximum length of the second attribute value (the sort key) is 1024
bytes.

#### _Boolean_
A Boolean type attribute can store either true or false.

#### _Null_
Null represents an attribute with an unknown or undefined state.

### Document Types
The document types are _list_ and _map_. These data types can be nested within each other, to represent
complex data structures up to 32 levels deep. 
There is no limit on the number of values in a list or a map, as long as the item containing the values fits
within the DynamoDB item size limit (400 KB).
An attribute value cannot be an empty String or empty Set (String Set, Number Set, or Binary Set).
However, empty Lists and Maps are allowed.

#### _List_
A list type attribute can store an ordered collection of values. Lists are enclosed in square brackets:
[ ... ]
A list is similar to a JSON array. There are no restrictions on the data types that can be stored in a list
element, and the elements in a list element do not have to be of the same type.

#### _Map_
A map type attribute can store an unordered collection of name-value pairs. Maps are enclosed in curly
braces: { ... }
A map is similar to a JSON object. There are no restrictions on the data types that can be stored in a map
element, and the elements in a map do not have to be of the same type.
Maps are ideal for storing JSON documents in DynamoDB. The following example shows a map that
contains a string, a number, and a nested list that contains another map:

```json
{
    "Day": "Monday",
    "UnreadEmails": 42,
    "ItemsOnMyDesk": [
        "Coffee Cup",
        "Telephone",
        {
            "Pens": { "Quantity" : 3},
            "Pencils": { "Quantity" : 2},
            "Erasers": { "Quantity" : 1}
        }
    ]
}
```
#### _Sets_
DynamoDB supports types that represent sets of _Number_, _String_, or _Binary_ values. All of the elements
within a set must be of the same type. For example, an attribute of type Number Set can only contain
numbers; String Set can only contain strings; and so on.
There is no limit on the number of values in a set, as long as the item containing the values fits within
the DynamoDB item size limit (400 KB).
Each value within a set must be unique. The order of the values within a set is not preserved; therefore,
your applications must not rely on any particular order of elements within the set. Finally, DynamoDB
does not support empty sets.
The following example shows a string set, a number set, and a binary set:
```python
["Black", "Green", "Red"]
[42.2, -19, 7.5, 3.14]
["U3Vubnk=", "UmFpbnk=", "U25vd3k="]
```