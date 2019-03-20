# make an assumption of value of C,i,F 
C<-1
i<- c(0.02,0.03,0.04)
F<-1
# use the pv formula 
PVfunction=function(i, C, F,n=length(i)) {
  sum(C * exp((-i)*(1:(n)/2))) + F * exp((-i[n])*(n/2)) }
PVfunction(i,C,F)


