install.packages("RMySQL")
install.packages("RMariaDB")
install.packages("DBI")
install.packages("odbc")
install.packages("RSQLite")
install.packages("devtools")
devtools::install_github("r-dbi/DBI")
library(odbc)
library(dbConnect)
library(DBI)
con <- dbConnect(RMySQL::MySQL(),
    dbname = "TwitterDB",
    host = "localhost",
    port = 3306,
    user = "root",
    password = "gaurav")

res <- dbSendQuery(con, "SELECT created_at, polarity FROM tesla")
str(res)

dbFetch(res, 5)
dbDisconnect(con)
