The data model consists of following tables:

 - D_PRODUCT - dimension contains all products;
 - D_CUSTOMER - dimension contains all customers;
 - D_USER_TIER - dimension contains all tiers;
 - F_SUBSCRIPTION - fact table contains all subscriptions (facts that customer owns certain product)
 
 All dimensions contain only two fields: _ID and _NAME (to make it simple). Only fact table contains all necessary fields.
 
 F_SUBSCRIPTION structure:
 - SUBSCRIPTION_ID -  surrogate key;
 - USER_TIER_ID - reference to D_USER_TIER dimension;
 - START_DATE - date when subscription starts;
 - END_DATE - date when subscription ends (NULL  for current subscription);
 - CUSTOMER_ID - reference to D_CUSTOMER dimension;
 - PRODUCT_ID - reference to D_PRODUCT dimension.
 
 
 I assume that one record in F_SUBSCRIPTION table represents a fact that customer owns one product in a certain tier. There are as many records for a particular 
 customer as products he owns. For example if a customer owns three products then there will be three records in F_SUBSCRIPTION table, each for 
 one product. All current records have END_DATE=NULL. If any product is cancelled then this record should be closed (END_DATE will be set to closure date).
 If customer moves to another tier than all corresponding records in F_SUBSCRIPTION table will be closed and new records will be created with a reference to the  
 new tier. All dimensions are static and have SCD type 1.
 Please find "scripts.sql" file which contains the scripts for following analytc requests:
 
 - Which user tier do most Intercom customers fall into now? How about 3 months ago?
 - How long has a customer had a certain product?
 - Which products are most popular on each user tier?
 
