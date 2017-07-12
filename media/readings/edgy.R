'
par(mfrow=c(1,1))
p = subset(log, Type == "trade")
plot(p$Price, ylim=c(0,60), ylab="Trade Price")
abline(h=mean(p$Price))
abline(h=30,col="red")

s1 = array(1:max(log$Period))
s2 = array(1:max(log$Period))
u1 = array(1:max(log$Period))
u2 = array(1:max(log$Period))
for (i in 1:max(log$Period)) {
  s1[i] = mean(subset(log, Period == i & Group == 1 & Type == "start")$Utility)
  s2[i] = mean(subset(log, Period == i & Group == 2 & Type == "start")$Utility)
  u1[i] = mean(subset(log, Period == i & Group == 1 & Type == "stop")$Utility)
  u2[i] = mean(subset(log, Period == i & Group == 2 & Type == "stop")$Utility)
}
plot(u1, col="red", ylim=c(0,6), ylab="Utility")
points(u2, col="blue")
abline(h=s1[1], col="red")
abline(h=s2[1], col="blue")
abline(lm(u1~array(1:max(log$Period))), col="red")
abline(lm(u2~array(1:max(log$Period))), col="blue")

par(mfrow=c(4,4))
for (i in 1:max(log$Period)) {
  p = subset(log, Period==i & Type == "order")
  plot(p$Elapsed, p$Price, ylim=c(0,60), xlab=i, ylab="Order Price")
  abline(a=mean(p$Price),b=0)
  abline(a=30,b=0,col="red")
}

par(mfrow=c(4,4))
for (i in 1:max(log$Period)) {
  p = subset(log, Period==i & Type == "trade")
  plot(p$Elapsed, p$Price, ylim=c(0,60), xlab=i, ylab="Trade Price")
  abline(a=mean(p$Price),b=0)
  abline(a=30,b=0,col="red")
}
'

alpha = c(0.36585, 0.75)
beta = c(0.63414, 0.25)
a = c(25, 25)
b = c(1, 1)
c = c(0.006285, 0.0069855)
utility = function(x, y, g) {
  return (c[g] * (a[g]*x)^alpha[g] * (b[g]*y)^beta[g])
}

u = matrix(nrow=500,ncol=20)
for (y in c(1:nrow(u))) {
  for (x in c(1:ncol(u))) {
    u[y,x] = x*y
  }
}
heatmap(u, Rowv=NA, Colv=NA, scale="none", col=heat.colors(512), labRow=NA, labCol=NA)