library(dplyr)
chicago <- readRDS("chicago.rds")
dim(chicago)
str(chicago) # columns

### R dplyr core methods
# Select() columns 
select(chicago, (city:date)) %>% head(3) # index slice
select(chicago, ends_with("2")) %>% head(3)
select(chicago, starts_with("d")) %>% head(3)
select(chicago, contains('mean')) %>% head(3)

# Filter() Rows
summary(chicago$pm25tmean2)
summary(filter(chicago, pm25tmean2 > 35)) # filter out if pm25<35
filter(chicago, (pm25tmean2>35 & tmpd >80)) %>% head(3) # two variable filter
filter(chicago, between(tmpd, 90, 95)) %>% head(5)

# Arrange() 
chicago_by_temp <- arrange(chicago, tmpd)
head(chicago_by_temp)

# Rename()
  chicago <- rename(chicago, dewpoint = dptp, pm25 = pm25tmean2) # renaming columns
  chicago %>% head(4)
# Mutate()
# Groupby()