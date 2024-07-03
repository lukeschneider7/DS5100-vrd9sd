# Ex 10.1
fib <- numeric(10)
fib[1] = 1
fib[2] = 1
for (i in 3:10){
  fib[i] <- fib[i-1] + fib[i-2]}
paste(fib)


# Ex 10.2
fibonacci <- function(x){
  fib <- numeric(x)
  fib[1] <- fib[2] <- 1
  for (i in 3:x){
    fib[i] <- fib[i-2] + fib[i-1]
  }
  return (fib)
}
print(fibonacci(17))


# Ex 10.3
filter <-function(y=2){
  if (y>=0 & y<=1){
    return(1)
  }
  else{
    return(0)
  }
}

# Ex 10.4
filter(.25)
filter(2.5)
filter(25)
filter(1)
filter(0)

