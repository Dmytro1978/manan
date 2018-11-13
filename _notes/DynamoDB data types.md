# DynamoDB Data Types
DynamoDB supports many different data types for attributes within a table. They can be categorized as
follows:
* Scalar Types – A scalar type can represent exactly one value. The scalar types are _number_, _string_,
_binary_, _Boolean_, and _null_.
* Document Types – A document type can represent a complex structure with nested attributes—such
as you would find in a JSON document. The document types are list and map.
* Set Types – A set type can represent multiple scalar values. The set types are _string_ set, _number_ set,
and _binary_ set.

## Scalar Types
###  String
Strings are Unicode with UTF-8 binary encoding. The length of a string must be greater than zero and is
constrained by the maximum DynamoDB item size limit of 400 KB.
The following additional constraints apply to primary key attributes that are defined as type string:
* For a simple primary key, the maximum length of the first attribute value (the partition key) is 2048
bytes.
* For a composite primary key, the maximum length of the second attribute value (the sort key) is 1024
bytes.

### Binary
Binary type attributes can store any binary data, such as compressed text, encrypted data, or images.
Whenever DynamoDB compares binary values, it treats each byte of the binary data as unsigned.
The length of a binary attribute must be greater than zero, and is constrained by the maximum
DynamoDB item size limit of 400 KB.
If you define a primary key attribute as a binary type attribute, the following additional constraints
apply:
* For a simple primary key, the maximum length of the first attribute value (the partition key) is 2048
bytes.
* For a composite primary key, the maximum length of the second attribute value (the sort key) is 1024
bytes.

### Boolean
A Boolean type attribute can store either true or false.

### Null
Null represents an attribute with an unknown or undefined state.

## Document Types
The document types are _list_ and _map_. These data types can be nested within each other, to represent
complex data structures up to 32 levels deep. 
There is no limit on the number of values in a list or a map, as long as the item containing the values fits
within the DynamoDB item size limit (400 KB).
An attribute value cannot be an empty String or empty Set (String Set, Number Set, or Binary Set).
However, empty Lists and Maps are allowed.

### List
A list type attribute can store an ordered collection of values. Lists are enclosed in square brackets:
[ ... ]
A list is similar to a JSON array. There are no restrictions on the data types that can be stored in a list
element, and the elements in a list element do not have to be of the same type.

### Map
A map type attribute can store an unordered collection of name-value pairs. Maps are enclosed in curly
braces: { ... }
A map is similar to a JSON object. There are no restrictions on the data types that can be stored in a map
element, and the elements in a map do not have to be of the same type.
Maps are ideal for storing JSON documents in DynamoDB. The following example shows a map that
contains a string, a number, and a nested list that contains another map:

```json
{
    Day: "Monday",
    UnreadEmails: 42,
    ItemsOnMyDesk: [
        "Coffee Cup",
        "Telephone",
        {
            Pens: { Quantity : 3},
            Pencils: { Quantity : 2},
            Erasers: { Quantity : 1}
        }
    ]
}
```
### Sets
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