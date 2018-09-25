-- -----------------------------------------------------
-- Table L_PRODUCT
-- -----------------------------------------------------

CREATE TABLE L_PRODUCT (
  PRODUCT_KEY integer ,
  ID integer ,
  PRODUCT_DESC integer ,
  MSRP number(18,2) ,
  EFFECTIVE_START_DATE DATE ,
  EFFECTIVE_END_DATE DATE ,
  CURRENT_FLAG CHAR(1) ,
  ETL_LOAD_DATE date ,
  PRIMARY KEY (PRODUCT_KEY));



-- -----------------------------------------------------
-- Table L_USER
-- -----------------------------------------------------
CREATE TABLE  L_USER (
  USER_KEY integer ,
  ID integer ,
  USER_FIRST_NAME varchar2(45) ,
  USER_LAST_NAME varchar2(45) ,
  VIP_FLAG CHAR(1)  ,
  ADDRESS varchar2(500) ,
  LAST_PURCHASE date ,
  EFFECTIVE_START_DATE DATE ,
  EFFECTIVE_END_DATE DATE ,
  CURRENT_FLAG CHAR(1)  ,
  ETL_LOAD_DATE date ,
  PRIMARY KEY (USER_KEY));



-- -----------------------------------------------------
-- Table L_ORDER_STATUS
-- -----------------------------------------------------
CREATE TABLE  L_ORDER_STATUS (
  ORDER_STATUS_KEY integer ,
  ORDER_STATUS_DESC varchar2(45) ,
  CREATE_DATE date ,
  UPDATE_DATE date ,
  PRIMARY KEY (ORDER_STATUS_KEY));



-- -----------------------------------------------------
-- Table L_DATE
-- -----------------------------------------------------
CREATE TABLE  L_DATE (
  DAY_KEY integer ,
  DAY_CODE DATE ,
  CREATE_DATE date ,
  UPDATE_DATE date ,
  PRIMARY KEY (DAY_KEY));



-- -----------------------------------------------------
-- Table F_ORDER
-- -----------------------------------------------------
CREATE TABLE  F_ORDER (
  ORDER_KEY integer,
  ID integer,
  DAY_KEY integer,
  ORDER_STATUS_KEY integer ,
  USER_KEY integer ,
  ORDER_TIME date,
  CHARGE_AMOUNT number(18,2) ,
  TAX_AMOUNT number(18,2) ,
  COUPON_AMOUNT number(18,2) ,
  ETL_LOAD_DATE date,
  PRIMARY KEY (ORDER_KEY));



-- -----------------------------------------------------
-- Table L_RETURN_REASON
-- -----------------------------------------------------
CREATE TABLE  L_RETURN_REASON (
  RETURN_REASON_KEY integer ,
  RETURN_REASON_DESC varchar2(45) ,
  CREATE_DATE date ,
  UPDATE_DATE date ,
  PRIMARY KEY (RETURN_REASON_KEY));



-- -----------------------------------------------------
-- Table L_VARIANT
-- -----------------------------------------------------
CREATE TABLE  L_VARIANT (
  VARIANT_KEY integer ,
  ID varchar2(45) ,
  PRODUCT_KEY integer ,
  SIZE_ varchar2(45) ,
  COST number(18,2) ,
  EFFECTIVE_START_DATE DATE ,
  EFFECTIVE_END_DATE DATE ,
  CURRENT_FLAG CHAR(1) ,
  ETL_LOAD_DATE varchar2(45) ,
  PRIMARY KEY (VARIANT_KEY));



-- -----------------------------------------------------
-- Table F_ITEM
-- -----------------------------------------------------
CREATE TABLE  F_ITEM (
  ITEM_KEY integer ,
  ID integer ,
  DAY_KEY integer,
  VARIANT_KEY integer ,
  ORDER_KEY integer ,
  SALE_PRICE number(18,2) ,
  QUANTITY_ORDERED integer ,
  QUANTITY_OVERSOLD integer ,
  ITEM_TIME date,
  ETL_LOAD_DATE date ,
  PRIMARY KEY (ITEM_KEY))



-- -----------------------------------------------------
-- Table L_ADMIN
-- -----------------------------------------------------
CREATE TABLE  L_ADMIN (
  ADMIN_KEY integer ,
  ADMIN_FIRST_NAME varchar2(45) ,
  ADMIN_LAST_NAME varchar2(45) ,
  ADMIN_USER_NAME varchar2(45) ,
  EFFECTIVE_START_DATE varchar2(45) ,
  EFFECTIVE_END_DATE varchar2(45) ,
  CURRENT_FLAG CHAR(1) ,
  CREATE_DATE date ,
  PRIMARY KEY (ADMIN_KEY));



-- -----------------------------------------------------
-- Table F_RETURN
-- -----------------------------------------------------
CREATE TABLE  F_RETURN (
  RETURN_KEY integer ,
  ID integer ,
  RETURN_REASON_KEY integer ,
  ITEM_KEY integer ,
  DAY_KEY integer ,
  RETURN_TIME date ,
  APPROVAL_FLAG CHAR(1) ,
  AMOUNT_REFUNDED number(18,2) ,
  ADMIN_KEY integer ,
  ETL_LOAD_DATE date ,
  PRIMARY KEY (RETURN_KEY));



-- -----------------------------------------------------
-- Table F_SHIPMENT
-- -----------------------------------------------------
CREATE TABLE  F_SHIPMENT (
  SHIPMENT_KEY integer ,
  ID integer ,
  ORDER_KEY integer ,
  DAY_KEY integer ,
  SHIPMENT_TIME date,
  START_DAY_KEY integer ,
  FINISH_DAY_KEY integer ,
  NUM_PACKAGES integer ,
  SHIPPING_CHARGE number(18,2) ,
  GIFT_FLAG CHAR(1) ,
  SHIPPING_ADDRESS varchar2(500) ,
  RECIPIENT_NAME varchar2(100) ,
  ETL_LOAD_DATE date ,
  PRIMARY KEY (SHIPMENT_KEY));