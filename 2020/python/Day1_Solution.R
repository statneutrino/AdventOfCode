library(tidyverse)
library(RCurl)
numbers <- readLines("./2020/input_2.txt") %>%
  as.numeric()

x <- vector()
y <- vector()
z <- vector()

for (i in numbers){
  for (j in numbers){
    for (k in numbers){
      if (i + j + k == 2020) {
        x <- i
        y <- j
        z <- k
      }
    }
  }
}
x
y
z
x * y * z
