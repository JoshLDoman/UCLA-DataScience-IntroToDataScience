IncomeBracket <- function(income) {
  if(income >= 5000) {
    result <- "High income earner" }
  else if (income >= 3000 & income < 5000) {
    result <- "Average income earner"  } 
  else {
    result <- "Low income earner"
  }
  return(result)
}

x <- c(0, 3000, 4000, 5000, 6000)
sapply(x, IncomeBracket)