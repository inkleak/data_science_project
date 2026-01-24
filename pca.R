# MLR model for football

PLdata<- read.csv("premier-player-23-24.csv",header = TRUE)

# sub-setting data by position

FW <- PLdata[ which(PLdata$Pos=='FW'),]
MF <- PLdata[ which(PLdata$Pos=='MF'),]
DF <- PLdata[ which(PLdata$Pos=='DF'),]
GK <- PLdata[ which(PLdata$Pos=='GK'),]



## Clustering

# Prepping data, sub-setting by position

PLdata_num <- PLdata[, sapply(PLdata, is.numeric)]
ScaledData<- scale(PLdata_num)

ScaledFW <- as.data.frame(scale(FW[, sapply(FW, is.numeric)]))
ScaledMF <- as.data.frame(scale(MF[, sapply(MF, is.numeric)]))
ScaledDF <- as.data.frame(scale(DF[, sapply(DF, is.numeric)]))
ScaledGK <- as.data.frame(scale(GK[, sapply(GK, is.numeric)]))

# Clustering by FW position

kmeansfitFW <- kmeans(ScaledFW,3)
aggregate(ScaledFW,by=list(kmeansfitFW$cluster),FUN=mean)
clusterdata<- data.frame(ScaledFW, kmeansfitFW$cluster)
summary(clusterdata)

pca <- prcomp(ScaledFW)

summary(pca)
plot(pca)

plot(
  pca$x[,1], pca$x[,2],
  col = kmeansfitFW$cluster,
  pch = 19,
  xlab = "PC1",
  ylab = "PC2",
  main = "K-means Clusters (PCA)"
)
legend(-5,10,legend = c("Group 1","Group 2", "Group 3"),
       col = c(1,2,3), pch = 19)

# Clustering by DF

kmeansfitDF <- kmeans(ScaledDF,3)
aggregate(ScaledDF,by=list(kmeansfitDF$cluster),FUN=mean)
clusterdata<- data.frame(ScaledDF, kmeansfitDF$cluster)
summary(clusterdata)

pca <- prcomp(ScaledDF)

summary(pca)
plot(pca)

plot(
  pca$x[,1], pca$x[,2],
  col = kmeansfitDF$cluster,
  pch = 19,
  xlab = "PC1",
  ylab = "PC2",
  main = "K-means Clusters (PCA)"
)
legend(-5,10,legend = c("Group 1","Group 2", "Group 3"),
       col = c(1,2,3), pch = 19)

# Clustering by MF

kmeansfitMF <- kmeans(ScaledMF,3)
aggregate(ScaledMF,by=list(kmeansfitMF$cluster),FUN=mean)
clusterdata<- data.frame(ScaledMF, kmeansfitMF$cluster)
summary(clusterdata)

pca <- prcomp(ScaledMF)

summary(pca)
plot(pca)

plot(
  pca$x[,1], pca$x[,2],
  col = kmeansfitMF$cluster,
  pch = 19,
  xlab = "PC1",
  ylab = "PC2",
  main = "K-means Clusters (PCA)"
)
legend(-8,10,legend = c("Group 1","Group 2", "Group 3"),
       col = c(1,2,3), pch = 19)

# attaching Cluster Membership to original Data sets


FW$clusters<-kmeansfitFW$cluster
